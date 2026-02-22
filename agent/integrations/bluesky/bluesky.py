#!/usr/bin/env python3
"""
Bluesky integration — post, metrics, verify.

Usage:
    ./bluesky.py --post                                    # Post 1 post + 1 reply from queue
    ./bluesky.py --post --limit-tweets 3 --limit-replies 3 # Post up to 3 of each
    ./bluesky.py --post --text "hello"                     # Post text directly
    ./bluesky.py --post --file thread.txt                  # Post specific file
    ./bluesky.py --metrics                                 # Print account metrics as JSON
    ./bluesky.py --metrics --compact                       # One-line summary
    ./bluesky.py --verify                                  # Verify credentials (raw API response)

Environment:
    BLUESKY_HANDLE, BLUESKY_APP_PASSWORD
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path

try:
    from atproto import Client, models
except ImportError:
    print('{"error": "Missing atproto. Run: pip install atproto"}')
    sys.exit(1)

MAX_GRAPHEME_LENGTH = 300
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR / "../../outputs/bluesky"
POSTED_DIR = OUTPUT_DIR / "posted"
SKIPPED_DIR = OUTPUT_DIR / "skipped"


def count_graphemes(text):
    """Count grapheme clusters in text. Uses grapheme library if available, falls back to len()."""
    try:
        import grapheme
        return grapheme.length(text)
    except ImportError:
        return len(text)


def get_client():
    """Create and authenticate Bluesky client from environment variables."""
    handle = os.environ.get("BLUESKY_HANDLE")
    password = os.environ.get("BLUESKY_APP_PASSWORD")

    if not handle or not password:
        print('{"error": "Missing credentials. Need BLUESKY_HANDLE and BLUESKY_APP_PASSWORD"}')
        sys.exit(1)

    client = Client()
    try:
        client.login(handle, password)
    except Exception as e:
        print(json.dumps({"error": f"Login failed: {e}"}))
        sys.exit(1)

    return client


# ---------------------------------------------------------------------------
# Verify
# ---------------------------------------------------------------------------

def cmd_verify(client, _args):
    """Verify credentials by fetching own profile."""
    try:
        profile = client.app.bsky.actor.get_profile({"actor": client.me.did})
        print(json.dumps({
            "did": profile.did,
            "handle": profile.handle,
            "display_name": profile.display_name,
            "followers": profile.followers_count,
            "following": profile.follows_count,
            "posts": profile.posts_count,
        }, indent=2))
        sys.exit(0)
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def cmd_metrics(client, args):
    """Fetch and display account metrics."""
    try:
        profile = client.app.bsky.actor.get_profile({"actor": client.me.did})
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

    metrics = {
        "handle": profile.handle,
        "display_name": profile.display_name,
        "followers": profile.followers_count,
        "following": profile.follows_count,
        "posts": profile.posts_count,
    }

    if args.compact:
        print(f"@{metrics['handle']}: {metrics['followers']} followers, {metrics['following']} following, {metrics['posts']} posts")
    else:
        print(json.dumps(metrics, indent=2))


# ---------------------------------------------------------------------------
# Post
# ---------------------------------------------------------------------------

class RateLimitError(Exception):
    pass


def resolve_post(client, uri):
    """Resolve a post URI to get both URI and CID (needed for strong refs)."""
    try:
        response = client.app.bsky.feed.get_posts({"uris": [uri]})
        if response.posts:
            post = response.posts[0]
            return post.uri, post.cid
    except Exception as e:
        print(f"  Warning: Could not resolve post {uri}: {e}")
    return None, None


def make_strong_ref(uri, cid):
    """Create a strong ref from URI and CID strings."""
    return models.ComAtprotoRepoStrongRef.Main(uri=uri, cid=cid)


def create_post(client, text, reply_to_uri=None):
    """Create a single post, optionally as a reply. Returns (uri, cid) or (None, None)."""
    text = text.strip()

    reply_ref = None
    if reply_to_uri:
        uri, cid = resolve_post(client, reply_to_uri)
        if not uri or not cid:
            print(f"  Could not resolve reply target: {reply_to_uri}")
            return None, None

        parent_ref = make_strong_ref(uri, cid)

        # Check if the target post is itself a reply (to get the thread root)
        try:
            response = client.app.bsky.feed.get_posts({"uris": [reply_to_uri]})
            if response.posts and response.posts[0].record.reply:
                # Target is a reply — use its root as our root
                root = response.posts[0].record.reply.root
                root_ref = make_strong_ref(root.uri, root.cid)
            else:
                root_ref = parent_ref
        except Exception:
            root_ref = parent_ref

        reply_ref = models.AppBskyFeedPost.ReplyRef(parent=parent_ref, root=root_ref)

    try:
        response = client.send_post(text=text, reply_to=reply_ref)
        print(json.dumps({"uri": response.uri, "cid": response.cid}))
        time.sleep(0.5)
        return response.uri, response.cid
    except Exception as e:
        error_str = str(e)
        if "rate" in error_str.lower() or "RateLimit" in error_str:
            raise RateLimitError(f"Bluesky rate limit hit: {e}")
        print(f"  Post failed: {e}")
        return None, None


def post_thread(client, content):
    """Post a thread (--- separated content). Returns True on success."""
    parts = [p.strip() for p in content.split("---") if p.strip()]

    if not parts:
        print('{"error": "Empty thread content"}')
        return False

    if len(parts) == 1:
        uri, _ = create_post(client, parts[0])
        return uri is not None

    print(f"Posting thread with {len(parts)} parts...")
    root_uri, root_cid = create_post(client, parts[0])
    if not root_uri:
        return False

    root_ref = make_strong_ref(root_uri, root_cid)
    prev_uri = root_uri
    prev_cid = root_cid

    for i, part in enumerate(parts[1:], 2):
        print(f"  Part {i}/{len(parts)}...")
        parent_ref = make_strong_ref(prev_uri, prev_cid)
        reply_ref = models.AppBskyFeedPost.ReplyRef(parent=parent_ref, root=root_ref)

        try:
            response = client.send_post(text=part.strip(), reply_to=reply_ref)
            print(json.dumps({"uri": response.uri, "cid": response.cid}))
            prev_uri = response.uri
            prev_cid = response.cid
            time.sleep(0.5)
        except Exception as e:
            if "rate" in str(e).lower():
                raise RateLimitError(f"Bluesky rate limit hit at part {i}: {e}")
            print(f"  Failed at part {i}: {e}")
            return False

    return True


def parse_reply_header(content):
    """Parse reply target from reply files. Handles:
    - REPLY_TO: at://did:plc:xxx/app.bsky.feed.post/rkey [---] {body}
    - REPLY_TO: {id} [---] {body}
    Returns (reply_to_uri, body) or (None, content).
    """
    lines = content.split("\n")

    # REPLY_TO header (canonical format)
    if lines and lines[0].startswith("REPLY_TO:"):
        reply_to = lines[0].replace("REPLY_TO:", "").strip()
        rest = "\n".join(lines[1:]).strip()
        if rest.startswith("---"):
            rest = rest[3:].strip()
        # Validate: must be AT URI, not a handle
        if not reply_to.startswith("at://"):
            print(f"  ⚠ Invalid reply target '{reply_to}' (must be AT URI, not a handle)")
            return None, rest
        return reply_to, rest

    # AT URI on first line
    if lines and lines[0].strip().startswith("at://"):
        reply_to = lines[0].strip()
        rest = "\n".join(lines[1:]).strip()
        return reply_to, rest

    return None, content


def is_thread(content):
    """Check if content is a thread (has --- separators)."""
    return "---" in content


def validate_content(content):
    """Validate content grapheme length. Returns error message or None if valid."""
    _, body = parse_reply_header(content)
    if is_thread(body):
        parts = [p.strip() for p in body.split("---") if p.strip()]
        for i, part in enumerate(parts, 1):
            length = count_graphemes(part)
            if length > MAX_GRAPHEME_LENGTH:
                return f"Thread part {i} is {length} graphemes (max {MAX_GRAPHEME_LENGTH})"
    else:
        length = count_graphemes(body)
        if length > MAX_GRAPHEME_LENGTH:
            return f"Post is {length} graphemes (max {MAX_GRAPHEME_LENGTH})"
    return None


def process_content(client, content):
    """Process content (post, thread, or reply)."""
    reply_to, body = parse_reply_header(content)
    if reply_to:
        print(f"  Replying to {reply_to}")
        uri, _ = create_post(client, body, reply_to_uri=reply_to)
        return uri is not None
    elif is_thread(body):
        return post_thread(client, body)
    else:
        uri, _ = create_post(client, body)
        return uri is not None


def cmd_post(client, args):
    """Post content from text, file, or queue."""

    # Direct text mode
    if args.text:
        error = validate_content(args.text)
        if error:
            print(f'{{"error": "{error}"}}')
            sys.exit(1)
        try:
            success = process_content(client, args.text)
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
            success = process_content(client, content)
        except RateLimitError as e:
            print(f"WARNING: {e}")
            sys.exit(1)
        sys.exit(0 if success else 1)

    # Queue mode
    POSTED_DIR.mkdir(parents=True, exist_ok=True)
    SKIPPED_DIR.mkdir(parents=True, exist_ok=True)

    all_pending = sorted(OUTPUT_DIR.glob("*.txt"))
    all_pending = [f for f in all_pending if f.is_file() and "posted" not in str(f) and "skipped" not in str(f)]

    all_replies = [f for f in all_pending if f.name.startswith("reply-")]
    all_tweets = [f for f in all_pending if not f.name.startswith("reply-")]

    if not all_tweets and not all_replies:
        print("No pending files")
        sys.exit(0)

    print(f"Queue: {len(all_tweets)} posts, {len(all_replies)} replies")

    posted_tweets = 0
    posted_replies = 0
    skipped = 0

    # Process tweets — skip invalid, keep going until limit posted or queue empty
    for filepath in all_tweets:
        if posted_tweets >= args.limit_tweets:
            break
        print(f"Processing: {filepath.name}")
        content = filepath.read_text().strip()

        error = validate_content(content)
        if error:
            print(f"  Skipping: {error}")
            filepath.rename(SKIPPED_DIR / filepath.name)
            skipped += 1
            continue

        try:
            if process_content(client, content):
                filepath.rename(POSTED_DIR / filepath.name)
                print("  Posted and archived")
                posted_tweets += 1
            else:
                print("  ⚠ Failed, skipping")
                filepath.rename(SKIPPED_DIR / filepath.name)
                skipped += 1
                continue
        except RateLimitError as e:
            print(f"\nWARNING: {e}")
            posted = posted_tweets + posted_replies
            print(f"Posted {posted} before rate limit. Remaining files will be retried next run.")
            sys.exit(0 if posted > 0 else 1)

    # Process replies — same logic
    for filepath in all_replies:
        if posted_replies >= args.limit_replies:
            break
        print(f"Processing: {filepath.name}")
        content = filepath.read_text().strip()

        error = validate_content(content)
        if error:
            print(f"  Skipping: {error}")
            filepath.rename(SKIPPED_DIR / filepath.name)
            skipped += 1
            continue

        try:
            if process_content(client, content):
                filepath.rename(POSTED_DIR / filepath.name)
                print("  Posted and archived")
                posted_replies += 1
            else:
                print("  ⚠ Failed, skipping")
                filepath.rename(SKIPPED_DIR / filepath.name)
                skipped += 1
                continue
        except RateLimitError as e:
            print(f"\nWARNING: {e}")
            posted = posted_tweets + posted_replies
            print(f"Posted {posted} before rate limit. Remaining files will be retried next run.")
            sys.exit(0 if posted > 0 else 1)

    posted = posted_tweets + posted_replies
    print(f"Done: {posted} posted, {skipped} skipped")
    sys.exit(0)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Bluesky integration")

    # Commands (mutually exclusive)
    cmd = parser.add_mutually_exclusive_group(required=True)
    cmd.add_argument("--post", action="store_true", help="Post content from queue or direct")
    cmd.add_argument("--metrics", action="store_true", help="Fetch account metrics")
    cmd.add_argument("--verify", action="store_true", help="Verify credentials")

    # Post options
    parser.add_argument("--limit-tweets", type=int, default=1, help="Max posts/threads to post (default: 1)")
    parser.add_argument("--limit-replies", type=int, default=1, help="Max replies to post (default: 1)")
    parser.add_argument("--text", type=str, help="Post text directly")
    parser.add_argument("--file", type=str, help="Post specific file")

    # Metrics options
    parser.add_argument("--compact", action="store_true", help="One-line metrics summary")

    args = parser.parse_args()
    client = get_client()

    if args.post:
        cmd_post(client, args)
    elif args.metrics:
        cmd_metrics(client, args)
    elif args.verify:
        cmd_verify(client, args)


if __name__ == "__main__":
    main()
