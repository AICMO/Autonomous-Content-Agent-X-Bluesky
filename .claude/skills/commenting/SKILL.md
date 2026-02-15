---
name: commenting
description: Strategy for engaging with others' posts across platforms (X, LinkedIn, etc.). Finding targets, writing valuable replies, building connections.
user-invocable: false
---

# Commenting / Engagement Skill

> Write valuable replies that build relationships and visibility

Commenting turns visibility into connections. Publishing broadcasts; commenting connects.

---

## Critical Constraint: Queue-Delayed Replies

**Agent-created replies are posted hours to days late, killing algorithmic value.**

**Week 4 evidence:**
- Replies to individual creators: 0-6 impressions (all stale)
- Reply to @OpenAI: 24 impressions (official accounts less time-sensitive)
- Time decay: replies lose 50% visibility every 6 hours

**What works via queue:**
- Replies to official brand accounts (@OpenAI, @claudeai, @googlecloud)
- Adding expertise on evergreen topics (not time-sensitive discourse)

**What doesn't work:**
- Replies to individuals (always stale before posting)
- Replies to news/discourse (moment passes)

**Recommendation:** Until real-time engagement is possible, minimize reply creation. Focus on original content (news hooks) instead.

---

## Why Commenting Matters

**For accounts under 100 followers, commenting > original posts for growth.**

**Evidence (2026):**
- One viral reply = 12K impressions vs 400 from original post (30x)
- Reply-to-reply = 75x algorithm multiplier
- Mid-tier account replies (10K-100K followers) = 10-20x reach vs timeline posts

**Why it works:**
- Exposure to established audiences (their 50K vs your 7)
- Algorithm boost (reply-to-reply = 75x vs Like baseline)
- Authority showcase without self-promotion
- Reciprocity drives profile visits and follows

---

## Finding Reply Targets

### Target Selection Rules

**DO Reply To:**
- Mid-tier accounts (10K-100K followers) — won't get buried, they engage
- Posts 2-6 hours old — momentum building, not stale
- Topics with real expertise (call center AI, startups, infrastructure→AI, agents)
- Conversation-starters (questions, contrarian takes, frameworks)
- Accounts that engage with replies

**DON'T Reply To:**
- Mega-accounts (>500K) — buried in 1000+ comments
- Stale posts (>24h) — algorithm moved on
- Generic hot takes — everyone's replying
- Accounts that never engage
- Topics you know nothing about

### How to Find Targets

**Web Search for Tweet IDs:**
```
WebSearch: "site:x.com @username {topic}"
```
Extract tweet ID from URL (x.com/user/status/**1234567890**)

**X Communities (when Premium active):**
- Browse community feeds for fresh posts
- Community replies get amplified in For You feed
- Best leverage for small accounts

**Storage:** Track in `agent/memory/research/reply-targets.md`

---

## Writing Good Replies

### The Value Test (Quality Gate)

Before posting ANY reply:
- Does this add insight the OP missed?
- Would someone click my profile after reading this?
- Is this better than 90% of comments on this post?

**If NO to any → don't post.**

### Reply Principles

**Effective patterns:**
1. **Respectful disagreement** — sparks conversation, invites reply-to-reply (75x multiplier)
2. **Add specific insight** — shows expertise without self-promotion
3. **Ask sharp questions** — pushes conversation forward, invites OP to engage
4. **Share contrarian data** — adds new info, makes people rethink
5. **Add tactical framework** — gives takeaway, builds authority

**Voice:**
- Conversational (shorter than publishing)
- Specific (reference what they said)
- Curious (ask genuine follow-ups)
- Credit freely ("building on your point...")

**What NEVER works:**
- Empty agreement ("Great post!", "This!", "🔥")
- Self-promotion ("Check out my thread")
- Obvious observations everyone's saying
- Desperation ("Please follow me")
- Stale replies (>24h old)
- Long essays (save for your posts)

### Diversify Reply Angles

**Avoid formulaic pattern.** Week 3 fell into:
1. Reference their point
2. Connect to autonomous agent
3. Add repo link

**This pattern, repeated 30+ times, reads as automated spam.**

**Better approach:**
- Most replies have NO link (pure conversation)
- Some ask questions (invite reply-to-reply)
- Some disagree respectfully (independent thinking)
- Not every reply connects to agent (draw on call center AI, startups, infra)
- Some add data/frameworks (authority)

**Max 50% of replies about agent.** Use author's broader expertise:
- Call center AI / Ender Turing (7 years production)
- Startup building (15+ years, 2 companies)
- Infrastructure → AI journey
- Broader AI/ML trends

---

## Reply File Format

### X (Twitter)
File: `agent/outputs/x/reply-YYYYMMDD-NNN.txt`

```
REPLY_TO: 2019637612076494985
---
Your reply text here.
```

---

## Session Allocation Rules

**If queue > 15:** CREATE ZERO NEW CONTENT (including replies).

**If queue < 15:**
- Max 2 content pieces per session (mix of tweets, replies, threads)
- Max 5 pending replies at any time (timeliness > volume)

**Time allocation (when < 100 followers):**
- 70% engaging with others (replies, comments)
- 30% creating original posts

**Timeliness rule:** Only reply to posts < 24h old. Ideally 2-6h old.

**Evidence:** Week 3 created 45+ replies to mega-accounts, many stale. Result: +1 follower.

---

## Reply Quality Checklist

**Must have:**
- [ ] Adds insight OP didn't mention
- [ ] Shows domain expertise (examples, frameworks, data)
- [ ] 2-4 sentences (concise, valuable)
- [ ] Would make someone click profile
- [ ] Passes "better than 90%" test
- [ ] Post is < 24h old (ideally 2-6h)
- [ ] Target is mid-tier (10K-100K) or community post

**Never do:**
- [ ] Generic praise ("Great!", "This!", "🔥")
- [ ] Self-promotion without context
- [ ] Obvious observations
- [ ] Desperation energy
- [ ] Reply to posts >24h old
- [ ] Reply to mega-accounts (buried)
- [ ] Add links (reduces reach)

---

## Algorithm Context (Key Points)

**Engagement weights (Jan 2026):**
- Reply-to-reply: 75x vs Like
- Repost: 20x
- Reply: 13.5x
- Bookmark: 10x
- Like: 1x (baseline)

**Implication:** Replies that get replies = 75x more valuable. Ask questions, spark debate.

**First 30 minutes = critical.** If reply gets 5+ likes or replies → algorithm boosts it.

**X Premium impact:**
- Reply visibility: 30-40% higher vs free accounts
- Reply ranking: Premium replies at top of threads
- External links hurt reach (even for Premium)

**Recommendation:** Avoid links in replies. Pure conversation performs better.

---

## Evidence Sources

- `agent/memory/research/2026-02-10-reply-strategy-evidence.md` (2026 data)
- `agent/memory/research/2026-02-10-x-engagement-tactics-communities.md` (Communities)
- `agent/memory/learnings/retro-weekly-2026-02-08.md` (Week 3 learnings)
