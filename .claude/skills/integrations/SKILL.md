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

### Reply File Format
Reply files use `REPLY_TO:` header with the **numeric tweet ID** (NOT a handle or URL).

```
REPLY_TO: 1893847362910283745

Your reply text here...
```

**NEVER use handles** like `@AnthropicAI` — the API requires numeric IDs matching `^[0-9]{10,}$`.
To find a tweet ID: it's the number at the end of the tweet URL (e.g., `https://x.com/user/status/1893847362910283745`).

Invalid reply targets are auto-skipped to `skipped/`.

### Rate Limits
- Free tier: 17 tweets per 24-hour rolling window (observed limit; official docs say higher but enforcement is stricter)
- Workflow adds 5s delay between posts
- On 429 error, stops processing remaining files

Evidence: Week 1 (2026-02-03) hit 429 after 17th tweet. See `agent/memory/learnings/2026-02-03-x-rate-limits.md`.

## Bluesky Integration

### Credentials
App password authentication (no OAuth complexity).

| Name | Type | Description |
|------|------|-------------|
| `BLUESKY_HANDLE` | var | Bluesky handle (e.g., `user.bsky.social`) |
| `BLUESKY_APP_PASSWORD` | secret | App password (Settings > App Passwords) |

### Rate Limits
- **300 grapheme limit** per post (not characters — emoji/CJK may count differently)
- ~11,666 createRecord calls per day (1,667/hour for repo writes)
- Login: 30 per 5 minutes, 300 per day per handle
- Script adds 0.5s delay between posts

### Reply File Format
Reply files use `REPLY_TO:` header with an **AT URI** (NOT a handle or URL).

```
REPLY_TO: at://did:plc:nphpplr7dcdi4wyjuizmz2wg/app.bsky.feed.post/3mfhgscgm4h2o

Your reply text here...
```

**NEVER use handles** like `@anthropic.com` — the API requires AT URIs starting with `at://`.
Script resolves URI → CID automatically for strong refs.
Invalid reply targets are auto-skipped to `skipped/`.

### Thread Support
Same `---` separator as X. Each part must be under 300 graphemes.
Thread replies chain via `reply.root` (first post) + `reply.parent` (previous post).

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
| Files in `posted/` but not posted | Bad exit code | Check integration script logs |
| Files in `skipped/` | Invalid content (bad reply target, duplicate, etc.) | Check reply format — must use numeric ID (X) or AT URI (Bluesky), not handles |
| Auth errors | Missing credentials | Check `gh variable list` |

## Adding New Platforms

1. Create `agent/integrations/{platform}/post.sh`
   - Takes content as arg: `post.sh "content"`
   - Returns 0 on success, 1 on failure
2. Create `agent/outputs/{platform}/`
3. Add credentials to `process-outputs.yml` env section