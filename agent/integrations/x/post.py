#!/usr/bin/env python3
"""
Post tweets and threads to X.

Usage:
    ./post.py                     # Post 1 pending file
    ./post.py --limit 3           # Post up to 3 files
    ./post.py --text "hello"      # Post text directly
    ./post.py --file thread.txt   # Post specific file

Environment:
    X_API_KEY, X_API_KEY_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
"""

import os
import sys
import json
import argparse
from pathlib import Path

try:
    from requests_oauthlib import OAuth1Session
except ImportError:
    print('{"error": "Missing requests-oauthlib. Run: pip install requests requests-oauthlib"}')
    sys.exit(1)

API_URL = "https://api.twitter.com/2/tweets"
MAX_TWEET_LENGTH = int(os.environ.get("X_MAX_TWEET_LENGTH", 25000))  # X Premium: 25000, Free: 280
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

    return OAuth1Session(
        api_key,
        client_secret=api_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_secret
    )


class RateLimitError(Exception):
    pass


def post_tweet(session, text, reply_to=None):
    """Post a single tweet, optionally as a reply."""
    payload = {"text": text.strip()}

    if reply_to:
        payload["reply"] = {"in_reply_to_tweet_id": reply_to}

    response = session.post(API_URL, json=payload)

    if response.status_code == 429:
        raise RateLimitError("X API rate limit hit (429). Content remains queued for next run.")

    try:
        data = response.json()
    except Exception:
        print(f"Invalid response (status {response.status_code}): {response.text[:200]}")
        return None

    print(json.dumps(data))

    if "data" in data and "id" in data["data"]:
        return data["data"]["id"]
    return None


def post_thread(session, content):
    """Post a thread (--- separated content)."""
    parts = [p.strip() for p in content.split("---") if p.strip()]

    if not parts:
        print('{"error": "Empty thread content"}')
        return False

    if len(parts) == 1:
        # Single tweet, not a thread
        return post_tweet(session, parts[0]) is not None

    print(f"Posting thread with {len(parts)} parts...")

    # Post first tweet
    tweet_id = post_tweet(session, parts[0])
    if not tweet_id:
        return False

    # Reply with each subsequent part
    for i, part in enumerate(parts[1:], 2):
        print(f"  Part {i}/{len(parts)}...")
        tweet_id = post_tweet(session, part, reply_to=tweet_id)
        if not tweet_id:
            print(f'  ✗ Failed at part {i}')
            return False

    return True


def parse_reply_header(content):
    """Parse REPLY_TO header from reply files. Returns (reply_to_id, body) or (None, content)."""
    lines = content.split("\n")
    if lines and lines[0].startswith("REPLY_TO:"):
        reply_to = lines[0].replace("REPLY_TO:", "").strip()
        rest = "\n".join(lines[1:]).strip()
        # Strip the --- separator between header and body
        if rest.startswith("---"):
            rest = rest[3:].strip()
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


def main():
    parser = argparse.ArgumentParser(description="Post tweets and threads to X")
    parser.add_argument("--limit", type=int, default=1, help="Max files to post (default: 1)")
    parser.add_argument("--text", type=str, help="Post text directly")
    parser.add_argument("--file", type=str, help="Post specific file")
    args = parser.parse_args()

    session = get_oauth_session()

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

    # Find pending files (both tweet-*.txt and thread-*.txt)
    POSTED_DIR.mkdir(parents=True, exist_ok=True)
    SKIPPED_DIR.mkdir(parents=True, exist_ok=True)

    pending = sorted(OUTPUT_DIR.glob("*.txt"))
    pending = [f for f in pending if f.is_file() and "posted" not in str(f) and "skipped" not in str(f)][:args.limit]

    if not pending:
        print("No pending files")
        sys.exit(0)

    posted = 0
    failed = False

    for filepath in pending:
        print(f"Processing: {filepath.name}")
        content = filepath.read_text().strip()

        # Validate content length
        error = validate_content(content)
        if error:
            print(f"  ⚠ Skipping: {error}")
            filepath.rename(SKIPPED_DIR / filepath.name)
            continue

        try:
            if process_content(session, content):
                # Move to posted
                filepath.rename(POSTED_DIR / filepath.name)
                print("  ✓ Posted and archived")
                posted += 1
            else:
                print("  ✗ Failed")
                failed = True
                break
        except RateLimitError as e:
            print(f"\nWARNING: {e}")
            print(f"Posted {posted} of {args.limit} before rate limit.")
            sys.exit(1)

    print(f"Posted: {posted}/{args.limit}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()