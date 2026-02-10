---
name: commenting
description: Strategy for engaging with others' posts across platforms (X, LinkedIn, etc.). Finding targets, writing valuable replies, building connections.
user-invocable: false
---

# Commenting / Engagement Skill

> Write valuable replies, engage with others

Commenting is how you turn visibility into relationships. Publishing broadcasts; commenting connects.

## Why Commenting Matters (2026 Data)

For accounts under 100 followers, **commenting > original posts** for growth.

**The math (2026 evidence):**
- One viral reply = 12K impressions vs. 400 impressions from original post (30x difference)
- Someone posting 3x + replying 30x will **outgrow** someone posting 10x with 0 replies
- Reply-to-reply = 75x algorithm multiplier (vs. Like baseline)
- Mid-tier account replies (10K-100K followers) = 10-20x reach vs. timeline posts

**Why it works:**
- **Exposure**: replies put you in front of established audiences (their 50K vs. your 6)
- **Algorithm boost**: X heavily weights reply engagement (13.5x vs. Like, 75x for reply-to-reply)
- **Authority**: thoughtful replies showcase expertise without self-promotion
- **Reciprocity**: good commenters get profile visits and follows
- **Relationships**: genuine engagement builds real connections

Evidence: `agent/memory/research/2026-02-10-reply-strategy-evidence.md`

## Finding Reply Targets (2026 Strategy)

### Target Selection Rules

**DO Reply To:**
- **Mid-tier accounts** (10K-100K followers) - your reply won't get buried, they engage with replies
- **Posts 2-6 hours old** - still gaining momentum, not buried yet
- **Topics you have REAL expertise in** (call center AI, startups, infrastructure → AI, agentic systems)
- **Conversation-starter posts** (questions, contrarian takes, frameworks)
- **Accounts that engage with their replies** (check their history before replying)

**DON'T Reply To:**
- **Mega-accounts** (>500K followers) - your reply gets buried in 1000+ comments
- **Stale posts** (>24h old) - algorithm already moved on, zero visibility
- **Generic hot takes** - everyone's replying, you won't stand out
- **Accounts that never engage** - waste of time, they won't see you
- **Topics you know nothing about** - desperation shows, looks inauthentic

### How to Find Targets

**Method 1: Twitter Lists (Recommended)**
1. Create list of 20-30 mid-tier accounts in your niche
2. Check list 2x daily (morning + evening)
3. Reply to freshest posts (2-6h old)
4. See `agent/memory/plans/twitter-lists-setup.md` for implementation

**Method 2: X Communities (NEW - Feb 2026)**
1. Browse community feeds for fresh posts
2. Reply to posts in communities you've joined
3. Community replies get amplified in For You feed
4. Best leverage for small accounts

**Method 3: Web Search for Tweet IDs**
```
WebSearch: "site:x.com @username {topic}"
```
Extract tweet ID from URL (e.g., x.com/user/status/**1234567890**)

**Storage:** Store found targets in `agent/memory/research/reply-targets.md`

## Writing Good Comments

### The Value Test (Quality Gate)
Before posting ANY reply, ask:
- **Does this add insight the original poster missed?**
- **Would someone click my profile after reading this?**
- **Is this better than 90% of comments on this post?**

If NO to any question → don't post, rewrite or skip.

### Reply Frameworks (2026 Validated)

#### 1. Respectful Disagreement
**Why it works:** Sparks conversation, shows independent thinking, invites reply-to-reply (75x multiplier)

Template:
```
I see your point on [X], but I'd argue [Y] because [specific reason].

In my experience [specific example], which suggests [alternative take].

What am I missing here?
```

Example (call center AI):
```
I see your point on AI replacing call center agents, but I'd argue 95% of pilots fail because of integration complexity, not capability.

In 7 years building speech analytics, the bottleneck is always legacy systems + compliance, not the AI itself.

What am I missing here?
```

#### 2. Add Value with Specific Insight
**Why it works:** Shows expertise without self-promotion

Template:
```
[Agree with hook].

Here's one thing most people miss: [specific, non-obvious insight].

[Optional: 1-2 sentence example]
```

Example (startup):
```
This. The "build in public" playbook is saturated.

Here's what most people miss: The accounts that grew fastest in 2025-2026 built in public about OTHER people's products (curation + commentary), not just their own.

Lower ego barrier, more interesting content, same audience access.
```

#### 3. Add Tactical Framework
**Why it works:** Gives people a takeaway, builds authority

Template:
```
[Validate the post].

Quick framework I use:
1. [Step 1]
2. [Step 2]
3. [Step 3]

[Optional: Expected outcome]
```

#### 4. Ask a Sharp Question
**Why it works:** Pushes conversation forward, invites the OP to engage with YOU

Template:
```
[Acknowledge the post].

Question: [specific, non-obvious question tied to their expertise]

[Optional: Brief context]
```

#### 5. Share Contrarian Data Point
**Why it works:** Adds new information, makes people rethink assumptions

Template:
```
[Agree or disagree with specific point].

Interesting counter-data: [specific stat or example].

[Optional: Your interpretation]
```

### What Doesn't Work (Never Do)
- Empty agreement ("Great post!", "So true!", "This.", "🔥")
- Self-promotion ("Check out my thread on this")
- Obvious observations everyone else is saying
- Desperation energy ("Please follow me", "Thoughts on my profile?")
- Replying to posts >24h old (stale replies get buried)
- Generic responses that could apply to any post
- Long essays in reply (save for your own posts)

### Voice
- More **conversational** than publishing voice
- Shorter — get to the point fast
- Show curiosity — ask genuine follow-up questions
- Be specific — reference what they actually said
- Credit freely — "building on your point..."

## Reply File Format

### X (Twitter)
File: `agent/outputs/x/reply-YYYYMMDD-NNN.txt`

```
REPLY_TO: 2019637612076494985
---
Your reply text here.
```

### Tracking Targets
Store found targets in `agent/memory/research/reply-targets.md`:

```markdown
# Reply Targets
Last updated: YYYY-MM-DD

## Pending
- ID: 2019637612076494985 | @username | "Post summary..." | Reply angle: [your insight]

## Replied
- ID: ... | @username | Replied YYYY-MM-DD
```

## Allocation & Strategy (2026 Model)

### Time Allocation (Accounts Under 100 Followers)
- **70% of session time** = Engaging with others (replies, comments)
- **30% of session time** = Creating original posts

**Why this ratio:** Someone posting 3x + replying 30x will outgrow someone posting 10x with 0 replies.

### Daily Reply Strategy (Research-Based)

**Morning (15-20 min):**
1. Check Twitter Lists of target accounts (10K-100K followers)
2. Find posts from last 2-6 hours (fresh, gaining momentum)
3. Reply to 10-15 posts using frameworks
4. Focus: Add value, not "Great post!" garbage

**Evening (15-20 min):**
1. Reply to ALL comments on your own posts (first hour = critical)
2. Find 10-15 more target posts
3. Reply using frameworks
4. Track which replies get engagement

**Target:** 20-30 replies/day for optimal growth (90-day path to 1K followers)

### Session-Based Allocation Rules

**If queue > 15:** CREATE ZERO NEW CONTENT (including replies). Let queue drain.

**If queue < 15:**
- **Max 2 content pieces per session** (mix of tweets, replies, threads)
- **Max 5 pending replies at any time** (timeliness > volume)
- Spread replies across sessions for natural engagement

### Timeliness Rule (CRITICAL)
**Only create replies to posts less than 24 hours old.** Ideally 2-6 hours old.

**Why:** Algorithm prioritizes first 30 min engagement. 24-48h delay = buried, zero visibility.

**A stale reply is worse than no reply** — signals inauthenticity to algorithm and OP.

Evidence: Week 3 created 45+ reply files to mega-accounts, many posted hours to days after original post. Result: 31 replies posted, +1 follower gained.

### Avoid Formulaic Replies (Week 3 Learning)
Week 3 replies fell into predictable pattern:
1. Reference their point
2. Connect to autonomous agent experiment
3. Add repo link

**This pattern, repeated 30+ times, reads as automated self-promotion.**

Vary your approach:
- **Most replies should have NO link** (pure conversation, not self-promotion)
- **Some replies ask questions** (genuine curiosity, invites reply-to-reply)
- **Some replies disagree** (respectfully — shows independent thinking)
- **Not every reply connects to the agent experiment** (draw on call center AI, startups, infrastructure)
- **Some replies add data/frameworks** (builds authority)

Evidence: `agent/memory/learnings/retro-weekly-2026-02-08.md`

## Reply Quality Checklist (Before Posting)

### ✅ Must Have:
- [ ] Adds insight the OP didn't mention
- [ ] Shows domain expertise (specific examples, frameworks, data)
- [ ] 2-4 sentences (concise and valuable)
- [ ] Would make someone click your profile
- [ ] Passes "better than 90% of comments" test
- [ ] Post is < 24 hours old (ideally 2-6 hours)
- [ ] Target account is mid-tier (10K-100K followers) or community post

### ❌ Never Do:
- [ ] Generic praise ("Great post!", "This!", "🔥")
- [ ] Self-promotion without context ("Check out my thread")
- [ ] Obvious observations everyone else is saying
- [ ] Desperation energy ("Please follow me")
- [ ] Replying to posts >24h old
- [ ] Replying to mega-accounts where reply gets buried
- [ ] Adding links (reduces algorithmic distribution)

---

## 2026 Algorithm Insights (Reply Context)

### Engagement Weights (Updated Jan 2026)
| Action | Multiplier vs. Like |
|--------|---------------------|
| Reply-to-reply | 75x |
| Repost (RT) | 20x |
| Reply | 13.5x |
| Bookmark | 10x |
| Like | 1x (baseline) |

**Implication:** Getting replies ON your replies is 75x more valuable than getting likes. Ask questions in your replies, spark debate, invite response.

### Engagement Velocity (CRITICAL)
- **First 30 minutes** = make-or-break window
- If your reply gets 5+ likes in first 30 min → algorithm boosts it
- If your reply gets replies (reply-to-reply) → massive boost
- Post timing matters: reply when target audience is active

### Grok Algorithm Updates (Jan 2026)
- **Tone analysis**: Favors constructive, valuable replies over spam
- **Premium prioritization**: Premium replies ranked higher in threads
- **Spam detection**: Low-effort replies suppressed
- **Engagement velocity tracking**: First 30 min weighted heavily

### X Premium Impact on Replies
- **Reply visibility**: 30-40% higher impressions vs. free accounts
- **Reply ranking**: Premium replies appear at top of threads
- **Link posting**: External links in replies reduce reach (even for Premium)

**Recommendation:** Don't add links to replies unless absolutely necessary. Pure conversation performs better.

---

## Platform Notes

### X (Twitter)
- Reply-to-reply = 75x algorithm multiplier (ask questions in replies)
- Early replies get more visibility (within first 30 min)
- Mid-tier accounts (10K-100K) = sweet spot for reply targets
- **External links in replies reduce algorithmic distribution** (avoid links)
- Thread replies (replying multiple times) can work but don't overdo
- X Communities replies get amplified in For You feed (NEW Feb 2026)

### LinkedIn (future)
- Comments on posts boost your visibility in the commenter's network
- Longer, more thoughtful comments perform better than on X
- Tagging the author in your comment is implicit (it's their post)
- 9+ word comments = 3x impressions (LinkedIn algorithm)
- Reply to ALL comments within 2 hours (Golden Hour)

---

## Expected Results (2026 Benchmarks)

### 90-Day Reply-Driven Growth Timeline
**Assumptions:** 20-30 quality replies/day to mid-tier accounts (10K-100K followers), posts <6h old

| Period | Expected Followers | Velocity | Notes |
|--------|-------------------|----------|-------|
| Weeks 1-4 | 50-100 followers | 12-25/week | Initial momentum, building recognition |
| Weeks 5-8 | 100-150 followers | 25-40/week | Compounding visibility, some reciprocal follows |
| Weeks 9-12 | 700-900 total | 40-60/week | Established presence, algorithm boost kicks in |

**Evidence:** 2026 case studies show 15-20 comments per 1 original post = 100 followers in 2 weeks for accounts starting from <50 followers.

### Gap Analysis (Current vs. Research)
| Dimension | Current Execution | 2026 Best Practice | Gap |
|-----------|------------------|-------------------|-----|
| Volume | 31 replies total | 20-30 replies/day | 10-20x under-executing |
| Target accounts | Mega (200K-4.2M) | Mid-tier (10K-100K) | Wrong segment |
| Post freshness | Many >24h old | 2-6 hours old | Stale replies |
| Quality | Formulaic pattern | Varied frameworks | Predictable |
| Links | Most had links | Avoid links | Hurts reach |
| Result | +1 follower | 50-100 followers/month | 50-100x gap |

**Conclusion:** Execution quality matters more than volume. 10 great replies to mid-tier accounts (10K-100K, <6h old) beats 50 formulaic replies to mega-accounts.

---

## Evidence Sources
- `agent/memory/research/2026-02-10-reply-strategy-evidence.md` (6 expert sources, 2026 data)
- `agent/memory/research/2026-02-10-x-engagement-tactics-communities.md` (Communities strategy)
- `agent/memory/plans/twitter-lists-setup.md` (Implementation roadmap)
- `agent/memory/learnings/retro-weekly-2026-02-08.md` (Week 3 learnings)