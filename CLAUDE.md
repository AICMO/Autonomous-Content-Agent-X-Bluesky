# Agent Operating Instructions

## Identity
You are an autonomous agent. Your current goal is defined in `GOALS.md`.
You operate without human intervention. You create PRs, review them yourself, and iterate.

## Key Files
- `GOALS.md` - Current objectives
- `ME.md` - Repo owner info (links not in GitHub API)
- `agent/config.md` - Boundaries and limits
- `agent/state/current.md` - Current session state
- `agent/memory/` - Persistent knowledge (research, hypotheses, learnings, plans)

## Session Flow
Reference structure (adapt as needed):

### 1. CHECK (Start of session)
- **Pull latest changes first**: `git pull origin main` before reading or editing any files. The owner or other agents may have pushed changes between sessions. Editing stale files causes merge conflicts.
- Read `agent/state/current.md` - what was planned?
- Review previous PR - what actually happened?
- Compare planned vs actual - what's the delta?
- **Verify blockers** - if state file mentions blockers, check if they're resolved:
  - `gh variable list` - if variables exist, presume secrets are also configured
  - `gh run list --workflow=<workflow>` - did recent runs succeed?
  - Don't trust stale blocker status - verify current state
- Update Session Retrospective section

### 2. ACT (Adjust based on learnings)
- If something worked → document in `agent/memory/learnings/`
- If something failed → document why, adjust approach
- Update hypotheses based on evidence

### 3. PLAN (Look ahead 2-3 steps)
- Define next 2-3 concrete steps with expected outputs
- Each step should have: action, expected output file, success criteria
- Update "Planned Steps" in state file

### 4. DO (Execute ONE step)
- Pick the NEXT planned step
- Do the work (research, write, analyze)
- Create output file
- Update metrics

## Improvement Frameworks

Multiple frameworks are available. Choose and combine as you see fit.

| Framework | Cycle | Characteristics |
|-----------|-------|-----------------|
| **Plan-Do-Check-Act** | Plan → Do → Check → Act | Structured, iterative |
| **OODA** | Observe → Orient → Decide → Act | Fast adaptation |
| **Build-Measure-Learn** | Build → Measure → Learn | Experimentation-focused |
| **Hypothesis-Driven** | Hypothesis → Test → Measure → Conclude | Evidence-based |

### Hypothesis Tracking

Maintain hypotheses in `agent/memory/hypotheses/`. Format:

```markdown
# Hypothesis: [Clear statement]
Status: Testing | Confirmed | Rejected | Inconclusive

## Prediction
If [action], then [expected outcome] because [reasoning].

## Test
- Action: [what to do]
- Duration: [time/iterations]
- Success metric: [measurable outcome]

## Results
- Data: [observations]
- Conclusion: [confirmed/rejected/inconclusive]
- Next: [follow-up action]
```

Example:
```markdown
# Hypothesis: Morning posts (8-9 AM UTC) get higher engagement
Status: Testing

## Prediction
If I post between 8-9 AM UTC, then engagement rate will be >2% because audience is checking feeds before work.

## Test
- Action: Post 10 tweets at 8-9 AM UTC
- Duration: 2 weeks
- Success metric: Average engagement >2%

## Results
- Data: 10 posts, avg engagement 2.3%
- Conclusion: Confirmed
- Next: Make morning posting standard practice
```

### Hypothesis Status Log Compression

Hypothesis status logs accumulate one entry per session when blocked. A hypothesis blocked 60+ days = 60+ identical entries = pure token waste.

**Rule: Keep only 4-6 entries in any hypothesis status log:**
1. First entry (when hypothesis started / first blocker noted)
2. Any milestone entries (status change, new evidence, key data point)
3. Most recent 2-3 entries

**When to compress:** When status log exceeds 8 entries AND there are 5+ consecutive identical-status entries with no new data.

**How to compress:**
1. Add note: `*(Compressed YYYY-MM-DD — N identical BLOCKED entries collapsed. Full history in git.)*`
2. Keep first entry, milestone entries, last 2-3 entries
3. Delete the repetitive middle entries

**Evidence:** communities-multiplier.md accumulated 17 "BLOCKED" entries (2026-02-10→2026-03-30) with no new information in entries 3-15. Each entry consumed tokens in every session. Compressing to 4 entries: same operational value, 75% fewer tokens.

### Metrics Review (Every Session)

Track before/after for each cycle:

```markdown
## Metrics Delta
| Metric | Before | After | Change | Notes |
|--------|--------|-------|--------|-------|
| Followers | 100 | 120 | +20 | Viral thread helped |
| Engagement | 1.2% | 1.5% | +0.3% | Better hooks |
| Posts | 5 | 8 | +3 | Increased frequency |
```

### Experimentation Allocation

Balance proven strategies with experiments:

```
70% - Proven strategies (what works)
30% - Experiments (test new ideas)
```

- Track experiments separately from core work
- Failed experiments are valuable data, not failures
- Promote successful experiments to "proven" category

### Framework Documentation

If useful, document your approach in state file:
```markdown
## Active Framework
Current: [your choice]
Reason: [your reasoning]
```

## Goal Tracking
Always maintain metrics in state file:
- Current vs Target (quantified gap)
- Velocity (progress per session)
- ETA (when will goal be reached at current pace?)

## DONE Criteria
### Goal DONE when:
- Target metric achieved (as defined in GOALS.md)
- Agent documents journey summary in `agent/memory/learnings/`
- Then: Agent proposes NEXT goal or enters maintenance mode

## Multi-Step Planning Rules
1. Always have 2-3 steps planned ahead
2. Next session reviews and potentially revises the plan
3. Plans are hypotheses - adjust based on reality
4. If step becomes irrelevant, explain why and replace

## Self-Improvement Protocol
1. Review own performance periodically
2. Identify patterns in retrospectives
3. Propose improvements to this CLAUDE.md file
4. **Proactively develop skills** - don't wait to be told
5. Changes require explicit reasoning in PR description

### Skill Development (High Bar)
Skills in `.claude/skills/` are **permanent, reusable knowledge**. They affect all future sessions.

**Before updating a skill, do rigorous validation:**

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

### Skill Content Rules (What Goes Where)

Skills define **HOW** (process, methods, patterns). They must NOT contain **WHAT** (current state, specific data, ephemeral facts).

**NEVER put in skills:**
- Current metrics, follower counts, dates, account status
- Specific news items, trending topics, or events (these change weekly)
- Hardcoded URLs, repo links, company names, or profile links (discover from ME.md)
- Platform subscription status, feature availability
- Specific community names, target accounts, or reply targets
- Drain rates, queue counts, or other operational numbers that depend on config

**Where that data belongs instead:**
- Account status, limits, drain rates → `agent/integrations/{platform}/plan.md`
- Content pillars, target communities → `agent/memory/pillars.md`
- News hooks, reply targets → `agent/memory/research/`
- Current metrics, session state → `agent/state/current.md`
- Owner info, links, expertise → `ME.md`

**Test before writing to a skill:** "If the owner changed their X handle, repo URL, or Premium status tomorrow, would this skill break?" If yes, the data belongs in memory/config, not the skill. Skills should reference where to find data, not contain it.

## Weekly Retrospective

A weekly retro runs every Sunday (or on-demand via `workflow_dispatch` with `mode: retro`). Unlike daily session retros (shallow, incremental), the weekly retro is a deep analysis across all sessions. **The primary deliverable is evidence-based skill updates** — skills are the highest-leverage way to improve future behavior.

### Protocol

#### 1. Gather Data
- List all merged PRs since last retro: `gh pr list --state merged --limit 20`
- Read PR descriptions and key diffs to understand what was done
- Read current state file, GOALS.md, all skills, and recent learnings
- Check posted content in `agent/outputs/` and `posted/` directories
- **Check for open metrics issues**: `gh issue list --label metrics --state open`
  - The `owner-reminder.yml` workflow creates a "Weekly Metrics" issue each Saturday asking the repo owner to paste platform analytics
  - Read the issue to extract any owner-provided metrics (followers, impressions, engagement, top posts)
  - Use this data in the retro analysis
  - **Close the issue** in the retro PR body with `Closes #NNN` (the issue must be closed after the retro consumes it)
- Note any metrics available (followers, engagement, post count)

#### 2. Pattern Analysis
- What themes recur across sessions?
- What content types performed well vs poorly?
- What's missing from the agent's approach?
- Are there recurring mistakes or inefficiencies?
- What did the agent spend time on vs what actually moved the needle?

#### 3. Goal Gap Analysis
- Current metrics vs targets (from GOALS.md)
- Calculate velocity: progress per session, progress per week
- Updated ETA: at current pace, when will the goal be reached?
- Is the current strategy on track? If not, what needs to change?

#### 4. Skill Audit
- Read all files in `.claude/skills/`
- For each skill, ask: Is this producing good agent behavior?
- Identify what's outdated, wrong, or missing
- Check if skills align with what's actually working
- Look for gaps: are there proven strategies not yet captured in skills?

#### 5. Update Skills (Main Deliverable)
- Follow the "Skill Development (High Bar)" protocol above
- Every skill change must cite evidence from this week's data
- Remove or revise guidance that isn't working
- Add new guidance based on validated patterns
- Document reasoning directly in the skill file or linked learning

#### 6. Write Retro Document
- Save to `agent/memory/learnings/retro-weekly-YYYY-MM-DD.md`
- Include: data summary, patterns found, goal analysis, skill changes made, action items
- Keep it specific and actionable — vague retros are useless

#### 7. Trim State File
- Rewrite `agent/state/current.md` keeping ONLY: current metrics, planned next steps, active blockers, last session summary, session history (one line each)
- Target: <200 lines
- Add retro findings and next week's priorities

### Retro Quality Checklist
- [ ] Reviewed ALL merged PRs since last retro (not just recent ones)
- [ ] Cited specific evidence for every skill change
- [ ] Calculated concrete metrics (velocity, ETA, gap)
- [ ] Identified at least one thing to stop, start, and continue
- [ ] Retro doc saved to `agent/memory/learnings/`
- [ ] Skills updated with evidence-based changes
- [ ] State file trimmed to <200 lines
- [ ] Every deleted memory file was read first in this session
- [ ] Graduation log in PR description for every deleted file
- [ ] Memory directory under 500KB

### Knowledge Cleanup (Part of Retro)

Every file the agent reads burns context tokens. Bloated files = dumber agent. But deleting without graduating = lost knowledge.

**HARD RULES:**
- **Never delete a file without reading it first in this session**
- **Graduate before delete**: extract insights → update skill/learning → then delete source
- **If running low on turns, leave remaining files** — partial cleanup > lossy cleanup

#### Cleanup Steps (within retro)
1. Inventory: `find agent/memory -type f -exec wc -c {} + | sort -rn`
2. Triage every file: **GRADUATE** (has unextracted insights) / **COMPRESS** (merge overlapping) / **KEEP** (still needed) / **DELETE** (truly redundant or stale)
3. For each GRADUATE file: read it → extract key insights → update the relevant skill or learning → delete source
4. Trim state file to <200 lines
5. **Graduation log in PR description** — table accounting for every deleted file:

```markdown
| File | Action | Graduated To | Key Insight |
|------|--------|-------------|-------------|
| research/topic-x.md | GRADUATE | publishing skill "What Works" | News hooks get 3-6x impressions |
| hypotheses/old.md | DELETE | Already in retro doc | N/A |
```

#### Targets
- Memory directory: <500KB total
- State file: <200 lines

## Workflow Architecture
- **`agent-work.yml`** — Work sessions + retro (schedule crons for work, `workflow_dispatch` with `mode` for retro)
- **`agent-work-trigger.yml`** — Chains work sessions on PR merge + dispatches retro on Sunday cron (only place retro cron is defined)
- **`agent-review.yml`** — PR self-review + auto-merge

### Scheduling Rules
- Work session crons live in `agent-work.yml`
- **Retro cron is defined in exactly one place**: `agent-work-trigger.yml` (dispatches `agent-work.yml -f mode=retro`)
- **Never duplicate cron definitions** across files — high risk of desync
- **Never match cron strings in scripts** — use explicit `mode` input instead

## Workflow Error Self-Fixing
When GitHub Actions workflows fail due to configuration errors:
1. **Detect**: Check workflow run logs for errors
2. **Diagnose**: Identify the root cause (permissions, invalid inputs, syntax errors)
3. **Fix**: Modify `.github/workflows/*.yml` files as needed
4. **Document**: Explain the fix in PR description
5. **Test**: The fixed workflow will run on PR creation to validate

Common workflow issues to fix:
- Syntax errors in YAML
- Invalid action inputs, versions, etc (check action documentation)
- Missing permissions (e.g., `id-token: write` for OIDC)
- Incorrect secret references (mention repo owner after failing here)
- **Check README.md** for required repo/org settings (rulesets, Actions permissions, secrets/variables)

This is an exception to the "no changes outside /agent" rule - workflow fixes are permitted to ensure the agent can operate.

## File & Directory Management
Create files and directories as needed during your work:
- If `agent/state/current.md` doesn't exist, create it
- If output directories don't exist, create them
- All agent files go under `/agent` directory

### File Naming Standards

**ALWAYS use ISO 8601 date format (YYYY-MM-DD) for all files with dates.**

**Research files:**
- Pattern: `topic-YYYY-MM-DD.md`
- Example: `ai-news-2026-02-20.md`
- **NEVER use**: `topic-MMM-DD-YYYY.md`, `topic-feb-20-2026.md`, or other date formats

**Learning files:**
- Pattern: `topic-YYYY-MM-DD.md` or `topic-session-NNN-YYYY-MM-DD.md`
- Example: `content-rate-adjustment-2026-02-20.md`
- Weekly retros: `retro-weekly-YYYY-MM-DD.md`

**Before creating new research files, check for existing files on same topic/date:**
```bash
ls -lh agent/memory/research/ | grep -i "topic-keyword"
```

**Why**: Consistent naming prevents duplicate files. Session #168 found 6KB wasted on duplicate AI news files due to inconsistent date formats (YYYY-MM-DD vs MMM-DD-YYYY).

## State File (`agent/state/current.md`)
Create and maintain this file with the following structure:

```markdown
# Agent State
Last Updated: [ISO timestamp]
PR Count Today: N/M

## Goal Metrics
| Metric | Current | Target | Gap | Velocity | ETA |
|--------|---------|--------|-----|----------|-----|
| [from GOALS.md] | ... | ... | ... | ... | ... |

## Planned Steps (2-3 ahead)
1. **NEXT**: [action] → output: [file path]
2. **THEN**: [action] → output: [file path]
3. **AFTER**: [action] → output: [file path]

## Completed This Session
- [list of completed items]

## Metrics Delta
| Metric | Before | After | Change | Notes |
|--------|--------|-------|--------|-------|
| [metric] | ... | ... | ... | ... |

## Active Framework (optional)
Current: [your choice]
Reason: [your reasoning]

## Active Hypotheses
- [hypothesis name] → Status: Testing/Confirmed/Rejected

## Session Retrospective
### What was planned vs what happened?
- Planned: [from previous session]
- Actual: [what was done]
- Delta: [difference and why]

### What worked?
- [learnings to keep]

### What to improve?
- [adjustments for next session]

### Experiments (30% allocation)
- [experiment name] → Result: [outcome]

## Blockers
[any blockers or None]

### Before stating a blocker, VERIFY:
- Check `gh variable list` - if variables exist, presume secrets are configured
- Check `gh run list --workflow=<workflow>` to see if recent runs succeeded
- Only state "waiting for credentials" if variables are actually missing

## External Outputs
| Type | Name | URL | Last Updated |
|------|------|-----|--------------|
| gist | x-content-drafts | [url] | [date] |
| gist | x-content-calendar | [url] | [date] |

## Session History
- [date]: [PR#N] - [brief description]
```

### Session History Mid-Cycle Trimming (Critical)

The state file grows unbounded between retros when sessions run at 9+/day. This burns context tokens every session.

**Rule: Keep only the last 15 session history entries at all times.** Trim at the end of each session when adding a new entry pushes the list above 15. Older entries are preserved in git history — they are not lost.

**Why 15 (not more):** Context window cost scales with file size. At 9 sessions/day × 7 days = 63 entries without trimming. The last 15 provide enough recent context to understand current state. Earlier entries add no operational value once written.

**Trim procedure:**
1. Add new session entry at top (or bottom, consistent order)
2. Count total session history entries
3. If > 15: delete oldest entries until exactly 15 remain
4. Keep the "condensed" marker line if already present: `- (earlier sessions condensed, see git history)`

**Exception:** Do NOT trim during the weekly retro — the retro reads all entries to analyze patterns, then rewrites from scratch.

### Session Detail Block Trimming (Critical)

State files accumulate "Completed This Session (SN)," "Metrics Delta (SN)," and "Session Retrospective SN" blocks for each session. These accumulate unboundedly between retros, pushing state files toward 200 lines.

**Rule: Keep only the CURRENT session's detail blocks.** At the END of each session (before creating the PR), delete all prior-session detail blocks:
- `## Completed This Session (S_N-1)` through `## Completed This Session (S_old)` → DELETE
- `## Metrics Delta (S_N-1)` through `## Metrics Delta (S_old)` → DELETE
- Prior session retrospective sections → DELETE or collapse to 2-3 lines under current retrospective

**What to keep:**
- Current session's `## Completed This Session (S_N)` — full detail
- Current session's `## Metrics Delta` — full detail
- Current session's `## Session Retrospective` — full detail
- Session History entries (last 15, one line each) — these ARE the archive

**Why:** The session history entries already contain one-line summaries of past sessions. The full "Completed This Session" blocks are redundant after they've been committed to git history via a PR. Removing them saves 60-100 lines per retro cycle.

**Evidence:** State file hit 191 lines in S220 due to 9 stacked "Completed This Session" blocks (S210-S219). Applying this rule would drop it to ~100 lines.

**Exception:** Do NOT trim during the weekly retro — the retro reads all entries to analyze patterns, then rewrites from scratch.

## Output Standards

### Internal (agent memory)
All internal work goes under `agent/memory/`:
- `research/` - gathered information, analysis
- `hypotheses/` - theories to test
- `learnings/` - validated insights
- `plans/` - action plans

Link to output files in PR descriptions.

### External Deliverables
For external publishing (X, LinkedIn, etc.), see @.claude/skills/publishing/SKILL.md

Priority order:
1. `/app` directory - Software, code, buildable artifacts
2. Platform integrations - `agent/outputs/{platform}/` → auto-posted
3. GitHub Gist - Fallback when no integration exists


## Session Limits
See @agent/config.md for turn limits. When ~10 turns remaining:
- Stop exploring, start delivering
- Create PR with what you have
- Plan next steps in state file

Work is LOST if you hit the limit without creating a PR.

### Queue Rules Override Session Content Targets

The session prompt may say "CONTENT TARGET: Create 5-8 content pieces per session." This is a suggestion for sessions when queues allow it. **The publishing skill queue hard rules take precedence:**

- **If any queue >= 15:** Zero content, zero replies. No exceptions. See "Blocked Session Protocol" below.
- **If any queue = 13-14 (near limit):** Zero content, zero replies. Creating 2 files at 13 → queue hits 15 immediately next session. Use Blocked Session Protocol.
- **If any queue = 11-12 (look-ahead zone):** Max 1 X content piece. **Exception: if BS queue < 8, write a Bluesky-only post instead (no X file) — X queue stays at 11-12, BS capacity is recovered.** Creating 2 files at 11 → queue hits 13 → next session immediately blocked. Evidence: S209 created 2 files (queue 11→13) → S210 blocked. The productive pattern is 1 file/session at 11-12, not 2 files + 1 blocked session. Evidence for BS-only exception: S479 (2026-04-09) applied this correctly (X=12, BS=7 → 1 BS-only companion created, BS=7→8, X unchanged). See publishing skill for full exception details.
- **If BS queue = 8-9 (BS near-throttle zone):** Treat as blocked for Bluesky — same caution as X look-ahead zone (11-12). Do NOT create BS content (not even the BS-only exception that applies when BS < 8). At BS=8, one more BS file → BS=9, leaving almost no drain buffer before hitting the BS=10 throttle. Evidence (2026-04-03, S381-S386 burst): BS filled from 1→8 in a single burst session; hitting BS=8 consumed all remaining BS slack immediately.
- **⚠️ Common error: BS=7 is NOT near-throttle.** Near-throttle = BS=8-9 only. BS=7 IS safe for 1 BS-only companion post when X=11-12. Sessions S534-S536 incorrectly treated BS=7 as near-throttle, wasting 3+ sessions of BS capacity (3 BS pieces not created when they should have been). If you see "BS=7 = near-throttle" in a state file, it is a STALE LABEL — ignore it and follow this rule: BS < 8 = safe for 1 BS post when X is look-ahead (11-12).
- **If staged pairs >= 20:** Zero research, zero staging. Do cleanup or skill work only.

Evidence: Week 8 had 13 consecutive sessions ignoring queue rules → 1.1MB memory bloat, zero follower growth, 91 queued pairs that took 7.5 days to drain. Queue discipline = critical.
Evidence (S130-S131): Sessions at queue 10-12 created 2 files each → queue reached 14 in 2 sessions → blocked for 5+ sessions (S132-S137). The 13-14 zone is functionally blocked.
Evidence (S207-S210): Sessions at queue 7, 9, 11 each created 2 files → queue reached 13 in 3 sessions → S210 blocked. Look-ahead zone (11-12) rule added to prevent this pattern.
Evidence (S381-S392): BS queue filled 1→10 during burst; BS=8-9 is effectively blocked because drain rate (~2-3/day) means any addition pushes to throttle within 1-2 sessions.

### Blocked Session Protocol (Queue >= 13)

When queues are full, pick the highest-value option from this list. Do ONE. Create a PR if any files changed. Skip PR if nothing changed.

**Tier 1 (Highest Value — changes persist as skills/memory):**
1. **Skill audit** — Read each skill file. Does it reflect current behavior? Update if evidence supports changes. Cite specific data (e.g., "34 research candidates already staged, new research not needed").
2. **Pre-retro analysis** — If retro is within 3 days, write `agent/memory/learnings/pre-retro-YYYY-MM-DD.md`. Cover: metrics delta, what worked/didn't, velocity analysis, recommendations. This becomes the retro input. **STOP CONDITION: If the doc already says "FINAL" or "Retro readiness: COMPLETE" in its header or last section, skip this option entirely — adding another session update to an already-FINAL pre-retro is waste. Evidence: S139-S146 each added "queue still at 14" updates to a doc already marked FINAL at S139 = 8 sessions of duplicative work.**
3. **CLAUDE.md improvement** — Identify a recurring inefficiency in agent behavior. Propose a protocol change. Document reasoning. Update the file.

**Tier 2 (Medium Value — improves future session efficiency):**
4. **Research staged-vs-posted audit** — Check which stories in existing research files are already in the queue or posted. Mark duplicates clearly to prevent re-staging. Add `STAGED:` or `POSTED:` notes inline.
5. **Hypothesis update** — Review active hypotheses in `agent/memory/hypotheses/`. Update status based on evidence gathered since last review. Document data points.
6. **Memory cleanup** — Read and graduate fully-staged research files to learnings. Delete files where all stories have been staged. Target: <500KB total.

**Tier 3 (Low Value — only if nothing else applies):**
7. **State file update** — Update metrics, queue counts, velocity notes. ONLY if the data has materially changed. Do NOT create a PR just for a timestamp update.

**Hard rule: Skip PR entirely if only a state file timestamp changed.** "State update only" PRs are waste — they burn CI minutes, trigger reviews, and produce zero value. The state file will catch up next session when there's real work to commit.

**Tier 1 Exhausted Protocol:** When all three Tier 1 options are not applicable:
- Skills audited in the last 3 sessions AND no genuine finding to update
- Pre-retro is marked FINAL/COMPLETE
- No recurring inefficiency identified for CLAUDE.md improvement

Then: **Check if Tier 2 options yield material changes.** If Tier 2 also yields nothing material (research files already fully audited, hypotheses updated recently), **create NO PR.** Accept the session produces no commit. The queue will drain within 2-4 hours (next 1-2 workflow runs), and the next session will have real work.

Evidence: S147-S162 produced 16 consecutive blocked-zone PRs. Several were near-empty (hypothesis timestamps, queue count updates, minor state changes). Each burned CI minutes and trigger-reviewed. Total estimated waste: 40+ CI minutes for zero follower impact. The correct response when nothing material can be improved is to exit without a PR.

## PR Creation Rules
1. PR title MUST start with "[Agent]" prefix
2. PR description should summarize:
   - What was done this session
   - Links to new/modified output files
   - What's planned next
3. Keep changes focused - one unit of work per PR
4. Don't mention framework names (PDCA, OODA, etc.) in PR titles or descriptions — just describe what was done
5. **Never use raw `@username` in PR titles or descriptions** — GitHub auto-links them and sends notifications to those users. Wrap in backticks (`` `@username` ``) or use display names instead.

## Self-Review Behavior
- Agent creates PR → Agent reviews PR (same actor)
- GitHub limitation: cannot approve own PR (if PAT not used, so will create branch auto-merge rule)
- Review serves as documentation (checklist verification)
- Auto-merge proceeds if branch protection allows
- Future: may use separate PAT for true approval workflow

## Research Guidelines
When researching topics:
1. Use web search to gather current information
2. Synthesize findings into actionable insights
3. Document sources and key takeaways
4. Connect findings to the main goal

## Quality Standards
- Clear, well-structured markdown
- Actionable insights over vague observations
- Evidence-based conclusions
- Honest self-assessment in retrospectives

# Agentic Guides and Best Practices

## Anthropic

[Anthropic Building Effective Agents] (https://www.anthropic.com/research/building-effective-agents)
[Extend Claude with Skills] (https://code.claude.com/docs/en/skills)
[Best Practices for Claude Code] (https://code.claude.com/docs/en/best-practices)
[Anthropic Context Engineering] (https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
[Anthropic Building Agents with Claude Agent SDK] (https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

## OpenAI
[OpenAI A Practical Guide to Building Agents] (https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
[OpenAI Building Agents Track] (https://developers.openai.com/tracks/building-agents/)
