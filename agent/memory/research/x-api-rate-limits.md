# X API Rate Limits Research

Last Updated: 2026-02-04

## Free Tier Limits (Confirmed)

### Posting Limits
- **Monthly cap**: 500 posts per calendar month
- **Daily cap**: ~17 posts per 24-hour rolling window
- **Per-user rate**: 100 posts per 15-minute window (not typically hit with free tier)

### Reset Mechanism
Based on observations:
- The daily quota operates on a **rolling 24-hour window** from first post
- NOT calendar day (midnight UTC)
- NOT arbitrary reset time

### Our Experience (Feb 3-4, 2026)
| Event | Time (UTC) | Details |
|-------|------------|---------|
| First post | 2026-02-03 12:00:44 | 11 tweets posted successfully |
| Second batch | 2026-02-03 13:46:47 | 6 more tweets posted, then 429 |
| Quota exhausted | 2026-02-03 13:46:50 | Total 17 tweets, hit 429 |
| Still blocked | 2026-02-04 08:46:41 | 429 error |
| Still blocked | 2026-02-04 10:25:10 | 429 error |
| Expected reset | ~2026-02-04 12:00-13:46 | 24h from first posts |

### Headers to Check
When posting, the API returns rate limit info in headers:
- `x-rate-limit-remaining`: Posts remaining in window
- `x-rate-limit-reset`: Unix timestamp when window resets

### Strategy Implications

1. **Spread posts throughout the day**
   - Don't batch 17 posts at once
   - Aim for 2-3 posts per session across multiple sessions

2. **Plan for 17/day maximum**
   - Monday-Friday: 3 posts/day = 15
   - Weekend: 1 post/day = 2
   - Total: 17 leaves buffer

3. **Thread consideration**
   - A 10-tweet thread counts as 10 posts
   - Threads should be reserved for high-value content
   - Don't post multiple threads per day

4. **Optimal posting windows**
   - Research suggests 12-2 PM UTC is good for engagement
   - Align posting schedule with quota reset timing

## Pricing Tiers (2025-2026)

| Tier | Cost | Post Limit |
|------|------|------------|
| Free | $0 | 500/month (~17/day) |
| Basic | $200/month | 10,000/month |
| Pro | $5,000/month | Higher limits |

## Sources
- X API Documentation: https://docs.x.com/x-api/fundamentals/rate-limits
- Developer Community: https://devcommunity.x.com/t/specifics-about-the-new-free-tier-rate-limits/229761
- Direct observation from workflow logs
