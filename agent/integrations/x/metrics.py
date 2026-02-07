#!/usr/bin/env python3
"""
Fetch account metrics from X API.

Usage:
    ./metrics.py              # Print metrics as JSON
    ./metrics.py --compact    # Print one-line summary

Environment:
    X_API_KEY, X_API_KEY_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
"""

import os
import sys
import json
import argparse

try:
    from requests_oauthlib import OAuth1Session
except ImportError:
    print('{"error": "Missing requests-oauthlib. Run: pip install requests requests-oauthlib"}')
    sys.exit(1)

API_URL = "https://api.twitter.com/2/users/me"


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


def fetch_metrics(session):
    """Fetch public metrics for the authenticated user."""
    response = session.get(API_URL, params={"user.fields": "public_metrics"})

    if not response.text:
        return {"error": "Empty response (likely rate limited)", "status": response.status_code}

    try:
        data = response.json()
    except Exception:
        return {"error": f"Invalid JSON: {response.text[:200]}", "status": response.status_code}

    if response.status_code != 200:
        return {"error": data, "status": response.status_code}

    user = data.get("data", {})
    metrics = user.get("public_metrics", {})

    return {
        "username": user.get("username"),
        "name": user.get("name"),
        "followers": metrics.get("followers_count"),
        "following": metrics.get("following_count"),
        "tweets": metrics.get("tweet_count"),
        "listed": metrics.get("listed_count"),
    }


def main():
    parser = argparse.ArgumentParser(description="Fetch X account metrics")
    parser.add_argument("--compact", action="store_true", help="One-line summary")
    args = parser.parse_args()

    session = get_oauth_session()
    metrics = fetch_metrics(session)

    if "error" in metrics:
        print(json.dumps(metrics, indent=2))
        sys.exit(1)

    if args.compact:
        print(f"@{metrics['username']}: {metrics['followers']} followers, {metrics['following']} following, {metrics['tweets']} tweets")
    else:
        print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
