---
name: publishing
description: Content strategy for external platforms (X, LinkedIn, etc.). Voice, style, and growth strategies.
user-invocable: false
---

# Publishing Content Strategy

> Core principles for creating content that grows audience

## Premium Status: ACTIVE ($20/mo, activated 2026-03-01)

X Premium is live. All Premium features unlocked:
- Communities access (30,000x reach multiplier)
- +100 TweepCred boost (escaped suppression)
- 10x algorithmic reach, link posting without suppression, reply visibility boost

**Current priorities (Premium era):**
1. **Create content aggressively** — X queue is empty, fill it
2. Post to Communities (Build in Public, AI/ML Builders, etc.)
3. Reply to own comments within 30 min (150x multiplier)
4. Continue cross-posting to Bluesky

---

## What Actually Works (Evidence-Based)

**Content formats ranked by performance (our data):**
1. **News hooks** — 3-6x average impressions (65, 62, 60, 51 imp vs 10 avg)
2. **Dollar-amount headlines** — ($285B, $2B, $1T) quantified impact stops scroll
3. **Name-drops** — (Karpathy, Altman, Anthropic, OpenAI) moderate boost
4. **Short posts** — outperform long framework posts by 3-6x
5. **Replies to official accounts** — (@OpenAI 24 imp) > individuals (0-6 imp)

**What underperforms:** Long authority/framework posts (<10 imp), process posts without news hook, personality without timeliness, stale replies (>6h = 0 imp).

**Premium multipliers:** Communities = 30,000x, reply-to-own <30min = 150x, reply-to-reply = 75x, videos 10+ sec = 10x, threads 4-6 = 40-60% more reach.

---

## Hype-Driven Content Strategy (Primary Direction)

> Owner directive: Focus on what's hottest in AI right now. Connect to how people are making money fast. Clickbait + actionable links.

### Content Formula: Hype + Money + Action

Every post MUST have all three:
1. **Hype hook** — What's viral/trending RIGHT NOW (this week, not last month)
2. **Money angle** — Dollar amounts, specific revenue numbers
3. **Action links** — Real repos, tools, tutorials the reader can use TODAY

### What's Hot Right Now (March 2026 — update weekly)

| Trend | Money Angle | Key Links |
|-------|-------------|-----------|
| **OpenAI $110B raise** ($840B valuation) | Amazon $50B, Nvidia $30B, SoftBank $30B | openai.com |
| **Anthropic-Pentagon standoff** | $200M contract refused, Claude #1 App Store | anthropic.com |
| **ChatGPT Agent Mode** | AI books, plans, executes autonomously | openai.com/index/introducing-chatgpt-agent |
| **Vibe Coding** (92% dev adoption) | Claude Code = 4% of GitHub commits | cursor.com, claude.ai |
| **$195B invested in AI Feb 2026** | Record venture month | bloomberg.com |

### Content Priorities (Ranked)

1. **Trending tools + repos with money proof** (50%+)
2. **"How people are making money" breakdowns** (30%)
3. **Personal experience / BIP connecting to trends** (20%)

### Predictions & Opinions (40-50% of content)

Don't just report news. Predict where it's going and what it means for business.

Every prediction: bold stance + business impact + timeline. No hedging.

**Formulas:**
- "[News] means [prediction]. Here's why: [reasoning]. Timeline: [when]."
- "Everyone's talking about [trend]. Nobody's asking: [deeper question]. My take: [opinion]."
- "Unpopular opinion: [contrarian take]. The data says [evidence]. Businesses should [action]."

**Use author's expertise:** Voice AI/call centers (7 years), autonomous agents (this repo), infra→AI migration, startup economics (15+ years).

### What NOT to Post

- **Politics (HARD BAN)**: Never post about politicians by name (presidents, senators, etc.), legislation, executive orders, Senate/Congress votes, elections, or political parties — even when the topic is AI or tech. Example of banned: "Senate voted to strip AI regulation" or "President on AI standards." Example of allowed: "Anthropic refused a Pentagon contract" (company decision, not political commentary). The test: if the post mentions a politician, a vote, or a law by name, don't post it.
- Enterprise analysis without money angle
- Benchmark comparisons without "so what"
- Authority/framework posts without links or CTAs
- Anything that makes the reader think but not ACT

### Research Cadence

**Daily (at session start):** Quick scan for what's viral — trending GitHub repos, X trending, HackerNews front page, ProductHunt, IndieHackers.

---

**Milestone content (technical CEO pattern):**
- Every PR milestone is a post (Session #150, #200, Premium activation, follower milestones)
- Radical transparency on numbers builds credibility
- **Target**: 15-20% of content should be BIP milestone posts

---

## Publishing Flow

Content is auto-posted by workflow from `agent/outputs/{platform}/`, then moved to `posted/`.

### Cross-Posting (X + Bluesky)

1. Write the X version first → `agent/outputs/x/`
2. Write a Bluesky version (max 290 chars hard limit) → `agent/outputs/bluesky/`
3. Use the same file name in both directories

**Bluesky rules:** If X post <290 chars → copy verbatim. If over → rewrite shorter. Posts >300 chars are auto-skipped by pipeline.

### File Naming
`{type}-{YYYYMMDD}-{NNN}.txt` — Threads: `thread-20260215-001.txt` (use `---` separator)

### Queue Management (Hard Rules)
1. **If any platform queue > 15: CREATE ZERO CONTENT** → research, cleanup, or skill work instead
2. **Create max 2 content pieces per session** (when all queues <15). Each piece = X + Bluesky files.
3. **Max 5 pending replies per platform**

**Queue check (MANDATORY at session start):**
```bash
find agent/outputs/x -maxdepth 1 -name "*.txt" -type f | wc -l
find agent/outputs/bluesky -maxdepth 1 -name "*.txt" -type f | wc -l
```
Never trust state file numbers without verification.

### Session Allocation
**< 100 followers:** 70% engagement, 30% content creation. Priority: Communities > reply to own <30min > replies to others > timeline posts.

**When queue >15:** 0% content, 40% cleanup/skills, 30% research (max 1/day), 30% other. Skip PR creation if nothing to commit.

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
- **Max 50% about autonomous agent.** Also draw on: call center AI (7 years), startup building (15+ years), infra→AI journey, broader AI trends.
- **25%+ BIP content** (progress, learnings, behind-scenes, failures)
- **15-20% question posts** for engagement
- **~20% promotional** (soft — repo link, profile, Ender Turing when relevant)

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
Every post >50 impressions should include soft CTA. Templates: "Building this in public → [repo link]", "More on my LinkedIn → [profile]". CTA from Day 1.

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
2. **Quality gate**: Would a stranger follow based on this post alone?
3. **Anti-AI check**: Vibe check passed? No banned patterns?
4. **Value type**: Content value OR outcome value, never both.
5. **Link allocation**: Only ~20% include links.
6. **Angle diversity**: Max 50% about agent. Check last 2 posts.
7. **BIP balance**: At least 25% of recent output.
8. **Category**: Authority / Personality / Shareability balanced.
9. **Hook**: First line stops the scroll.
10. **Bluesky version**: Under 290 chars, same filename in `agent/outputs/bluesky/`.
11. **Politics check**: No politicians, votes, or laws by name.

---

## Algorithm Awareness

**What X rewards:** Premium = 10x reach, Communities = 30,000x, reply-to-own <30min = 150x, reply-to-reply = 75x, videos 10+ sec = 10x, early engagement critical, threads 4-6 = 40-60% more.

**What hurts:** External links (use sparingly), heavy hashtags, posting and leaving, stale replies (50% visibility loss every 6h), low-effort spam replies.

**TweepCred:** Free accounts start at -128. Below 0.65 = critical suppression. Premium = +100 instant boost.

---

## Premium Growth Phase (Week 1-2)

1. Join 6 Communities (Build in Public, AI/ML Builders, Startup Founders, Call Center AI, Infra→AI, Indie Hackers)
2. Post 100% content to Communities
3. Reply to ALL own comments within 30 min
4. Create 5-10 replies/session to larger accounts
5. Track follower growth (target: 50-100 in 2 weeks vs 0.75/day baseline)

**Full details:** `agent/outputs/premium-activation-playbook.md`

---

## Reference Links

- Premium activation: `agent/outputs/premium-activation-playbook.md`
- Commenting/engagement: `.claude/skills/commenting/SKILL.md`
- Author info: `ME.md`
- Research archive: `agent/memory/research/`