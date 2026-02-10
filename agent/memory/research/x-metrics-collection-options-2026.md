# X Metrics Collection Options (2026)

**Created**: 2026-02-10
**Purpose**: Evaluate options for tracking engagement metrics on X (Twitter) to measure strategy effectiveness

## Problem Statement

The agent currently has:
- ✅ Ability to post tweets/replies via X API Free tier
- ❌ No ability to read engagement metrics (impressions, likes, retweets, replies)
- ❌ No data to validate hypotheses or measure strategy effectiveness
- ❌ "Engagement Rate: Unknown" status blocking progress measurement

**Impact**: Operating blind. Cannot answer:
- Which content types perform best?
- Are replies driving more engagement than original tweets?
- What's the actual engagement rate?
- Which hooks/topics resonate with audience?
- Is Premium subscription actually improving reach?

## X API Options (Official)

### Free Tier (Current)
**What it provides:**
- Post tweets (1,500/month limit)
- Read public data (severely limited - 1 request per 15 minutes)
- OAuth 1.0a authentication (stable tokens)

**What it DOES NOT provide:**
- Engagement metrics (impressions, likes, retweets)
- Analytics endpoints
- Tweet performance data
- Follower growth tracking
- Any meaningful read capabilities for metrics

**Cost**: Free
**Verdict**: ❌ Insufficient for metrics tracking

Sources:
- [How to Get X API Key: Complete 2026 Guide](https://elfsight.com/blog/how-to-get-x-twitter-api-key-in-2026/)
- [X API Twitter API read metrics engagement impressions 2026 free tier](https://tweetfull.com/blog/api-twitter-how-to-use-the-x-twitter-api-to-grow-and-automate-your-presence/)

### Basic Tier
**What it provides:**
- 10,000 tweets/month posting limit
- 7 days of search history
- Access to engagement endpoints
- Tweet metrics: `public_metrics`, `organic_metrics`
- User data and follower information
- Rate limits: reasonable for small-scale analytics

**Capabilities:**
- Read impressions, likes, retweets, replies per tweet
- Track follower count over time
- Analyze which content performs best
- Calculate engagement rate
- Validate hypotheses with data

**Cost**: $100-200/month (sources vary)
**Verdict**: ✅ Solves the problem but expensive

Sources:
- [X API v2 analytics tweet metrics followers 2026 pricing tiers](https://getlate.dev/blog/x-api)
- [Twitter API pricing, limits: detailed overlook](https://data365.co/guides/twitter-api-limitations-and-pricing)

### Pro Tier
**What it provides:**
- 100x more read capacity than Basic
- Full-archive search
- Real-time filtering
- Advanced analytics

**Cost**: $5,000/month
**Verdict**: ❌ Overkill for this use case

### Enterprise Tier
**Cost**: $42,000+/month
**Verdict**: ❌ Not relevant

## Free/Low-Cost Alternatives

### 1. X Analytics (Native Dashboard)
**What it provides:**
- Built-in analytics for all X accounts
- Post performance (impressions, engagements, engagement rate)
- Video metrics
- Top tweets
- Audience insights
- Campaign tracking

**Access:**
- Visit: analytics.x.com
- Or: Profile → More → Analytics
- Available for all accounts (no Premium required)

**Limitations:**
- Must be accessed manually (no API)
- Cannot be automated
- Requires human to export data

**Workflow:**
1. Human visits analytics.x.com weekly
2. Exports CSV or screenshots key metrics
3. Shares with agent (paste into issue/discussion)
4. Agent updates state file metrics

**Cost**: Free
**Verdict**: ✅ Best option for budget-constrained projects

Sources:
- [Free X/Twitter Analytics Tools: 12 Options You Should Know](https://profiletree.com/free-twitter-analytics/)
- [16 X (Twitter) Analytics Tools to Amplify your Strategy in 2026](https://sproutsocial.com/insights/twitter-analytics-tools/)

### 2. Third-Party Analytics Tools

#### Followerwonk
- **Focus**: Follower analysis, audience insights
- **Cost**: Free tier available
- **Pros**: Deep follower demographics
- **Cons**: Limited tweet-level metrics

#### Foller.Me
- **Focus**: Profile analytics, follower analysis
- **Cost**: Free
- **Pros**: Simple interface, competitive analysis
- **Cons**: No tweet-level engagement data

#### TweetArchivist
- **Focus**: Tweet archiving and analytics
- **Cost**: Free tier + paid plans from $24/month
- **Pros**: Historical data, hashtag tracking
- **Cons**: May require paid tier for full metrics

#### Circleboom
- **Focus**: Audience management, content analytics
- **Cost**: Free tier + paid plans
- **Pros**: Growth tracking, best time to post
- **Cons**: Limited in free tier

Sources:
- [Best Twitter Analytics Tools for 2026 (Free & Paid)](https://www.tweetarchivist.com/best-twitter-analytics-tools-2025)
- [Top 10 paid & free X (Twitter) analytics tools in 2025](https://contentstudio.io/blog/twitter-analytics-tools)

### 3. Data Scraping Services

#### Apify
- **What**: Twitter/X scraper with free plan
- **Capabilities**: Structured tweet data (text, timestamps, engagement metrics)
- **Output**: JSON or CSV
- **Cost**: Free plan available (usage-based pricing)
- **Legality**: Gray area - violates X ToS

#### Bright Data
- **What**: Enterprise data scraping platform
- **Capabilities**: Real-time and historical data, structured output
- **Cost**: Paid service (pricing varies)
- **Legality**: Gray area - violates X ToS

**Risk**: Account suspension if detected
**Verdict**: ⚠️ Not recommended due to ToS violation risk

Sources:
- [Best Twitter/X scrapers for data analysts in 2026](https://blog.apify.com/best-twitter-x-scrapers/)
- [Top 5 Twitter/X Data Providers Compared for 2026](https://brightdata.com/blog/web-data/best-twitter-x-data-providers)

## Recommendations

### Immediate (Week 1): Manual X Analytics
**Action**: Repo owner manually exports metrics from analytics.x.com weekly
**Frequency**: Every 7 days (Sunday before weekly retro)
**Data to collect**:
- Total followers (current count)
- Total tweets posted (lifetime)
- Top 10 tweets by impressions (last 7 days)
- Top 10 tweets by engagement rate (last 7 days)
- Average engagement rate (last 28 days)
- Impressions: total, average per tweet
- Link clicks (if any promotional tweets)

**Format**:
```markdown
## X Metrics (2026-02-10 to 2026-02-17)
- Followers: 6 → 12 (+6, +100%)
- Tweets posted: 233 → 280 (+47)
- Avg impressions/tweet: 45
- Avg engagement rate: 1.2%
- Top tweet: [text] - 450 impressions, 3.5% engagement
- Total profile visits: 28
```

**Cost**: $0 (5 minutes of human time per week)
**Benefit**: Enables data-driven decisions immediately

### Short-term (Week 2-4): Test Third-Party Free Tools
**Action**: Sign up for free tiers of:
1. Followerwonk (follower insights)
2. Foller.Me (profile analytics)
3. TweetArchivist free trial (if available)

**Purpose**: Supplement manual data with automated tracking
**Cost**: $0
**Risk**: Low

### Medium-term (Month 2): Decide on Paid Solution
**Condition**: If manual metrics show strategy is working (engagement >1%, follower growth >50/week)
**Options**:
1. **X API Basic tier** ($100-200/month) - Full automation, official
2. **Third-party tool** ($24-50/month) - Easier, possibly limited
3. **Continue manual** ($0/month) - If weekly cadence is acceptable

**Decision criteria**:
- Budget available
- Need for real-time data vs weekly acceptable
- Automation value (agent time saved)

### Long-term (Month 3+): Full Automation
If project shows ROI and budget allows:
- X API Basic tier ($100-200/month)
- Agent reads metrics via API
- Auto-updates state file with current metrics
- Hypothesis testing fully automated
- A/B testing content types with data

## Implementation Plan

### Phase 1: Manual Metrics (Week 1-2)
**Agent deliverable**: Create template for repo owner
**File**: `agent/templates/weekly-metrics-template.md`
**Owner action**: Fill template weekly, post to GitHub discussion
**Agent action**: Read discussion, update state file

### Phase 2: Process Automation (Week 3-4)
**Agent deliverable**: Script to parse metrics from discussion into state file
**Owner action**: Copy-paste raw analytics.x.com CSV into discussion
**Agent action**: Auto-parse and update metrics

### Phase 3: API Integration (Month 2+, if budget allows)
**Agent deliverable**: Integration script for X API Basic tier
**Owner action**: Subscribe to X API Basic, configure credentials
**Agent action**: Auto-fetch metrics daily, update state

## Metrics to Track (Priority Order)

### P0 - Core Growth Metrics
1. **Follower count** (absolute number, weekly delta, % growth)
2. **Engagement rate** (total engagements / total impressions)
3. **Posting velocity** (tweets/day, replies/day)

### P1 - Content Performance
4. **Impressions per tweet** (average, median, top 10)
5. **Top performing content types** (threads vs tweets vs replies)
6. **Best time to post** (based on engagement data)

### P2 - Engagement Quality
7. **Reply rate** (replies per tweet)
8. **Retweet rate** (retweets per tweet)
9. **Profile visits** (how many people clicked through)
10. **Link clicks** (for promotional tweets)

### P3 - Audience Insights
11. **Follower demographics** (if available)
12. **Top follower accounts** (who's following)
13. **Follower overlap** (with target accounts)

## Expected Impact

### With Manual Weekly Metrics
- ✅ Can validate if Premium subscription improved reach
- ✅ Can identify top-performing content angles
- ✅ Can calculate actual engagement rate
- ✅ Can test hypotheses with 7-day lag
- ✅ Can adjust strategy based on data
- ❌ Cannot do real-time A/B testing
- ❌ Cannot track daily/hourly patterns

### With X API Basic Tier
- ✅ All of the above, plus:
- ✅ Real-time hypothesis testing
- ✅ Daily/hourly engagement patterns
- ✅ Automated dashboards
- ✅ Per-tweet performance tracking
- ✅ Immediate strategy pivots based on data

## Cost-Benefit Analysis

| Option | Cost/month | Setup time | Data freshness | Automation | Verdict |
|--------|-----------|------------|----------------|------------|---------|
| Manual X Analytics | $0 | 5 min | Weekly | None | ✅ Start here |
| Free third-party tools | $0 | 30 min | Varies | Partial | ⚠️ Test if useful |
| X API Basic | $100-200 | 2 hours | Real-time | Full | ✅ If budget allows |
| Data scraping | Varies | High | Real-time | Full | ❌ ToS violation risk |

## Decision Framework

**Start with manual metrics (Phase 1)**
- Zero cost
- Immediate implementation
- Provides 80% of needed insights
- Low risk

**Upgrade to X API Basic if:**
- Manual metrics show strategy working (engagement >1%, followers >50/week)
- Budget available ($100-200/month acceptable)
- Real-time data would enable significantly better decisions
- Agent time saved > cost

**Stay manual if:**
- Growth is stalled (metrics show fundamental problem, not data frequency)
- Budget constrained
- Weekly data cadence is sufficient

## Next Steps for Repo Owner

1. **This week**: Visit analytics.x.com, screenshot or note:
   - Current follower count
   - Average impressions per tweet (last 28 days)
   - Average engagement rate (last 28 days)
   - Top 3 tweets by engagement

2. **Ongoing**: Post metrics weekly to GitHub discussion (every Sunday)

3. **Month 2 decision**: Based on Week 2-4 data, decide if X API Basic is worth the investment

## Agent Actions (This Session)

1. ✅ Research X API metrics options
2. ✅ Document findings in this file
3. ⏭️ Create weekly metrics template for repo owner
4. ⏭️ Update state file with "Metrics Collection Plan: Manual (Phase 1)"

## References

### X API Pricing & Capabilities
- [How to Get X API Key: Complete 2026 Guide](https://elfsight.com/blog/how-to-get-x-twitter-api-key-in-2026/)
- [X/Twitter API Pricing 2026: Complete Guide to All Tiers](https://getlate.dev/blog/twitter-api-pricing)
- [X (Twitter) API Guide 2026: Authentication, Endpoints & Pricing](https://getlate.dev/blog/x-api)
- [Twitter API pricing, limits: detailed overlook](https://data365.co/guides/twitter-api-limitations-and-pricing)

### Free Analytics Tools
- [16 X (Twitter) Analytics Tools to Amplify your Strategy in 2026](https://sproutsocial.com/insights/twitter-analytics-tools/)
- [Best Twitter Analytics Tools for 2026 (Free & Paid)](https://www.tweetarchivist.com/best-twitter-analytics-tools-2025)
- [Free X/Twitter Analytics Tools: 12 Options You Should Know](https://profiletree.com/free-twitter-analytics/)
- [Top 10 paid & free X (Twitter) analytics tools in 2025](https://contentstudio.io/blog/twitter-analytics-tools)

### Data Scraping
- [Best Twitter/X scrapers for data analysts in 2026](https://blog.apify.com/best-twitter-x-scrapers/)
- [Top 5 Twitter/X Data Providers Compared for 2026](https://brightdata.com/blog/web-data/best-twitter-x-data-providers)
