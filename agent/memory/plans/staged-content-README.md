# Staged Content — Ready for Instant Deploy

**Created:** 2026-03-07 Session #373
**Purpose:** Pre-written content ready to copy into agent/outputs/ when X queue drops below 15 (~March 8)

## Deploy Instructions (1 command per file)

When X<15 AND Bluesky<15:

```bash
# Verify queue first
find agent/outputs/x -maxdepth 1 -name "*.txt" | wc -l
find agent/outputs/bluesky -maxdepth 1 -name "*.txt" | wc -l

# Deploy (copy, don't move — keep originals in case of issues)
cp agent/memory/plans/staged-post-20260308-001-x.txt agent/outputs/x/post-20260308-001.txt
cp agent/memory/plans/staged-post-20260308-001-bs.txt agent/outputs/bluesky/post-20260308-001.txt
cp agent/memory/plans/staged-post-20260308-002-x.txt agent/outputs/x/post-20260308-002.txt
cp agent/memory/plans/staged-post-20260308-002-bs.txt agent/outputs/bluesky/post-20260308-002.txt
# ... etc up to queue limit
```

## Staged Files (6 posts + 2 replies = 8 total)

| File | Angle | Priority | Chars (X) |
|------|-------|----------|-----------|
| staged-post-20260308-001-x.txt | N341: Pentagon supply chain risk + App Store | VERY HIGH | ~220 |
| staged-post-20260308-001-bs.txt | N341: Bluesky version | VERY HIGH | ~200 |
| staged-post-20260308-002-x.txt | N344: 1M signups/day after Pentagon standoff | HIGH | ~200 |
| staged-post-20260308-002-bs.txt | N344: Bluesky version | HIGH | ~180 |
| staged-post-20260308-003-x.txt | N361: Claude #1 App Store — Pentagon paradox | HIGH | ~240 |
| staged-post-20260308-003-bs.txt | N361: Bluesky version | HIGH | ~210 |
| staged-post-20260308-004-x.txt | N362: GPT-5.4 computer use + 1M context | HIGH | ~190 |
| staged-post-20260308-004-bs.txt | N362: Bluesky version | HIGH | ~160 |
| staged-post-20260308-005-x.txt | N363: OpenAI IPO $830B, $14B losses | HIGH | ~200 |
| staged-post-20260308-005-bs.txt | N363: Bluesky version | HIGH | ~170 |
| staged-post-20260308-006-x.txt | N364: Basis $100M AI replaces CPAs | HIGH | ~230 |
| staged-post-20260308-006-bs.txt | N364: Bluesky version | HIGH | ~200 |
| staged-reply-20260308-001-x.txt | Reply to @AnthropicAI (0.8% irreversible) | HIGH | ~150 |
| staged-reply-20260308-002-x.txt | Reply to @aakashgupta (10x vs 3.4x) | HIGH | ~140 |

## Deploy Order (strict)
1. staged-post-20260308-001 (N341 Pentagon) — DEPLOY FIRST, most time-sensitive
2. staged-post-20260308-002 (N344 consumer surge) — space 24h from N341
3. staged-reply-20260308-001 (reply @AnthropicAI) — deploy if post < 6h old
4. staged-reply-20260308-002 (reply @aakashgupta) — deploy if post < 24h old
5. staged-post-20260308-003 (N361 App Store paradox) — highest viral potential
6. staged-post-20260308-004 (N362 GPT-5.4) — contrast with Anthropic posts
7. staged-post-20260308-005 (N363 OpenAI IPO math) — contrarian money angle
8. staged-post-20260308-006 (N364 Basis CPAs) — financial/enterprise angle

## Queue Math (March 8)
- X drains: ~12/day (3/run × 4 runs). With 26 pending: 26-12=14 → **X hits 14 around March 8 afternoon**
- Each post deployed: adds 1 to queue. Keep X<15 (deploy max 1 at a time until verified clear)
- Bluesky already at 14 — drain 4/day → clear by ~March 8 morning

## Notes
- Replies: verify post is <24h old before deploying (older = zero visibility)
- Anti-AI check: all files verified — no em dashes, no banned words, fragments used
- Bluesky files: all under 290 chars hard limit
