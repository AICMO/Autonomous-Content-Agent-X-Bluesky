#!/bin/bash
# X OAuth 2.0 PKCE Authentication
# One-time setup to get access_token and refresh_token
#
# Required env vars:
#   X_CLIENT_ID
#   X_CLIENT_SECRET
#
# Usage:
#   export X_CLIENT_ID="your_client_id"
#   export X_CLIENT_SECRET="your_client_secret"
#   ./auth.sh

set -e

if [ -z "$X_CLIENT_ID" ] || [ -z "$X_CLIENT_SECRET" ]; then
  echo "Error: X_CLIENT_ID and X_CLIENT_SECRET must be set"
  exit 1
fi

REDIRECT_URI="http://localhost:3000/callback"
SCOPES="tweet.read%20tweet.write%20users.read%20offline.access"

# Generate PKCE codes
CODE_VERIFIER=$(openssl rand -base64 32 | tr -d '=+/' | cut -c1-43)
CODE_CHALLENGE=$(echo -n "$CODE_VERIFIER" | openssl sha256 -binary | base64 | tr -d '=' | tr '+/' '-_')

echo "================================================"
echo "X OAuth 2.0 PKCE Authentication"
echo "================================================"
echo ""
echo "Step 1: Open this URL in your browser:"
echo ""
echo "https://twitter.com/i/oauth2/authorize?response_type=code&client_id=${X_CLIENT_ID}&redirect_uri=${REDIRECT_URI}&scope=${SCOPES}&state=state&code_challenge=${CODE_CHALLENGE}&code_challenge_method=S256"
echo ""
echo "Step 2: Authorize the app"
echo ""
echo "Step 3: You'll be redirected to localhost (will fail to load - that's OK)"
echo "        Copy the 'code' parameter from the URL"
echo "        Example: http://localhost:3000/callback?state=state&code=XXXXXX"
echo ""
read -p "Paste the code here: " AUTH_CODE

if [ -z "$AUTH_CODE" ]; then
  echo "Error: No code provided"
  exit 1
fi

echo ""
echo "Exchanging code for tokens..."
echo ""

# Exchange code for tokens
curl -s -X POST "https://api.twitter.com/2/oauth2/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "${X_CLIENT_ID}:${X_CLIENT_SECRET}" \
  -d "code=${AUTH_CODE}&grant_type=authorization_code&redirect_uri=${REDIRECT_URI}&code_verifier=${CODE_VERIFIER}"

echo ""
echo ""
echo "================================================"
echo "Save the refresh_token to GitHub secrets as X_REFRESH_TOKEN"
echo "================================================"