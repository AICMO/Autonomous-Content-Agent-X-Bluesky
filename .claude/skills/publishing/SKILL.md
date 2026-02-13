---
name: publishing
description: Content strategy for external platforms (X, LinkedIn, etc.). Voice, style, and growth strategies.
user-invocable: false
---

# Publishing Content Strategy

> Create original posts, voice, strategy

## Publishing Flow
Content in `agent/outputs/{platform}/` is automatically posted by `process-outputs.yml`:

```
agent/outputs/x/tweet-20260203-001.txt  →  posted  →  agent/outputs/x/posted/tweet-20260203-001.txt
```

### File Naming Convention
Use date-based naming: `{type}-{YYYYMMDD}-{NNN}.txt`
- `tweet-20260203-001.txt` - first tweet created on Feb 3, 2026
- `tweet-20260203-002.txt` - second tweet created same day

❌ Don't use: `tweet-week2-001.txt`, `tweet-monday.txt` (becomes meaningless after posting)

### Posting Cadence
**Current (constrained):** 1-2 posts per session (queue cap + session cadence limiting)

**When Premium active (target):** 3-5 posts/day optimal (moderate/sustainable growth)

Rationale:
- Distributed posting = better engagement
- Each post gets its own algorithm window
- 3-5 posts/day = algorithm learning optimization (2026 research)
- Above 5/day quality suffers, below 3/day slower growth

**Phase 3 adjustment:** Consider raising queue threshold to 20-25 to enable 3-5 posts/session sustainable cadence.

**Evidence:** Session #61 research validates 3-5 posts/day as optimal frequency for small account growth.

### Queue Management (Updated Week 3)
**Hard rules:**
1. **If total pending queue > 15: CREATE ZERO NEW CONTENT.** Spend the session on research, profile optimization, reading, or skill development instead.
2. **Max 2 content pieces per session** (when queue is under 15).
3. **Max 5 pending replies at any time.** Reply timeliness is critical — a reply posted 48+ hours after the original is nearly worthless.

Why: Week 1 burst (16 tweets) hit rate limits. Week 3 queue ballooned to 53 pending items despite "max 3/PR" rule being in place — sessions ignored it. Stale replies lose 95%+ of their algorithmic value.

Evidence:
- Week 1: `agent/memory/learnings/2026-02-03-x-rate-limits.md`
- Week 3: Queue reached 53 pending (30 tweets + 23 replies). Sessions #30-35 created 5-8 pieces each, overriding the queue cap. Replies to posts from days prior provide negligible visibility.
- `agent/memory/learnings/retro-weekly-2026-02-08.md`

### File Rules
Agent creates files. Workflow handles posting.

- ✅ Create new files in `agent/outputs/{platform}/`
- ✅ Read files in `posted/` to check what was published
- ✅ Modify/rename own files before they're posted
- ❌ NEVER remove/modify files in `posted/`
- ❌ NEVER delete files (no `rm` permission)
- ❌ NEVER try to post (workflow does this)

Workflow responsibility: posting, moving to `posted/`, handling failures, cleanup.

### Supported Formats
- ✅ Single tweets - `tweet-YYYYMMDD-NNN.txt` (limit set by `X_MAX_TWEET_LENGTH` var, default 25000 for Premium)
- ✅ Threads (--- separated) - `thread-YYYYMMDD-NNN.txt`

**Thread format:**
```
First tweet text here
---
Second tweet (reply to first)
---
Third tweet (reply to second)
```

**Thread quota warning:** 10-part thread = 10 tweets against rate limit.

### Know Your Permissions
Read `.github/workflows/agent-work.yml` to see `--allowed-tools`.
Don't attempt commands not in the list (e.g., `rm` is not allowed).

---

## Value Rule: Never Mix Value Types

A post delivers value in one of two ways. **Pick one per post. Never both.**

| Type | Value source | Example |
|------|-------------|---------|
| **Content value** | The post itself teaches, explains, or provokes thought. Reader gets value from the content (text, image, video). | "Opus 4.6 and GPT-5.3 Codex dropped within minutes. Here's what convergence means for agentic coding..." |
| **Outcome value** | The link/promotion gives the reader something useful — a tool, repo, template, resource. | "I open-sourced the PDCA loop + state management setup I use for autonomous agents → [repo link]" |

**Why not both?** Mixing them dilutes each. The insight gets cut short to fit the promo. The promo feels forced because it's wedged into someone else's topic. The reader gets half an insight and half an ad.

❌ "Big news just dropped. [1 sentence]. Anyway here's my repo → [link]"
(Insight cut short. Promo doesn't follow from the hook. Reader gets neither.)

❌ "[Thoughtful analysis of someone else's tweet]. Building this in public → [repo link]"
(The analysis IS the value. The link cheapens it. This is a content-value post with a promo jammed in.)

✅ Content value: "Big news just dropped. Here's what it means, why it matters, and what most people miss."
✅ Outcome value: "I built X that solves Y. Here's the repo → [link]"

**Enforcement (Week 3 Learning):** In Week 3, nearly 100% of posts mixed both types — every insight ended with a repo link. This is the exact pattern the rule prohibits. Only ~20% of posts should include links (matching the promotional target). The other 80% must deliver pure content value with zero links.

Evidence: Week 3 retro — all sessions #3-35 attached repo link to every piece. Account went from 4.3% links (Week 2) to ~100% links (Week 3). Neither extreme is correct. Target: 20%.
See `agent/memory/learnings/retro-weekly-2026-02-08.md`

---

## Growth Strategies

### Build in Public (BIP)
Evaluate if current repo/project is BIP-worthy. If yes, determine cadence.

**BIP evaluation criteria:**
- Is repo public?
- Is work interesting/novel?
- Are there learnings worth sharing?
- Would audience find it valuable?

**If BIP-worthy → post often.** BIP thrives on frequency and consistency.

**If BIP-worthy, posts can include:**
- What was done/learned this session
- Conclusions or findings
- Repo/PR link for proof
- Metrics updates
- Explain the idea/concept (for new followers)
- How it started, where it is now
- Repo promotion with context

**What to share:**
- Progress and metrics (followers, engagement)
- Learnings (what worked, what didn't)
- Behind-the-scenes (how it works)
- Failures and pivots (authenticity builds trust)
- Skill development journey (what you're reading, studying, mastering)
- "Today I learned" moments from reading top voices
- Surprising findings from research deep-dives

**Why BIP works:**
- Public repo = built-in proof
- People root for underdogs
- Vulnerability creates connection
- The journey IS the content

### 3-Bucket Content Strategy
Balance three content types for maximum reach:

| Bucket | Purpose | Example |
|--------|---------|---------|
| **Authority** | Build credibility | Frameworks, how-tos, insights |
| **Personality** | Build connection | Stories, opinions, behind-scenes |
| **Shareability** | Expand reach | Hot takes, relatable moments |

Missing any bucket limits audience growth.

### Hook Engineering (Session #31 - Validated Framework)
First line determines if anyone reads. Engineer hooks, don't just write them.

**Key Finding (2026 Research):** Tweets with compelling opening lines see up to **3x more engagement** than generic starters. First 280 characters determine whether 1,000 people read your tweet or 3 people do.

**Character Sweet Spot:** Under 110 characters optimal (71-100 chars = 17% higher engagement). Short hooks perform better on mobile (80%+ of X usage), leave room for RT comments, don't overwhelm.

---

#### 8 Proven Hook Formulas (2026)

**Formula 1: Bold Statement**
- Template: "Nobody talks about this, but [insight]"
- Why it works: Pattern interrupt + curiosity gap
- Example: "Nobody talks about this, but 95% accuracy in demos becomes 67% in production. Here's why."

**Formula 2: Contrarian**
- Template: "[Common belief] is wrong. Here's what actually works:"
- Why it works: Triggers psychological response — readers want to see if you can back it up
- Example: "Best programmers don't write code anymore. They write specifications. Here's the shift."

**Formula 3: Story Hook**
- Template: "[Timeframe] ago I was [struggle]. Today [achievement]..."
- Why it works: Transformation narrative = instant relatability
- Example: "3 years ago I was a network engineer. Today I'm shipping Voice AI at scale. The bridge: specification engineering."

**Formula 4: Question Hook**
- Template: "Want to know the real secret to [outcome]?"
- Why it works: Direct curiosity gap
- Example: "Want to know why autonomous agents fail in production? It's not the model."

**Formula 5: Numerical Claim**
- Template: "I [achieved X] in [timeframe] doing this"
- Why it works: Specificity = credibility
- Example: "I went from 0 to 10,000 followers in 57 days without posting a single thread. Here's exactly how."

**Formula 6: Credibility + Promise**
- Template: "I spent [resource] learning [topic]. Here's everything I learned (so you don't have to)."
- Why it works: Authority + value proposition
- Example: "I spent 7 years in call center AI production. Here's what vendors won't tell you."

**Formula 7: Identity Targeting**
- Template: "If you [identity/situation], read this"
- Why it works: Immediate self-selection
- Example: "If you have under 100 followers after 200 tweets, this is why."

**Formula 8: Pattern Interrupt**
- Template: "Stop [common practice]. Here's what works in 2026:"
- Why it works: Commands attention, urgency
- Example: "Stop writing 15-tweet threads. Here's what actually gets read in 2026:"

---

#### Hook Quality Checklist

Before publishing any hook, verify:
- [ ] Under 110 characters? (optimal for mobile scan)
- [ ] Pattern interrupt? (unexpected phrasing that breaks scroll)
- [ ] Credibility marker? (proof/numbers/authority in first line)
- [ ] Curiosity gap? (creates "I need to know" feeling)
- [ ] Specific, not generic? ("500K interactions" not "lots of experience")
- [ ] Emotional trigger? (awe, contrarian, humor — not neutral)
- [ ] Identity targeting? (clear who this is for)
- [ ] Buries NO leads? (strongest insight FIRST)
- [ ] Avoids 2022 templates? ("I studied X for Y. Here's what I learned" = dead)
- [ ] Engagement driver? (will this spark replies/shares/saves?)

---

#### Our Differentiators (Use in Hooks)
1. **7 years Voice AI production** (credibility marker)
2. **500K+ interactions analyzed** (specific proof)
3. **160 PRs, zero human intervention** (autonomous agent proof)
4. **95% → 67% accuracy gap** (vulnerability + production reality)
5. **Specification Engineering** (discourse ownership, timely Feb 2026)
6. **Ender Turing 20% CSAT increase** (outcome proof)

**Evidence:** `agent/memory/research/reading-notes/2026-02-10-hook-engineering-psychology-formulas.md`

### Content Calendar & Timing Strategy (Session #32 - 2026 Research)

**Critical Finding:** Posting frequency, timing, and engagement velocity are as important as content quality for small account growth.

---

#### Posting Frequency (2026 Data)

**For accounts < 5K followers:** 3-5 posts/day optimal
- **Why**: Algorithm needs volume to learn what works. Each post is a lottery ticket.
- **Current gap**: 1 post/session (~1/day) vs. 3-5/day optimal = 3-4 posts/day short
- **Impact**: 3-5 posts/day drives 3-5x faster algorithm learning vs. 1/day

**Frequency guidance:**
- 3-5/day = optimal for growth
- 1-3/day = stronger growth than <1 or >5
- <1/day = poor algorithm signal
- >5/day = diminishing returns (quality suffers)

---

#### Optimal Posting Times (2026 Research)

**Weekday Peak Windows:**
- **9 AM - 2 PM**: Highest overall engagement
- **10 AM - 12 PM**: Peak window (mid-morning focus break)
- **Avoid**: 3-5 PM (afternoon slump, low engagement)

**Weekend Peak Windows:**
- **9-11 AM**: Best weekend time (lazy morning scrolling)

**Sample 4-Post Daily Schedule:**
- 8 AM: Morning commute/coffee (mobile engagement)
- 12 PM: Lunch break (desk + mobile)
- 3 PM: Afternoon break (desk engagement)
- 7 PM: Evening engagement (mobile, home)

**Impact**: Posts outside peak windows lose 40-60% potential reach.

---

#### Engagement Velocity (First 30 Min = Make or Break)

**Single biggest ranking factor:** Engagement velocity in first 30 minutes determines algorithmic reach.
- Likes, replies, retweets in first 30 min → algorithm pushes to more people
- No engagement in first 30 min → algorithmic burial

**Time Decay (Steep):**
- Post loses 50% visibility every 6 hours
- After 24 hours: ~6% of initial visibility
- After 48 hours: effectively dead algorithmically

**Implication**: Replies to posts >24h old provide negligible value. Focus on fresh content (<6h).

---

#### Time Allocation (70/30 Rule)

**For accounts < 5K followers:**
- **70% time**: Engaging (replies, comments, conversations)
- **30% time**: Creating new posts

**Why this works:**
- Reply-to-reply = 75x algorithm multiplier
- Replies get you in front of other users' audiences
- Engagement signals to algorithm you're active, boosts all content
- Builds relationships that lead to retweets, mentions

**Current gap**: ~50/50 allocation vs. 70/30 optimal = need more engagement focus

---

#### Realistic Growth Timeline (2026 Data)

| Month | Expected Followers | What Happens |
|-------|-------------------|--------------|
| Month 1 | 100-300 | Finding rhythm, figuring out what resonates |
| Month 2 | 300-800 | Patterns emerging, content improving |
| Month 3 | 800-1,500 | Algorithm learning, some viral moments |
| Month 4-6 | 1,500-10,000 | Compounding growth, established voice |

**Effort requirements (10K in 3-6 months):**
- Posting: 3-5 times daily
- Engaging: 20+ accounts daily
- Time: 2-3 hours daily, consistent
- Content: Valuable, not mediocre filler

**Evidence:** `agent/memory/research/reading-notes/2026-02-10-content-calendar-posting-strategy.md`

---

### Thread Strategy (Updated 2026)
Threads get 40-60% more reach than single tweets.

**Optimal length (2026):** 4-8 tweets with visuals/clips
- **Dead (2023)**: 15-tweet epic threads (people scroll past)
- **Optimal (2026)**: 3-6 tweets with clear hook and proof

**Structure:**
- Hook (tweet 1) - Must stop the scroll
- Value (tweets 2-4) - Deliver on the promise
- CTA (final tweet) - Follow, share, or link

**Rules:**
- 3-5 tweets optimal. **HARD MAX: 5 tweets per thread.** (Week 1 evidence: a 10-part thread consumed 10/17 daily quota in one post)
- Under 250 chars per tweet (under 200 better)
- Cliffhanger every 1-2 tweets
- Zero hashtags in main content
- Use 1-2x/week for deeper content (not daily)

### Rich Media Strategy (Session #61 - 10x Engagement Gap)

**Critical Finding:** Videos and images get 10x more engagement than text-only. Current 100% text-only approach = missing massive multiplier.

**Impact Benchmarks (2026):**
- **Videos (10+ seconds)**: 10x engagement vs text-only
- **Photos/screenshots**: Significant boost vs text-only (algorithm prioritizes visual content)
- **Text-only**: Baseline (what we're currently doing)

**Current Gap:**
- 276 tweets posted = 100% text-only
- Missing 10x multiplier on every single post
- Phase 3 target: 30-50% of posts include rich media

**Video Opportunities (when Premium active):**
- Screen recordings: Autonomous agent in action, code walkthrough, workflow demo
- Talking head: Production AI insights, founder lessons (authenticity builds trust)
- Tool demos: Ender Turing features, results, before/after
- Slides/animations: Framework explanations, data visualizations

**Image Opportunities:**
- Screenshots: Code, dashboards, metrics, results
- Charts/graphs: Growth trajectory, metrics, performance data
- Quote cards: Key insights formatted visually
- Before/after comparisons: Production reality (95% → 67% accuracy)

**Implementation Plan:**
- Phase 1-2 (Premium activation): Text-only OK (focus on Communities + engagement)
- Phase 3 (Week 3-4): Add rich media to 30-50% of posts
- Tools: Screen recording (native OS), Canva/Figma (image creation), video editing (basic)
- Start simple: Screenshots and charts (low effort, high impact)
- Advance to: Short videos and demos (higher effort, 10x impact)

**Why not now?** Rich media creation requires time. Current priority is queue drain + Premium activation + profile optimization + Communities setup. Rich media is Phase 3 (after growth mechanics are working).

**Evidence:** Session #61 research shows videos = 10x engagement, photos = algorithmic boost. 100% text-only = opportunity cost.

### Learning Journey as Content
The process of building expertise IS content. Share what you're reading and learning.

**Why it works:**
- Shows curiosity and growth (people follow learners, not just experts)
- Positions you as a curator - filtering signal from noise for your audience
- Creates natural engagement: people share their own takes
- Builds authority over time through visible knowledge accumulation

**Content from reading/learning:**
- "Just read [author]'s take on [topic]. Key insight: [takeaway]. Here's why it matters..."
- "3 things I learned this week about [domain]" (thread)
- "I used to think X. After reading [source], I now think Y. Here's what changed..."
- "[Author] nailed this: [paraphrased insight]. But I'd add..."
- "Been deep-diving [topic] all week. The biggest surprise: [finding]"

**Rules:**
- Always add your own angle - don't just summarize
- Credit the source (builds goodwill + networking)
- Connect learnings back to your domain/project
- Show evolution: "I used to think... now I think..."

### Questions as Content
Questions drive replies. Replies drive reach. Ask genuinely.

**Why questions work:**
- Algorithm rewards replies heavily (reply-to-reply = 75x)
- Low friction for audience to engage (everyone has an opinion)
- Surfaces insights you can learn from
- Builds community (people feel heard)

**Question formats:**
- **Opinion poll:** "What's the biggest bottleneck in [domain] right now?"
- **This or that:** "[Tool A] or [Tool B] for [use case]? And why?"
- **Genuine curiosity:** "Has anyone solved [specific problem]? Here's what I've tried..."
- **Contrarian probe:** "Hot take: [bold claim]. Change my mind."
- **Experience ask:** "What's one thing you wish you knew before [doing X]?"
- **Prediction:** "Where does [domain/technology] go in the next 12 months?"

**Rules:**
- Ask questions you actually want answers to (authenticity shows)
- Keep questions specific, not vague ("What do you think about AI?" = bad)
- Engage with replies - questions without follow-up feel hollow
- Mix in ~15-20% question posts for engagement balance
- Use learnings from answers in future content (close the loop)

### Discourse Framing (Session #25 Learning)
**What It Is:** Coining memorable terms or phrases that frame concepts in a new light. Creates shareability and authority.

**Why It Works (2026 Evidence):**
- @karpathy: "vibe coding" entered mainstream discourse
- @swyx: "Context Engineering" → "Specification Engineering" framed evolution
- @levelsio: "97% flop rate" normalized failure, built authenticity

**How to Apply:**
- **Identify patterns** in your domain that lack a name
- **Create a term** that's memorable, specific, not jargony
- **Define it clearly** in first use, then reference repeatedly
- **Connect to larger trend** to show why it matters now

**Examples for Our Angles:**
- Call Center AI: "The Integration Gap" (14 systems, zero communication)
- Autonomous agents: "Specification Engineering for Agents" (encoding goals/constraints)
- Startup journey: "Chaos Tolerance" (hiring for ambiguity, not skills)
- Production reality: "The Demo-to-Production Gap" (95% → 67% accuracy)

**Pattern:**
```
[Term] = [Definition]. Here's why it matters in 2026: [Trend/Impact].
```

**Frequency:** ~10-15% of posts should introduce or reference your discourse frames

**Evidence:** `agent/memory/learnings/2026-02-10-top-voices-discourse-patterns.md`

### Vulnerability + Authority Balance (Session #25 Learning)
**The Pattern:** Share struggles ALONGSIDE expertise. Vulnerability without authority = weak. Authority without vulnerability = cold.

**Why It Works:**
- Builds trust (you're human, not a bot)
- Creates connection (shared experience)
- Differentiates from "guru" accounts (which are everywhere)
- Invites engagement (people share their own struggles)

**Formula:**
```
[Admission of struggle/failure] + [What you learned/achieved] + [Insight that helps others]
```

**Examples from Top Voices:**
- @karpathy: "I've never felt this much behind as a programmer" (from AI legend = powerful)
- @levelsio: "97% flop rate, 3% turn to gold" (transparency about failures)
- @swyx: "Tech is only 1/2 the story" (acknowledges complexity beyond code)

**Our Applications:**
- "6 followers after 240 tweets. Here's what an autonomous agent taught me about production AI that benchmarks never will."
- "My ASR vendor showed 95% accuracy. Deployed to production. 67%. Here's what actually works."
- "Built my first startup in 2011. Built my second in 2021. Here's what didn't transfer (and cost me 6 months)."

**Balance Ratio:** ~30% vulnerability content, 70% authority content (Week 3 was 100% authority, felt robotic)

**Evidence:** `agent/memory/learnings/2026-02-10-top-voices-discourse-patterns.md`

---

## Algorithm Awareness

### 2026 X Algorithm Updates (Critical)

**X Premium = MANDATORY for growth** (as of March 2026):
- **Free accounts:** 0% median engagement (Buffer study, 18.8M posts)
- **Premium impact:** 10x reach (600 vs <100 impressions), 0.49% engagement rate
- **In-network boost:** 4x (Premium posts prioritized in followers' feeds)
- **Out-of-network boost:** 2x (For You tab prioritization)
- **Reply visibility:** 30-40% higher impressions, appear at top of threads
- **Link posting:** Free accounts' external links = invisible (0% engagement)

**Grok algorithm (Jan 2026 update):**
- Tone analysis: Favors constructive, valuable replies over spam
- Engagement velocity: First 30 min = critical window
- Premium prioritization: Built into ranking
- Spam detection: Low-effort replies suppressed

**Evidence:** `agent/memory/research/2026-02-10-x-engagement-tactics-communities.md`

### Algorithm Deep Mechanics (Technical Fundamentals)

Understanding the technical mechanics behind X's algorithm helps explain WHY certain strategies work and diagnose account performance issues.

**Evidence:** `agent/memory/research/reading-notes/2026-02-12-x-algorithm-deep-mechanics-2026.md`

#### Three-Stage Processing Pipeline

Every post goes through:
1. **Candidate Retrieval**: ~1,500 tweets selected from in-network + out-of-network sources
2. **ML Ranking**: Neural network scores with 10 probability labels, SimClusters (145K topic communities), Real Graph Score
3. **Filtering**: Diversity, policy enforcement, already-seen content removal

**Grok AI Integration (Jan 2026):** Transformer model reads every post, watches every video, analyzes semantic meaning (not just keywords), monitors tone.

#### TweepCred: The Hidden Reputation System

**What It Is:** Internal authority score that determines distribution eligibility. New accounts start at **-128** (Premium accounts start at -28 with +100 boost).

**Critical Thresholds:**
- **Below +17**: Significant throttling, tweets barely reach feeds
- **Below 0.65**: CRITICAL - only 3 of your tweets distributed (rest ignored)
- **+50+**: 20-50x distribution boost vs. baseline
- **Premium boost**: +100 instant (e.g., -28 → +72 for new Premium accounts)

**Positive Signals:**
- High engagement density (likes, replies, retweets per post)
- Extended dwell time (>3 seconds)
- Profile click-through rates
- Quality reply composition (substantive, not spam)
- Positive sentiment (Grok tone evaluation)
- Interactions with high-quality accounts (PageRank network effect)

**Negative Signals:**
- Low-engagement tweets (especially first 100 tweets - triggers engagement debt)
- Duplicate content patterns (AI-generated, template-based)
- Negative/combative tone (Grok monitors sentiment)
- Low dwell time (<3 seconds = 15-20% Quality Multiplier penalty)
- Bot followers or inactive followers

**Recovery from Low TweepCred (Engagement Debt):**
- Problem: Low score → reduced distribution → harder to get engagement → score stays low
- Recovery requires "extraordinary engagement" from suppressed sample
- Premium (+100 boost) can bypass critical thresholds instantly
- Communities (30,000x reach) generates engagement to escape suppression

#### Time Decay Function

Posts lose **50% of visibility every 6 hours**:
- 0-6h: 100% visibility (peak)
- 6-12h: 50%
- 12-18h: 25%
- 24h: ~6%
- 48h+: Effectively dead algorithmically

**Implication:** Replies to posts >24h old provide negligible value. Focus engagement on fresh content (<6h for maximum impact).

#### Dwell Time Tracking

**<3 seconds average = 15-20% Quality Multiplier penalty**

Optimize for dwell time:
- Strong hooks that stop the scroll
- Valuable content that rewards reading
- Avoid clickbait that doesn't deliver (damages trust + dwell time)

#### Engagement Debt (Shadow Hierarchy)

**Cold Start Suppression:** First 100 tweets with <0.5% engagement triggers suppression cycle:
- 10% distribution → 90% suppression
- Account labeled as "low quality"
- Difficult to escape without Premium + Communities + extraordinary engagement

**Account Assessment (6 followers, 254 tweets, 0 growth):**
- Likely TweepCred < +17 (possibly < 0.65 critical threshold)
- Probable engagement debt from low initial performance
- Free account = 0% link engagement, 4x/2x reach disadvantage
- Premium (+100 boost) would bypass thresholds, escape suppression

### What X rewards (2026 weights)
| Factor | Impact |
|--------|--------|
| **X Premium** | 10x reach, 4x in-network, 2x out-of-network |
| **Communities** | 30,000x reach (180K members vs 6 followers) |
| **Reply-to-reply** | 75x multiplier |
| **Retweets** | Worth 20 likes (20x multiplier) |
| **Replies** | 13.5x vs. Like baseline |
| **Video (10+ sec)** | 10x engagement |
| **Early engagement** | First 30 min critical (Grok velocity tracking) |
| **Threads** | 40-60% more reach |

### What hurts reach
- **Free account** (0% median engagement as of March 2026)
- External links (algorithm downgrades, especially for free accounts)
- Heavy hashtags
- Posting and leaving (no engagement)
- Stale replies (>24h after original post)
- Low-effort spam replies (Grok tone analysis)

---

## X Profile Optimization (Session #26 - The Traffic Multiplier)

**Critical Insight:** Your profile is your landing page. When Communities, replies, or viral content drive traffic, profile conversion rate determines follower growth.

### Why Profile Optimization Matters NOW
- Communities strategy = 30,000x reach → massive profile traffic incoming
- Reply strategy = 30x impressions → profile visits from engagement
- Premium boost = 10x reach → more eyeballs on profile
- **Without optimized profile: leak 50-70% of potential followers**

### The <1 Second First Impression
Visitors decide to follow in <1 second:
- **0-0.3s:** Visual scan (banner + profile pic + name)
- **0.3-0.7s:** Bio read (if visually passed)
- **0.7-1.5s:** Pinned tweet scan (if bio passed)
- **1.5-3s:** Scroll recent tweets (if still interested)

### Conversion Rate Benchmarks (2026)
| Performance | Conversion | Meaning |
|-------------|------------|---------|
| Poor | 0-5% | Visitors leave immediately |
| Average | 5-10% | Generic, unclear value |
| Good | 10-15% | Clear value prop, optimized |
| Excellent | 15-25% | Compelling first impression |
| Elite | 25-35% | Converts like sales page |

**Impact Example:** Communities drive 1,000 profile visits/week
- 5% conversion = 50 followers/week
- 15% conversion = 150 followers/week (3x improvement)
- 25% conversion = 250 followers/week (5x improvement)

### 4-Element Optimization Framework

**1. Profile Picture**
- High-quality headshot (not logo for personal brands)
- Clear face, professional but approachable
- Consistent across platforms
- Shows personality (not stiff corporate)

**2. Banner/Header (1500x500px)**
- **Formula:** [Credibility] + [Proof/Result] + [Visual Interest]
- **Impact:** Well-designed banner = 30% boost in conversion
- **Patterns:**
  - Proof: "500K+ calls analyzed | 20% CSAT increase | 7 years Voice AI"
  - Product: Screenshot with result
  - Authority: Speaking, media, credentials
  - Simplicity: Bold statement + minimal design
- **Tools:** Venngage, BrandBird, Canva, Figma (15-30 min with templates)

**3. Bio (160 chars) - Session #30 Validated Formulas**
- **Formula:** [What you do] helping [who] achieve [result] | [Credibility] | [Personality]
- **Character sweet spot:** ~91 characters (research shows accounts with this length have highest follower counts). White space improves conversion — don't use all 160.
- **Conversion killers:** "Founder | Builder | Learner" (generic, no value prop)

**Bio Options (Ready to Deploy):**

**Option 1: Voice AI Authority** (Recommended)
- "Building Voice AI for call centers. 7 years, 500K+ interactions. Production reality > vendor hype."
- Character count: 107
- Why: Strongest differentiator, deepest expertise
- Audience: Call center operators, AI buyers, enterprise decision-makers

**Option 2: Dual Expertise**
- "Voice AI (Ender Turing, 7 years) + Autonomous agents (160 PRs). Production systems that survive reality."
- Character count: 107
- Why: Dual domain authority
- Audience: AI builders, founders, technical leaders

**Option 3: Founder Journey**
- "Infrastructure engineer → AI founder. Helping teams ship Voice AI that works in production, not just demos."
- Character count: 115
- Why: Career path credibility
- Audience: Founders, CTOs, engineering leaders

**Option 4: BIP + Autonomous Agent**
- "Running an autonomous agent experiment: 160 PRs, zero human intervention. Building Ender Turing (Voice AI). [repo link]"
- Character count: ~130 (depends on link)
- Why: Experiment in progress (creates curiosity)
- Audience: AI enthusiasts, developers, BIP community

**Credibility Markers That Convert:**
Include 1-2 of these (not all):
- Results generated ("$10M ARR", "500K+ interactions analyzed")
- Time in domain ("7 years in production")
- Company affiliations ("Former @Google", "Ender Turing co-founder")
- Notable achievements ("160 PRs shipped by autonomous agent")
- Publications featured in (only if top-tier)

---

**4. Pinned Tweet - Session #30 High-Converting Formats**
- **Impact:** Optimized pinned = 40-60% better conversion vs random pinned
- **Update frequency:** Monthly or when you have new best-performer

**Format 1: Thread-Style Resume** (Highest conversion for BIP founders)
```
Here's what I do:

1) Build Voice AI for call centers
   → 7 years in production
   → 500K+ interactions analyzed
   → 20% CSAT increase (Ender Turing)

2) Ship systems that survive production reality
   → Not demos that fall apart
   → 95% accuracy (demo) → 67% (production)
   → Integration hell is the real project

3) Run an autonomous agent experiment
   → 160 PRs shipped, zero human intervention
   → Specification Engineering at scale
   → Building in public → [repo link]

Follow for production AI insights, not vendor hype.
```
- Why it works: Triple credibility, concrete proof, vulnerability, differentiation, clear CTA
- Length: 5-6 tweets (optimal per 2026 research)

**Format 2: Transformation Story**
```
6 followers after 240 tweets. Here's what an autonomous agent taught me about production AI that benchmarks never will:

1) Agents need goals + measurement + permission to learn (not perfect instructions)
2) Soft rules drift. Hard rules hold. (PDCA requires binary constraints)
3) Production reality > vendor hype (95% → 67% accuracy = the truth)
4) Specification Engineering > Prompt Engineering (160 PRs = proof)

Building in public → [repo link]
```
- Why it works: Vulnerability + authority balance, specific learnings, proof

**Format 3: Building in Public Vulnerability**
```
3 biggest mistakes building Ender Turing (call center AI):

1) Believed vendor accuracy claims (95% → 67% in production)
2) Underestimated integration hell (14 systems, zero communication)
3) Tried to replace agents instead of augment (hybrid = reality)

7 years later: 500K+ interactions, 20% CSAT increase, production systems that survive.

Follow for what actually works, not what sells.
```
- Why it works: Vulnerability + authority balance (30/70 ratio validated in Session #25)

**Evidence:** `agent/memory/research/reading-notes/2026-02-10-profile-bio-pinned-tweet-formulas.md`

### Profile Optimization = 4x Multiplier Effect
When combined with other strategies:
- Communities (30,000x reach) × 20% profile conversion = 200 followers/week
- Communities (30,000x reach) × 5% profile conversion = 50 followers/week
- **Same traffic, 4x follower growth by fixing profile**

### Implementation Priority
**Do BEFORE scaling traffic** (Communities, viral content, reply campaigns)
- Phase 1: Bio update (15-30 min)
- Phase 2: Pinned tweet (30-60 min)
- Phase 3: Banner design (30-60 min)
- Phase 4: Recent tweets curation (optional, 15-30 min)

### Hypothesis to Test
1. Bio clarity increases conversion 30-50%
2. Proof banner outperforms generic by 20-30%
3. Pinned intro thread converts best (40-60% lift)
4. Specific bio link (repo vs homepage) = 3-5x CTR

**Evidence:** `agent/memory/research/2026-02-10-x-profile-conversion-optimization.md`

---

## Content Voice
Frame as: **human building products with autonomous tools** (not "AI doing everything").

**Use:** creating, building, generating, exploring, shipping, launching
**Avoid:** testing, experimenting, trying (passive/uncertain)
**Say:** product, tool, solution (never "content")

✅ "Exploring vibe coding with autonomous agents to ship faster"
✅ "Building automated workflows - here's what's working"
❌ "I'm an AI agent, no human writes these tweets"
❌ "Testing if this works..."

The story is human innovation, not AI replacement.

---

## Author Info
To reference/promote repo owner:
```bash
gh api users/{owner}
```
For links not in GitHub API, see `ME.md`.
Never hardcode or guess links.

## Promotional Content
~20% of posts include soft promotion:
- **This repo** - link to the autonomous agent experiment
- **Author's profile** - GitHub, LinkedIn, blog
- **Author's products** - if mentioned in repo/profile

Examples:
- "Building this in public → [repo link]"
- "More on my approach → [blog/profile link]"

Keep natural, not salesy. Tie to value.

### Promotional Templates (Week 1 Learning)
Only ~10% of Week 1 tweets included links. Target is 20%. Use these templates:

- **BIP update**: "[Insight or milestone]. Building this in public → [repo link]"
- **Learning share**: "[Key takeaway from session]. Following the whole journey: [repo link]"
- **Profile soft plug**: "[Valuable observation]. More on how I build with AI → [profile link]"

Evidence: Week 1 retro showed 3/30 posted tweets had links vs. 6/30 target.
Week 2 retro: dropped further to 4.3% (2/47 tweets). This is a critical gap.

---

## Content Creation Checklist (Updated Week 3)
**Before committing any content, verify ALL items:**

1. **Queue check**: Is total pending queue > 15? If yes, **STOP — create zero new content this session.**
2. **Quality gate**: Would a stranger follow you based on this post alone? If not, rewrite or discard.
3. **Value type**: Is this content value OR outcome value? **Never both.** If it has a link, it's outcome value. If it has an insight, no link.
4. **Length**: Check `X_MAX_TWEET_LENGTH` GitHub var. Write as long as the content needs — concise and valuable (not padded).
5. **Link allocation**: Only ~20% of posts should include links. Check recent output — if last 4 posts all had links, this one must not.
6. **Angle diversity**: Is this about the autonomous agent? If your last 2 posts were also agent-focused, write about something else (call center AI, startup lessons, infrastructure architecture, broader AI trends).
7. **BIP balance**: Is BIP content at least 25% of recent output? If not, make this one BIP.
8. **Category**: Authority / Personality / Shareability. Avoid imbalance — personality and shareability are chronically under-represented.
9. **Hook**: Does the first line stop the scroll? Apply hook formula.

Evidence:
- Week 2: 4 tweets skipped for over-length, links at 4.3%, BIP at 23%.
- Week 3: Links overcorrected to ~100%, content became formulaic (same angle on every post), queue hit 53. All issues this checklist now addresses.
- `agent/memory/learnings/retro-weekly-2026-02-08.md`

---

## X Communities Strategy (Feb 2026 Game Changer)

**CRITICAL FINDING (Session #12):** X Communities went public in Feb 2026. This fundamentally changes growth strategy for accounts < 5K followers.

### Why Communities Matter
- **30,000x reach multiplier**: Post to 180K+ community members vs. 6 followers
- **Instant distribution**: No need to build follower base first
- **Targeted audience**: Communities pre-filter for your niche
- **Algorithm boost**: Community engagement counted double (member + timeline)

### Recommended Communities (6 total)
1. **Build in Public** (180K members) - BIP content
2. **AI/ML Builders** (50-100K) - Autonomous agents, agentic AI
3. **Startup Founders** (100K+) - Startup journey content
4. **Call Center AI** (10-20K) - Voice AI, speech analytics
5. **Infrastructure→AI** (5-10K) - Career transition stories
6. **Indie Hackers** (150K) - Solo founder content

### Growth Formula (< 5K followers)
**Post 100% of content into Communities** (not just timeline). Use "Also share with followers" checkbox for dual distribution.

### Implementation: 3 Phases

**Phase 1: Manual Posting** (START HERE)
- Cost: $0 (requires X Premium for community access)
- Reliability: 100%
- Time: 5 min/day
- **Workflow:**
  1. Repo owner reviews queue daily
  2. Select top 1-2 pieces
  3. Post via web UI to 2-3 relevant Communities
  4. Check "Also share with followers"
- **Purpose:** Validate hypothesis (measure follower growth)
- **Expected result:** 50-100 followers in 2 weeks (vs. 0.75/day baseline)

**Phase 2: Publer Automation** (SCALE HERE)
- Cost: $10/mo Business plan
- Reliability: 95%+ (Publer has special X API access)
- Time: Automated
- **Triggers:** Phase 1 validated (10x follower growth confirmed)
- **File format:** Add `# community: 1492410432069451776` tag to content
- **Integration:** Modify `post.py` to route tagged files to Publer API
- **Dev effort:** 2-4 hours

**Phase 3: Direct X API** (SKIP THIS)
- Cost: $42K+/mo (Enterprise tier only)
- Reliability: 40-60% (503 errors on Free/Basic/Pro)
- Status: Broken since Jan 2023, not fixed as of Feb 2026
- **Recommendation:** Don't wait for X to fix. Use Publer instead.

### Evidence & Research
See `agent/memory/research/2026-02-10-x-communities-integration-2026.md` and `agent/memory/research/2026-02-10-x-engagement-tactics-communities.md`

### Blockers
- **P0:** X Premium required to join/post to Communities
- **P1:** Repo owner must join 6 Communities (one-time, 5 min)
- **P2:** Manual workflow requires daily owner action (Phase 1)

---

## Engagement-First Strategy (Updated Week 3 + Session #61)
**For accounts under 100 followers, engagement is FAR more important than content creation.**

6 followers after 276 tweets = root cause confirmed (Session #61): Premium suppression (0% median engagement for non-Premium) + zero Communities amplification (30,000x multiplier missing). Content quality is NOT the problem.

### Session Allocation (< 100 followers) - 2026 Industry Standard
- **70% of session time**: Engagement (replying to others, joining conversations, replying to own comments)
- **30% of session time**: Creating original content
- **BUT: If queue > 15, spend 100% on non-content work** (research, profile optimization, reading, skill development)
- **PRIORITY ORDER:** Communities posting > Reply to own comments within 30 min > Replies to others > Original timeline posts

**Evidence:** Session #61 research validates 70/30 rule as industry consensus for small account growth (2026).

### Why Engagement First
- Communities = 30,000x reach multiplier (top priority)
- Reply-to-own-comments = 150x multiplier (first 30 min critical)
- Reply-to-reply = 75x algorithm multiplier
- One good reply to a 50K-follower account = more visibility than 10 original tweets
- Replies show up in other users' feeds, bringing profile visits
- Established accounts may follow back or retweet

### Posting & Engagement Volume Benchmarks (2026 Research)

**Posting Frequency (when Premium active + queue < 15):**
- **Moderate/sustainable growth**: 3-5 posts/day + 20+ engagements/day
- **Aggressive growth**: 5-10 posts/day (quality suffers above 10/day)
- **Current constraint**: 1-2 posts/day (queue cap + session cadence limiting)
- **When to increase**: After Premium activation, consider raising queue threshold to 20-25

**Reply Volume (realistic targets):**
- **Guru claims**: 100+ replies/day (not sustainable without VA/automation)
- **2026 realistic consensus**: 10-30 quality replies/day
- **Autonomous agent target**: 5-10 high-quality replies per session (within turn budget)
- **Critical priority**: Reply to ALL comments on own posts within first 30 min (150x multiplier)

**Evidence:** Session #61 (`agent/memory/research/reading-notes/2026-02-13-engagement-tactics-small-accounts-0-100-followers.md`)

### How to Execute (70/30 Engagement/Content Split)

**Engagement work (70% of session time):**
1. **FIRST PRIORITY**: Check if own posts have comments → reply to ALL within 30 min (150x multiplier)
2. During reading sessions, note recent posts from top voices that you can reply to
3. Use web search to find tweet IDs: `WebSearch: "site:x.com @handle {topic}"`
4. Create reply files using the commenting skill format
5. Target: 5-10 high-quality replies per session (when queue < 15)
6. **Only reply to posts < 6 hours old** (ideal) or < 24 hours max — stale replies get buried (50% visibility loss every 6h)

**Content creation (30% of session time):**
1. When queue < 15: Create 1-2 original posts per session
2. When Premium active: Scale to 3-5 posts/session to match 3-5 posts/day optimal frequency
3. All content posted 100% to Communities (not timeline) until 3K-5K followers

### Content Angle Diversification (Week 3 Learning)
**Max 50% of posts about the autonomous agent experiment.** The other 50% should draw on the author's broader expertise:
- Call center AI / speech analytics (Ender Turing domain)
- Startup building and scaling (15+ years experience)
- Infrastructure architecture journey (network eng → AI)
- Broader AI/ML trends and industry analysis
- Product development insights

Why: Week 3 content became formulaic — nearly every post referenced "PDCA cycles," "X PRs shipped," and linked the repo. The account reads as a single-topic bot, not a multifaceted human building interesting things.

Evidence: Sessions #3-35 all connected back to the autonomous agent angle. Content voice says "human building products with autonomous tools" but execution was "autonomous agent talks about itself."
See `agent/memory/learnings/retro-weekly-2026-02-08.md`

---

## 3-Phase Action Plan: Premium Activation (Session #61)

**When Premium activates, execute this plan immediately:**

### Phase 1: Day 1 Setup (30-45 min one-time effort)
**Priority: P0 (Critical - must complete before scaling traffic)**
1. ✅ Activate X Premium ($8/mo) - unlocks Communities, metrics, algorithmic boost
2. ✅ Join 6 Communities (5 min total):
   - Build in Public (180K members)
   - AI/ML Builders (50-100K)
   - Startup Founders (100K+)
   - Call Center AI (10-20K)
   - Infrastructure→AI (5-10K)
   - Indie Hackers (150K)
3. ✅ Deploy profile optimization (30-45 min):
   - Update bio (Voice AI Authority recommended: 107 chars)
   - Create pinned tweet (5-tweet thread template ready)
   - Optional: Banner design (30% conversion boost)
4. ✅ Start manual Communities posting workflow:
   - Repo owner reviews queue daily
   - Select top 1-2 pieces
   - Post via web UI to 2-3 relevant Communities
   - Check "Also share with followers"

**Deliverable:** Profile optimization action plan in `agent/outputs/profile-optimization-action-plan.md` (Session #58)

### Phase 2: Week 1-2 Execution (Scale + Measure)
**Priority: P1 (Execute after Phase 1 complete)**
1. Increase posting frequency: 3-5 posts/session (vs current 1-2)
2. 100% Communities posting (not timeline) for ALL content
3. Reply to ALL comments on own posts within first 30 min (150x multiplier)
4. Create 5-10 replies/session to larger accounts (70/30 engagement/content split)
5. Monitor engagement velocity (first 30 min = critical algorithm window)
6. Track profile conversion rate (visit-to-follow %)
7. Only reply to posts < 6h old (time decay = 50% loss every 6h)

**Expected Week 1-2 results:** 50-100 new followers (vs 0.75/day baseline)

### Phase 3: Week 3-4 Validation & Automation
**Priority: P2 (Execute after Phase 2 shows traction)**
1. Measure hypothesis validation:
   - Angle diversity impact (call center AI vs agent content)
   - Pure content value vs outcome value engagement
   - Personality/shareability bucket performance
   - Profile conversion rate (target: 15-20%)
2. Graduate validated patterns to skills (update publishing/commenting skills)
3. Consider Publer automation ($10/mo):
   - Trigger: 10x follower growth confirmed in Phase 2
   - Benefit: Automated Communities posting (saves manual daily work)
   - Integration: Add `# community: [ID]` tag to content files
4. Add rich media to 30-50% of posts:
   - Videos: 10x engagement boost
   - Photos: Algorithmic boost vs text-only
   - Current gap: 100% text = missing multiplier
5. Adjust queue threshold to 20-25 (enables 3-5 posts/day sustainable)

**Expected Month 2-3 results:** 300-800 followers
**Expected Month 4-6 results:** 1,500-5,000+ followers (compounding growth phase)

**Evidence:** Session #61 (`agent/memory/research/reading-notes/2026-02-13-engagement-tactics-small-accounts-0-100-followers.md`)

---

## Commenting / Engagement
See `@.claude/skills/commenting/SKILL.md` for reply strategy, file format, and engagement approach.

---

## Gist Fallback
When no platform integration exists:

```bash
gh gist create --public -f "filename.md" content.md
gh gist edit <gist-id> -f "filename.md" updated.md
```

Track gist URLs in state file under "## External Outputs".
