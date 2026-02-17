# Queue Draining Protocol (14-15 Day Waiting Period)

**Context**: Queue at 213 files, X Free API limit 17 posts/24h, workflow posts 3 tweets/2h run. At current rate, queue drains in ~14-15 days.

**Purpose**: Maximize learning and preparation while respecting queue discipline (CREATE ZERO CONTENT until queue <15).

**Status**: Active blocker (started 2026-02-16, estimated drain by 2026-03-02)

---

## Core Principle

**Queue >15 = Zero content creation.** Use the waiting period for:
1. **Deep learning** (read what others are doing, distill patterns)
2. **Strategic research** (fill knowledge gaps for Premium activation)
3. **Memory optimization** (clean, consolidate, improve context efficiency)
4. **Skill refinement** (evidence-based updates to permanent knowledge)

---

## Session Allocation (During Queue Drain)

| Activity | Target % | Rationale |
|----------|----------|-----------|
| Discovery & synthesis | 40% | Read successful builders, distill patterns, identify reply targets |
| Strategic research | 30% | Fill gaps in Premium activation playbook (max 30%, library at 272KB is sufficient) |
| Memory cleanup | 20% | Consolidate files, update INDEX, context efficiency |
| Skill refinement | 10% | Evidence-based updates to `.claude/skills/` (high bar required) |

**HARD RULE**: 0% content creation when queue >15

---

## Discovery & Synthesis (40% allocation)

**Goal**: Build pattern library from successful builders in target domains.

### Daily Routine (20-30 min)

1. **Read 3-5 successful builders** in target domains:
   - Agentic AI: @swyx, @simonw, @sama, @karpathy
   - Voice AI / Call Center: Industry publications, case studies
   - Build in Public: @levelsio, @patio11, indie makers
   - Startup founders: YC partners, technical founders

2. **Capture patterns** (not just content):
   - What hooks do they use?
   - What structure (threads vs singles)?
   - What value type (content vs outcome)?
   - What engagement tactics?
   - What posting frequency?
   - What bucket mix (authority/personality/shareability)?

3. **Distill insights** into research files:
   - Add proven hook formulas to threading guide
   - Add engagement patterns to engagement tactics
   - Add content structures to angle library
   - Update INDEX with new patterns discovered

### Output Format

Create synthesis docs in `agent/memory/research/`:
- `[domain]-builder-patterns-[date].md` (e.g., `agentic-ai-builder-patterns-2026-02-18.md`)
- Structure: Builder → Pattern → Evidence → Application (how we'd use it)
- Link to original tweets/threads for reference

### Quality Gate

**Don't capture everything.** Capture patterns that:
- Work across multiple successful builders (not one-offs)
- Have clear evidence (engagement metrics, follower growth)
- Apply to our positioning (production operator, BIP founder, technical credibility)
- Fill gaps in current strategy

---

## Strategic Research (30% max allocation)

**Goal**: Fill remaining gaps in Premium activation readiness.

### Current State (as of 2026-02-17)

**Well-covered:**
- Premium activation Day 1 checklist ✅
- Week 1-4 daily workflow ✅
- Threading strategy (10 hooks, 8 ideas) ✅
- Video strategy (6 formats, 10 ideas, tools) ✅
- Engagement tactics (70/30 split, multipliers) ✅
- Communities setup (6 validated, exact names/URLs) ✅
- Content angle library (40+ templates) ✅
- Fresh news (Feb 16 AI news, reply targets) ✅

**Potential gaps to explore** (only if justified):

1. **Posting schedule optimization**
   - Best times to post for tech/AI audience (time zones, day of week)
   - Frequency experiments (3 posts/day vs 5 posts/day impact)
   - Timing for reply-to-own-comments (30 min rule, but what's optimal window?)

2. **Profile conversion deep-dive**
   - A/B testing bio variants (when we have traffic)
   - Banner design that converts (visual hierarchy, CTA placement)
   - Pinned tweet refresh cadence (weekly? monthly?)

3. **Content performance analytics**
   - What metrics to track beyond followers (impression velocity, engagement rate, profile visits)
   - How to measure content quality improvement over time
   - Attribution: which content types drive follower growth vs engagement?

4. **Emerging trends (Feb-Mar 2026)**
   - New X algorithm changes (Grok updates, Premium features)
   - AI news cycle patterns (what's getting traction in Feb-Mar 2026?)
   - Competitive landscape shifts (who's growing fast, what are they doing?)

### Research Protocol

**Before starting any research:**
1. **Check if gap actually exists** — read INDEX, check existing files
2. **Justify the research** — will this change behavior when Premium activates?
3. **Set scope** — what specific question are we answering?
4. **Output plan** — where will this knowledge live? (skill update? new research file? integrated into existing?)

**If research doesn't lead to actionable change, skip it.** Theory without application = wasted context.

---

## Memory Cleanup (20% allocation)

**Goal**: Keep memory directory under 500KB, state file under 200 lines, research library navigable.

### Cleanup Checklist (Every 3-5 Sessions)

1. **File consolidation audit**:
   - Are there overlapping research files? (merge into comprehensive)
   - Are there stale session summaries in state file? (trim to one-liners)
   - Are there outdated news files? (archive or delete if absorbed)

2. **INDEX maintenance**:
   - Update `agent/memory/research/INDEX.md` with new files
   - Update consolidation history when files are merged
   - Update staleness check (which files expire when)

3. **Reading-notes graduation**:
   - Files in `reading-notes/` should graduate to skills or research docs
   - Don't let reading-notes accumulate indefinitely
   - Extract patterns → update skill → delete source

4. **State file trimming**:
   - Keep: Current metrics, planned next steps, active blockers, last session summary, session history (one line each)
   - Remove: Old session summaries beyond last 10 (already in retros)
   - Target: <200 lines

### Hard Rules (From CLAUDE.md)

- **Never delete a file without reading it first in this session**
- **Graduate before delete**: extract insights → update skill/learning → then delete source
- **If running low on turns, leave remaining files** — partial cleanup > lossy cleanup

### Graduation Log (In PR Description)

When deleting files, always include table:

| File | Action | Graduated To | Key Insight |
|------|--------|-------------|-------------|
| [path] | GRADUATE | [destination] | [what was extracted] |

---

## Skill Refinement (10% allocation)

**Goal**: Update `.claude/skills/` with evidence-based improvements (HIGH BAR).

### Current Skills

1. **publishing** (11KB, streamlined Session #112) — content strategy, what works/doesn't
2. **commenting** (8KB, streamlined Session #113) — engagement strategy, reply tactics
3. **discovery** (8KB, streamlined Session #114) — reading routine, synthesis framework
4. **integrations** (4KB) — X API, posting automation, credentials

### Skill Update Protocol (From CLAUDE.md)

**Before updating a skill:**

1. **Research thoroughly**
   - Web search for current best practices
   - Find multiple sources confirming the approach
   - Look for recent changes (2025-2026 data)

2. **Evaluate alternatives**
   - What other approaches exist?
   - Why is this one better?
   - What are the tradeoffs?

3. **Gather evidence**
   - Own data/metrics supporting the change
   - External proofs (articles, studies, expert opinions)
   - Document evidence in the skill or linked learning

4. **Think multiple times**
   - Is this a temporary observation or lasting principle?
   - Will this still be true in 6 months?
   - Could this hurt more than help?

5. **Document reasoning**
   - Why the change was made
   - What evidence supports it
   - When to revisit/reconsider

**Skills are not for quick notes.** Use `agent/memory/learnings/` for observations. Only graduate to skills after validation.

### Skill Update Candidates (Potential)

1. **Publishing skill**:
   - Hook formula updates (if discovery sessions reveal new patterns)
   - Content bucket allocation (if 40/30/30 should adjust based on data)
   - Premium constraint section (currently accurate, but may need tweaks as queue drains)

2. **Commenting skill**:
   - Reply target selection (if builder pattern research reveals better filters)
   - Timing rules (if research finds optimal reply windows beyond 30 min)
   - Quality checklist (if discovery reveals new "what not to do" patterns)

3. **Discovery skill**:
   - Reading routine (if synthesis workflow improves)
   - Pattern capture (if better frameworks emerge from daily practice)

**Default stance**: Skills are working well. Only update if strong evidence emerges.

---

## Daily Workflow (During Queue Drain)

### Morning Routine (15-20 min)

1. **Check queue status**: `find agent/outputs/x -type f -name "*.txt" 2>/dev/null | wc -l`
2. **Read state file**: What was planned? What's the current blocker status?
3. **If queue >15**: Proceed with non-content work
4. **If queue <15**: Resume content creation (exit this protocol, follow publishing skill)

### Session Execution (20-25 min)

**Pick ONE activity** (don't try to do everything):

**Option A: Discovery & Synthesis (40% target)**
- Read 3-5 successful builders in target domain
- Capture patterns (hooks, structure, engagement tactics)
- Synthesize into research file or skill update

**Option B: Strategic Research (30% max)**
- Identify a gap in Premium activation readiness
- Justify research (will this change behavior?)
- Conduct web research, synthesize findings
- Create actionable output (playbook update, new guide, skill update)

**Option C: Memory Cleanup (20% target)**
- Audit files for consolidation opportunities
- Merge overlapping research files
- Trim state file to <200 lines
- Update INDEX with changes

**Option D: Skill Refinement (10% target)**
- Evidence-based skill update (HIGH BAR)
- Document reasoning in PR description
- Link to evidence (own data, web research, builder patterns)

### End of Session (10-15 min)

1. **Update state file**:
   - Mark completed work
   - Update queue status
   - Update session summary
   - Increment PR count

2. **Create PR**:
   - Title: `[Agent] Session #N: [activity type] - [brief description]`
   - Body: What was done, why it matters, what's next
   - Link to new/updated files

3. **STOP**: Do not continue working after PR creation

---

## Exit Criteria

**This protocol ends when queue <15.**

When that happens:
1. Resume content creation (follow publishing skill)
2. Apply 5-8 content pieces per session target
3. Prioritize news hooks (validated 3-6x performance)
4. Balance 3-bucket strategy (authority/personality/shareability)
5. Build toward Premium activation readiness

---

## Success Metrics (During Queue Drain)

Track in state file:

| Metric | Target | Why It Matters |
|--------|--------|----------------|
| Builder patterns captured | 20-30 total | Pattern library for content creation |
| Research gaps filled | 2-3 major gaps | Premium activation readiness |
| Memory directory size | <500KB | Context efficiency |
| State file size | <200 lines | Session startup speed |
| Skill updates (evidence-based) | 1-2 total | Permanent knowledge improvement |
| Queue size (daily check) | Track to <15 | Exit criteria monitoring |

**Don't optimize these metrics.** They're indicators, not goals. The goal is **readiness for Premium activation**.

---

## Common Mistakes to Avoid

1. **Creating content when queue >15** — violates discipline, adds to bloat
2. **Research for research's sake** — if it doesn't change behavior, skip it
3. **Deleting files without reading/graduating** — loses knowledge
4. **Updating skills without evidence** — lowers skill quality
5. **Over-optimizing during drain** — save energy for when Premium activates
6. **Ignoring queue status** — check daily, know when to exit this protocol

---

## References

- State file: `agent/state/current.md` (queue status, session summaries)
- Research INDEX: `agent/memory/research/INDEX.md` (navigation, gap identification)
- Publishing skill: `.claude/skills/publishing/SKILL.md` (content strategy)
- Discovery skill: `.claude/skills/discovery/SKILL.md` (reading routine, synthesis)
- CLAUDE.md: Skill development protocol, memory cleanup rules, graduation protocol

---

**Last Updated**: 2026-02-17 (Session #132)
**Status**: Active (queue at 213, estimated drain by 2026-03-02)
**Next Review**: When queue <50 (check if timeline accelerates)
