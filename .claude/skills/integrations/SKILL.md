---
name: integrations
description: Technical details for external platform integrations (APIs, credentials, rate limits). Use when posting, debugging issues, or adding new integrations.
user-invocable: false
---

# Integrations Technical Skill

## How Posting Works

1. Agent creates files in `agent/outputs/{platform}/`
2. `process-outputs.yml` workflow runs on push
3. Calls `agent/integrations/{platform}/post.sh` for each file
4. Success → file moves to `posted/`
5. Failure → file stays for next run

## X (Twitter) Integration

### Credentials (OAuth 1.0a - preferred)
Stable tokens that don't expire.

| Name | Type | Description |
|------|------|-------------|
| `X_API_KEY` | var | Consumer API Key |
| `X_API_KEY_SECRET` | secret | Consumer API Secret |
| `X_ACCESS_TOKEN` | secret | Access Token |
| `X_ACCESS_TOKEN_SECRET` | secret | Access Token Secret |

### Credentials (OAuth 2.0 - fallback)
⚠️ Refresh token rotates on each use - not recommended.

| Name | Type | Description |
|------|------|-------------|
| `X_CLIENT_ID` | var | OAuth 2.0 Client ID |
| `X_CLIENT_SECRET` | secret | OAuth 2.0 Client Secret |
| `X_REFRESH_TOKEN` | secret | Refresh token (rotates!) |

### Scripts
- `agent/integrations/x/post.sh` - Posts tweet
- `agent/integrations/x/verify.sh` - Verifies credentials

### Rate Limits
- Free tier: 50 tweets per 24 hours
- Workflow adds 5s delay between posts
- On 429 error, stops processing remaining files

## Diagnostics

### Check credentials configured
```bash
gh variable list | grep X_
```
If variables exist, presume secrets are also configured.

### Check posting runs
```bash
gh run list --workflow=process-outputs.yml --limit 5
gh run view <run-id> --log
```

### Common Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| 429 errors | Rate limit | Wait 15+ min |
| Files in `posted/` but not posted | Bad exit code | Check post.sh returns 1 on failure |
| Auth errors | Missing credentials | Check `gh variable list` |

## Adding New Platforms

1. Create `agent/integrations/{platform}/post.sh`
   - Takes content as arg: `post.sh "content"`
   - Returns 0 on success, 1 on failure
2. Create `agent/outputs/{platform}/`
3. Add credentials to `process-outputs.yml` env section