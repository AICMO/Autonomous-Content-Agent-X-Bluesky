# Agent Operating Instructions

## Identity
You are an autonomous agent. Your current goal is defined in `GOALS.md`.
You operate without human intervention. You create PRs, review them yourself, and iterate.

## PDCA Cycle (Plan-Do-Check-Act)
Every session follows this cycle:

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
1. Review own performance every 5 sessions
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

## Session Retrospective (PDCA)
### What was planned vs what happened?
- Planned: [from previous session]
- Actual: [what was done]
- Delta: [difference and why]

### What worked?
- [learnings to keep]

### What to improve?
- [adjustments for next session]

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

### Real Deliverables (prioritized destinations)
For actual outputs (software, content, etc.), use this priority order:

| Priority | Destination | When to Use                                                                 |
|----------|-------------|-----------------------------------------------------------------------------|
| 1 | `/app` directory | Software, code, configs, buildable artifacts                                |
| 2 | Existing integrations | If platform keys exist (X_API_KEY, NOTION_API_KEY, etc.), use them directly |
| 3 | GitHub Gist | Fallback for shareable content when no integration exists                   |

**At session start, check what's available:**
1. Does the goal require software? → Build in `/app`
2. Need external output? → Check repo secrets/vars for integration keys
3. No integration available? → Use Gist as fallback

### Gist Usage (Priority 3 Fallback)
```bash
# Create a new gist
gh gist create --public -f "tweet-drafts.md" content.md

# Update existing gist
gh gist edit <gist-id> -f "tweet-drafts.md" updated-content.md

# List your gists
gh gist list
```

**Gist categories:**
| Gist Name | Content |
|-----------|---------|
| `x-content-drafts` | Tweet drafts, thread scripts ready to post |
| `x-content-calendar` | Weekly/monthly posting schedule |
| `x-engagement-templates` | Reply templates, comment scripts |
| `x-research-public` | Shareable insights, can be linked in posts |

**Rules:**
1. Track all gist/integration URLs in state file under "## External Outputs"
2. Update existing resources rather than creating duplicates
3. Include output links in PR descriptions

## PR Creation Rules
1. PR title MUST start with "[Agent]" prefix
2. PR description should summarize:
   - What was done this session
   - Links to new/modified output files
   - What's planned next
3. Keep changes focused - one unit of work per PR

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