# Learning: X API Integration Issues

Date: 2026-02-03
Category: Technical / Integration

## What Happened

Attempted to post 11 tweets via the process-outputs.yml workflow. The X API integration failed for all posts.

## Root Causes Identified

### 1. OAuth 2.0 Refresh Token Invalid
```
{"error": "Failed to get access token", "details": {"error":"invalid_request","error_description":"Value passed for the token was invalid."}}
```

**Why**: The X_REFRESH_TOKEN secret is either expired, revoked, or was never properly configured.

**Note from SKILL.md**: OAuth 2.0 tokens "rotate on use" - if the token was used once and the new token wasn't saved, subsequent uses will fail.

### 2. OAuth 1.0a Not Configured
The workflow logs show only OAuth 2.0 vars set (X_CLIENT_ID), meaning OAuth 1.0a credentials (X_API_KEY, X_API_KEY_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET) are not configured.

OAuth 1.0a is listed as "preferred" in SKILL.md because tokens are stable and don't expire/rotate.

### 3. Workflow Bug - False Positives
The process-outputs.yml workflow has a logic bug:
```bash
if "$integration_script" "$(cat "$file")"; then
  mv "$file" "${output_dir}posted/"
```

The script returns exit code 0 even when X API returns an error, because:
- curl succeeds (HTTP request completed)
- Script doesn't check the HTTP response for errors

**Result**: Files get moved to `posted/` even when posting fails, making it appear successful.

### 4. JSON Encoding Issue
First tweet attempt returned:
```
{"errors":[{"message":"Request body is not valid JSON."}]}
```

The post.sh script uses:
```bash
JSON_BODY=$(jq -n --arg text "$TWEET_TEXT" '{"text": $text}')
```

This should work, but the error suggests something is wrong with how the tweet text is being passed. Possible issues:
- Special characters in tweet text not being escaped
- Newlines in the tweet causing issues

## Recommendations

### Immediate (Requires Repo Owner)
1. Configure OAuth 1.0a credentials (stable tokens):
   - `X_API_KEY` (var)
   - `X_API_KEY_SECRET` (secret)
   - `X_ACCESS_TOKEN` (secret)
   - `X_ACCESS_TOKEN_SECRET` (secret)

### Agent Can Fix (Workflow Error Fix Exception)
1. Fix post.sh to check HTTP response and return proper exit code
2. Fix process-outputs.yml to not move files on API error

## Impact

- 11 tweets written but not posted
- Files moved to `posted/` directory incorrectly
- No actual X presence established
- Timeline: 2 days into 180-day goal with 0 progress

## Next Steps

1. Document this blocker in state file
2. Create new tweet files following voice guidelines (since old ones are in `posted/`)
3. Wait for repo owner to configure X API credentials
4. Consider fixing workflow bugs under "Workflow Error Fix Exception"
