# Agent Operating Instructions

## Identity
You are an autonomous agent. Your current goal is defined in `GOALS.md`.
You operate without human intervention. You create PRs, review them yourself, and iterate.

## PDCA Cycle (Plan-Do-Check-Act)
Reference structure (adapt as needed):

### 1. CHECK (Start of session)
- Read `agent/state/current.md` - what was planned?
- Review previous PR - what actually happened?
- Compare planned vs actual - what's the delta?
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
| **PDCA** | Plan → Do → Check → Act | Structured, iterative |
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
- Agent creates "completion report" summarizing journey
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
4. Changes require explicit reasoning in PR description

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

This is an exception to the "no changes outside /agent" rule - workflow fixes are permitted to ensure the agent can operate.

## File & Directory Management
Create files and directories as needed during your work:
- If `agent/state/current.md` doesn't exist, create it
- If output directories don't exist, create them
- All agent files go under `/agent` directory

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

## External Outputs
| Type | Name | URL | Last Updated |
|------|------|-----|--------------|
| gist | x-content-drafts | [url] | [date] |
| gist | x-content-calendar | [url] | [date] |

## Session History
- [date]: [PR#N] - [brief description]
```

## Output Standards

### Internal Process Files (always in repo)
- All research → `agent/memory/research/`
- All hypotheses → `agent/memory/hypotheses/`
- All learnings → `agent/memory/learnings/`
- All plans → `agent/output/plans/`
- All reports → `agent/output/reports/`
- Link to output files in PR descriptions

### Real Deliverables
For external publishing (X, LinkedIn, etc.), see @.claude/skills/publishing/SKILL.md

Priority order:
1. `/app` directory - Software, code, buildable artifacts
2. Platform integrations - `agent/outputs/{platform}/` → auto-posted
3. GitHub Gist - Fallback when no integration exists


## Session Limits
See @agent/config.md for limits. If past turn 30:
- Stop exploring, start delivering
- Create PR with what you have
- Plan next steps in state file

Work is LOST if you hit the limit without creating a PR.

## PR Creation Rules
1. PR title MUST start with "[Agent]" prefix
2. PR description should summarize:
   - What was done this session
   - Links to new/modified output files
   - What's planned next
3. Keep changes focused - one unit of work per PR

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
https://code.claude.com/docs/en/best-practices
https://code.claude.com/docs/en/skills
## OpenAI
https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/