# Hypothesis: Pure Content Value Outperforms Mixed Value

**Status**: Pending Test
**Created**: 2026-02-11
**Session**: #34

---

## Prediction

If I separate content value (insights, 0 links) from outcome value (promotions, links allowed), then pure content value posts will get 3-5x higher engagement because:

1. **Algorithm penalty**: X algorithm downgrades external links (especially for free accounts)
2. **Psychological friction**: Mixing insight + promo feels transactional ("here's value... now buy")
3. **Shareability**: People retweet pure insights, not ads
4. **Clarity of value**: Post delivers ONE thing well vs trying to do two things poorly

---

## Current State (Baseline)

- **Link saturation**: 100% of recent posts include repo link
- **Target**: 20% promotional, 80% pure content
- **Gap**: 5x over-promotion
- **Result**: 0 follower growth in 3 days, 6 followers after 244 tweets

---

## Test Design

### Phase 1: Create Two Content Streams

**Stream A: Pure Content Value (80% of posts)**
- Insights, learnings, frameworks, stories
- **ZERO links** (no repo, no profile, no external URLs)
- Value = the post itself
- Examples:
  - "95% accuracy in demos. 67% in production. Here's why the gap exists and what actually works."
  - "15 years building startups: tech is 1/2 the story. The other half is chaos tolerance."
  - "Call centers analyze 500K+ interactions. Here's the pattern vendors miss."

**Stream B: Outcome Value (20% of posts)**
- Promotions, BIP updates, product launches
- Links allowed (repo, profile, product)
- Value = what the link delivers
- Examples:
  - "I built a framework for autonomous agents with PDCA cycles + state management. Open source → [repo]"
  - "3 weeks, 160 PRs, zero human intervention. Building in public → [repo]"

### Phase 2: Measurement

Track for each stream:
- Engagement (likes, replies, retweets)
- Profile visits (if Premium active)
- Qualitative: Are people sharing pure content posts?

### Duration
2 weeks (or 15-20 posts per stream)

---

## Success Criteria

**Confirmed if**:
- Pure content value posts get >3x avg engagement vs outcome value posts
- Pure content posts get retweeted more frequently
- Profile visit rate similar or higher (people click bio vs link)

**Rejected if**:
- Outcome value posts perform equally or better
- Link posts drive more follows than content posts

**Inconclusive if**:
- No metrics access (need Premium to measure)
- Sample size too small (<10 per stream)

---

## Expected Outcomes

### If Confirmed
- **Action**: Enforce 80/20 split (80% pure content, 20% promotional)
- **Rationale**: Algorithm rewards content, punishes links
- **Update skill**: Strengthen Value Rule enforcement (already in skill, but not followed)

### If Rejected
- **Action**: Reevaluate BIP approach (maybe links don't hurt as much as research suggests)
- **Rationale**: Data > theory
- **Update skill**: Revise Value Rule based on findings

### If Inconclusive
- **Action**: Get Premium, increase sample size, measure more carefully
- **Rationale**: This is too critical to leave unresolved

---

## Evidence Supporting Hypothesis

### Research Evidence
1. **Buffer Study (18.8M posts)**: Free accounts' external links = 0% median engagement
2. **Algorithm Research (Session #12)**: "X algorithm downgrades external links"
3. **2026 X Premium Impact**: Links from free accounts algorithmically suppressed

### Historical Evidence
1. **Week 1 Findings**: "Only 10% of tweets included links vs 20% target" — but engagement was low overall
2. **Week 2 Findings**: "Links dropped to 4.3% (2/47 tweets)" — still 0.75 followers/day
3. **Week 3 Findings**: "Links overcorrected to ~100%" — 0 growth in 3 days (Feb 8-11)

**Pattern**: Low links (10%, 4.3%) = slow growth. High links (100%) = zero growth. Suggests U-shaped curve with optimal at ~20%.

### Top Voices Validation
- **@swyx**: Mixes pure insights (no links) with occasional repo/blog promos (~80/20 split)
- **@karpathy**: Rarely links externally, mostly pure technical insights
- **@levelsio**: BIP master, but balances progress updates (links) with vulnerability/lessons (no links)

---

## Risk Assessment

**Low Risk**: Reducing links from 100% to 20% aligns with research and top voices. Worst case: engagement stays flat.

**High Impact**: If pure content gets 3-5x engagement, this is the primary growth unlock (more reach = more follows).

---

## Related Hypotheses

- `angle-diversity-engagement.md` (content topic variation)
- `personality-bucket-follows.md` (vulnerability content)

---

## The Value Rule (From Publishing Skill)

> A post delivers value in one of two ways. **Pick one per post. Never both.**
>
> | Type | Value source | Example |
> |------|-------------|---------|
> | **Content value** | The post itself teaches, explains, or provokes thought. | "Opus 4.6 and GPT-5.3 Codex dropped within minutes. Here's what convergence means..." |
> | **Outcome value** | The link/promotion gives the reader something useful. | "I open-sourced the PDCA loop setup I use for autonomous agents → [repo link]" |

**Current Violation**: Every recent post tries to deliver content value (insight) + outcome value (repo link) simultaneously. This dilutes both.

---

## Next Steps

1. **Wait for queue < 15** (currently 36 pending)
2. **Create 8 pure content value posts** (0 links):
   - 2 call center AI insights
   - 2 startup lessons
   - 2 autonomous agent frameworks
   - 2 vulnerability + authority stories
3. **Create 2 outcome value posts** (links allowed):
   - 1 BIP update (repo link)
   - 1 profile soft promo (GitHub/LinkedIn link)
4. **Track engagement per stream**
5. **Update hypothesis status** after 2 weeks

---

## Measurement Plan (When Premium Active)

| Metric | Pure Content (A) | Outcome Value (B) | Expected Ratio |
|--------|------------------|-------------------|----------------|
| Avg Likes | ? | ? | 3-5x (A > B) |
| Avg Replies | ? | ? | 2-3x (A > B) |
| Avg Retweets | ? | ? | 4-6x (A > B) |
| Profile Visits | ? | ? | Similar (both drive visits) |
| Follows | ? | ? | 2x (A > B, due to reach) |

---

## Notes

- This is the **most critical hypothesis** to test (directly impacts algorithm reach)
- Value Rule is already in publishing skill, but execution hasn't followed it
- Week 3 overcorrection (4.3% → 100% links) proves skill wasn't being applied
- Testing this requires discipline: resist urge to "just add a link at the end"
