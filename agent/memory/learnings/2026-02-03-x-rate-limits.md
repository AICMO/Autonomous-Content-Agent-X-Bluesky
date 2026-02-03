# Learning: X API Rate Limits

**Date**: 2026-02-03
**Context**: First successful tweet posting session
**Category**: Technical / API

## What Happened

After OAuth 1.0a credentials were configured by the repo owner, the posting workflow successfully posted 5 tweets. However, 3 additional tweets hit rate limits (HTTP 429 "Too Many Requests").

### Successful Posts (5)
- tweet-week2-002.txt
- tweet-week2-003.txt
- tweet-week2-004.txt
- tweet-week2-005.txt
- tweet-week2-007.txt

### Rate Limited (3)
- tweet-week2-001.txt
- tweet-week2-006.txt
- tweet-week2-008.txt

## X API Free Tier Limits

The X API v2 Free tier has strict limits:
- **Posts**: 17 tweets per 24-hour window (per app/user)
- **Reads**: 1,500 tweets per month

With 11 old tweets potentially attempted earlier (wrong voice), plus 5 successful today, we may have hit the daily limit.

## Implications for Strategy

1. **Batch posting is risky**: Cannot post all queued tweets at once
2. **Need pacing**: Spread tweets across time windows
3. **Queue management**: Keep track of what's pending vs. posted
4. **Rate limit recovery**: Wait 24 hours before retrying failed posts

## Recommendations

1. **One tweet per workflow run**: Instead of processing all tweets at once, process one at a time with delays
2. **Schedule multiple workflow dispatches**: Spread posts throughout the day
3. **Track rate limit state**: Could add a cooldown file or timestamp tracking
4. **Prioritize quality over quantity**: With limited posts per day, each tweet matters more

## Action Items

- [ ] Consider modifying workflow to limit posts per run
- [ ] The 3 rate-limited tweets will retry on next workflow run (in 24h)
- [ ] For growth strategy: Focus on quality engagement rather than high volume
