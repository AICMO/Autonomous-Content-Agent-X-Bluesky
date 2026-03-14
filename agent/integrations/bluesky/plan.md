# Bluesky Platform Plan
Last updated: 2026-03-14

## Account Status
- **Handle:** johnios.bsky.social
- **Tier:** Free

## Posting Limits
- 300 grapheme limit per post (not characters — emoji/CJK may count differently)
- ~11,666 createRecord calls per day
- Workflow: 1 post/run + 1 reply/run, ~4 runs/day = **4 posts + 4 replies per day**
- Queue hard limit: 15 pending files max
- Bluesky is the bottleneck (4/day vs X's 12/day)

## Content Notes
- Write Bluesky posts separately from X (different constraints)
- Posts >300 chars are auto-skipped by pipeline
- OK to skip Bluesky version if topic doesn't compress to 290 chars
- Bluesky posts are compressed summaries, NOT the template for X posts

## Current Priorities
1. Queue discipline (>15 = zero content)
2. Write independently from X — never let 290-char limit shrink X posts
