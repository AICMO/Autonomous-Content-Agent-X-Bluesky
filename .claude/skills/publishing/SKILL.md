---
name: publishing
description: Content strategy for external platforms (X, LinkedIn, etc.). Voice, style, and growth strategies.
user-invocable: false
---

# Publishing Content Strategy

> Core principles for creating content that grows audience

## Platform Status

Check current platform status (Premium tier, features, limits) in the integration plan files:
- X: `agent/integrations/x/plan.md`
- Bluesky: `agent/integrations/bluesky/plan.md`

If plan files don't exist, create them from current state.

---

## Expertise Pillars (Content Filter)

Every post MUST connect to at least one pillar. If it doesn't, skip it.

### How Pillars Work

Pillars are the account's content lanes — topics where the owner has real authority. They are **discovered, not hardcoded.**

**Where pillars come from:**
1. **ME.md** — Owner's background, expertise areas, current projects
2. **GOALS.md** — What the account is trying to achieve
3. **This repo's purpose** — What the agent actually does (autonomous content automation)
4. **What's working** — Topics that get engagement (check metrics during retros)

**Pillar lifecycle:**
- Discover pillars at session start by reading ME.md and GOALS.md
- Follow the same pillars for 2-4 weeks (consistency builds audience recognition)
- Review and potentially evolve pillars during weekly retros based on engagement data
- Some pillars are always available (owner's permanent expertise areas from ME.md) but the agent can explore new ones

**Current pillars** are stored in `agent/memory/pillars.md`. If that file doesn't exist, discover pillars from ME.md and GOALS.md and create it.

**AI Industry news** is allowed ONLY as a hook to reach a pillar. The news is never the point. The connection to our expertise is.

**Pillar gate:** Before writing any post, answer: "Which pillar does this connect to, and what's MY angle?" If you can't answer both, skip.

---

## What Actually Works (Evidence-Based)

**Content formats ranked by performance (our data):**
1. **News hooks** — 3-6x average impressions (65, 62, 60, 51 imp vs 10 avg)
2. **Dollar-amount headlines** — ($285B, $2B, $1T) quantified impact stops scroll
3. **Name-drops** — (Karpathy, Altman, Anthropic, OpenAI) moderate boost
4. **Replies to official accounts** — (@OpenAI 24 imp) > individuals (0-6 imp)

**What underperforms:** Generic framework posts without news hook (<10 imp), process posts without news hook, personality without timeliness, stale replies (>6h = 0 imp).

### X Post Length (Premium = up to 25,000 chars)

X Premium unlocks long-form posts. The agent has been writing 270-450 char posts (old free-tier length). This wastes Premium. **Write X posts at full length. Bluesky is a separate platform with separate constraints — never let Bluesky's 290-char limit shrink X posts.**

**Hard minimums for X (characters, not words):**

| Post type | Min chars | Target chars | Notes |
|-----------|-----------|-------------|-------|
| Hot takes, reactions | 150 | 200-350 | Only category allowed to be short |
| News + opinion | 500 | 600-1000 | Hook + context + opinion + so-what. Use the space. |
| BIP / milestone | 400 | 500-800 | Numbers + story + what changed + what's next |
| Promo / OS | 500 | 600-1000 | What it does + proof links + why it matters + repo |
| Predictions | 500 | 600-900 | Stance + evidence + timeline + business impact |
| Threads (4-6 posts) | 1500 total | 2000-3000 | Each post 300-600 chars. 40-60% more reach. **Minimum 2 threads per week.** |

**If a news/opinion/BIP/promo post is under 500 chars, you haven't said enough. Add:** the "so what," a personal angle, a prediction, specific numbers, or a CTA. Don't pad with filler — add substance.

**Every sentence must add value.** Short and empty is worse than long and dense. Cut filler, not substance.

**Premium multipliers:** Communities = 30,000x, reply-to-own <30min = 150x, reply-to-reply = 75x, videos 10+ sec = 10x, threads 4-6 = 40-60% more reach.

---

## Pillar-Filtered Content Strategy

> Every post starts from expertise (pillars 1-4). News hooks are allowed but only as a doorway into a pillar topic. The news is the hook; the pillar expertise is the value.

### Content Formula: Hook + Pillar Expertise + Insight

Every post MUST have:
1. **Hook** — Timely, specific, stops the scroll (news, number, question, or personal story)
2. **Pillar connection** — Which pillar (P1-P4) does this come from? What's MY angle?
3. **Original insight** — What do I know from experience that the reader doesn't? Not just reporting news, but adding expertise the reader can't get elsewhere.

### News Hook Filtering

News hooks belong in `agent/memory/research/`, NOT in this skill. This skill defines HOW to filter, not WHAT to post about.

**When scanning news, for each item ask:**
1. Which pillar does this connect to?
2. What's MY angle — what do I know from experience that adds value beyond reporting?
3. If you can't answer both, skip it.

**Good example:** "Gartner says 40% of agent projects will be abandoned by 2027" → Pillar: Autonomous Agents → Our angle: "We've run 700+ PRs autonomously. Here's what governance actually looks like in production."

**Bad example:** "NVIDIA invests $2B in Nebius" → No pillar connection → Skip. (Unless you can tie it to inference costs affecting agent economics — then it's a hook, not the topic.)

**Store pillar-filtered news hooks in:** `agent/memory/research/ai-news-YYYY-MM-DD.md` with a `Pillar` and `Our Angle` column.

### Content Priorities (Ranked)

1. **Pillar expertise + timely hook** (40%) — News/trend that connects to a pillar, with original insight from experience
2. **Building in public / lessons learned** (30%) — Agent milestones, founder stories, what's working/failing
3. **Industry analysis through pillar lens** (20%) — AI economics, startup patterns, market shifts that affect our domain
4. **Promotional** (10%) — Repo, live outputs, Ender Turing — only when the post is genuinely about what we build

### Predictions & Opinions (40-50% of content)

Don't just report news. Predict where it's going and what it means for business.

Every prediction: bold stance + business impact + timeline. No hedging.

**Formulas:**
- "[News] means [prediction]. Here's why: [reasoning]. Timeline: [when]."
- "Everyone's talking about [trend]. Nobody's asking: [deeper question]. My take: [opinion]."
- "Unpopular opinion: [contrarian take]. The data says [evidence]. Businesses should [action]."

**Ground predictions in pillar expertise.** Read ME.md for the owner's background. Every prediction should come from a place of authority, not generic speculation.

### Repo Linking (Organic Only)

**Only link the repo when the post is genuinely about building or running agents.** The repo link is proof, not decoration. If the post is about call center AI trends or startup economics, the repo has no business being there.

**When to link:** Posts about autonomous agent architecture, BIP milestones, automation lessons, agentic workflows. The repo IS the topic.
**When NOT to link:** Posts about industry news, funding rounds, or expertise topics that don't involve the repo. Forcing a link onto unrelated content looks synthetic.

**When you do link, use the full URL** (not "this repo"). Find the current repo URL from ME.md or `gh repo view --json url`.

### What NOT to Post

- **Off-pillar news** — Funding rounds, chip specs, acquisitions, or investment analysis that doesn't connect to a pillar. If the post could be written by any generic AI news account, it's not ours.
- **Forced repo links** — Never graft the repo URL onto an unrelated topic. If the post isn't about building/running agents, the repo link doesn't belong.
- **Don't promote X on X** — Never post "follow me on X" or link to the X profile in X posts. That's circular. Promote the blog, Substack, Telegram, repos, or live outputs instead.
- **Politics (HARD BAN)**: Never post about politicians by name (presidents, senators, etc.), legislation, executive orders, Senate/Congress votes, elections, or political parties — even when the topic is AI or tech. The test: if the post mentions a politician, a vote, or a law by name, don't post it.
- Benchmark comparisons without "so what"
- Authority/framework posts without links or CTAs
- Anything that makes the reader think but not ACT

### Research Cadence

**Daily (at session start):** Quick scan for pillar-relevant news. Filter through pillars before saving. Save to `agent/memory/research/` with pillar tags. Skip anything that doesn't connect to a pillar.

---

**Milestone content (technical CEO pattern):**
- Every PR milestone is a post (Session #150, #200, Premium activation, follower milestones)
- Radical transparency on numbers builds credibility
- **Target**: 15-20% of content should be BIP milestone posts

---

## Publishing Flow

Content is auto-posted by workflow from `agent/outputs/{platform}/`, then moved to `posted/`.

### Platform-Independent Publishing

**X and Bluesky are separate platforms. Write for each independently. Never let one platform's constraints affect the other.**

#### X Posts
1. Write the X version at full Premium length → `agent/outputs/x/`
2. Follow the X length minimums above (most posts 500-1000 chars)
3. X has no meaningful character limit with Premium (25,000 chars)

#### Bluesky Posts
1. Write a separate Bluesky version → `agent/outputs/bluesky/`
2. Bluesky hard limit: 290 chars. Posts >300 chars are auto-skipped by pipeline.
3. Same file name as X version, but the content should be independently written for Bluesky's format
4. Bluesky posts are compressed summaries, NOT the template for X posts
5. If a topic can't be meaningfully compressed to 290 chars, it's OK to skip the Bluesky version

**The old pattern was:** write short → copy to both. **The new pattern is:** write X at full length → write Bluesky separately as a short summary.

### File Naming
`{type}-{YYYYMMDD}-{NNN}.txt` — Threads: `thread-20260215-001.txt` (use `---` separator)

### Queue Management (Hard Rules)
1. **If any platform queue > 15: CREATE ZERO CONTENT** → research, cleanup, or skill work instead
2. **Create max 2 content pieces per session** (when all queues <15). X post is required. Bluesky version is optional (write separately if topic compresses well).
3. **Max 5 pending replies per platform**
4. **Max 20 staged pairs in `agent/memory/plans/`** — when >20, STOP staging. Do cleanup, engagement, or skip PR.
   - Evidence: Week 8 accumulated 91 staged pairs (7.5 days backlog), caused 1.1MB memory bloat and 13 wasted sessions.
   - At 12 X posts/day drain rate, 20 pairs = ~1.7 days buffer. More than enough.

**Queue check (MANDATORY at session start):**
```bash
find agent/outputs/x -maxdepth 1 -name "*.txt" -type f | wc -l
find agent/outputs/bluesky -maxdepth 1 -name "*.txt" -type f | wc -l
```
Never trust state file numbers without verification.

**Drain rates:** Check platform plan files (`agent/integrations/*/plan.md`) for current posting limits and drain rates. Bluesky is typically the bottleneck — plan accordingly when queue is full.

### Session Allocation
**< 100 followers:** 70% engagement, 30% content creation. Priority: Communities > reply to own <30min > replies to others > timeline posts.

**When queue >15 AND staged pairs <20:** 0% content, 40% cleanup/skills, 30% research (max 1 file/day), 30% staging from existing research.

**When queue >15 AND staged pairs >=20:** 0% content, 0% research, 0% staging. 50% cleanup/memory management, 50% skill work or engagement prep. **Skip PR creation entirely if nothing meaningful to commit.** DO NOT create more research or staged files.
- Evidence (Week 8): 13 consecutive sessions all doing research+staging while queue-blocked. Result: 1.1MB memory, zero value.
- Evidence (Week 9): 70+ of 105 sessions were "queue blocked, state update only" PRs. Each PR triggers CI, eats minutes, produces zero value. A PR that only updates the state file timestamp is waste.

**HARD RULE: No empty PRs.** If the session has no new content files, no research files, no skill updates, and no meaningful state changes — do NOT create a PR. "State update only" PRs are banned. The state file will be updated next session when there's actual work to commit.

---

## Core Strategy

### Value Rule
Pick one per post: **Content value** (post teaches/provokes) OR **Outcome value** (link gives tool/resource). Never both. Target ~20% link posts.

### 3-Bucket Mix
| Bucket | Target % |
|--------|----------|
| **Authority** (frameworks, insights) | 40% |
| **Personality** (stories, opinions) | 30% |
| **Shareability** (hot takes, relatable) | 30% |

### Content Diversification
- **Spread across pillars** — don't let any single pillar dominate more than 50% of output. Check last 5 posts for balance.
- **25%+ BIP content** (progress, learnings, behind-scenes, failures)
- **15-20% question posts** for engagement
- **~10-15% promotional** — CTAs that drive stars, subscriptions, leads (see below)

### Promotion & CTAs (~1 in 7 posts)

**Goal of every CTA:** Drive a measurable action — GitHub stars, blog/Substack subscribers, Telegram joins, Ender Turing leads. Not vanity ("follow me"), but funneling attention into the owner's properties.

**What to promote** (discover from ME.md, don't hardcode):
- Owner's repos and orgs (use discovery skill's OS scan)
- Live agent outputs: blog, Substack, Telegram channel
- Owner's company (Ender Turing) when post topic aligns with call center AI
- Owner's profiles (LinkedIn, GitHub) as secondary CTAs

**Best promo angles (ranked):**
1. **Specific live outcome** — Link a real article/post produced by the agent this week. "This was written by an AI agent. No human." + direct link. Specific > generic.
2. **Live outputs** — "This AI runs daily. See the results: [link]." Proof > promises.
3. **Trend overlap** — Trending topic aligns with a repo or outcome? Post about the trend, link as "we built this."
4. **Milestone** — Star threshold, subscriber count, new release.

**Rules:**
- CTA must match the post topic. Agent post → repo link. Voice AI post → Ender Turing. Don't cross-wire.
- Only promo what you've scanned this session (stale info = bad post)
- Frame as value to reader ("you can use this"), not vanity
- Don't repeat same promo angle twice in a row

---

## Tactical Execution

### Hook Engineering

First line determines if anyone reads. Under 110 chars optimal.

| Type | Formula |
|------|---------|
| Bold statement | "Nobody talks about this, but [insight]" |
| Contrarian | "[Common belief] is wrong. Here's what works:" |
| Story | "[Timeframe] ago I was [struggle]. Today [achievement]..." |
| Numerical | "I [achieved X] in [timeframe] doing this" |
| Dollar lead | "$[amount] [action]. [Impact]." |
| Percentage shock | "[X%] of [group] [state]. [Implication]." |
| Product milestone | "[Product]: [new capability]. [What's now possible]." |

**First-line test:** Does the first line work as a standalone tweet? If no, rewrite. Value in first 5 words. No throat-clearing.

### Content Voice

Frame as **human building products with autonomous tools**.

**Use:** creating, building, shipping, launching. **Avoid:** testing, experimenting, trying. **Say:** product, tool, solution (never "content").

### CTA Discipline
Every post should drive attention toward owner's properties (repos, blog, Substack, Telegram, company). Match CTA to post topic — agent posts → repo, voice AI → Ender Turing, general → blog/Substack. Discover links from ME.md, don't hardcode.

### Educational Simplification
For complex concepts: "Here's [concept]. In plain English: [1-2 sentences]. Why it matters: [implication]."

---

## Content Templates (Validated from 18 Builders)

| # | Name | Template | Bucket |
|---|------|----------|--------|
| 1 | TIL | "TIL: [discovery]. This matters because [implication]." | Personality/BIP |
| 2 | Metrics BIP | "[Session #X], [PR #N]: [metric]. [Interpretation]." | BIP |
| 3 | Vocab Definition | "[Term] = [definition]. Here's why this matters..." | Authority |
| 4 | Expert Vulnerability | "I've [impressive thing] for [duration]. I still [struggle]..." | Personality |
| 5 | Milestone | "[Milestone]. [Casual observation]." | BIP |
| 6 | Enterprise Adoption | "[Product] powers [company]. What it means for [industry]..." | Authority |
| 7 | Founder Journey | "Started at [age]. Built [project]. Now [outcome]. [Lesson]." | Personality |
| 8 | Philosophy Shift | "I was skeptical in [year]. Here's why I changed..." | Shareability |
| 9 | Origin Story | "Built [product] because I needed [solution]. Now [outcome]." | BIP |
| 10 | Technical + Human | "[Technical achievement] means [human impact]." | Authority |
| 11 | Time-Boxed | "I spend [X min] creating daily. System: [workflow]. Result: [outcome]." | Shareability |
| 12 | Idea List | "[Number] ideas for [audience]: 1. [idea] 2. [idea]..." | Authority |
| 13 | How-To | "How to [outcome]: - [principle 1] - [principle 2]..." | Authority |
| 14 | Platform Strategy | "I stopped [old]. Now I [new]. Result: [outcome]." | BIP |
| 15 | Prediction | "[Trend]. My prediction: [take]. Timeline: [when]. Why: [reasoning]." | Authority |
| 16 | Business Use Case | "[Tech] + [industry] = [use case]. Revenue impact: [estimate]." | Authority |

Use variety. Don't repeat same template 3+ times in a row. Target 25%+ BIP (templates 2, 5, 9, 14).

---

## Anti-AI Writing Rules (MANDATORY)

Every piece of content MUST pass as human-written. These rules override all templates.

### BANNED Patterns
1. **Em dash abuse** — use periods, commas, or semicolons instead
2. **"Not just X, it's Y"** — #1 AI tell, never use
3. **Perfect rule-of-three lists** with parallel structure — break the pattern
4. **Banned words:** "Delve," "elevate," "innovative," "tapestry," "realm," "landscape," "leverage," "robust," "holistic," "comprehensive," "cutting-edge," "game-changer," "paradigm," "furthermore," "moreover," "additionally," "let's dive in," "buckle up"
5. **Exaggerated praise** — say "I liked [specific thing]" not "genuinely captivating"
6. **Constant clarification** — never "to clarify," "in other words," "to put it simply"
7. **Forced analogies** — if it doesn't come naturally, skip it
8. **LinkedIn format** — hook + ethos + bullets + result + conclusion = banned structure
9. **Uniform sentence length** — vary dramatically. Short. Then longer. Then short.
10. **Summarizing at the end** — just stop when you're done

### Human Patterns (use these)
- **Personal anecdotes** with specific details (numbers, companies, timelines from author's life)
- **Brief tangents** — side thoughts that aren't strictly necessary
- **Casual phrasing** — contractions, fragments, idioms ("shipped it" not "deployed the solution")
- **Real specifics** — name actual tools, numbers, companies, people
- **Clear opinions** — no hedging ("This kills per-seat SaaS" not "time will tell")
- **Sentence fragments** — "Not kidding." "Zero." "Wild."
- **Start with "And" or "But"** — AI avoids this, humans don't

### Vibe Check (Final Gate)
Does this sound like a real person typed it? Would I say this to a colleague? Does every sentence add new info? If no → rewrite from scratch.

---

## Content Creation Checklist

1. **Queue check**: Queue > 15? STOP.
2. **Pillar check**: Which pillar does this connect to? What's MY angle? If neither, skip.
3. **Repo link check**: Is this post genuinely about agents/automation? If not, no repo link.
4. **X length check**: News/opinion/BIP/promo/prediction post under 500 chars? Add more substance.
5. **Thread check**: Have you created 2+ threads this week? If not, make one now.
6. **Quality gate**: Would a stranger follow based on this post alone?
7. **Anti-AI check**: Vibe check passed? No banned patterns?
8. **Value type**: Content value OR outcome value, never both.
9. **Pillar diversity**: No single pillar > 50% of last 5 posts.
10. **BIP balance**: At least 25% of recent output.
11. **Category**: Authority / Personality / Shareability balanced.
12. **Hook**: First line stops the scroll.
13. **Bluesky version**: Written separately, under 290 chars. OK to skip if topic doesn't compress.
14. **Politics check**: No politicians, votes, or laws by name.

---

## Algorithm Awareness

**What X rewards:** Premium = 10x reach, Communities = 30,000x, reply-to-own <30min = 150x, reply-to-reply = 75x, videos 10+ sec = 10x, early engagement critical, threads 4-6 = 40-60% more.

**What hurts:** External links (use sparingly), heavy hashtags, posting and leaving, stale replies (50% visibility loss every 6h), low-effort spam replies.

**TweepCred:** Free accounts start at -128. Below 0.65 = critical suppression. Premium = +100 instant boost.

---

## Reference Links

- Commenting/engagement: `.claude/skills/commenting/SKILL.md`
- Author info: `ME.md`
- Platform plans: `agent/integrations/x/plan.md`, `agent/integrations/bluesky/plan.md`
- Research archive: `agent/memory/research/`
- Content pillars: `agent/memory/pillars.md`