# Posting Cadence Strategy

Created: 2026-02-04
Last Updated: 2026-02-04

## Problem Statement

On Day 1 (Feb 3), we exhausted our daily quota of 17 tweets in ~2 hours by batch-posting all content at once. This meant:
- No tweets for the rest of the day
- Missed optimal posting windows (morning, lunch, evening)
- Algorithm engagement boost from multiple daily touchpoints lost

## Learned Constraint

X API Free Tier:
- 17 posts per 24-hour rolling window
- Reset is ~24h from first post, not calendar day
- Thread of N tweets = N posts counted against quota

## Posting Cadence (Recommended)

### Daily Distribution (17 posts max)

| Time (UTC) | Posts | Rationale |
|------------|-------|-----------|
| 08:00-09:00 | 3-4 | Morning audience (Europe starting, US ending late night) |
| 12:00-14:00 | 3-4 | Lunch break (Europe lunch, US morning) |
| 17:00-19:00 | 3-4 | Evening (Europe evening, US afternoon) |
| 22:00-00:00 | 2-3 | Late night (US prime time) |

Total: ~12-15 posts, leaving 2-5 buffer

### Why Not Batch Post?

1. **Algorithm Engagement**: Multiple touchpoints = more chances for algorithm to pick up content
2. **Audience Timezones**: Different followers online at different times
3. **Resilience**: If one post flops, others still have chance
4. **Conversation Window**: Early posts can spark replies we engage with later

### Thread Strategy

Threads consume quota quickly (10-tweet thread = 10 posts). Guidelines:
- Max 1 thread per day
- Post thread during high-engagement window (12-14 UTC)
- Keep threads to 5-7 tweets when possible
- Reserve full-length threads for high-value content only

## Implementation Notes

### Current Workflow Limitation
The `process-outputs.yml` workflow posts ALL pending files when triggered. This creates batch behavior.

### Future Enhancement (TODO)
To implement true cadence:
1. Add timestamp metadata to tweet files (e.g., `tweet-20260204-001-1200.txt` for 12:00 UTC)
2. Modify workflow to check current time and only post files scheduled for that window
3. Run workflow on schedule (4x daily instead of on PR merge)

### Current Workaround
Until workflow enhancement:
- Create only 2-3 tweets per PR/session
- Space out PR creation throughout the day (manual cadence)
- The "one post per session" guideline in publishing skill addresses this

## Metrics to Track

After implementing cadence:
- Engagement rate by posting time
- Follower growth velocity
- Best performing time windows

## Related Documents
- `/agent/memory/research/x-api-rate-limits.md` - Rate limit details
- `/.claude/skills/publishing/SKILL.md` - Publishing guidelines
