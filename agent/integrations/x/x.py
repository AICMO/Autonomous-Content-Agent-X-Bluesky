#!/usr/bin/env python3
"""
X (Twitter) integration — post, metrics, verify.

Usage:
    ./x.py --post                                    # Post 1 tweet + 1 reply from queue
    ./x.py --post --limit-tweets 3 --limit-replies 3 # Post up to 3 of each
    ./x.py --post --text "hello"                     # Post text directly
    ./x.py --post --file thread.txt                  # Post specific file
    ./x.py --metrics                                 # Print account metrics as JSON
    ./x.py --metrics --compact                       # One-line summary
    ./x.py --verify                                  # Verify credentials (raw API response)

Environment:
    X_API_KEY, X_API_KEY_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
    X_MAX_TWEET_LENGTH (optional, default 25000)
"""

import os
import re
import sys
import json
import time
import random
import argparse
from pathlib import Path

try:
    from requests_oauthlib import OAuth1Session
except ImportError:
    print('{"error": "Missing requests-oauthlib. Run: pip install requests requests-oauthlib"}')
    sys.exit(1)

API_BASE = "https://api.twitter.com/2"
MAX_TWEET_LENGTH = int(os.environ.get("X_MAX_TWEET_LENGTH", 25000))
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "../../outputs/x"
POSTED_DIR = OUTPUT_DIR / "posted"
SKIPPED_DIR = OUTPUT_DIR / "skipped"


def get_oauth_session():
    """Create OAuth1 session from environment variables."""
    api_key = os.environ.get("X_API_KEY")
    api_secret = os.environ.get("X_API_KEY_SECRET")
    access_token = os.environ.get("X_ACCESS_TOKEN")
    access_secret = os.environ.get("X_ACCESS_TOKEN_SECRET")

    if not all([api_key, api_secret, access_token, access_secret]):
        print('{"error": "Missing credentials. Need X_API_KEY, X_API_KEY_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET"}')
        sys.exit(1)

    session = OAuth1Session(
        api_key,
        client_secret=api_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_secret
    )
    # Realistic browser-like headers to avoid Cloudflare WAF blocks.
    # Header order matters — Cloudflare checks for anomalies.
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    })

    # Route through proxy if configured (e.g. Bright Data residential proxy)
    proxy_url = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    if proxy_url:
        session.proxies = {"https": proxy_url, "http": proxy_url}
        print(f"  Using proxy: {proxy_url.split('@')[-1]}")  # Log host only, hide credentials

    return session


# ---------------------------------------------------------------------------
# Verify
# ---------------------------------------------------------------------------

def get_user_endpoint():
    """Return the best user lookup endpoint. Prefers /users/by/username/:username
    over /users/me (which has known 503 issues on X API)."""
    username = os.environ.get("X_USERNAME")
    if username:
        return f"{API_BASE}/users/by/username/{username}"
    return f"{API_BASE}/users/me"


def cmd_verify(session, _args):
    """Verify credentials and print raw response."""
    endpoint = get_user_endpoint()
    print(f"Endpoint: {endpoint}")
    response = session.get(endpoint, params={"user.fields": "public_metrics"})
    try:
        print(json.dumps(response.json(), indent=2))
    except Exception:
        print(response.text[:500])
    sys.exit(0 if response.status_code == 200 else 1)


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def cmd_metrics(session, args):
    """Fetch and display account metrics."""
    endpoint = get_user_endpoint()
    response = session.get(endpoint, params={"user.fields": "public_metrics"})

    if not response.text:
        print('{"error": "Empty response (likely rate limited)", "status": ' + str(response.status_code) + '}')
        sys.exit(1)

    try:
        data = response.json()
    except Exception:
        print(json.dumps({"error": f"Invalid JSON: {response.text[:200]}", "status": response.status_code}))
        sys.exit(1)

    if response.status_code != 200:
        print(json.dumps({"error": data, "status": response.status_code}, indent=2))
        sys.exit(1)

    user = data.get("data", {})
    pub = user.get("public_metrics", {})
    metrics = {
        "username": user.get("username"),
        "name": user.get("name"),
        "followers": pub.get("followers_count"),
        "following": pub.get("following_count"),
        "tweets": pub.get("tweet_count"),
        "listed": pub.get("listed_count"),
    }

    if args.compact:
        print(f"@{metrics['username']}: {metrics['followers']} followers, {metrics['following']} following, {metrics['tweets']} tweets")
    else:
        print(json.dumps(metrics, indent=2))


# ---------------------------------------------------------------------------
# Post
# ---------------------------------------------------------------------------

class RateLimitError(Exception):
    pass


class DuplicateContentError(Exception):
    pass


class TemporaryError(Exception):
    """Temporary API failure (5xx) — leave in queue for retry."""
    pass


MAX_RETRIES = 4
RETRY_DELAYS = [10, 30, 60, 120]  # longer backoff — CF challenges can clear after ~60s


def post_tweet(session, text, reply_to=None):
    """Post a single tweet, optionally as a reply. Retries on temporary errors."""
    payload = {"text": text.strip()}
    if reply_to:
        payload["reply"] = {"in_reply_to_tweet_id": reply_to}

    endpoint = f"{API_BASE}/tweets"
    from datetime import datetime, timezone

    for attempt in range(MAX_RETRIES + 1):
        response = session.post(endpoint, json=payload)

        daily_remaining = response.headers.get("x-app-limit-24hour-remaining")
        daily_limit = response.headers.get("x-app-limit-24hour-limit")
        daily_reset = response.headers.get("x-app-limit-24hour-reset")
        if daily_remaining and daily_limit:
            print(f"  Daily limit: {daily_remaining}/{daily_limit} remaining", end="")
            if daily_reset:
                reset_time = datetime.fromtimestamp(int(daily_reset), tz=timezone.utc).strftime("%H:%M:%S UTC")
                print(f" (resets {reset_time})", end="")
            print()

        if response.status_code == 429:
            body = response.text[:500] if response.text else "(empty body)"
            raise RateLimitError(f"X API rate limit hit (429). {daily_remaining or '?'}/{daily_limit or '?'} daily posts remaining. Body: {body}")

        # Check for temporary errors (5xx or Cloudflare HTML)
        is_server_error = response.status_code >= 500
        content_type = response.headers.get("content-type", "")
        is_cloudflare = "text/html" in content_type or (response.text and response.text.strip().startswith("<!DOCTYPE"))

        if is_server_error or is_cloudflare:
            # Cloudflare blocks are persistent per IP — fewer retries, shorter waits
            max_retries = 2 if is_cloudflare else MAX_RETRIES
            cf_delays = [10, 30]
            delays = cf_delays if is_cloudflare else RETRY_DELAYS

            if attempt < max_retries:
                delay = delays[attempt] + random.uniform(0, 5)  # jitter
                reason = f"server error ({response.status_code})" if is_server_error else f"Cloudflare block ({response.status_code})"
                print(f"  ⏳ {reason} on {endpoint}, retrying in {delay:.0f}s (attempt {attempt + 1}/{max_retries})...")
                time.sleep(delay)
                continue
            # All retries exhausted
            body = response.text[:200] if response.text else "(empty body)"
            if is_server_error:
                raise TemporaryError(f"X API server error ({response.status_code}) on {endpoint} after {max_retries} retries: {body}")
            raise TemporaryError(f"Cloudflare block ({response.status_code}) on {endpoint} after {max_retries} retries: {body}")

        # Not a temporary error — break out of retry loop
        break

    try:
        data = response.json()
    except Exception:
        print(f"Invalid response (status {response.status_code}): {response.text[:200]}")
        return None

    print(json.dumps(data))

    # Detect duplicate content rejection
    if response.status_code == 403:
        detail = data.get("detail", "")
        if "duplicate" in detail.lower():
            raise DuplicateContentError(detail)

    if "data" in data and "id" in data["data"]:
        time.sleep(0.5)
        return data["data"]["id"]
    return None


def post_thread(session, content):
    """Post a thread (--- separated content)."""
    parts = [p.strip() for p in content.split("---") if p.strip()]

    if not parts:
        print('{"error": "Empty thread content"}')
        return False

    if len(parts) == 1:
        return post_tweet(session, parts[0]) is not None

    print(f"Posting thread with {len(parts)} parts...")
    tweet_id = post_tweet(session, parts[0])
    if not tweet_id:
        return False

    for i, part in enumerate(parts[1:], 2):
        print(f"  Part {i}/{len(parts)}...")
        tweet_id = post_tweet(session, part, reply_to=tweet_id)
        if not tweet_id:
            print(f'  ✗ Failed at part {i}')
            return False

    return True


def parse_reply_header(content):
    """Parse reply target from reply files. Handles multiple formats:
    - REPLY_TO: {id} [---] {body}           (canonical)
    - {numeric_id}\\n{body}                  (raw ID on first line)
    - tweet_id: {id} [reply_to: @handle]    (metadata headers)
    - TWEET_ID: {id} [AUTHOR: @handle]      (metadata headers)
    - reply_to: {numeric_id}                (lowercase variant)
    - in_reply_to: {numeric_id}             (at start or end of file)
    Returns (reply_to_id, body) or (None, content).
    """
    lines = content.split("\n")

    if lines and lines[0].startswith("REPLY_TO:"):
        reply_to = lines[0].replace("REPLY_TO:", "").strip()
        rest = "\n".join(lines[1:]).strip()
        if rest.startswith("---"):
            rest = rest[3:].strip()
        # Validate: must be numeric tweet ID, not a handle
        if not re.match(r'^\d{10,}$', reply_to):
            print(f"  ⚠ Invalid reply target '{reply_to}' (must be numeric tweet ID, not a handle)")
            return None, rest
        return reply_to, rest

    if lines and re.match(r'^\d{10,}$', lines[0].strip()):
        reply_to = lines[0].strip()
        rest = "\n".join(lines[1:]).strip()
        return reply_to, rest

    m = re.match(r'^(?:tweet_id|TWEET_ID)\s*:\s*(\d+)', lines[0]) if lines else None
    if m:
        reply_to = m.group(1)
        body_start = 1
        for i in range(1, len(lines)):
            line = lines[i].strip()
            if line == '' or re.match(r'^(reply_to|REPLY_TO|AUTHOR|author)\s*:', line):
                body_start = i + 1
            else:
                break
        rest = "\n".join(lines[body_start:]).strip()
        return reply_to, rest

    m = re.match(r'^(?:reply_to|in_reply_to)\s*:\s*(\d{10,})', lines[0]) if lines else None
    if m:
        reply_to = m.group(1)
        rest = "\n".join(lines[1:]).strip()
        return reply_to, rest

    for i in range(len(lines) - 1, -1, -1):
        m = re.match(r'^(?:in_reply_to|reply_to)\s*:\s*(\d{10,})', lines[i])
        if m:
            reply_to = m.group(1)
            rest = "\n".join(lines[:i]).strip()
            return reply_to, rest

    return None, content


def is_thread(content):
    """Check if content is a thread (has --- separators)."""
    return "---" in content


def validate_content(content):
    """Validate content length. Returns error message or None if valid."""
    _, body = parse_reply_header(content)
    if is_thread(body):
        parts = [p.strip() for p in body.split("---") if p.strip()]
        for i, part in enumerate(parts, 1):
            if len(part) > MAX_TWEET_LENGTH:
                return f"Thread part {i} is {len(part)} chars (max {MAX_TWEET_LENGTH})"
    else:
        if len(body) > MAX_TWEET_LENGTH:
            return f"Tweet is {len(body)} chars (max {MAX_TWEET_LENGTH})"
    return None


def process_content(session, content):
    """Process content (tweet, thread, or reply)."""
    reply_to, body = parse_reply_header(content)
    if reply_to:
        print(f"  Replying to tweet {reply_to}")
        return post_tweet(session, body, reply_to=reply_to) is not None
    elif is_thread(body):
        return post_thread(session, body)
    else:
        return post_tweet(session, body) is not None


def cmd_post(session, args):
    """Post tweets/threads/replies."""

    # Direct text mode
    if args.text:
        error = validate_content(args.text)
        if error:
            print(f'{{"error": "{error}"}}')
            sys.exit(1)
        try:
            success = process_content(session, args.text)
        except RateLimitError as e:
            print(f"WARNING: {e}")
            sys.exit(1)
        sys.exit(0 if success else 1)

    # Specific file mode
    if args.file:
        filepath = (OUTPUT_DIR / args.file).resolve()
        if not str(filepath).startswith(str(OUTPUT_DIR.resolve())):
            print('{"error": "File path must be within output directory"}')
            sys.exit(1)
        if not filepath.exists():
            print(f'{{"error": "File not found: {args.file}"}}')
            sys.exit(1)
        content = filepath.read_text().strip()
        error = validate_content(content)
        if error:
            print(f'{{"error": "{error}"}}')
            sys.exit(1)
        try:
            success = process_content(session, content)
        except RateLimitError as e:
            print(f"WARNING: {e}")
            sys.exit(1)
        sys.exit(0 if success else 1)

    # Queue mode
    POSTED_DIR.mkdir(parents=True, exist_ok=True)
    SKIPPED_DIR.mkdir(parents=True, exist_ok=True)

    all_pending = sorted(OUTPUT_DIR.glob("*.txt"))
    all_pending = [f for f in all_pending if f.is_file() and "posted" not in str(f) and "skipped" not in str(f)]

    replies = [f for f in all_pending if f.name.startswith("reply-")][:args.limit_replies]
    tweets = [f for f in all_pending if not f.name.startswith("reply-")][:args.limit_tweets]
    pending = tweets + replies

    if not pending:
        print("No pending files")
        sys.exit(0)

    print(f"Queue: {len(tweets)} tweets, {len(replies)} replies")

    posted = 0
    cf_blocked = False  # If CF blocks one request, all subsequent will fail too (same IP)

    for filepath in pending:
        if cf_blocked:
            print(f"Skipping {filepath.name}: Cloudflare blocking this IP, will retry next run")
            continue

        print(f"Processing: {filepath.name}")
        content = filepath.read_text().strip()

        error = validate_content(content)
        if error:
            print(f"  ⚠ Skipping: {error}")
            filepath.rename(SKIPPED_DIR / filepath.name)
            continue

        try:
            if process_content(session, content):
                filepath.rename(POSTED_DIR / filepath.name)
                print("  ✓ Posted and archived")
                posted += 1
            else:
                print("  ⚠ Failed, skipping")
                filepath.rename(SKIPPED_DIR / filepath.name)
                continue
        except TemporaryError as e:
            err_str = str(e)
            print(f"  ⏳ Temporary error, leaving in queue for retry: {e}")
            if "Cloudflare" in err_str:
                cf_blocked = True
                print("  🛑 Cloudflare is blocking this runner IP. Skipping remaining files.")
            continue
        except DuplicateContentError as e:
            print(f"  ⚠ Duplicate content, skipping: {e}")
            filepath.rename(SKIPPED_DIR / filepath.name)
            continue
        except RateLimitError as e:
            print(f"\nWARNING: {e}")
            print(f"Posted {posted} before rate limit. Remaining files will be retried next run.")
            sys.exit(0 if posted > 0 else 1)

    print(f"Posted: {posted} ({len(tweets)} tweets, {len(replies)} replies queued)")
    sys.exit(0)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="X (Twitter) integration")

    # Commands (mutually exclusive)
    cmd = parser.add_mutually_exclusive_group(required=True)
    cmd.add_argument("--post", action="store_true", help="Post tweets/threads/replies")
    cmd.add_argument("--metrics", action="store_true", help="Fetch account metrics")
    cmd.add_argument("--verify", action="store_true", help="Verify credentials")

    # Post options
    parser.add_argument("--limit-tweets", type=int, default=1, help="Max tweets/threads to post (default: 1)")
    parser.add_argument("--limit-replies", type=int, default=1, help="Max replies to post (default: 1)")
    parser.add_argument("--text", type=str, help="Post text directly")
    parser.add_argument("--file", type=str, help="Post specific file")

    # Metrics options
    parser.add_argument("--compact", action="store_true", help="One-line metrics summary")

    args = parser.parse_args()
    session = get_oauth_session()

    if args.post:
        cmd_post(session, args)
    elif args.metrics:
        cmd_metrics(session, args)
    elif args.verify:
        cmd_verify(session, args)


if __name__ == "__main__":
    main()
