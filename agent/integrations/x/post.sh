#!/bin/bash
# Post single tweets to X from pending files
# NOTE: Does NOT support threads. Use post.py for threads.
#
# Finds tweet-*.txt files in agent/outputs/x/, posts up to LIMIT, moves to posted/
# Skips thread-*.txt files (handled by post.py)
#
# Usage:
#   ./post.sh           # Post 1 file (default)
#   ./post.sh 3         # Post up to 3 files
#   ./post.sh "text"    # Post single text directly (legacy)
#
# OAuth 1.0a (preferred):
#   X_API_KEY, X_API_KEY_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
#
# OAuth 2.0 (fallback):
#   X_CLIENT_ID, X_CLIENT_SECRET, X_REFRESH_TOKEN

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_DIR="$SCRIPT_DIR/../../outputs/x"
POSTED_DIR="$OUTPUT_DIR/posted"
API_URL="https://api.twitter.com/2/tweets"

# Parse argument - number = limit, text = direct post
if [[ "$1" =~ ^[0-9]+$ ]]; then
  LIMIT="$1"
  DIRECT_TEXT=""
elif [ -n "$1" ]; then
  LIMIT=1
  DIRECT_TEXT="$1"
else
  LIMIT=1
  DIRECT_TEXT=""
fi

# Post a single tweet, return 0 on success
post_tweet() {
  local TEXT="$1"
  local JSON_BODY=$(jq -n --arg text "$TEXT" '{"text": $text}')

  # OAuth 1.0a - preferred
  if [ -n "$X_API_KEY" ] && [ -n "$X_API_KEY_SECRET" ] && [ -n "$X_ACCESS_TOKEN" ] && [ -n "$X_ACCESS_TOKEN_SECRET" ]; then
    NONCE=$(openssl rand -hex 16)
    TIMESTAMP=$(date +%s)

    urlencode() {
      python3 -c "import urllib.parse; print(urllib.parse.quote('$1', safe=''))"
    }

    OAUTH_PARAMS="oauth_consumer_key=$X_API_KEY"
    OAUTH_PARAMS="$OAUTH_PARAMS&oauth_nonce=$NONCE"
    OAUTH_PARAMS="$OAUTH_PARAMS&oauth_signature_method=HMAC-SHA1"
    OAUTH_PARAMS="$OAUTH_PARAMS&oauth_timestamp=$TIMESTAMP"
    OAUTH_PARAMS="$OAUTH_PARAMS&oauth_token=$X_ACCESS_TOKEN"
    OAUTH_PARAMS="$OAUTH_PARAMS&oauth_version=1.0"

    BASE_STRING="POST&$(urlencode "$API_URL")&$(urlencode "$OAUTH_PARAMS")"
    SIGNING_KEY="$(urlencode "$X_API_KEY_SECRET")&$(urlencode "$X_ACCESS_TOKEN_SECRET")"
    SIGNATURE=$(echo -n "$BASE_STRING" | openssl dgst -sha1 -hmac "$SIGNING_KEY" -binary | base64)
    SIGNATURE_ENCODED=$(urlencode "$SIGNATURE")

    AUTH_HEADER="OAuth oauth_consumer_key=\"$X_API_KEY\""
    AUTH_HEADER="$AUTH_HEADER, oauth_nonce=\"$NONCE\""
    AUTH_HEADER="$AUTH_HEADER, oauth_signature=\"$SIGNATURE_ENCODED\""
    AUTH_HEADER="$AUTH_HEADER, oauth_signature_method=\"HMAC-SHA1\""
    AUTH_HEADER="$AUTH_HEADER, oauth_timestamp=\"$TIMESTAMP\""
    AUTH_HEADER="$AUTH_HEADER, oauth_token=\"$X_ACCESS_TOKEN\""
    AUTH_HEADER="$AUTH_HEADER, oauth_version=\"1.0\""

    RESPONSE=$(curl -s -X POST "$API_URL" \
      -H "Authorization: $AUTH_HEADER" \
      -H "Content-Type: application/json" \
      -d "$JSON_BODY")

  # OAuth 2.0 - fallback
  elif [ -n "$X_CLIENT_ID" ] && [ -n "$X_CLIENT_SECRET" ] && [ -n "$X_REFRESH_TOKEN" ]; then
    TOKEN_CACHE="/tmp/.x_token"

    if [ -f "$TOKEN_CACHE" ]; then
      ACCESS_TOKEN=$(cat "$TOKEN_CACHE")
    else
      TOKEN_RESPONSE=$(curl -s -X POST "https://api.twitter.com/2/oauth2/token" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -u "${X_CLIENT_ID}:${X_CLIENT_SECRET}" \
        -d "grant_type=refresh_token&refresh_token=${X_REFRESH_TOKEN}")

      ACCESS_TOKEN=$(echo "$TOKEN_RESPONSE" | jq -r '.access_token')

      if [ "$ACCESS_TOKEN" == "null" ] || [ -z "$ACCESS_TOKEN" ]; then
        echo '{"error": "Failed to get access token"}'
        return 1
      fi
      echo "$ACCESS_TOKEN" > "$TOKEN_CACHE"
    fi

    RESPONSE=$(curl -s -X POST "$API_URL" \
      -H "Authorization: Bearer $ACCESS_TOKEN" \
      -H "Content-Type: application/json" \
      -d "$JSON_BODY")
  else
    echo '{"error": "Missing credentials"}'
    return 1
  fi

  echo "$RESPONSE"

  # Check for errors
  if echo "$RESPONSE" | jq -e '.errors' > /dev/null 2>&1; then return 1; fi
  if echo "$RESPONSE" | jq -e '.error' > /dev/null 2>&1; then return 1; fi
  if echo "$RESPONSE" | jq -e '.title' > /dev/null 2>&1; then return 1; fi
  if ! echo "$RESPONSE" | jq -e '.data.id' > /dev/null 2>&1; then return 1; fi
  return 0
}

# Direct text mode (legacy)
if [ -n "$DIRECT_TEXT" ]; then
  post_tweet "$DIRECT_TEXT"
  exit $?
fi

# Find and post pending tweet files (skip thread files)
mkdir -p "$POSTED_DIR"
PENDING=$(find "$OUTPUT_DIR" -maxdepth 1 -type f -name "tweet-*.txt" 2>/dev/null | sort | head -n "$LIMIT")

if [ -z "$PENDING" ]; then
  echo "No pending files"
  exit 0
fi

POSTED=0
FAILED=0

for FILE in $PENDING; do
  FILENAME=$(basename "$FILE")
  echo "Processing: $FILENAME"

  TEXT=$(cat "$FILE")

  if post_tweet "$TEXT"; then
    mv "$FILE" "$POSTED_DIR/"
    echo "  ✓ Posted and archived"
    POSTED=$((POSTED + 1))
  else
    echo "  ✗ Failed"
    FAILED=1
    break
  fi
done

echo "Posted: $POSTED/$LIMIT"
exit $FAILED