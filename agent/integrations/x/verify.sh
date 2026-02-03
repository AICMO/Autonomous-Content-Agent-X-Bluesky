#!/bin/bash
# Verify X credentials and show account info

set -e

if [ -z "$X_API_KEY" ] || [ -z "$X_API_KEY_SECRET" ] || [ -z "$X_ACCESS_TOKEN" ] || [ -z "$X_ACCESS_TOKEN_SECRET" ]; then
  echo '{"error": "Missing env vars: X_API_KEY, X_API_KEY_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET"}'
  exit 1
fi

API_URL="https://api.twitter.com/2/users/me"
METHOD="GET"

# URL encode function
urlencode() {
  python3 -c "import urllib.parse; print(urllib.parse.quote('$1', safe=''))"
}

# Generate OAuth 1.0a signature
NONCE=$(openssl rand -hex 16)
TIMESTAMP=$(date +%s)

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

curl -s "$API_URL" -H "Authorization: $AUTH_HEADER"