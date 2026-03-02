# X (Twitter) Integration

Post tweets via X API v2.

## Authentication Options

### OAuth 1.0a (Preferred)
Stable tokens that don't expire. Recommended for automation.

| Name | Type | Description |
|------|------|-------------|
| `X_API_KEY` | var | Consumer API Key |
| `X_API_KEY_SECRET` | secret | Consumer API Secret |
| `X_ACCESS_TOKEN` | secret | Access Token |
| `X_ACCESS_TOKEN_SECRET` | secret | Access Token Secret |

Setup: Get all 4 from X Developer Portal → Your App → Keys and tokens

### OAuth 2.0 (Fallback)
⚠️ Refresh token rotates on each use - not recommended for automation.

| Name | Type | Description |
|------|------|-------------|
| `X_CLIENT_ID` | var | OAuth 2.0 Client ID |
| `X_CLIENT_SECRET` | secret | OAuth 2.0 Client Secret |
| `X_REFRESH_TOKEN` | secret | Refresh token (rotates!) |

## Scripts

- `post.sh` - Posts tweet (tries OAuth 1.0a first, falls back to 2.0)
- `verify.sh` - Verifies credentials are working
- `auth_2.0.sh` - OAuth 2.0 authorization flow (one-time setup)

## Proxy (Cloudflare bypass)

GitHub Actions runner IPs get blocked by Cloudflare. Set a residential proxy to route API calls through a clean IP.

| Name | Type | Description |
|------|------|-------------|
| `HTTPS_PROXY` | secret | Proxy URL (e.g. `http://user:pass@brd.superproxy.io:22225`) |

Optional. If unset, requests go direct. Credentials are hidden in logs (only host:port shown).

## Rate Limits

**Current tier: X Premium subscription, Free API tier**

- **Real limit: 17 posts per 24 hours** (rolling window, from `x-app-limit-24hour-limit` header)
- Tweet max length: 25,000 chars (set via `X_MAX_TWEET_LENGTH` GitHub var)
- Script checks daily quota before posting and skips if exhausted
- Script adds 0.5s delay between posts to avoid burst limits
- On 429 error: partial success (some posted) exits 0, zero posted exits 1

Note: The `x-rate-limit-*` headers show misleading high numbers (1,080,000). The real
posting limit is in `x-app-limit-24hour-*` and `x-user-limit-24hour-*` headers.

## Usage

```bash
# Post a tweet
./post.sh "Hello world!"

# Verify credentials
./verify.sh
```

## Workflow

1. Agent creates tweet → `agent/outputs/x/tweet-YYYYMMDD-NNN.txt`
2. `process-outputs.yml` calls `post.sh` for each file
3. Posted tweets move to `agent/outputs/x/posted/`