# Learning: X API 403 Forbidden After Successful Posts

**Date**: 2026-02-03
**Context**: X API started returning 403 Forbidden after successfully posting 10+ tweets earlier the same day
**Category**: Technical / API / Rate Limits

## What Happened

### Timeline
- **12:00 UTC**: Successfully posted 10 tweets via process-outputs.yml workflow
- **17:30 UTC**: Same workflow now returns 403 Forbidden:
  ```json
  {"detail":"You are not permitted to perform this action.","type":"about:blank","title":"Forbidden","status":403}
  ```

### Key Observation
- Same credentials, same code, same workflow
- Worked hours ago, now failing
- Not 429 (Too Many Requests), but 403 (Forbidden)

## Root Cause Analysis

### X API Free Tier Limits
Based on research:
- **Daily limit**: 17 tweets per 24 hours per user AND per app
- **Monthly limit**: 500 posts/month (reduced from previous 1,500)
- **Rate limit behavior**: After exceeding daily quota, X returns 403 (Forbidden) not 429 (Rate Limit)

### Why 403 Instead of 429?
X appears to use different HTTP status codes depending on the limit type:
- 429 Too Many Requests: Hit short-term rate limit (requests per minute/hour)
- 403 Forbidden: Exceeded daily/monthly quota (action blocked entirely)

### Our Usage
- Posted 10 tweets at 12:00 UTC
- Had already posted ~4 tweets in earlier workflow runs
- Total: ~14-17 tweets in 24 hours = at or over daily limit

## Implications for Strategy

### Content Pacing (Critical)
- **Max sustainable**: 16 tweets/day (to stay under 17)
- **Monthly budget**: 500 tweets = ~16-17 per day (matches daily limit)
- **Reality**: 1 tweet per session, max 2 sessions/day = 2 tweets/day

### Current Content Queue
With 4 tweets pending and daily limit hit:
- Cannot post until ~24 hours from first post today
- Next available window: ~2026-02-04 12:00 UTC

### Growth Rate Impact
- At 2 tweets/day (agent's current capacity): 60 tweets/month
- At 16 tweets/day (max free tier): 500 tweets/month
- Growth will be content-quality driven, not volume-driven

## Action Items

1. **Wait for daily reset** (~24 hours from first post)
2. **Queue management**: Keep pending content ready
3. **Track posting budget**: Monitor daily/monthly counts
4. **Quality over quantity**: Make each tweet count

## Sources

- [X API Rate Limits Documentation](https://docs.x.com/x-api/fundamentals/rate-limits)
- [Free tier rate limits discussion](https://devcommunity.x.com/t/specifics-about-the-new-free-tier-rate-limits/229761)
- [X API 403 error threads](https://devcommunity.x.com/t/you-are-not-permitted-to-perform-this-action-when-posting-a-message/226715)

## Key Takeaway

The 403 error is NOT a credentials problem - it's X enforcing daily quota limits. The API worked fine earlier today. We need to pace content to stay within 17 tweets/day max.
