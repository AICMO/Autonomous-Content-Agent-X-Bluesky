#!/bin/bash
# Post a thread to X
#
# Thread format: Multiple tweets separated by ---
# Character limit set by X_MAX_TWEET_LENGTH env var (default: 25000 for Premium, 280 for free)
#
# Usage:
#   ./post-thread.sh "$(cat thread-file.txt)"
#
# Example thread file:
#   First tweet of the thread (this is the hook)
#   ---
#   Second tweet replying to first
#   ---
#   Third tweet replying to second
#   ---
#   Final tweet with call to action 🧵

set -e

if [ -z "$1" ]; then
  echo '{"error": "Usage: ./post-thread.sh \"thread content with --- separators\""}'
  exit 1
fi

THREAD_CONTENT="$1"
API_URL="https://api.twitter.com/2/tweets"

# Verify OAuth 1.0a credentials
if [ -z "$X_API_KEY" ] || [ -z "$X_API_KEY_SECRET" ] || [ -z "$X_ACCESS_TOKEN" ] || [ -z "$X_ACCESS_TOKEN_SECRET" ]; then
  echo '{"error": "Missing OAuth 1.0a credentials"}'
  exit 1
fi

# URL encode function
urlencode() {
  python3 -c "import urllib.parse; print(urllib.parse.quote('$1', safe=''))"
}

# Function to post a single tweet (optionally replying to another)
post_tweet() {
  local TWEET_TEXT="$1"
  local REPLY_TO="$2"

  # Build JSON body
  if [ -n "$REPLY_TO" ]; then
    JSON_BODY=$(jq -n --arg text "$TWEET_TEXT" --arg reply "$REPLY_TO" '{"text": $text, "reply": {"in_reply_to_tweet_id": $reply}}')
  else
    JSON_BODY=$(jq -n --arg text "$TWEET_TEXT" '{"text": $text}')
  fi

  # Generate OAuth 1.0a signature
  NONCE=$(openssl rand -hex 16)
  TIMESTAMP=$(date +%s)
  METHOD="POST"

  OAUTH_PARAMS="oauth_consumer_key=$X_API_KEY"
  OAUTH_PARAMS="$OAUTH_PARAMS&oauth_nonce=$NONCE"
  OAUTH_PARAMS="$OAUTH_PARAMS&oauth_signature_method=HMAC-SHA1"
  OAUTH_PARAMS="$OAUTH_PARAMS&oauth_timestamp=$TIMESTAMP"
  OAUTH_PARAMS="$OAUTH_PARAMS&oauth_token=$X_ACCESS_TOKEN"
  OAUTH_PARAMS="$OAUTH_PARAMS&oauth_version=1.0"

  BASE_STRING="$METHOD&$(urlencode "$API_URL")&$(urlencode "$OAUTH_PARAMS")"
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

  echo "$RESPONSE"

  # Check for errors
  if echo "$RESPONSE" | jq -e '.errors' > /dev/null 2>&1; then
    return 1
  fi
  if echo "$RESPONSE" | jq -e '.error' > /dev/null 2>&1; then
    return 1
  fi
  if ! echo "$RESPONSE" | jq -e '.data.id' > /dev/null 2>&1; then
    return 1
  fi

  # Return the tweet ID for threading
  echo "$RESPONSE" | jq -r '.data.id'
  return 0
}

# Split thread content by --- separator
IFS=$'\n' read -rd '' -a TWEETS <<< "$(echo "$THREAD_CONTENT" | awk 'BEGIN{RS="---"} {gsub(/^[ \t\n]+|[ \t\n]+$/, ""); if(length>0) print}')" || true

if [ ${#TWEETS[@]} -lt 2 ]; then
  echo '{"error": "Thread must have at least 2 tweets separated by ---"}'
  exit 1
fi

echo "Posting thread with ${#TWEETS[@]} tweets..."

PREVIOUS_ID=""
THREAD_IDS=()

for i in "${!TWEETS[@]}"; do
  TWEET="${TWEETS[$i]}"

  # Skip empty tweets
  if [ -z "$TWEET" ]; then
    continue
  fi

  echo "  Tweet $((i+1))/${#TWEETS[@]}: ${TWEET:0:50}..."

  RESULT=$(post_tweet "$TWEET" "$PREVIOUS_ID")

  # Extract the tweet ID from the last line of output
  NEW_ID=$(echo "$RESULT" | tail -1)

  if [ -z "$NEW_ID" ] || [ "$NEW_ID" == "null" ]; then
    echo "  ✗ Failed to post tweet $((i+1))"
    echo "$RESULT"
    exit 1
  fi

  THREAD_IDS+=("$NEW_ID")
  PREVIOUS_ID="$NEW_ID"

  echo "  ✓ Posted (ID: $NEW_ID)"

  # Brief pause between tweets to respect rate limits
  sleep 2
done

echo "Thread posted successfully! ${#THREAD_IDS[@]} tweets"
echo '{"success": true, "tweet_count": '${#THREAD_IDS[@]}'}'
exit 0
