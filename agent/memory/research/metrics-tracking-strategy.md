# Metrics Tracking Strategy

Created: 2026-02-04
Last Updated: 2026-02-04

## Problem Statement

To achieve our goal of 5,000 followers with >1% engagement, we need to measure:
- Current follower count
- Engagement rate (likes, replies, reposts per impression)
- Which content types perform best
- Growth velocity over time

Without metrics, we can't validate hypotheses or optimize strategy.

## API Tier Constraints

### X API Free Tier (Current)
- **Write-only**: Can post tweets, cannot read data
- **No access to**: User timeline, mentions, engagement metrics
- **Limit**: 17 posts per 24-hour rolling window

### X API Basic Tier ($100/month)
- **Read access**: User profile, tweets, engagement metrics
- **Limit**: 10,000 tweets/month read
- **Required for**: Automated metrics tracking

### X API Pay-Per-Use (Beta as of Dec 2025)
- No subscription, pay only for what you use
- May be more cost-effective for limited reads
- Monitor [@XDevelopers](https://twitter.com/XDevelopers) for rollout

## Available Options

### Option 1: Manual Metrics Collection (No Cost)
**How it works:**
- Manually check X dashboard/analytics periodically
- Record metrics in state file during agent sessions
- Human provides metrics updates when running agent

**Pros:**
- Free
- Accurate (straight from X)

**Cons:**
- Requires human intervention
- Not automated
- Delays in data availability

**Implementation:**
```markdown
## Manual Metrics (Update periodically)
| Date | Followers | Posts | Top Post Engagement |
|------|-----------|-------|---------------------|
| 2026-02-04 | ? | 16 | ? |
```

### Option 2: Basic Tier API ($100/month)
**How it works:**
- Upgrade to Basic tier
- Add read scripts to integration
- Automated metrics collection

**Pros:**
- Fully automated
- Real-time data
- Enables hypothesis testing

**Cons:**
- $100/month cost
- May be overkill for early stage

**Recommendation:** Consider after proving concept (reach 500 followers?)

### Option 3: Third-Party Analytics Tools
**How it works:**
- Use free analytics tools (Buffer, Hootsuite free tier)
- Export or manually record data

**Pros:**
- Often free
- Good visualization

**Cons:**
- May require manual export
- Limited features on free tiers

### Option 4: Web Scraping (Not Recommended)
- Against X ToS
- Risk of account ban
- **Do not implement**

## Recommended Approach

### Phase 1: Bootstrap (Current - 500 followers)
- **Strategy**: Manual metrics collection
- **Frequency**: Weekly update in state file
- **Source**: X Analytics dashboard or profile page
- **Who**: Human provides update when running agent

### Phase 2: Growth (500 - 2,000 followers)
- **Strategy**: Evaluate Basic tier value
- **Trigger**: If hypothesis testing is blocked by lack of data
- **Consider**: Pay-per-use if available

### Phase 3: Scale (2,000+ followers)
- **Strategy**: Automated metrics pipeline
- **Investment**: Basic tier justified by validated growth

## Metrics to Track

### Primary Metrics (Weekly minimum)
| Metric | Definition | Target |
|--------|------------|--------|
| Followers | Total followers | 5,000 (6-month goal) |
| Engagement Rate | (likes + replies + reposts) / impressions | >1% |
| Profile Visits | Users viewing profile | Track trend |

### Secondary Metrics (When available)
| Metric | Why It Matters |
|--------|----------------|
| Impressions per post | Reach/distribution health |
| Best performing content | What to create more of |
| Follower growth rate | Velocity tracking |
| Posting time performance | Optimal scheduling |

### Content Performance Tracking
Track in state file:
```markdown
## Content Performance (Manual)
| Post Date | Content Type | Engagement | Notes |
|-----------|--------------|------------|-------|
| 2026-02-03 | Thread | TBD | First thread |
| 2026-02-03 | Single | TBD | BIP content |
```

## State File Integration

Add this section to `agent/state/current.md`:

```markdown
## Metrics Snapshot
Last Manual Update: [date by human]

| Metric | Value | Previous | Change |
|--------|-------|----------|--------|
| Followers | ? | 0 | ? |
| Engagement Rate | ? | N/A | ? |
| Posts Live | 16 | 0 | +16 |

Note: Metrics require manual update from X Analytics or profile.
```

## Hypothesis Testing Without Read API

Even without automated metrics, we can test hypotheses:

1. **Threads vs Singles**: Compare manually after 1 week
2. **Posting Time**: Track which posts get most engagement visually
3. **Content Type**: Note which types get quoted/replied most

## Action Items

1. [x] Document metrics constraint (this document)
2. [ ] Add metrics section to state file template
3. [ ] Request human to provide follower count periodically
4. [ ] Evaluate Basic tier at 500 follower milestone

## Sources

- [X API Introduction](https://docs.x.com/x-api/introduction)
- [X API Free Tier Limitations](https://dev.to/superface/twitter-api-changes-the-missing-faq-for-free-basic-access-2lil)
- [X API Pricing Guide 2026](https://getlate.dev/blog/x-api)
