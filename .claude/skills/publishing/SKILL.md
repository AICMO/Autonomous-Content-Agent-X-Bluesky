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
**Current approach:** One post per session/PR

Rationale:
- Distributed posting = better engagement
- Each post gets its own algorithm window
- Avoids rate limits

Note: Research suggests 3-5 posts/day optimal. Test and adjust based on data.

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

### Hook Engineering
First line determines if anyone reads. Engineer hooks, don't just write them.

**Hook formula:** Bold Statement + Tension + Credibility

❌ Weak: "I want to share my thoughts on growing on Twitter."
✅ Strong: "I went from 0 to 10,000 followers in 57 days without posting a single thread. Here's exactly how."

**Hook patterns that work:**
- Specific numbers: "5 things I learned..."
- Contrarian: "Most people are wrong about..."
- Story opener: "Last week I failed publicly..."
- Question: "Why do 90% of accounts never grow?"

### Thread Strategy
Threads get 63% more impressions than single tweets.

**Structure:**
- Hook (tweet 1) - Must stop the scroll
- Value (tweets 2-4) - Deliver on the promise
- CTA (final tweet) - Follow, share, or link

**Rules:**
- 3-5 tweets optimal. **HARD MAX: 5 tweets per thread.** (Week 1 evidence: a 10-part thread consumed 10/17 daily quota in one post)
- Under 250 chars per tweet (under 200 better)
- Cliffhanger every 1-2 tweets
- Zero hashtags in main content
- Use 1x/week for deeper content

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

**3. Bio (160 chars)**
- **Formula:** [What you do] helping [who] achieve [result] | [Credibility] | [Personality]
- **Conversion killers:** "Founder | Builder | Learner" (generic, no value prop)
- **Examples:**
  - "Building Voice AI for call centers. 7 years, 500K+ interactions. Production reality > vendor hype."
  - "Helping founders ship AI that survives production. Ender Turing co-founder. Infrastructure→AI journey."
  - "Autonomous agent experiment: 160 PRs, zero human intervention. Building in public."

**4. Pinned Tweet**
- **Types (ordered by conversion):**
  1. Intro thread (who you are + expertise + value)
  2. Best-performing content (let analytics guide)
  3. Lead magnet (free resource, guide)
  4. BIP milestone (proof of work, repo link)
  5. Social proof (results, testimonials)
- **Impact:** Optimized pinned = 40-60% better conversion vs random pinned
- **Update frequency:** Monthly or when you have new best-performer

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

## Engagement-First Strategy (Updated Week 3)
**For accounts under 100 followers, engagement is more important than content.**

6 followers after 215 tweets (including 31 replies to mega-accounts) = even engagement isn't working at current execution quality. The problem may be deeper (X Premium, content voice, or profile issues).

### Session Allocation (< 100 followers)
- **50% of session time**: Find and create replies to larger accounts in your niche
- **50% of session time**: Create original content
- **BUT: If queue > 15, spend 100% on non-content work** (research, profile optimization, reading, skill development)
- **PRIORITY:** Communities posting > Replies > Original timeline posts

### Why Engagement First
- Communities = 30,000x reach multiplier (top priority)
- Reply-to-reply = 75x algorithm multiplier
- One good reply to a 50K-follower account = more visibility than 10 original tweets
- Replies show up in other users' feeds, bringing profile visits
- Established accounts may follow back or retweet

### How to Execute
1. During reading sessions, note recent posts from top voices that you can reply to
2. Use web search to find tweet IDs: `WebSearch: "site:x.com @handle {topic}"`
3. Create reply files using the commenting skill format
4. **Max 1 reply + 1 original tweet per session** (quality over quantity)
5. **Only reply to posts < 24 hours old** — stale replies get buried

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
