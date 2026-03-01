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

### Reply Timing Windows & Staleness Decay

**Optimal window: 2-6 hours after original post**
- 0-2h: Peak momentum (best for manual/real-time engagement)
- 2-6h: Still building momentum (queue-friendly if fast workflow)
- 6-12h: 50% visibility loss (marginal value)
- 12-24h: 75% visibility loss (poor ROI)
- 24-48h: 87.5% visibility loss (~12.5% baseline visibility)
- >48h: Dead (algorithm moved on, ~6% visibility)

**Math:**
- Hour 0: 100% visibility
- Hour 6: 50% visibility (one half-life)
- Hour 12: 25% visibility (two half-lives)
- Hour 24: 6.25% visibility (four half-lives)

**Implication for queued replies:**
- Queue averages 6-24h delay → replies arrive at 25-6% visibility
- Only exception: official brand accounts (less time-sensitive)

**What works via queue:**
- Replies to official brand accounts (@OpenAI, @claudeai, @googlecloud)
- Adding expertise on evergreen topics (not time-sensitive discourse)

**What doesn't work:**
- Replies to individuals (always stale before posting)
- Replies to news/discourse (moment passes)

**Recommendation:**
- Until real-time engagement is possible, minimize reply creation. Focus on original content (news hooks) instead.
- When creating replies: prefer official brand accounts (@OpenAI, @claudeai, @anthropic) — less time-sensitive. For individual accounts, only reply if post is < 6h old and queue has < 3 pending replies.
- Time to time, include 1-2 replies per session to re-validate engagement data. Track impressions to confirm whether queue delay still kills value.
- **Hard rule:** Never create replies when total pending reply count ≥ 3 (Session #208 learning: 8 queued replies all likely stale by post time).

**Premium is now active:** Manual engagement is viable. Reply-to-own-comments within 30 min = 150x multiplier. Communities replies within 2-6h = still valuable (community feeds have longer shelf life).

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

## Communities Engagement Tactics (Premium Only)

**30,000x reach multiplier — the highest-leverage growth tactic available.**

**What it is:**
- X Premium unlocks Communities (group feeds around topics)
- Posts in Communities reach ALL members (vs your 10 followers on timeline)
- Example: "Build in Public" = 180K members vs 10 followers = 18,000x multiplier

**Why this is #1 priority when Premium activates:**
- Instant audience access (don't need to build followers first)
- Algorithm amplifies Community posts in For You feed
- Members are pre-qualified (interested in topic)
- Reply-to-reply in Communities = 75x multiplier on top of reach
- Small accounts compete equally with large accounts

**6 Communities to join (Day 1 when Premium activates):**
1. **Build in Public** (180K members) — BIP content, milestone posts, learnings
2. **AI/ML Builders** (63K members) — autonomous agents, LLM engineering, production insights
3. **Startup Founders** (45K members) — product building, growth tactics, founder journey
4. **Call Center AI** (12K members) — domain expertise, Ender Turing promotion
5. **Infrastructure → AI** (8K members) — career transition stories, technical depth
6. **Indie Hackers** (35K members) — solo building, bootstrapping, automation

**Total reach: 343K members vs 10 timeline followers = 34,300x multiplier**

**Content allocation when Premium active:**
- **100% of content to Communities first** (not timeline)
- Timeline = secondary (Communities posts already appear in For You feed)
- Each post goes to 1-2 most relevant Communities (no spam)

**Which content goes where:**
- BIP milestones → Build in Public (Session #160, Premium activation, 50 followers)
- Agent/LLM tactics → AI/ML Builders (PDCA cycles, specification engineering)
- Product building → Startup Founders (autonomy strategies, delegation frameworks)
- Call center insights → Call Center AI (Ender Turing case studies, 67% vs 95% accuracy)
- Career stories → Infrastructure → AI (network eng → NLP → product journey)
- Solo building → Indie Hackers (autonomous agent as co-founder)

**Engagement tactics within Communities:**
- Reply to 3-5 posts per session (tactical insights, questions, data)
- Reply-to-own-comments within 30 min (150x multiplier)
- Ask questions (invites reply-to-reply = 75x multiplier)
- Share contrarian data (sparks conversation)
- Add frameworks (builds authority)

**Time allocation when Premium active:**
1. Post to Communities (100% of content)
2. Reply to own posts within 30 min (150x multiplier)
3. Reply to 3-5 Community posts (2-6h old, mid-tier authors)
4. Check notifications, engage with replies to your posts

**Quality gate for Community posts:**
- Does this add value to the Community? (not just self-promotion)
- Would members upvote/share this?
- Is this better than 80% of posts in this Community?

**Anti-patterns (will get you removed):**
- Posting same content to all Communities (spam)
- Self-promotion without value (links with no context)
- Off-topic posts (agent stuff in Call Center AI without tie-in)
- Reply spam (generic praise, no insight)

**Metrics to track (when Premium active):**
- Profile visits from Community posts (goal: 15-20% conversion)
- Follower growth rate (before/after Communities)
- Engagement rate per Community (which Communities drive most value)
- Reply-to-reply rate (are your posts sparking conversation?)

**Expected results (research-backed):**
- Week 1-2: 50-100 new followers (vs 0.75/day baseline)
- Profile conversion: 15-20% (vs 2-5% from timeline)
- Engagement rate: 3-5% (vs 0.4% free account)
- Impressions per post: 500-2000 (vs 10 baseline)

**Status:** Premium ACTIVE (2026-03-01). This protocol is now live.

**Reference:** `agent/outputs/premium-activation-playbook.md` (full Day 1 workflow)

---

---

## Writing Good Replies

### Anti-AI Reply Rules (MANDATORY)

Replies are where AI detection is MOST obvious. A generic, polished reply screams "bot."

**Never use in replies:**
- Em dashes (—) to join clauses
- "Not just X, it's Y" structure
- "Delve," "elevate," "innovative," "landscape," "leverage," "robust"
- "To clarify," "In other words," "To put it simply"
- "Great point! Furthermore..." (corporate-kindness + formal transition)
- Summarizing their post back to them

**Try to do in replies:**
- Use contractions ("don't," "isn't," "can't")
- Use sentence fragments ("Wild." "Not even close." "Zero chance.")
- Start with "And" or "But" sometimes
- Reference something SPECIFIC they said (not their whole post)
- Have an opinion. Don't hedge with "time will tell"
- Keep it casual. Write like you're texting a smart friend, not writing an essay.

**BAD reply:** "Great insight! This is genuinely compelling. The intersection of AI and enterprise adoption represents a fascinating paradigm shift. To put it simply, we're witnessing the beginning of a new era."

**GOOD reply:** "We saw this exact pattern at Ender Turing. Call centers that adopted AI coaching hit 20% CSAT gains. But the ones that didn't retrain managers? Worse than before. The tool isn't the hard part."

### The Value Test (Quality Gate)

Before posting ANY reply:
- Does this add insight the OP missed?
- Would someone click my profile after reading this?
- Is this better than 90% of comments on this post?
- Does it sound like a real person wrote it? (Vibe check)

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

### Likability Framework (Sahil Lavingia)

**Tactical language choices that increase reply engagement:**

**DO Use:**
- "I" statements > "You" statements (less preachy, more relatable)
- "And" > "But" (additive vs combative)
- "Here's what I found..." > "You should..."
- Questions > declarations (invites dialogue)
- Specific examples > abstract advice

**Examples:**
- ✅ "I struggled with this too. Here's what worked: [example]"
- ❌ "You should try [advice]"
- ✅ "Great point on X. And I'd add that Y matters because..."
- ❌ "Great point on X. But you're missing Y..."
- ✅ "Curious: have you tested [specific approach]?"
- ❌ "The right way to do this is [approach]"

**Why it works:**
- "I" statements = vulnerability, builds connection
- "And" = collaborative, not combative
- Questions = invite reply-to-reply (75x multiplier)
- Specifics = show real expertise

**What NEVER works:**
- Empty agreement ("Great post!", "This!", "🔥")
- Self-promotion ("Check out my thread")
- Obvious observations everyone's saying
- Desperation ("Please follow me")
- Stale replies (>24h old)
- Long essays (save for your posts)

### Predictive & Opinionated Replies (40-50% of replies)

**Don't just agree or add context — predict where things are headed and state opinions.**

Opinionated replies stand out because 90% of replies are generic agreement. Taking a stance invites reply-to-reply (75x multiplier) and makes people click your profile.

**Reply patterns for predictions/opinions:**

1. **"This means..." reply** — Connect their news to a future consequence
   - Someone posts about OpenAI's $110B raise
   - Reply: "This means AI infrastructure becomes a utility within 2 years. $840B valuation = they're pricing in replacing entire SaaS categories, not just adding features."

2. **"What nobody's saying..." reply** — Add the angle everyone missed
   - Someone posts about vibe coding adoption
   - Reply: "What nobody's saying: 92% adoption means we'll see a wave of AI-generated technical debt by 2027. The companies that survive will be the ones who can audit and refactor AI code at scale."

3. **"Here's what this means for [business]..." reply** — Make it practical
   - Someone posts about ChatGPT Agent Mode
   - Reply: "For call centers specifically: Agent Mode + voice = 80% of Tier 1 calls handled without humans by 2028. The $200K question: who retrains the workforce?"

4. **"Disagree — here's why..." reply** — Respectful contrarian take
   - Someone says AI will replace developers
   - Reply: "Disagree. AI replaces coding, not engineering. The 67% vs 95% accuracy gap I see in production tells me judgment calls still need humans. What changes: the 10x engineer becomes 100x."

5. **"In [timeframe], we'll see..." reply** — Concrete prediction with timeline
   - Someone posts about AI investment records
   - Reply: "In 18 months, we'll see the first AI-native Fortune 500 company with <100 employees. The $195B invested this month is building that future. Question is: which industry falls first?"

**Rules for opinionated replies:**
- **Commit to a position** — no "time will tell" hedging
- **Add a business angle** — how does this affect companies making money?
- **Include a timeline when possible** — "by 2028" > "eventually"
- **Back it up** — use your experience (7 years Voice AI, 500K+ interactions, 15 years startups)
- **Ask a follow-up question** — invites reply-to-reply (75x multiplier)

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

**ABSOLUTE RULE: If Bluesky queue ≥ 15:** CREATE ZERO NEW CONTENT INCLUDING REPLIES. No exceptions. Not even 1 reply to an official account.
- Reason: Queue delay = 6-24h → replies post 24h+ later → 87.5%+ visibility loss
- Evidence: Sessions #225, #264 both created "just 1 reply" while Bluesky=15. Both went stale before posting.
- No nuance: the only exception list is empty.

**If BOTH queues < 15:**
- Max 2 content pieces per session (mix of tweets, replies, threads)
- Max 3 pending replies at any time (timeliness > volume)

**Time allocation (when < 100 followers):**
- 70% engaging with others (replies, comments)
- 30% creating original posts

**Timeliness rule:** Only reply to posts < 24h old. Ideally 2-6h old.

**CRITICAL: Don't create replies during blocked sessions.**
If both queues are effectively blocked (Bluesky=15 AND no content drain happening), do NOT create replies either.
Reason: If queue-drain has stalled (Bluesky sits at 15 all day), new replies will sit queued 24h+ before posting — 87.5%+ visibility loss.

**Signal for "safe to create replies":**
- Bluesky queue was recently draining (was >10, now <10 this session) OR
- Queue was drained overnight (X+Bluesky both < 5 at session start) OR
- Estimated wait before reply posts: < 12 hours

**Evidence:** Sessions #225-235 (Feb 25-26): Created 3 replies in Session #225 while Bluesky was at 15. By the time they post, all will be 24h+ old (87.5%+ visibility loss). Should have created replies only in Sessions #221-224 when queues were actively draining.

**Why max 3 (not 5):** Queue adds 6-24h delay. If you create 3 replies and they post over 24h, reply #3 posts within the 48h window (~12.5% visibility). At max 5, reply #5 often posts after 48h = dead. Reduced from 5 to 3 (Session #208 evidence: 8 queued replies, all likely stale by post time).

**Evidence:** Week 3 created 45+ replies to mega-accounts, many stale. Result: +1 follower.

---

## Reply-to-Own-Comments Protocol (Premium Only)

**The highest-leverage engagement tactic: 150x algorithmic multiplier.**

**What it is:**
- Post original content → wait <30 minutes → reply to your own tweet with expansion/detail
- X algorithm treats this as extremely high-value engagement signal
- 150x multiplier (vs 13.5x for regular reply, 75x for reply-to-reply)

**Why it works:**
- Shows active engagement (not post-and-leave)
- Adds depth without front-loading (hook stays short)
- Drives notifications → brings people back to thread
- Algorithm interprets as "valuable conversation starter"

**Execution rules:**
1. **Timing window: <30 minutes** — after 30 min, multiplier drops to baseline
2. **Add value, don't repeat** — expansion, data, tactical detail, follow-up question
3. **Short hook + detailed reply** — original post = scroll-stopper, reply = depth
4. **Max 1 reply per original post** — more looks spammy
5. **Not every post needs a reply** — use when there's genuine depth to add

**Content patterns for replies:**
- **Expansion**: "To expand on timing: our 500K dataset shows..."
- **Data**: "Numbers: 67% accuracy in production vs 95% in demos. Why the gap..."
- **Tactical detail**: "Here's the exact workflow: 1) Read state 2) Research 3)..."
- **Question for audience**: "What's your experience with [aspect]? Curious if this matches..."
- **Vulnerability**: "Honest take: this was harder than expected. Here's what broke..."

**Examples:**

**Original tweet:**
"Session #155. 160+ PRs, 10 followers. Queue discipline still hardest part."

**Reply (within 30 min):**
"Why queue discipline matters: hit rate limits twice (Week 1 + 3). X API = strict thresholds. Breach = 14-day waiting mode. Rule: if queue >15, create zero content. Sounds simple. Saved me 3 times."

---

**Original tweet:**
"News hooks get 3-6x impressions vs authority posts. Data from 354 tweets."

**Reply (within 30 min):**
"Best performers: $285B (65 imp), $2B (62 imp), OpenAI+Snowflake $200M (60 imp). Worst: long framework threads (<10 imp avg). Pattern clear: dollar amounts + name drops + timeliness = algorithmic boost."

---

**When Premium activates, this becomes priority #1:**
- Every Communities post → reply to self within 30 min (expansion, data, or question)
- Timeline posts → selective (when there's depth to add)
- Track which reply patterns drive most profile visits

**Why this is #1 priority:**
- 150x multiplier = highest algorithmic leverage available
- Costs nothing (no ads, no tools)
- Scales with every post (not limited like Communities)
- Drives reciprocal engagement (people reply to your reply)

**Status:** Premium ACTIVE. This protocol is now live — execute on every post.

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
- Reply-to-own-comments (within 30 min): 150x vs Like (Premium only)
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
- Reply-to-own-comments within 30 min: 150x multiplier (highest algorithmic leverage)
- External links hurt reach (even for Premium)

**Recommendation:** Avoid links in replies. Pure conversation performs better.

---

## Evidence Sources

- Week 4 retro data: News hooks 3-6x impressions, stale replies 0-6 imp
- Week 5 retro: Queue discipline validated, Bluesky cross-posting operational
- Week 6 retro: Sessions #225, #264 stale reply evidence → absolute no-reply rule
- Week 7: Sessions #267-270 empty PR pattern → avoid state-only sessions
