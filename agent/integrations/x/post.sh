#!/bin/bash
# Post a tweet to X
#
# Supports OAuth 1.0a (preferred) or OAuth 2.0 (fallback)
#
# OAuth 1.0a (stable tokens, no expiry):
#   X_API_KEY            - Consumer API Key
#   X_API_KEY_SECRET     - Consumer API Key Secret
#   X_ACCESS_TOKEN       - Access Token
#   X_ACCESS_TOKEN_SECRET - Access Token Secret
#
# OAuth 2.0 (tokens rotate on use):
#   X_CLIENT_ID      - OAuth 2.0 Client ID
#   X_CLIENT_SECRET  - OAuth 2.0 Client Secret
#   X_REFRESH_TOKEN  - Refresh token (rotates!)
#
# Usage:
#   ./post.sh "Your tweet text here"

set -e

if [ -z "$1" ]; then
  echo '{"error": "Usage: ./post.sh \"tweet text\""}'
  exit 1
fi

TWEET_TEXT="$1"
API_URL="https://api.twitter.com/2/tweets"
JSON_BODY=$(jq -n --arg text "$TWEET_TEXT" '{"text": $text}')

# OAuth 1.0a - preferred (stable tokens)
if [ -n "$X_API_KEY" ] && [ -n "$X_API_KEY_SECRET" ] && [ -n "$X_ACCESS_TOKEN" ] && [ -n "$X_ACCESS_TOKEN_SECRET" ]; then

  # Generate OAuth 1.0a signature
  NONCE=$(openssl rand -hex 16)
  TIMESTAMP=$(date +%s)
  METHOD="POST"

  # URL encode function
  urlencode() {
    python3 -c "import urllib.parse; print(urllib.parse.quote('$1', safe=''))"
  }

  # OAuth parameters (sorted alphabetically)
  OAUTH_PARAMS="oauth_consumer_key=$X_API_KEY"
  OAUTH_PARAMS="$OAUTH_PARAMS&oauth_nonce=$NONCE"
  OAUTH_PARAMS="$OAUTH_PARAMS&oauth_signature_method=HMAC-SHA1"
  OAUTH_PARAMS="$OAUTH_PARAMS&oauth_timestamp=$TIMESTAMP"
  OAUTH_PARAMS="$OAUTH_PARAMS&oauth_token=$X_ACCESS_TOKEN"
  OAUTH_PARAMS="$OAUTH_PARAMS&oauth_version=1.0"

  # Create signature base string
  BASE_STRING="$METHOD&$(urlencode "$API_URL")&$(urlencode "$OAUTH_PARAMS")"

  # Create signing key
  SIGNING_KEY="$(urlencode "$X_API_KEY_SECRET")&$(urlencode "$X_ACCESS_TOKEN_SECRET")"

  # Generate signature
  SIGNATURE=$(echo -n "$BASE_STRING" | openssl dgst -sha1 -hmac "$SIGNING_KEY" -binary | base64)
  SIGNATURE_ENCODED=$(urlencode "$SIGNATURE")

  # Build Authorization header
  AUTH_HEADER="OAuth oauth_consumer_key=\"$X_API_KEY\""
  AUTH_HEADER="$AUTH_HEADER, oauth_nonce=\"$NONCE\""
  AUTH_HEADER="$AUTH_HEADER, oauth_signature=\"$SIGNATURE_ENCODED\""
  AUTH_HEADER="$AUTH_HEADER, oauth_signature_method=\"HMAC-SHA1\""
  AUTH_HEADER="$AUTH_HEADER, oauth_timestamp=\"$TIMESTAMP\""
  AUTH_HEADER="$AUTH_HEADER, oauth_token=\"$X_ACCESS_TOKEN\""
  AUTH_HEADER="$AUTH_HEADER, oauth_version=\"1.0\""

  curl -s -X POST "$API_URL" \
    -H "Authorization: $AUTH_HEADER" \
    -H "Content-Type: application/json" \
    -d "$JSON_BODY"

# OAuth 2.0 - fallback (tokens rotate)
elif [ -n "$X_CLIENT_ID" ] && [ -n "$X_CLIENT_SECRET" ] && [ -n "$X_REFRESH_TOKEN" ]; then

  TOKEN_CACHE="/tmp/.x_token"

  # Use cached token if exists, otherwise refresh
  if [ -f "$TOKEN_CACHE" ]; then
    ACCESS_TOKEN=$(cat "$TOKEN_CACHE")
  else
    TOKEN_RESPONSE=$(curl -s -X POST "https://api.twitter.com/2/oauth2/token" \
      -H "Content-Type: application/x-www-form-urlencoded" \
      -u "${X_CLIENT_ID}:${X_CLIENT_SECRET}" \
      -d "grant_type=refresh_token&refresh_token=${X_REFRESH_TOKEN}")

    ACCESS_TOKEN=$(echo "$TOKEN_RESPONSE" | jq -r '.access_token')

    if [ "$ACCESS_TOKEN" == "null" ] || [ -z "$ACCESS_TOKEN" ]; then
      echo '{"error": "Failed to get access token", "details": '"$TOKEN_RESPONSE"'}'
      exit 1
    fi

    echo "$ACCESS_TOKEN" > "$TOKEN_CACHE"
  fi

  curl -s -X POST "$API_URL" \
    -H "Authorization: Bearer $ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d "$JSON_BODY"

else
  echo '{"error": "Missing credentials. Need OAuth 1.0a (X_API_KEY, X_API_KEY_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET) or OAuth 2.0 (X_CLIENT_ID, X_CLIENT_SECRET, X_REFRESH_TOKEN)"}'
  exit 1
fi