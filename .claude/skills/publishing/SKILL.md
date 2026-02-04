---
name: publishing
description: Content strategy for external platforms (X, LinkedIn, etc.). Voice, style, and growth strategies.
user-invocable: false
---

# Publishing Content Strategy

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

### Posting Cadence
**Current approach:** One post per session/PR

Rationale:
- Distributed posting = better engagement
- Each post gets its own algorithm window
- Avoids rate limits

Note: Research suggests 3-5 posts/day optimal. Test and adjust based on data.

### File Rules
Agent creates files. Workflow handles posting.

- ✅ Create new files in `agent/outputs/{platform}/`
- ✅ Read files in `posted/` to check what was published
- ✅ Modify/rename own files before they're posted
- ❌ NEVER remove/modify files in `posted/`
- ❌ NEVER delete files (no `rm` permission)
- ❌ NEVER try to post (workflow does this)

Workflow responsibility: posting, moving to `posted/`, handling failures, cleanup.

### Supported Formats
- ✅ Single tweets (≤280 chars) - `tweet-YYYYMMDD-NNN.txt`
- ✅ Threads (--- separated) - `thread-YYYYMMDD-NNN.txt`

**Thread format:**
```
First tweet text here
---
Second tweet (reply to first)
---
Third tweet (reply to second)
```

**Thread quota warning:** 10-part thread = 10 tweets against rate limit.

### Know Your Permissions
Read `.github/workflows/agent-work.yml` to see `--allowed-tools`.
Don't attempt commands not in the list (e.g., `rm` is not allowed).

---

## Growth Strategies

### Build in Public (BIP)
Evaluate if current repo/project is BIP-worthy. If yes, determine cadence.

**BIP evaluation criteria:**
- Is repo public?
- Is work interesting/novel?
- Are there learnings worth sharing?
- Would audience find it valuable?

**If BIP-worthy → post often.** BIP thrives on frequency and consistency.

**If BIP-worthy, posts can include:**
- What was done/learned this session
- Conclusions or findings
- Repo/PR link for proof
- Metrics updates
- Explain the idea/concept (for new followers)
- How it started, where it is now
- Repo promotion with context

**What to share:**
- Progress and metrics (followers, engagement)
- Learnings (what worked, what didn't)
- Behind-the-scenes (how it works)
- Failures and pivots (authenticity builds trust)

**Why BIP works:**
- Public repo = built-in proof
- People root for underdogs
- Vulnerability creates connection
- The journey IS the content

### 3-Bucket Content Strategy
Balance three content types for maximum reach:

| Bucket | Purpose | Example |
|--------|---------|---------|
| **Authority** | Build credibility | Frameworks, how-tos, insights |
| **Personality** | Build connection | Stories, opinions, behind-scenes |
| **Shareability** | Expand reach | Hot takes, relatable moments |

Missing any bucket limits audience growth.

### Hook Engineering
First line determines if anyone reads. Engineer hooks, don't just write them.

**Hook formula:** Bold Statement + Tension + Credibility

❌ Weak: "I want to share my thoughts on growing on Twitter."
✅ Strong: "I went from 0 to 10,000 followers in 57 days without posting a single thread. Here's exactly how."

**Hook patterns that work:**
- Specific numbers: "5 things I learned..."
- Contrarian: "Most people are wrong about..."
- Story opener: "Last week I failed publicly..."
- Question: "Why do 90% of accounts never grow?"

### Thread Strategy
Threads get 63% more impressions than single tweets.

**Structure:**
- Hook (tweet 1) - Must stop the scroll
- Value (tweets 2-4) - Deliver on the promise
- CTA (final tweet) - Follow, share, or link

**Rules:**
- 3-5 tweets optimal (sweet spot)
- Under 250 chars per tweet (under 200 better)
- Cliffhanger every 1-2 tweets
- Zero hashtags in main content
- Use 1x/week for deeper content

---

## Algorithm Awareness

### What X rewards (2025)
| Factor | Impact |
|--------|--------|
| Reply-to-reply | 75x multiplier |
| Retweets | Worth 20 likes |
| Video (10+ sec) | 10x engagement |
| Early engagement | First 30 min critical |
| Threads | 40-60% more reach |

### What hurts reach
- External links (algorithm downgrades)
- Heavy hashtags
- Posting and leaving (no engagement)

---

## Content Voice
Frame as: **human building products with autonomous tools** (not "AI doing everything").

**Use:** creating, building, generating, exploring, shipping, launching
**Avoid:** testing, experimenting, trying (passive/uncertain)
**Say:** product, tool, solution (never "content")

✅ "Exploring vibe coding with autonomous agents to ship faster"
✅ "Building automated workflows - here's what's working"
❌ "I'm an AI agent, no human writes these tweets"
❌ "Testing if this works..."

The story is human innovation, not AI replacement.

---

## Author Info
To reference/promote repo owner:
```bash
gh api users/{owner}
```
For links not in GitHub API, see `ME.md`.
Never hardcode or guess links.

## Promotional Content
~20% of posts include soft promotion:
- **This repo** - link to the autonomous agent experiment
- **Author's profile** - GitHub, LinkedIn, blog
- **Author's products** - if mentioned in repo/profile

Examples:
- "Building this in public → [repo link]"
- "More on my approach → [blog/profile link]"

Keep natural, not salesy. Tie to value.

---

## Gist Fallback
When no platform integration exists:

```bash
gh gist create --public -f "filename.md" content.md
gh gist edit <gist-id> -f "filename.md" updated.md
```

Track gist URLs in state file under "## External Outputs".
