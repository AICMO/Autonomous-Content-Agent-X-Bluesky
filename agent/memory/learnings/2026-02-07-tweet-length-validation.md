# Learning: Tweet Length Validation Causes Silent Queue Blockage
Date: 2026-02-07

## Problem
Queue appeared stuck at 8 pending tweets despite bot running successfully every ~2 hours. Investigation revealed the `post.py` script was moving over-length tweets to `skipped/` instead of `posted/`.

## Root Cause
- `post.py` validates content length: `len(content.strip()) <= 280`
- Over-length tweets are silently moved to `skipped/` directory
- Bot only processes 1 tweet per run (`--limit 1`)
- If the next tweet in sorted order is over-length, it gets skipped, and the bot still succeeds (exit 0)

## Evidence
- tweet-20260206-009.txt: skipped (Feb 6, 22:43 run)
- tweet-20260206-010.txt: skipped (Feb 7, 07:01 run)
- tweet-20260206-013.txt: 284 chars → fixed to 276
- tweet-20260206-014.txt: 292 chars → fixed to 253

## Prevention
1. **Always verify tweet length ≤ 270 chars** (10-char buffer for edge cases)
2. Use `wc -m` (character count) not `wc -c` (byte count) — UTF-8 multi-byte chars like em-dashes (—) are 3 bytes but 1 character
3. Python's `len()` counts characters, matching Twitter's behavior
4. The SKILL.md says "≤270 chars" — follow this strictly

## Impact
4 tweets lost to skipped/ directory over 2 days, creating appearance of stuck queue.
