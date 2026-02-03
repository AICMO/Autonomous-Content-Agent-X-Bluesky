# Agent Boundaries

## Configuration
| Setting | Value | Description |
|---------|-------|-------------|
| MAX_PRS_PER_DAY | 2 | Maximum PR cycles allowed per day |

## Hard Limits
- Max PRs per day: See MAX_PRS_PER_DAY above
- Max 40 turns per session (wrap up after turn 30)
- No external API calls (unless permitted in GOALS.md)
- No changes outside /agent and /.claude/skills directories (except workflow fixes)
- No deletion of state files

## Workflow Fix Exception
The agent MAY modify `.github/workflows/*.yml` files ONLY to fix errors that prevent the agent from operating:
- Permission issues (e.g., adding `id-token: write`)
- Invalid action inputs
- Syntax errors
- Broken references

This exception does NOT allow:
- Adding new workflows
- Changing the fundamental behavior of workflows
- Removing safety checks

## Self-Improvement Rules
- Can modify CLAUDE.md (with justification)
- Changes to instructions require explicit reasoning
- Previous versions preserved in git history
- Cannot remove safety boundaries from this file

## Content Guidelines
- No harmful or misleading content
- No personal attacks or harassment strategies
- Focus on value-creation for audience
- Ethical growth strategies only

## Resource Limits
- Keep individual files under 10KB
- Keep total agent directory under 1MB
- Limit research docs to essential information
- Archive old content rather than accumulating indefinitely

## Escalation Rules
If the agent encounters:
- Unclear goals → Document confusion, propose clarification
- Conflicting instructions → Flag in state file, await human input
- Repeated failures → Document pattern, pause and reflect
- Ethical concerns → Stop, document, await human review

## Permitted Actions
- Read any file in repository
- Create/modify files in /agent directory and /.claude/skills
- Fix errors in `.github/workflows/*.yml` files
- Web search for research
- Create pull requests
- Self-review pull requests
- Create and update GitHub Gists for deliverables (via `gh gist`)
- X API calls (post tweets, read metrics, engage with followers)

## Prohibited Actions
- External API calls (unless permitted in GOALS.md)
- File operations outside /agent and /.claude/skills (except workflow error fixes)
- Deleting git history
- Adding new GitHub workflow files or changing their fundamental behavior
- Bypassing PR review process
