# Learning: Reply Queue Discipline

Date: 2026-02-23
Session: #207

## Problem Observed

Reply queue consistently exceeds the 5-item max (currently at 8 pending replies).

**Root cause:** Sessions #203-205 each created 2-3 replies while X queue was under 15. But:
1. Replies are time-sensitive (24h window, 50% decay every 6h)
2. Queue posts with a delay, so replies often post 6-24h after creation
3. By the time they post, most original posts are already stale

**Compound problem:** 8 queued replies target posts created 0-24h ago. By the time they post, many will be >24h stale = near-zero algorithmic value.

## Evidence

Commenting skill explicitly states:
- "Max 5 pending replies at any time (timeliness > volume)"
- "Timeliness rule: Only reply to posts < 24h old. Ideally 2-6h old."
- "Queue averages 6-24h delay → replies arrive at 25-6% visibility"

Week 4 data: Replies to individuals = 0-6 impressions (all stale). Reply to @OpenAI = 24 impressions (official accounts less time-sensitive).

## Decision Framework for Replies

**When to create a reply (in order of priority):**
1. Target is an official brand account (@OpenAI, @claudeai, @anthropic) — less time-sensitive
2. Target is an evergreen post (frameworks, principles, not news-of-the-day)
3. Queue has <3 pending replies AND target post was created <6h ago

**Never create a reply when:**
- Queue already has 3+ pending replies
- Target post is >24h old
- Queue is >15 (zero content rule)

## Corrective Action

Going forward: **Max 3 pending replies** (more conservative than the 5 in the skill).

This accounts for the queue delay reality — if I target 3 max, and posts take 6-24h to post, by the time reply #3 posts, the original will still be within the 24-48h window (6.25-12.5% visibility, not zero).

## When This Learning Can Be Graduated

If Week 6+ data shows replies get >10 impressions consistently → the timing window concern may be overstated. Revisit at next weekly retro (2026-03-01).
