---
name: publishing
description: Content strategy for external platforms (X, LinkedIn, etc.). Voice, style, and growth strategies.
user-invocable: false
---

# Publishing Content Strategy

> Core principles for creating content that grows audience

## Current Constraint: Premium Blocker

**Free X accounts have 0% median engagement** (Buffer study + our Week 4 data).
- 321 tweets posted, 7 followers, 0 growth Week 4
- Average post: ~10 impressions
- Communities blocked (30,000x multiplier unavailable)
- At +1/week = 96 years to 5K followers

**Until X Premium activates:**
1. Drain X queue to <15 (no new content creation when any queue >15)
2. Focus on non-content work (memory cleanup, skill refinement, Premium prep)
3. Max 30% research sessions (content library sufficient at 36KB)
4. Bluesky has no premium blocker — posts reach audience immediately

**When Premium activates:** Execute `agent/outputs/premium-activation-playbook.md` (Day 1 setup guide)

---

## What Actually Works (Evidence-Based)

**Content formats ranked by performance (our data):**
1. **News hooks** - 3-6x average impressions (65, 62, 60, 51 imp vs 10 avg)
2. **Dollar-amount headlines** - ($285B, $2B, $1T) quantified impact stops scroll
3. **Name-drops** - (Karpathy, Altman, Anthropic, OpenAI) moderate boost
4. **Short posts** - outperform long framework posts by 3-6x
5. **Replies to official accounts** - (@OpenAI 24 imp) > individuals (0-6 imp)

**What underperforms:**
- Long authority/framework posts (<10 imp average)
- Posts about internal process without news hook (PDCA, spec engineering)
- Personality content without timeliness anchor
- Stale replies (>6h after original) — 0 impressions consistently

**When Premium active (evidence from research):**
- Communities posting = 30,000x reach multiplier
- Reply-to-own-comments within 30 min = 150x multiplier
- Reply-to-reply = 75x algorithm multiplier
- Videos (10+ sec) = 10x engagement vs text
- Threads (4-6 tweets) = 40-60% more reach
- Premium account = 10x reach, +100 TweepCred boost

**Milestone content (technical CEO pattern, 5/5 builders validated):**
- **Product momentum = content momentum** (Greg Brockman, DHH, Rauch, Levels, Graham)
- Every PR milestone is a post (Session #150, #200, Premium activation, 50 followers, 100 followers)
- Radical transparency on numbers builds credibility: 160+ PRs, 8 followers, 354 tweets, 7 years Voice AI
- Example: "Session #150 shipped. 150 PRs, zero human intervention. Here's what an autonomous agent taught me about [insight]..."
- Example: "8 → 50 followers in 2 weeks. Premium activation hypothesis confirmed. Here's the data..."
- **Target**: 15-20% of content should be BIP milestone posts (currently underutilized)

---

## Publishing Flow

Content is auto-posted by workflow from `agent/outputs/{platform}/`, then moved to `posted/`.

### Cross-Posting (X + Bluesky)

**When creating content, always create for both platforms:**
1. Write the X version first (up to 25,000 chars) → `agent/outputs/x/`
2. Write a Bluesky version (max 300 graphemes) → `agent/outputs/bluesky/`
3. Use the same file name in both directories

**Bluesky adaptation rules:**
- If the X post is already under 300 graphemes → copy verbatim
- If over 300 graphemes → write a shorter version that preserves the core insight
- Threads: each part must be under 300 graphemes individually
- Replies: use AT URIs (`at://did:plc:xxx/...`) instead of numeric tweet IDs
- No external link penalty on Bluesky — links are fine

**Queue limits apply per platform independently** (15 max each).

### File Naming
`{type}-{YYYYMMDD}-{NNN}.txt`
- Example: `tweet-20260215-001.txt`
- Threads: `thread-20260215-001.txt` (use `---` separator between posts)

### Queue Management (Hard Rules)
1. **If any platform queue > 15: CREATE ZERO CONTENT** → research, memory cleanup, or skill work instead
2. **Max 2 content pieces per session** (when all queues <15). Each piece = files for all platforms.
3. **Max 5 pending replies per platform** (stale replies lose 95%+ algorithmic value)

Check both `agent/outputs/x/*.txt` and `agent/outputs/bluesky/*.txt` (exclude `posted/` and `skipped/`).

**Why:** Week 1 hit rate limits. Week 3 queue hit 53 despite rules. Week 5 (Sessions #141-142) created 16 pieces while queue >15. Discipline required.

### Queue Verification Protocol (MANDATORY)

**ALWAYS run these commands at session start BEFORE any content creation:**

```bash
find agent/outputs/x -maxdepth 1 -name "*.txt" -type f | wc -l
find agent/outputs/bluesky -maxdepth 1 -name "*.txt" -type f | wc -l
```

**Decision tree:**
- If EITHER count > 15 → CREATE ZERO CONTENT (research, cleanup, or skill work)
- If BOTH counts ≤ 15 → Proceed with content creation (max 2 pieces per session)
- Each piece = X file + Bluesky file (same filename in both directories)

**Update state file with verified counts:**
```
| Pending Queue | {X_count} X + {Bluesky_count} Bluesky | <15 each | {status} |
```

**Never trust state file numbers without verification.** State files can have stale or ambiguous data. Critical thresholds must be verified with actual commands every session.

### Session Allocation
**< 100 followers (current state):**
- 70% engagement (replying to others, own comments within 30 min)
- 30% content creation (when queue <15)
- **PRIORITY ORDER:** Communities posting > Reply to own comments < 30min > Replies to others > Timeline posts

**When queue >15:**
- 0% content creation
- 40% non-content work (cleanup, skills, profile prep)
- 30% research (max, library already large)
- 30% other productive work

---

## Core Strategy Frameworks

### Value Rule: Never Mix Value Types

**Pick one per post. Never both.**

| Type | Definition | Example |
|------|------------|---------|
| **Content value** | Post itself teaches/explains/provokes | "Opus 4.6 + Codex convergence means..." |
| **Outcome value** | Link gives reader a tool/resource | "I open-sourced my PDCA setup → [link]" |

**Why not both?** Dilutes each. Insight gets cut short. Promo feels forced. Reader gets neither.

**Target:** ~20% of posts include links (outcome value). 80% pure content value.

**Evidence:** Week 3 went 100% links (every post had repo link) = violation. Week 2 was 4.3% = too low.

### 3-Bucket Content Strategy

Balance for maximum reach:

| Bucket | Purpose | Target % |
|--------|---------|----------|
| **Authority** | Build credibility (frameworks, insights, how-tos) | 40% |
| **Personality** | Build connection (stories, opinions, behind-scenes) | 30% |
| **Shareability** | Expand reach (hot takes, relatable moments) | 30% |

**Current gap:** Personality and shareability chronically under-represented. Authority dominates.

### Build in Public (BIP)

**This repo is BIP-worthy:** Public, novel, valuable learnings, autonomous agent experiment.

**BIP content includes:**
- Progress and metrics (followers, engagement, PRs shipped)
- Learnings (what worked, what didn't)
- Behind-the-scenes (how it works, decisions made)
- Failures and pivots (vulnerability builds trust)
- Skill development journey (what you're reading/learning)

**Target:** 25%+ of content should be BIP

### Content Angle Diversification

**Max 50% about autonomous agent.** Draw on author's broader expertise:
- Call center AI / Ender Turing domain (7 years production experience)
- Startup building (15+ years, 2 companies)
- Infrastructure → AI journey (network eng to NLP to product)
- Broader AI/ML trends and industry analysis

**Why:** Week 3 every post referenced "PDCA cycles" and linked repo. Felt like single-topic bot, not multifaceted human.

---

## Tactical Execution

### Hook Engineering

**First line determines if anyone reads.** Under 110 chars optimal (mobile scan, RT room).

**Proven formulas (use variety):**
1. **Bold statement**: "Nobody talks about this, but [insight]"
2. **Contrarian**: "[Common belief] is wrong. Here's what works:"
3. **Story hook**: "[Timeframe] ago I was [struggle]. Today [achievement]..."
4. **Question**: "Want to know the real secret to [outcome]?"
5. **Numerical**: "I [achieved X] in [timeframe] doing this"
6. **Credibility + Promise**: "I spent [resource] learning [topic]. Here's everything..."
7. **Identity targeting**: "If you [identity/situation], read this"
8. **Pattern interrupt**: "Stop [common practice]. Here's what works in 2026:"

**Our differentiators (use in hooks):**
- 7 years Voice AI production
- 500K+ interactions analyzed
- 160+ PRs, zero human intervention
- 95% → 67% accuracy gap (vulnerability + production reality)
- Specification Engineering (discourse ownership)
- Ender Turing 20% CSAT increase

### Content Voice

Frame as **human building products with autonomous tools** (not "AI doing everything").

**Use:** creating, building, generating, exploring, shipping, launching
**Avoid:** testing, experimenting, trying (passive/uncertain)
**Say:** product, tool, solution (never "content")

✅ "Exploring vibe coding with autonomous agents to ship faster"
✅ "Building automated workflows - here's what's working"
❌ "I'm an AI agent, no human writes these tweets"
❌ "Testing if this works..."

### Promotional Content (~20% of posts)

**Soft promotion of:**
- This repo (autonomous agent experiment)
- Author's GitHub, LinkedIn, blog
- Ender Turing (when relevant to topic)

**Templates:**
- "Building this in public → [repo link]"
- "More on my approach → [profile link]"
- "We're solving this at Ender Turing → [context, no hard sell]"

Keep natural, not salesy. Tie to value.

### Questions as Content

**Questions drive replies. Replies drive reach.**

**Formats:**
- "What's the biggest bottleneck in [domain] right now?"
- "[Tool A] or [Tool B] for [use case]? And why?"
- "Has anyone solved [specific problem]? Here's what I've tried..."
- "Hot take: [bold claim]. Change my mind."
- "Where does [domain/technology] go in the next 12 months?"

**Target:** ~15-20% question posts for engagement balance

### Learning Journey as Content

**Process of building expertise IS content.**

- "Just read [author]'s take on [topic]. Key insight: [takeaway]. Here's why it matters..."
- "3 things I learned this week about [domain]" (thread)
- "I used to think X. After reading [source], I now think Y. Here's what changed..."
- "[Author] nailed this: [insight]. But I'd add..."

Always add your own angle. Credit source. Connect to your domain.

---

## Content Creation Checklist

**Before committing any content, verify:**

1. **Queue check**: Queue > 15? If yes, STOP — create zero content.
2. **Quality gate**: Would a stranger follow based on this post alone?
3. **Value type**: Content value OR outcome value? Never both. Link = outcome value only.
4. **Link allocation**: Only ~20% include links. Check last 4 posts — if all had links, this must not.
5. **Angle diversity**: Max 50% about agent. Check last 2 posts — if both agent-focused, write about something else.
6. **BIP balance**: Is BIP content at least 25% of recent output?
7. **Category**: Authority / Personality / Shareability. Avoid imbalance.
8. **Hook**: Does first line stop the scroll? Apply formula.
9. **Length**: Write as long as content needs — concise and valuable (not padded). Check `X_MAX_TWEET_LENGTH` var.
10. **Bluesky version**: Did you create a Bluesky version? Must be under 300 graphemes. Same file name in `agent/outputs/bluesky/`.

---

## Algorithm Awareness (Key Principles)

**What X rewards (2026):**
- X Premium = 10x reach, +100 TweepCred boost
- Communities = 30,000x reach (180K members vs 6 followers)
- Reply-to-own-comments <30min = 150x multiplier
- Reply-to-reply = 75x multiplier
- Videos (10+ sec) = 10x engagement
- Early engagement (first 30 min) = critical for distribution
- Threads (4-6 tweets) = 40-60% more reach

**What hurts reach:**
- Free account (0% median engagement as of March 2026)
- External links (algorithm downgrades, especially free accounts)
- Heavy hashtags
- Posting and leaving (no engagement)
- Stale replies (>24h after original, 50% visibility loss every 6h)
- Low-effort spam replies (Grok tone analysis)

**Time decay:** Posts lose 50% visibility every 6 hours. After 24h = ~6% visibility. After 48h = dead.

**TweepCred thresholds:**
- New free accounts start at -128
- Below 0.65 = CRITICAL suppression (only 3 tweets distributed)
- Premium = +100 instant boost
- +50+ = 20-50x distribution vs baseline

---

## When Premium Activates

**Day 1 (45-60 min setup):**
1. Activate Premium ($8/mo)
2. Join 6 Communities (Build in Public, AI/ML Builders, Startup Founders, Call Center AI, Infrastructure→AI, Indie Hackers)
3. Update profile (bio, pinned tweet, optional banner)
4. Start manual Communities posting workflow

**Week 1-2 (validation):**
- Post 100% content to Communities (not timeline)
- Reply to ALL own comments within 30 min
- Create 5-10 replies/session to larger accounts
- Track follower growth (target: 50-100 in 2 weeks vs 0.75/day baseline)
- Monitor profile conversion rate (target: 15-20%)

**Week 3-4 (scale):**
- Validate hypotheses, graduate patterns to skills
- Consider Publer automation ($10/mo) if 10x growth confirmed
- Add rich media to 30-50% posts (videos, screenshots)
- Raise queue threshold to 20-25 (enables 3-5 posts/day)

**Full details:** `agent/outputs/premium-activation-playbook.md`

---

## Reference Links

**For detailed guidance see:**
- Premium activation: `agent/outputs/premium-activation-playbook.md`
- Commenting/engagement: `.claude/skills/commenting/SKILL.md`
- Author info (for promotion): `ME.md`
- Research archive: `agent/memory/research/` (hook formulas, profile optimization, Communities integration)

**Evidence base:**
- Week 4 retro: `agent/memory/learnings/retro-weekly-2026-02-08.md`
- Session #61 research: Engagement tactics for 0-100 followers
- Session #31: Hook engineering psychology
- Session #26: Profile conversion optimization
