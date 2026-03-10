# Agent Memory

> Key learnings for future sessions. Keep concise — lines past 200 get truncated.

## Queue Rules (HARD LIMITS — violating these wastes sessions)

- **If X queue >= 15 OR Bluesky queue >= 15:** Zero content. Zero replies. Zero research. Zero staging.
- **If staged pairs >= 20:** Zero research. Zero staging. Only skill work or engagement prep.
- **Reply max: 5 pending per platform.** Never create when at or above 5.
- **Max 2 content pieces per session** (when queues clear).
- **Verify queues at start:** `find agent/outputs/x -maxdepth 1 -name "*.txt" | wc -l`

Evidence: Week 8 had 13 sessions ignoring blocked rules → 1.1MB memory bloat, 91 staged pairs, zero growth.

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

## What Content Works (Evidence-Based)

- **News hooks:** 3-6x impressions vs average
- **Dollar amounts in headlines:** Stops scroll
- **Short posts:** Outperform long by 3-6x
- **Replies to official accounts (@OpenAI, @nvidia):** 24+ imp vs 0-6 for individuals
- **What fails:** Long authority posts, stale replies (>6h), external links (-30-50% reach)

## Anti-AI Writing (Mandatory)

**Never use:** Em dashes, "Not just X, it's Y", "Delve/elevate/innovative/leverage/robust/furthermore/moreover", "Let's dive in", perfect parallel lists.

**Do use:** Contractions, fragments ("Wild." "Zero."), start with "And"/"But", vary sentence length dramatically.

## Key Stats (March 2026)

- Followers: 17 | Goal: 5,000 | Velocity: +1/week (critical)
- Premium: Active since 2026-03-01 (Day 10)
- Communities: 30,000x multiplier — ZERO posts made (12 days overdue, requires UI)
- Claude Code: 4% of GitHub commits → target 20% EOY
- Anthropic: $19-20B ARR, 40% enterprise share (was 4% Jan 2025)
- AI inference: $30 → $0.10/M tokens (92% drop in 3 years)
- NVIDIA GTC: March 16-19 (Vera Rubin, Feynman chip 1nm TSMC)

## Communities = Most Urgent Untested Lever

**Owner must join manually:** x.com/i/communities
Targets: Build in Public (180K), AI/ML Builders (63K), Startup Founders (45K), Indie Hackers (35K)
Without Communities: follower velocity = +1/week → 5K goal ETA = 95 years.

## File Naming Standards

- Always ISO 8601: `topic-YYYY-MM-DD.md` (NEVER `topic-MMM-DD-YYYY.md`)
- Research: `agent/memory/research/topic-YYYY-MM-DD.md`
- Learning: `agent/memory/learnings/topic-YYYY-MM-DD.md`

## Queue-Blocked Session Options (No content allowed)

1. Update skills (`.claude/skills/`) with evidence-based changes
2. Update reply-targets research for future deployment
3. Update hypotheses with current status
4. Memory cleanup (if rm not sandboxed)
5. Update MEMORY.md itself
6. Update state file planned steps

## PR Rules

- Always start title with "[Agent]"
- Max PRs per day: check `PR Count Today` in state file
- STOP immediately after `gh pr create` succeeds
- All session work goes in ONE PR

## GTC Deadline (March 16, 2026)

- Pre-reply staged: `reply-20260310-001.txt` (to @NVIDIAGTC, Feynman chip angle)
- Need: Second live-reply when queue drains (stage March 13-15)
- Our angle: Vera Rubin 10x cheaper = call center AI economics reset
- X clears March 11-12, Bluesky clears March 13-14
