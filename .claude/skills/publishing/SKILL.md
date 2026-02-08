---
name: publishing
description: Content strategy for external platforms (X, LinkedIn, etc.). Voice, style, and growth strategies.
user-invocable: false
---

# Publishing Content Strategy

> Create original posts, voice, strategy

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

### Queue Management (Updated Week 3)
**Hard rules:**
1. **If total pending queue > 15: CREATE ZERO NEW CONTENT.** Spend the session on research, profile optimization, reading, or skill development instead.
2. **Max 2 content pieces per session** (when queue is under 15).
3. **Max 5 pending replies at any time.** Reply timeliness is critical — a reply posted 48+ hours after the original is nearly worthless.

Why: Week 1 burst (16 tweets) hit rate limits. Week 3 queue ballooned to 53 pending items despite "max 3/PR" rule being in place — sessions ignored it. Stale replies lose 95%+ of their algorithmic value.

Evidence:
- Week 1: `agent/memory/learnings/2026-02-03-x-rate-limits.md`
- Week 3: Queue reached 53 pending (30 tweets + 23 replies). Sessions #30-35 created 5-8 pieces each, overriding the queue cap. Replies to posts from days prior provide negligible visibility.
- `agent/memory/learnings/retro-weekly-2026-02-08.md`

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
- ✅ Single tweets - `tweet-YYYYMMDD-NNN.txt` (limit set by `X_MAX_TWEET_LENGTH` var, default 25000 for Premium)
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

## Value Rule: Never Mix Value Types

A post delivers value in one of two ways. **Pick one per post. Never both.**

| Type | Value source | Example |
|------|-------------|---------|
| **Content value** | The post itself teaches, explains, or provokes thought. Reader gets value from the content (text, image, video). | "Opus 4.6 and GPT-5.3 Codex dropped within minutes. Here's what convergence means for agentic coding..." |
| **Outcome value** | The link/promotion gives the reader something useful — a tool, repo, template, resource. | "I open-sourced the PDCA loop + state management setup I use for autonomous agents → [repo link]" |

**Why not both?** Mixing them dilutes each. The insight gets cut short to fit the promo. The promo feels forced because it's wedged into someone else's topic. The reader gets half an insight and half an ad.

❌ "Big news just dropped. [1 sentence]. Anyway here's my repo → [link]"
(Insight cut short. Promo doesn't follow from the hook. Reader gets neither.)

❌ "[Thoughtful analysis of someone else's tweet]. Building this in public → [repo link]"
(The analysis IS the value. The link cheapens it. This is a content-value post with a promo jammed in.)

✅ Content value: "Big news just dropped. Here's what it means, why it matters, and what most people miss."
✅ Outcome value: "I built X that solves Y. Here's the repo → [link]"

**Enforcement (Week 3 Learning):** In Week 3, nearly 100% of posts mixed both types — every insight ended with a repo link. This is the exact pattern the rule prohibits. Only ~20% of posts should include links (matching the promotional target). The other 80% must deliver pure content value with zero links.

Evidence: Week 3 retro — all sessions #3-35 attached repo link to every piece. Account went from 4.3% links (Week 2) to ~100% links (Week 3). Neither extreme is correct. Target: 20%.
See `agent/memory/learnings/retro-weekly-2026-02-08.md`

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
- Skill development journey (what you're reading, studying, mastering)
- "Today I learned" moments from reading top voices
- Surprising findings from research deep-dives

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
- 3-5 tweets optimal. **HARD MAX: 5 tweets per thread.** (Week 1 evidence: a 10-part thread consumed 10/17 daily quota in one post)
- Under 250 chars per tweet (under 200 better)
- Cliffhanger every 1-2 tweets
- Zero hashtags in main content
- Use 1x/week for deeper content

### Learning Journey as Content
The process of building expertise IS content. Share what you're reading and learning.

**Why it works:**
- Shows curiosity and growth (people follow learners, not just experts)
- Positions you as a curator - filtering signal from noise for your audience
- Creates natural engagement: people share their own takes
- Builds authority over time through visible knowledge accumulation

**Content from reading/learning:**
- "Just read [author]'s take on [topic]. Key insight: [takeaway]. Here's why it matters..."
- "3 things I learned this week about [domain]" (thread)
- "I used to think X. After reading [source], I now think Y. Here's what changed..."
- "[Author] nailed this: [paraphrased insight]. But I'd add..."
- "Been deep-diving [topic] all week. The biggest surprise: [finding]"

**Rules:**
- Always add your own angle - don't just summarize
- Credit the source (builds goodwill + networking)
- Connect learnings back to your domain/project
- Show evolution: "I used to think... now I think..."

### Questions as Content
Questions drive replies. Replies drive reach. Ask genuinely.

**Why questions work:**
- Algorithm rewards replies heavily (reply-to-reply = 75x)
- Low friction for audience to engage (everyone has an opinion)
- Surfaces insights you can learn from
- Builds community (people feel heard)

**Question formats:**
- **Opinion poll:** "What's the biggest bottleneck in [domain] right now?"
- **This or that:** "[Tool A] or [Tool B] for [use case]? And why?"
- **Genuine curiosity:** "Has anyone solved [specific problem]? Here's what I've tried..."
- **Contrarian probe:** "Hot take: [bold claim]. Change my mind."
- **Experience ask:** "What's one thing you wish you knew before [doing X]?"
- **Prediction:** "Where does [domain/technology] go in the next 12 months?"

**Rules:**
- Ask questions you actually want answers to (authenticity shows)
- Keep questions specific, not vague ("What do you think about AI?" = bad)
- Engage with replies - questions without follow-up feel hollow
- Mix in ~15-20% question posts for engagement balance
- Use learnings from answers in future content (close the loop)

---

## Algorithm Awareness

### What X rewards (latest known)
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

### Promotional Templates (Week 1 Learning)
Only ~10% of Week 1 tweets included links. Target is 20%. Use these templates:

- **BIP update**: "[Insight or milestone]. Building this in public → [repo link]"
- **Learning share**: "[Key takeaway from session]. Following the whole journey: [repo link]"
- **Profile soft plug**: "[Valuable observation]. More on how I build with AI → [profile link]"

Evidence: Week 1 retro showed 3/30 posted tweets had links vs. 6/30 target.
Week 2 retro: dropped further to 4.3% (2/47 tweets). This is a critical gap.

---

## Content Creation Checklist (Updated Week 3)
**Before committing any content, verify ALL items:**

1. **Queue check**: Is total pending queue > 15? If yes, **STOP — create zero new content this session.**
2. **Quality gate**: Would a stranger follow you based on this post alone? If not, rewrite or discard.
3. **Value type**: Is this content value OR outcome value? **Never both.** If it has a link, it's outcome value. If it has an insight, no link.
4. **Length**: Check `X_MAX_TWEET_LENGTH` GitHub var. Write as long as the content needs — concise and valuable (not padded).
5. **Link allocation**: Only ~20% of posts should include links. Check recent output — if last 4 posts all had links, this one must not.
6. **Angle diversity**: Is this about the autonomous agent? If your last 2 posts were also agent-focused, write about something else (call center AI, startup lessons, infrastructure architecture, broader AI trends).
7. **BIP balance**: Is BIP content at least 25% of recent output? If not, make this one BIP.
8. **Category**: Authority / Personality / Shareability. Avoid imbalance — personality and shareability are chronically under-represented.
9. **Hook**: Does the first line stop the scroll? Apply hook formula.

Evidence:
- Week 2: 4 tweets skipped for over-length, links at 4.3%, BIP at 23%.
- Week 3: Links overcorrected to ~100%, content became formulaic (same angle on every post), queue hit 53. All issues this checklist now addresses.
- `agent/memory/learnings/retro-weekly-2026-02-08.md`

---

## Engagement-First Strategy (Updated Week 3)
**For accounts under 100 followers, engagement is more important than content.**

6 followers after 215 tweets (including 31 replies to mega-accounts) = even engagement isn't working at current execution quality. The problem may be deeper (X Premium, content voice, or profile issues).

### Session Allocation (< 100 followers)
- **50% of session time**: Find and create replies to larger accounts in your niche
- **50% of session time**: Create original content
- **BUT: If queue > 15, spend 100% on non-content work** (research, profile optimization, reading, skill development)

### Why Engagement First
- Reply-to-reply = 75x algorithm multiplier
- One good reply to a 50K-follower account = more visibility than 10 original tweets
- Replies show up in other users' feeds, bringing profile visits
- Established accounts may follow back or retweet

### How to Execute
1. During reading sessions, note recent posts from top voices that you can reply to
2. Use web search to find tweet IDs: `WebSearch: "site:x.com @handle {topic}"`
3. Create reply files using the commenting skill format
4. **Max 1 reply + 1 original tweet per session** (quality over quantity)
5. **Only reply to posts < 24 hours old** — stale replies get buried

### Content Angle Diversification (Week 3 Learning)
**Max 50% of posts about the autonomous agent experiment.** The other 50% should draw on the author's broader expertise:
- Call center AI / speech analytics (Ender Turing domain)
- Startup building and scaling (15+ years experience)
- Infrastructure architecture journey (network eng → AI)
- Broader AI/ML trends and industry analysis
- Product development insights

Why: Week 3 content became formulaic — nearly every post referenced "PDCA cycles," "X PRs shipped," and linked the repo. The account reads as a single-topic bot, not a multifaceted human building interesting things.

Evidence: Sessions #3-35 all connected back to the autonomous agent angle. Content voice says "human building products with autonomous tools" but execution was "autonomous agent talks about itself."
See `agent/memory/learnings/retro-weekly-2026-02-08.md`

---

## Commenting / Engagement
See `@.claude/skills/commenting/SKILL.md` for reply strategy, file format, and engagement approach.

---

## Gist Fallback
When no platform integration exists:

```bash
gh gist create --public -f "filename.md" content.md
gh gist edit <gist-id> -f "filename.md" updated.md
```

Track gist URLs in state file under "## External Outputs".
