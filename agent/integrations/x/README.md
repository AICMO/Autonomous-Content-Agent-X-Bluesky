# X (Twitter) Integration

Post tweets via X API v2.

## Required Secrets/Vars

| Name | Type | Description |
|------|------|-------------|
| `X_CLIENT_ID` | var | OAuth 2.0 Client ID |
| `X_CLIENT_SECRET` | secret | OAuth 2.0 Client Secret |
| `X_REFRESH_TOKEN` | secret | Refresh token (from auth.sh) |

## Setup

1. Run auth flow once locally:
   ```bash
   export X_CLIENT_ID="your_client_id"
   export X_CLIENT_SECRET="your_client_secret"
   ./auth.sh
   ```

2. Save the `refresh_token` to GitHub secrets as `X_REFRESH_TOKEN`

## Agent Workflow

1. Agent creates tweet → saves to `agent/outputs/x/tweet-TIMESTAMP.txt`
2. Workflow reads from `agent/outputs/x/`, posts via `post.sh`
3. Posted tweets moved to `agent/outputs/x/posted/`

## Manual Usage

```bash
./post.sh "Hello world!"
```

## Token Lifetime

- Access token: 2 hours (auto-refreshed by post.sh)
- Refresh token: 6 months

## Note

X may rotate refresh tokens. If posts start failing after ~6 months, re-run `auth.sh`.