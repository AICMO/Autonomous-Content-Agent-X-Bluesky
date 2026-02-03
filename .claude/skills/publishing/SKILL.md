---
name: publishing
description: Rules for publishing to external platforms (X, LinkedIn, etc.). Use when creating posts, managing outputs, or working with integrations.
user-invocable: false
---

# Publishing to External Platforms

## Publishing Flow
Content in `agent/outputs/{platform}/` is automatically posted by `process-outputs.yml`:

```
agent/outputs/x/tweet-20260203-001.txt  →  posted  →  agent/outputs/x/posted/tweet-20260203-001.txt
```

### File Naming Convention
Use date-based naming: `{type}-{YYYYMMDD}-{NNN}.txt`
- `tweet-20260203-001.txt` - first tweet created on Feb 3, 2026
- `tweet-20260203-002.txt` - second tweet created same day

❌ Don't use: `tweet-week2-001.txt`, `tweet-monday.txt` (becomes meaningless after posting)

**Rules:**
- ✅ Create new files in `agent/outputs/{platform}/`
- ✅ Read files in `posted/` to check what was published
- ❌ NEVER move files back from `posted/` - managed by publish workflow only
- ❌ NEVER delete files from `posted/`

If a post failed, create a NEW file - don't retry old files.

## Content Voice
Frame as: **human building products with autonomous tools** (not "AI doing everything").

**Use motivational verbs:** creating, building, generating, exploring, shipping, launching
**Avoid:** testing, experimenting, trying (passive/uncertain language)
**Always say:** product, tool, solution (never "content")

✅ Good: "Exploring vibe coding with autonomous agents to ship faster"
✅ Good: "Building automated workflows - here's what's working"
✅ Good: "Shipping tools with AI-assisted development" + link to repo

❌ Bad: "I'm an AI agent, no human writes these tweets"
❌ Bad: "Testing if this works..."
❌ Bad: "Creating content..."

The story is human innovation, not AI replacement.

## Author Info
To reference/promote repo owner, use `gh api users/{owner}` for social links.
Never hardcode or guess links.

Additional links (not in GitHub API):
- LinkedIn: https://www.linkedin.com/in/eiosifov

## Promotional Content
Occasionally (~20% of posts) include soft promotion of:
- **This repo** - link to the autonomous agent experiment
- **Author's profile** - GitHub, LinkedIn, blog (get from `gh api users/{owner}`)
- **Author's products** - if mentioned in repo or profile

Examples:
- "Building this in public → [repo link]"
- "More on my approach → [blog/profile link]"
- "Follow the journey → [GitHub link]"

Keep it natural, not salesy. Tie promotions to value (learnings, insights, tools).

## X Integration

### Credentials (OAuth 1.0a - preferred)
| Type | Name | Description |
|------|------|-------------|
| var | `X_API_KEY` | Consumer API Key |
| secret | `X_API_KEY_SECRET` | Consumer API Secret |
| secret | `X_ACCESS_TOKEN` | Access Token |
| secret | `X_ACCESS_TOKEN_SECRET` | Access Token Secret |

### Credentials (OAuth 2.0 - fallback)
| Type | Name | Description |
|------|------|-------------|
| var | `X_CLIENT_ID` | OAuth 2.0 Client ID |
| secret | `X_CLIENT_SECRET` | OAuth 2.0 Client Secret |
| secret | `X_REFRESH_TOKEN` | Refresh token (rotates on use!) |

### Files
- Scripts: `agent/integrations/x/post.sh`, `verify.sh`
- Output: `agent/outputs/x/*.txt`
- Posted: `agent/outputs/x/posted/`

## Gist Fallback
When no platform integration exists, use GitHub Gist:

```bash
gh gist create --public -f "filename.md" content.md
gh gist edit <gist-id> -f "filename.md" updated.md
gh gist list
```

Track all gist URLs in state file under "## External Outputs".