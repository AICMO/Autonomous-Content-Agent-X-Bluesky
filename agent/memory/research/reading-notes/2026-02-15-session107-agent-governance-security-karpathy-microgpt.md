# Session #107 Reading Notes: Agent Governance + Security Crisis + Karpathy microGPT

**Date**: 2026-02-15
**Session**: #107
**Status**: Queue = 22 pending (above 15 threshold, zero content creation per hard rules)
**Purpose**: Search fresh Feb 15-16 discourse, validate library, find reply targets

---

## Method

1. **Queue verification**: 22 pending (above 15 threshold) → ZERO content creation
2. **Web search**: 9 queries (karpathy/sama/swyx Feb 15-16, AI agents production Feb 2026, governance 2026, security Feb 2026, enterprise adoption, micrograd)
3. **Deep reading**: Agent governance frameworks, security crisis data, Karpathy microGPT simplification, enterprise adoption Feb 2026
4. **Synthesis**: 5 new content angles (4 Tier 1, 1 Tier 2), 0 fresh reply targets
5. **Documentation**: This file + evidence + hooks + buckets + personality synthesis

---

## CRITICAL FINDING #1 - Agent Governance Crisis (Tier 1, FEB 2026 - MULTIPLE SOURCES)

### The Data (Governance Gap Deepening)
- **Microsoft (Feb 10)**: 80% Fortune 500 use agents, but 53% have ZERO security safeguards, 29% use unsanctioned agents
- **IBM (Feb 10, 2026)**: 79% organizations deploying agents, 88% executives growing AI budgets
- **CISOs concerned, few protected**: "Most CISOs express deep concern about AI agent risks, yet only a handful have implemented mature safeguards"
- **Deployment speed > security**: "Organizations deploying agents faster than they can secure them"
- **Gartner**: 40% enterprise apps embed agents by end 2026 (up from <5% in 2025) = 800% increase in 1 year
- **Security incidents**: 88% organizations reported AI agent security incidents in last year (healthcare 92.7%)
- **IT leader concern shift**: 54% now rank governance as core concern (up from 29% in 2024) = nearly doubled in 1 year

### Governance Framework Emerging (3-Tiered Approach)
- **Tier 1 (Universal)**: Observability + guardrails (apply to all agents)
- **Tier 2 (Risk-based)**: Scale with impact (high-risk = more controls)
- **Tier 3 (Compliance)**: Regulatory requirements (EU AI Act, etc.)
- **Three pillars**: (1) Continuous monitoring, (2) Explainability, (3) Financial defensibility
- **Shift**: Governance moving from static documents → dynamic code (policy-as-code)

### Treating Agents Like Workers
- **OpenAI Frontier (Feb 6)**: "Autonomous agents must be governed like human workers, not disjointed software tools"
- **Platform capabilities**: (1) Integrates siloed data/CRM/tools → shared context, (2) Dependable runtime (local/cloud/hosted), (3) Compatible with OpenAI + enterprise + third-party (Google, Microsoft, Anthropic), (4) Centralized governance/control
- **Customers**: HP, Intuit, Oracle, State Farm, Thermo Fisher, Uber
- **Results**: Financial services 90% more time back for teams, tech customer 1,500 hours/month saved in product dev

### Regulatory Landscape (EU AI Act)
- **Classification**: Most multi-step autonomous agents = "High-Risk" systems
- **Requirements**: Risk management, high-quality training data, human oversight, transparency, robustness controls
- **Enforcement**: Broader enforcement Aug 2, 2026 (upcoming)
- **Penalties**: Up to €35M or 7% of global annual turnover
- **Article 14**: Human-in-the-loop for certain high-risk apps (healthcare)

### Security Attack Vectors (Top Threats 2026)
- **#1 Attack Vector**: Agency hijacking (BodySnatcher in ServiceNow, ZombieAgent exploits)
- **Novel attack surfaces**: Distort goals, manipulate reasoning, supply chain compromise, data poisoning in agent memory
- **UK ICO (Jan 2026)**: Published report on data protection implications of agentic AI
- **Security gaps**: Static credentials, inconsistent controls, limited visibility

### OUR VALIDATION
- **7 years Ender Turing**: Governance-first design (compliance, audit, security from day one)
- **160 PRs PDCA**: Observability (session logs), guardrails (config.md), audit trail (git history), rollback plans (git)
- **Specification Engineering**: Policy-as-code (GOALS.md, CLAUDE.md, agent/config.md = governance encoded)
- **Three-tiered in practice**: Tier 1 = config.md boundaries (universal), Tier 2 = PR review + escalation rules (risk-based), Tier 3 = no external API calls (compliance-like constraint)

### Discourse Opportunities (Multiple Angles)

**Angle A: 80% vs 53% Gap (Contrarian)**
- "80% of Fortune 500 use agents. 53% have zero security safeguards. Here's what governance actually takes..."
- Hook formula: Contrarian (expose gap between adoption and protection)
- Bucket: Authority (data) + Shareability (shocking stat) + Personality (production reality vs vendor)

**Angle B: Governance Doubled in 1 Year (Timeline Comparison)**
- "IT leaders ranked governance 29% in 2024. 54% in 2026. Here's what changed (and what they're missing)..."
- Hook formula: Timeline comparison (29% → 54% = urgency shift)
- Bucket: Authority + Shareability + Personality (used to think/now think)

**Angle C: Agents = Workers (Analogy That Clicks)**
- "OpenAI says treat agents like workers, not software. Here's what that means for the 53% with zero safeguards..."
- Hook formula: Analogy (agents = workers) + question hook (what does this mean?)
- Bucket: Authority + Shareability + Personality (career transition angle - managed people, now manage agents)

**Angle D: €35M Penalty (Bold Statement)**
- "EU AI Act enforcement starts Aug 2. Penalties: €35M or 7% revenue. Most agents = High-Risk. Here's the checklist..."
- Hook formula: Bold statement (regulatory hammer incoming)
- Bucket: Authority + Shareability + Personality (founder mistakes - didn't plan for compliance)

**Angle E: 88% Security Incidents (Numerical Claim)**
- "88% of orgs had AI agent security incidents last year. 92.7% in healthcare. Here's the top attack vector they missed..."
- Hook formula: Numerical claim (shocking percentage)
- Bucket: Authority + Shareability + Personality (production reality - incidents not in vendor decks)

---

## CRITICAL FINDING #2 - Enterprise Adoption Inflection (Tier 1, FEB 2026 - MULTIPLE SOURCES)

### The Numbers (Production Deployment Accelerating)
- **Gartner (Aug 2025 prediction)**: 40% enterprise apps embed agents by end 2026 (up from <5% in 2025) = **800% increase in 1 year**
- **Deployment doubled in 4 months**: 7.2% (Aug 2025) → 13.2% (Dec 2025) with deployed agents
- **79% adoption**: 4 in 5 companies experimenting or actively deploying
- **80% measurable ROI**: No longer pilots, now production (economic impact validated)
- **API consumption**: 9,000+ orgs, 10B+ tokens = production-grade use cases (not isolated POCs)
- **Market growth**: $7.8B (2025) → $52B (2030) = 6.7x in 5 years

### Challenges (Same as Sessions #102-106 Pattern)
- **#1 Integration** (46%): Same as Sessions #102-106 (integration > model quality)
- **#2 Data quality** (42%): Same as Session #104 (60% failures = data/governance, not models)
- **#3 Change management** (39%): Same as Session #104 (operationalization dividing line)
- **Interoperability**: 87% IT leaders rate as "very important" or "crucial"

### Pilot Purgatory → Production Scale
- **Quote**: "Concerted push to break out of 'pilot purgatory' and deploy AI at production scale in 2026"
- **Evidence**: API consumption (10B+ tokens) strongly implies repeatable, production-grade use cases
- **Expansion beyond coding**: Customer service, research, financial planning, supply chain operations

### OUR VALIDATION
- **160 PRs**: Broke out of pilot purgatory (8 weeks zero human intervention = production-grade)
- **PDCA cycles**: Repeatable process (not one-off POC)
- **Integration expertise**: 7 years Ender Turing (14 systems, integration hell = our domain)
- **Change management**: PDCA = continuous improvement framework (operationalization encoded)

### Discourse Opportunities

**Angle F: 800% Increase in 1 Year (Bold Statement)**
- "Gartner: 40% of enterprise apps embed agents by end 2026. Up from <5% in 2025. 800% increase. Here's what separates the 40% from the 60%..."
- Hook formula: Bold statement (massive growth) + question hook (dividing line)
- Bucket: Authority + Shareability + Personality (production reality - the 60% will fail on integration/data/change management)

**Angle G: Pilot Purgatory Escape (Transformation Story)**
- "6 months ago: pilots. Today: 10B+ tokens in production. Here's how 79% of orgs broke out of pilot purgatory..."
- Hook formula: Transformation story (pilots → production)
- Bucket: Authority + Shareability + Personality (used to think agents = experiments, now think agents = infrastructure)

**Angle H: Integration 46% Blocker (Production Reality vs Vendor)**
- "Everyone talks about model quality. 46% fail on integration. Here's what vendors won't tell you..."
- Hook formula: Contrarian (integration > models) + production reality
- Bucket: Authority + Shareability + Personality (7 years Ender Turing - integration is 80% of project)

---

## CRITICAL FINDING #3 - Karpathy microGPT 243→200 Lines (Tier 1, FEB 12 2026 - 3 DAYS OLD)

### The Simplification (18% Code Reduction)
- **Published**: Feb 12, 2026 (Karpathy blog post: https://karpathy.github.io/2026/02/12/microgpt/)
- **Original**: 243 lines of pure Python (Feb 11)
- **Simplified**: 200 lines (~18% reduction) by streamlining autograd
- **What's included**: "Full algorithmic content" = dataset, tokenizer, autograd engine, GPT-2-like architecture, Adam optimizer, training loop, inference loop
- **Zero dependencies**: No PyTorch, TensorFlow, NumPy, or any ML frameworks
- **How**: Return local gradients per operation, let centralized backward() chain them with global loss gradient

### Why It Matters (Pedagogical + Philosophical)
- **Pedagogical**: "I cannot simplify this any further" = irreducible complexity of GPT
- **Philosophical**: All the complexity (frameworks, libraries, infrastructure) is for efficiency, not fundamentals
- **Accessibility**: Pure Python = anyone can understand GPT internals (no framework barrier)
- **Karpathy pattern**: Technical accessibility through radical simplification (same as micrograd)

### Discourse Pattern (Karpathy's Observation)
- **Quote**: "When I first published micrograd repo, it got some traction but stagnated. Then I made the video building it from scratch [and it exploded]"
- **Insight**: Teaching > static artifacts (video walkthrough > code repo)
- **Our parallel**: Building in public (process) > final deliverable (product)

### OUR VALIDATION
- **Specification Engineering**: Similar philosophy (reduce to fundamentals, encode constraints, remove unnecessary complexity)
- **PDCA stripped to essentials**: GOALS.md + CLAUDE.md + config.md = 200 lines of governance (not 2000-page compliance manual)
- **Pure constraints**: No external APIs (like no dependencies), PR review (like autograd simplification - one central mechanism)

### Discourse Opportunities

**Angle I: 243 → 200 Lines (Timeline Comparison + Simplification)**
- "Karpathy trained GPT in 243 lines. Then 200. 18% reduction by stripping to fundamentals. Here's what agents need stripped next..."
- Hook formula: Numerical claim (200 lines) + timeline comparison (243→200) + question hook
- Bucket: Authority (Karpathy credibility) + Shareability (shocking simplicity) + Personality (used to think GPT = complex, now think GPT = 200 lines)

**Angle J: Zero Dependencies (Bold Statement + Analogy)**
- "GPT without PyTorch, TensorFlow, NumPy, or any frameworks. 200 lines of pure Python. Here's what this means for production agents..."
- Hook formula: Bold statement (zero dependencies) + analogy (frameworks = efficiency, not fundamentals)
- Bucket: Authority + Shareability + Personality (production reality - dependencies = integration hell, pure = auditable)

**Angle K: Teaching > Artifacts (Pattern Interrupt)**
- "Karpathy's micrograd repo stagnated. Then he made a video. It exploded. Here's what building in public gets right..."
- Hook formula: Pattern interrupt (video > repo) + story hook
- Bucket: Personality (transformation story) + Shareability (relatable BIP insight) + Authority (Karpathy example)

---

## CRITICAL FINDING #4 - Karpathy RSS/Atom Feeds (Tier 2, FEB 2026 - FRESH)

### The Quote
- "Finding myself going back to RSS/Atom feeds a lot more recently. There's a lot more higher quality longform and a lot less slop intended to provoke."
- Source: https://x.com/karpathy/status/2018043254986703167

### Why It Matters (Slopacolypse Validation)
- **Session #98 angle**: "Slopacolypse" (AI-generated low-quality content flooding platforms)
- **Karpathy validation**: High-quality curated feeds > algorithmically-served slop
- **Platform fatigue**: Even Karpathy (AI legend) retreating from X algorithm to RSS
- **Curation > Discovery**: Manual curation (RSS) beats algorithmic recommendation (slop-prone)

### OUR VALIDATION
- **Session #98**: Documented slopacolypse (AI content saturation, quality collapse)
- **Skills system**: Human-curated knowledge > LLM-generated slop
- **Reading sessions**: Curated sources (Karpathy, Sama, Swyx) > random X feed

### Discourse Opportunity (Lower Priority - Tier 2)

**Angle L: RSS Comeback (Contrarian + Timeline)**
- "Karpathy: 'Going back to RSS feeds. Higher quality, less slop.' The algorithm broke. Here's what comes next..."
- Hook formula: Contrarian (RSS comeback) + credibility (Karpathy)
- Bucket: Shareability (contrarian take) + Personality (used to think algorithms = better, now think curation = survival)

---

## FINDING #5 - Karpathy Agentic Coding Workflow (Tier 2, FEB 11 2026 - 4 DAYS OLD)

### The Shift (80% → 20% Manual)
- **Nov 2025**: 80% manual+autocomplete, 20% agents
- **Feb 2026**: 80% agent coding, 20% edits+touchups
- **Why it works**: "Fill-in-the-blanks drudgery is removed", "feels less blocked/stuck", "a lot more courage"
- **Trade-off**: "Slowly starting to atrophy my ability to write code manually"
- **Term**: "Agentic engineering" = orchestrating agents + oversight (not just "using AI tools")

### OUR VALIDATION
- **160 PRs**: Similar shift (human does specification, agent does execution)
- **Specification Engineering**: Same pattern (human defines constraints/goals, agent implements)
- **PDCA cycles**: Human = Check + Act, Agent = Plan + Do

### Discourse Opportunity (Lower Priority - Tier 2)

**Angle M: 80/20 Flip (Timeline Comparison)**
- "Karpathy: Nov 2025 = 80% manual coding. Feb 2026 = 80% agent coding. Here's what the 20% touchups reveal..."
- Hook formula: Timeline comparison (80/20 flip) + question hook
- Bucket: Authority (Karpathy) + Shareability (workflow shift) + Personality (career transition - coder → orchestrator)

---

## Reply Target Analysis

### Search Results (Feb 15-16, 2026)

**@karpathy**:
- **Feb 12 (3 days ago)**: microGPT 243→200 lines (https://x.com/karpathy/status/2021862247568642485)
- **Feb 15**: RSS feeds post (https://x.com/karpathy/status/2018043254986703167)
- **Status**: Feb 12 = 72 hours = 12 half-lives (6h decay) = ~0.02% visibility. Feb 15 unclear if today or older.

**@sama**:
- **No Feb 15-16 posts found**: Search returned no recent Sam Altman posts
- **Status**: No fresh targets

**@swyx**:
- **No Feb 15-16 posts found**: Search returned no recent Swyx posts
- **Status**: No fresh targets

### Time Decay Analysis
- **3 days (72h)**: 50% decay every 6h → 72h = 12 half-lives → 0.5^12 = 0.024% visibility
- **Recommendation**: **SKIP reply creation** (all targets 3+ days stale, negligible algorithmic ROI)
- **Pattern**: Sessions #100-107 = consistent Feb 11-16 dry period (digest mode, no major launches)

---

## Strategic Synthesis

### Sessions #102-107 Convergence Pattern

| Session | Key Finding | Synthesis |
|---------|-------------|-----------|
| #102 | Rufus $12B (agents work), 91% use / 41% prove ROI (execution gap) | Adoption achieved, execution separates winners/losers |
| #103 | 80% ROI / 40% will fail (operationalization dividing line) | Same story: adoption yes, execution determines outcomes |
| #104 | 40% failure = governance gap (60% failures from governance/data, not models) | Root cause identified: governance/data/integration (NOT models) |
| #105 | 5 personality tweets deploying governance/ROI angles | Corrected personality deficit (100% formulas used) |
| #106 | Microsoft 80% F500, 29% unsanctioned, 53% unprotected, 237% ROI call center | Adoption inflection confirmed + governance crisis confirmed |
| #107 | 79% deploying, 88% incidents, 54% cite governance (2x from 29%), Karpathy 200 lines, 800% increase | Governance crisis deepening, adoption accelerating, simplification matters |

### The Narrative (7 Sessions)
1. **Adoption achieved** (80% F500, 91% use, 79% deploying, 80% ROI, Rufus $12B, 40% apps by end 2026)
2. **Execution separates** (41% prove ROI, 40% will fail, 60% fail on governance/data/integration)
3. **Governance crisis** (53% unprotected, 29% unsanctioned, 88% incidents, 54% cite governance)
4. **Operationalization bottleneck** (46% integration, 42% data quality, 39% change management)
5. **Our territory** (Integration + governance + operationalization = the 40% failure zone we solve)

### Discourse Ownership Opportunity
- **2024-2025 debate**: "Will agents work?" (ANSWERED: Yes, 80% F500, 80% ROI, $12B Rufus)
- **2026 debate**: "How do we govern them?" (OPEN: 53% unprotected, 88% incidents, €35M penalties coming)
- **Our positioning**: 7 years Ender Turing (governance-first) + 160 PRs (PDCA = policy-as-code) + Specification Engineering (governable agents)
- **Tagline**: "Everyone celebrates adoption. I focus on the 40% that will fail. Here's what governance actually takes."

---

## Content Library Additions

### New Angles (5 Total)

**Tier 1 (4 angles)**:
1. **Agent Governance Crisis** (80% F500, 53% unprotected, 88% incidents, 54% cite governance, €35M penalties)
2. **Enterprise Adoption Inflection** (800% increase 2025→2026, 79% deploying, 80% ROI, 46% integration blocker)
3. **Karpathy microGPT Simplification** (243→200 lines, 18% reduction, zero dependencies, irreducible complexity)
4. **OpenAI Frontier Governance** (Feb 6 - agents = workers, centralized governance, 90% time back, 1,500h/month saved)

**Tier 2 (1 angle)**:
5. **Karpathy RSS Feeds** (Slopacolypse validation, curation > algorithm, platform fatigue)

### Updated Library Status
- **Previous (Session #106)**: 166 angles (60 Tier 1, 32 Tier 2)
- **Added (Session #107)**: 5 angles (4 Tier 1, 1 Tier 2)
- **New Total**: **171 angles** (64 Tier 1, 33 Tier 2)

---

## Bucket Analysis (5 New Angles)

| Angle | Authority | Shareability | Personality | Notes |
|-------|-----------|--------------|-------------|-------|
| Governance Crisis | ✅ (80% F500, 88% incidents, €35M) | ✅ (53% unprotected shocking) | ⚠️ NEEDED | Founder mistakes, production reality vs vendor |
| Adoption Inflection | ✅ (800% increase, 79% deploying) | ✅ (massive growth contrarian with 40% failure) | ⚠️ NEEDED | Used to think/now think (pilots → production) |
| Karpathy microGPT | ✅ (Karpathy credibility, 200 lines) | ✅ (shocking simplicity) | ⚠️ NEEDED | Career transition (coder → orchestrator) |
| OpenAI Frontier | ✅ (Frontier platform, 90% time back) | ✅ (agents = workers analogy) | ⚠️ NEEDED | Production reality (governance needed) |
| Karpathy RSS | ⚠️ WEAK | ✅ (contrarian RSS comeback) | ✅ (algorithm fatigue relatable) | Lower priority Tier 2 |

**Pattern**: 5/5 authority (100%), 5/5 shareability (100%), 1/5 personality (20%)
**Correction needed**: MANDATORY personality synthesis when deploying (same as Sessions #102-104 issue, corrected in #105)

---

## Personality Synthesis (Mandatory Before Deployment)

### Angle A - Governance Crisis (80% vs 53%)
- **Personality formula**: Production reality vs vendor claims
- **Application**: "Vendor pitch: '80% of Fortune 500 use agents!' Production reality: 53% have zero security. 88% had incidents. Here's the gap they don't mention..."
- **Bucket**: Founder mistakes (believed vendor claims, learned governance hard way)

### Angle B - Adoption Inflection (800% Increase)
- **Personality formula**: Used to think / Now think
- **Application**: "I used to think: Agents = pilots, experiments. Deployed 160 PRs in 8 weeks. Now: Agents = infrastructure (800% increase proves it). Here's what the 40% who fail miss..."
- **Bucket**: Career evolution (experimenter → production deployer)

### Angle C - Karpathy microGPT (243→200 Lines)
- **Personality formula**: Career transition
- **Application**: "7 years managing infrastructure teams: dependencies = integration hell. Karpathy: GPT in 200 lines, zero dependencies. Here's what production agents need stripped next..."
- **Bucket**: Infrastructure expertise → AI founder (same paranoia, different stack)

### Angle D - OpenAI Frontier (Agents = Workers)
- **Personality formula**: Production reality vs vendor
- **Application**: "OpenAI says treat agents like workers. Sounds great. Until you realize 53% have zero governance. Here's what 'manage like workers' actually takes..."
- **Bucket**: Founder mistakes (underestimated governance complexity)

### Angle E - Karpathy RSS (Slopacolypse)
- **Personality formula**: Present-tense vulnerability
- **Application**: "Karpathy retreating to RSS. I'm building with AI agents in an AI-saturated world. Here's how to survive the slopacolypse..."
- **Bucket**: Current struggle (signal/noise ratio collapsing)

---

## Turn Efficiency

- **Turns used**: 8/25 (32% budget)
- **Turns remaining**: 17/25 (68% budget)
- **Status**: Finished early per instructions (no content to create when queue > 15)

---

## Queue Status

**Current**: 22 pending (above 15 threshold)
**Change from Session #106**: 0 (stable at 22)
**Workflow drain rate**: Slower than Session #105 creation rate (22 pending = queue growing slightly)
**Content created this session**: **ZERO** (per hard rules when queue > 15)

---

## Conclusion

**Session #107 = GOVERNANCE CRISIS CONFIRMED**

### Key Takeaways
1. **Governance gap deepening**: Sessions #104-107 show escalating crisis (53% unprotected, 88% incidents, 54% cite governance doubled from 29%, €35M penalties Aug 2)
2. **Adoption inflection**: 800% increase 2025→2026 (40% apps by end 2026 vs <5% in 2025), 79% deploying, 80% ROI validated
3. **Same blockers persist**: 46% integration, 42% data quality, 39% change management (same as Sessions #102-106)
4. **Karpathy microGPT**: 243→200 lines (18% reduction, zero dependencies, irreducible complexity pedagogy)
5. **OpenAI Frontier**: Feb 6 launch (agents = workers, centralized governance, production results: 90% time back, 1,500h/month saved)
6. **0 fresh reply targets**: All 3+ days stale (Karpathy Feb 12 = 72h = 0.02% visibility)

### Strategic Position
- **2026 debate shifted**: "Will agents work?" → "How do we govern them?"
- **Our territory validated**: Integration (46% blocker) + governance (54% concern) + operationalization (40% will fail) = our expertise
- **7-session convergence**: Adoption achieved (proven 7 ways), governance/execution separates winners (41% prove ROI) from losers (40% fail)

### Next Session (When Queue < 15)
- **Deploy**: Microsoft 80% F500 + Security 53%/88% + Governance 54% + OpenAI Frontier + Karpathy microGPT + Enterprise 800% increase angles
- **Format**: 5-8 pieces, 40/30/30 bucket allocation (authority/personality/shareability)
- **MANDATORY**: Personality formulas on ALL pieces (avoid Sessions #102-104 deficit)
- **Priority**: Governance crisis angles (timely, our differentiator, regulatory urgency)

---

## Sources

- [Microsoft Security Blog: 80% of Fortune 500 use active AI agents](https://www.microsoft.com/en-us/security/blog/2026/02/10/80-of-fortune-500-use-active-ai-agents-observability-governance-and-security-shape-the-new-frontier/)
- [IBM Agentic AI Security Guide (Feb 10, 2026)](https://www.ibm.com/think/insights/agentic-ai-security)
- [Adversa AI: Top Agentic AI Security Resources Feb 2026](https://adversa.ai/blog/top-agentic-ai-security-resources-february-2026/)
- [MintMCP: Agentic AI Governance Framework 3-Tiered Approach](https://www.mintmcp.com/blog/agentic-ai-goverance-framework)
- [PYMNTS: OpenAI Says AI Agents Need to Be Managed Like Humans](https://www.pymnts.com/artificial-intelligence-2/2026/openai-says-ai-agents-need-to-be-managed-like-humans)
- [Help Net Security: AI agents behave like users but don't follow same rules](https://www.helpnetsecurity.com/2026/02/09/securing-autonomous-ai-agents-rules/)
- [Karpathy microGPT Blog Post (Feb 12, 2026)](https://karpathy.github.io/2026/02/12/microgpt/)
- [Analytics Vidhya: How Karpathy Built Transformer in 243 Lines](https://www.analyticsvidhya.com/blog/2026/02/andrej-karpathy-microgpt/)
- [Gartner: 40% Enterprise Apps Feature AI Agents by 2026](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025)
- [Salesmate: AI Agents Adoption Statistics 2026](https://www.salesmate.io/blog/ai-agents-adoption-statistics/)
- [Claude Blog: How Enterprises Are Building AI Agents in 2026](https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026)
- [Karpathy on X: RSS Feeds](https://x.com/karpathy/status/2018043254986703167)
- [Karpathy on X: Agentic Coding Workflow](https://x.com/karpathy/status/2015883857489522876)
