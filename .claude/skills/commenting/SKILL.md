---
name: commenting
description: Strategy for engaging with others' posts across platforms (X, LinkedIn, etc.). Finding targets, writing valuable replies, building connections.
user-invocable: false
---

# Commenting / Engagement Skill

> Write valuable replies that build relationships and visibility

## Why Commenting Matters

For accounts under 100 followers, commenting > original posts for growth. One viral reply = 12K impressions vs 400 from original post (30x). Reply-to-reply = 75x algorithm multiplier.

---

## Queue-Delayed Replies (Critical Constraint)

Agent-created replies post hours to days late, killing algorithmic value.

**Time decay:** Replies lose 50% visibility every 6 hours. At 24h = ~6% visibility.

**What works via queue:** Replies to official brand accounts (@OpenAI, @claudeai, @anthropic) — less time-sensitive. Evergreen topics.

**What doesn't work:** Replies to individuals (always stale). Replies to news/discourse (moment passes).

**Hard rules:**
- Never create replies when pending reply count >= 3
- Only reply to posts < 24h old (ideally 2-6h)
- If any platform queue >= 15: create zero content including replies

**Premium active:** Manual engagement is viable. Reply-to-own-comments within 30 min = 150x multiplier. Communities replies within 2-6h = still valuable.

---

## Finding Reply Targets

**DO reply to:** Mid-tier accounts (10K-100K), posts 2-6h old, topics with real expertise, conversation-starters, accounts that engage back.

**DON'T reply to:** Mega-accounts (>500K, buried), stale posts (>24h), generic hot takes, accounts that never engage.

**How to find (X API is write-only, use web search):**
```
WebSearch: "site:x.com @username {topic}"
WebSearch: "site:x.com {topic} {current_year}"
```
Extract tweet ID from URL: `x.com/user/status/**1234567890**`

**X Communities (Premium):** Browse community feeds for fresh posts. Community replies get amplified in For You feed. Best leverage for small accounts.

**Store targets:** `agent/memory/research/reply-targets.md`

---

## Writing Good Replies

### Anti-AI Reply Rules (MANDATORY)

**Never use:** Em dashes joining clauses, "Not just X, it's Y", "Delve/elevate/innovative/landscape/leverage/robust", "To clarify/In other words", "Great point! Furthermore...", summarizing their post back.

**Do use:** Contractions, sentence fragments ("Wild." "Zero chance."), start with "And"/"But", reference something SPECIFIC they said, have an opinion, keep it casual.

### Reply Patterns

| Pattern | When to use |
|---------|-------------|
| **Respectful disagreement** | Sparks reply-to-reply (75x) |
| **Add specific insight** | Shows expertise without self-promo |
| **Ask sharp questions** | Pushes conversation forward |
| **Share contrarian data** | Adds new info |
| **"This means..." prediction** | Connect their news to a consequence |
| **"What nobody's saying..."** | Add the angle everyone missed |

### Likability Rules
- "I" statements > "You" statements (less preachy)
- "And" > "But" (additive vs combative)
- "Here's what I found..." > "You should..."
- Questions > declarations (invites dialogue)
- Specific examples > abstract advice

### What NEVER Works
Empty agreement ("Great post!"), self-promotion ("Check out my thread"), obvious observations, links in replies (reduces reach), stale replies (>24h).

### Diversify Reply Angles
**Max 50% about agent.** Also use: call center AI (7 years), startups (15+ years), infra→AI journey. Most replies = NO link. Some ask questions. Some disagree respectfully.

---

## Reply-to-Own-Comments Protocol (Premium)

**150x algorithmic multiplier — highest-leverage engagement tactic.**

Post original content → reply to your own tweet within 30 min with expansion/detail.

**Rules:**
1. Timing: <30 minutes (after 30 min, multiplier drops)
2. Add value, don't repeat — expansion, data, follow-up question
3. Short hook + detailed reply
4. Max 1 reply per original post
5. Not every post needs it — use when there's genuine depth

**Reply patterns:** Expansion ("To expand: our 500K dataset shows..."), data points, tactical detail, question for audience, vulnerability.

**Priority #1 when Premium active:** Every Communities post → reply to self within 30 min.

---

## Communities Engagement (Premium)

**30,000x reach multiplier — post to Communities, not just timeline.**

**6 Communities:** Build in Public (180K), AI/ML Builders (63K), Startup Founders (45K), Call Center AI (12K), Infrastructure→AI (8K), Indie Hackers (35K).

**Rules:**
- 100% of content to Communities first (timeline = secondary)
- Each post to 1-2 most relevant Communities (no spam)
- Reply to 3-5 Community posts per session
- Reply to own posts within 30 min

**Anti-patterns:** Same content to all Communities, self-promo without value, off-topic posts, reply spam.

---

## Session Allocation

**If any queue >= 15:** Zero content including replies. No exceptions.

**If both queues < 15:** Max 2 content pieces per session. Max 3 pending replies.

**Time allocation (<100 followers):** 70% engaging (replies, comments), 30% original posts.

---

## Reply Quality Checklist

**Must have:** Adds insight OP missed, shows expertise, 2-4 sentences, would make someone click profile, post < 24h old, target is mid-tier or community post.

**Never:** Generic praise, self-promotion, obvious observations, links, posts >24h old, mega-accounts.

---

## Algorithm Context

| Action | Weight vs Like |
|--------|---------------|
| Reply-to-own <30min (Premium) | 150x |
| Reply-to-reply | 75x |
| Repost | 20x |
| Reply | 13.5x |
| Bookmark | 10x |
| Like | 1x |

Replies that get replies = 75x more valuable. Ask questions, spark debate. First 30 minutes = critical.

---

## Reply File Format

File: `agent/outputs/x/reply-YYYYMMDD-NNN.txt`
```
REPLY_TO: 2019637612076494985
---
Your reply text here.
```