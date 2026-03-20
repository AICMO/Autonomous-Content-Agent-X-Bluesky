# Agent Memory

> Key learnings for future sessions. Keep concise — lines past 200 get truncated.

## Queue Rules (HARD LIMITS — violating these wastes sessions)

- **If X queue >= 13 OR Bluesky queue >= 13:** Zero content. Zero replies. The 13-14 zone is functionally blocked: staging 2 files at 13 pushes to 15 immediately.
- **If X queue >= 15 OR Bluesky queue >= 15:** Hard stop. No exceptions.
- **If staged pairs >= 20:** Zero research. Zero staging. Only skill work.
- **Max 2 content pieces per session** (when ALL queues <= 12).
- **Verify queues at session start:** `find agent/outputs/x -maxdepth 1 -name "*.txt" | wc -l`

Evidence: S67 created 6 files → 6 consecutive blocked sessions. S130-S131 each created 2 at queue 10-12 → pushed to 14 → blocked for 5+ sessions.

## Drain Rates (Observed)

- X: 3 posts/run × ~4 runs/day = **12/day max**
- Bluesky: 1 post/run × ~4 runs/day = **4/day max**
- Bluesky is the bottleneck. Plan around it.

## Reply File Format (CRITICAL)

```
REPLY_TO: 2019637612076494985
---
Reply text here.
```

- **REPLY_TO must be numeric tweet ID ONLY.** URL or @username = silently skipped.
- Extract from URL: `x.com/user/status/THIS_IS_THE_ID`
- Reply-to-own: 100% success. Outbound to non-followers: 0% (403 "not mentioned by author").

## X Post Length (Premium = up to 25K chars)

**Hard minimums for X content:**
- News/opinion/BIP/promo/prediction: **500 chars minimum** (target 600-1000)
- Hot takes: 150-350 chars (only allowed short category)
- Threads: 1500 chars total (4-6 posts, 40-60% more reach)

**Bluesky is separate:** 290-char hard limit. Write X at full length first, then write Bluesky separately. Never let Bluesky's limit shrink X posts.

## What Content Works (Evidence-Based)

- **News hooks:** 3-6x impressions vs average (65, 62, 60, 51 imp vs 10 avg)
- **Dollar amounts in headlines:** Stops scroll ($285B, $2B, $1T)
- **Name-drops:** (Karpathy, Altman, Anthropic, OpenAI) moderate boost
- **What fails:** Generic authority posts without news hook, stale replies (>6h), external links (-30-50% reach)
- **Outbound replies to non-followers:** 0% success rate (403 API restriction)

## Anti-AI Writing (Mandatory)

**Never use:** Em dashes, "Not just X, it's Y", "Delve/elevate/innovative/leverage/robust/furthermore/moreover", "Let's dive in", perfect parallel lists.

**Do use:** Contractions, fragments ("Wild." "Zero."), start with "And"/"But", vary sentence length dramatically.

## Current Stats (2026-03-20, S148)

- Followers: 23 | Goal: 5,000 | Velocity: +8-9/week (up from +1/week)
- ETA at current velocity: ~11-12 months (still 35x short of 6-month goal pace)
- Premium: Active since 2026-03-01 (Day 20)
- Communities: 30,000x multiplier — ZERO posts made (50+ days overdue, requires UI)
- X queue: 14 (near limit zone — blocked). Bluesky queue: 14 (near limit zone — blocked).
- X posted total: ~610+ | Bluesky total: ~249+
- Memory: ~82KB (target <500KB) — pre-retro doc 48KB (delete after retro 2026-03-22)

## Communities = Most Urgent Untested Lever

**Owner must join manually:** x.com/i/communities
Targets: Build in Public (180K), AI/ML Builders (63K), Startup Founders (45K), Indie Hackers (35K)
**Agent cannot post to Communities programmatically** — requires UI. Owner action needed.

## File Naming Standards

- Always ISO 8601: `topic-YYYY-MM-DD.md` (NEVER `topic-MMM-DD-YYYY.md`)
- Research: `agent/memory/research/topic-YYYY-MM-DD.md`
- Learning: `agent/memory/learnings/topic-YYYY-MM-DD.md`

## Blocked Session Protocol (Queue >= 13)

Pick ONE. Create PR only if files changed. Do NOT create "state update only" PRs.

**Tier 1 (Highest value):**
1. Skill audit — read skills, update if evidence supports changes
2. Pre-retro analysis — if retro within 3 days, update pre-retro doc. **STOP CONDITION: If doc says "FINAL" or "Retro readiness: COMPLETE" anywhere, skip — adding more updates is waste (evidence: S139-S146 each added redundant updates to an already-FINAL doc = 8 sessions of duplicative work)**
3. CLAUDE.md improvement — identify recurring inefficiency, update protocol

**Tier 2 (Medium value):**
4. Research audit — mark staged/posted stories in research files to prevent re-staging
5. Hypothesis update — review active hypotheses, update status with evidence
6. Memory cleanup — read and graduate research files to learnings, delete fully-staged files

**Tier 3 (Low value — only if nothing else applies):**
7. State file update — only if data materially changed (no PR for timestamp-only updates)

## PR Rules

- Always start title with "[Agent]"
- Max PRs per day: check `PR Count Today` in state file (default 15)
- STOP immediately after `gh pr create` succeeds
- All session work goes in ONE PR
- **No empty PRs** — if only state timestamp changed, skip the PR

## Content Pillar Gate (Before Writing Any Post)

1. **Which pillar?** P1: Autonomous Agents | P2: Marketing/Content Automation | P3: Call Center AI | P4: Startup Building/AI Economics
2. **What's MY angle?** What do I know from experience the reader can't get elsewhere?
3. **Repo link?** Only if post is genuinely about building/running agents
4. **Politics ban:** Never post about politicians, votes, legislation by name

## Weekly Retro Protocol (Sundays)

- Check metrics issue: `gh issue list --label metrics --state open`
- All merged PRs since last retro: `gh pr list --state merged --limit 20`
- Key deliverables: evidence-based skill updates + state file trim to <200 lines
- Delete pre-retro doc after writing retro doc
- Memory cleanup: <500KB target
