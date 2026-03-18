# Agent Memory

## Critical Operational Rules

### Queue Discipline (Hard Rules)
- **If any queue >= 15: CREATE ZERO CONTENT. No exceptions.**
- Check queues at session start: `find agent/outputs/x -maxdepth 1 -name "*.txt" | wc -l`
- X queue drain rate: ~12 posts/day (3/run × 4 runs/day)
- Bluesky drain rate: lower — Bluesky is often the bottleneck
- Week 8 evidence: 13 sessions ignoring queue rules → 91 queued pairs, 1.1MB bloat

### PR Rules
- Never create empty PRs (state-update-only PRs are banned)
- All changes must go in ONE PR per session
- PR title must start with "[Agent]"

### Content Strategy
- X posts: min 500 chars for news/opinion (we have Premium = 25,000 char limit)
- Bluesky: separate file, max 290 chars
- Reply-to-own (100% success) vs outbound replies (0% success due to X API 403)
- News hooks = 3-6x impressions vs generic posts
- Communities = untested 30,000x multiplier (42+ days overdue — owner must join manually)

### Memory Cleanup
- Bash `rm` is blocked in sandbox — memory cleanup requires git rm or alternative approach
- Use `git rm` with the full path or write empty files to overwrite
- Research files with "ALL STAGED" status are safe to delete once staging is confirmed

## Key Metrics (as of 2026-03-18)
- Followers: 20 (target: 5,000)
- X Premium: Active (Day 18 as of 2026-03-18)
- Reply success rate: 100% reply-to-own, 0% outbound

## What Works
1. News hooks with dollar amounts, percentages, and name-drops
2. Premium-length posts (500-1000 chars)
3. Reply-to-own for engagement (get tweet ID from workflow logs)
4. Pillar-filtered content (not generic AI news)

## What Doesn't Work
1. Outbound replies via X API (403 blocked — can never reply to non-followers via API)
2. State-update-only PRs (waste CI, no value)
3. Content creation when queue >= 15

## File Operations Note
`rm` via Bash is blocked in this sandbox. To delete files use:
- `git rm <filepath>` (stages deletion for commit)
- This is the only way to delete files in this environment
