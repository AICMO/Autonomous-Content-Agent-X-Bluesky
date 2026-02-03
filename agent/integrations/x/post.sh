#!/bin/bash
# Post a tweet to X
#
# Why refresh token?
#   - Access token expires in 2 hours (too short for scheduled jobs)
#   - Refresh token lives 6 months
#   - We store refresh token in secrets, get fresh access token on each call
#   - No need to re-authenticate for 6 months
#
# Required env vars:
#   X_CLIENT_ID      - OAuth 2.0 Client ID (authenticates the app)
#   X_CLIENT_SECRET  - OAuth 2.0 Client Secret (authenticates the app)
#   X_REFRESH_TOKEN  - Refresh token from auth.sh (lives 6 months)
#
# Usage:
#   ./post.sh "Your tweet text here"

set -e

if [ -z "$X_CLIENT_ID" ] || [ -z "$X_CLIENT_SECRET" ] || [ -z "$X_REFRESH_TOKEN" ]; then
  echo '{"error": "Missing required env vars: X_CLIENT_ID, X_CLIENT_SECRET, X_REFRESH_TOKEN"}'
  exit 1
fi

if [ -z "$1" ]; then
  echo '{"error": "Usage: ./post.sh \"tweet text\""}'
  exit 1
fi

TWEET_TEXT="$1"

# Get fresh access token using refresh token
TOKEN_RESPONSE=$(curl -s -X POST "https://api.twitter.com/2/oauth2/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "${X_CLIENT_ID}:${X_CLIENT_SECRET}" \
  -d "grant_type=refresh_token&refresh_token=${X_REFRESH_TOKEN}")

ACCESS_TOKEN=$(echo "$TOKEN_RESPONSE" | jq -r '.access_token')
NEW_REFRESH_TOKEN=$(echo "$TOKEN_RESPONSE" | jq -r '.refresh_token')

if [ "$ACCESS_TOKEN" == "null" ] || [ -z "$ACCESS_TOKEN" ]; then
  echo '{"error": "Failed to get access token", "details": '"$TOKEN_RESPONSE"'}'
  exit 1
fi

# Post tweet
curl -s -X POST "https://api.twitter.com/2/tweets" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"$TWEET_TEXT\"}"

# Note: If refresh token rotates, the new one is in NEW_REFRESH_TOKEN
# You may want to update X_REFRESH_TOKEN secret if it changed