# Autonomous Agent Experiment 2026-01

A self-managing agent that autonomously and iteratively works toward a given goal without human participation.

## Architecture

This system is **fully self-contained in GitHub** - no local servers, no external schedulers.

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│                               AUTONOMOUS LOOP                                     │
│                                                                                   │
│   ┌───────────────────────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐   │
│   │         TRIGGER           │───>│  AGENT   │───>│   PR     │───>│  AGENT   │   │
│   │SCHEDULE 8AM | State Change│    │  works   │    │ created  │    │ reviews  │   │
│   └───────────────────────────┘    └──────────┘    └──────────┘    └──────────┘   │
│                 ^                                                       │         │
│                 │                                                       v         │
│                 │             state change                        ┌──────────┐    │
│                 └─────────────────────────────────────────────────│  MERGE   │    │
│                             triggers next work                    │ (auto)   │    │
│                                                                   └──────────┘    │
└───────────────────────────────────────────────────────────────────────────────────┘
```

## How It Works

```
8 AM UTC ──> Work ──> PR ──> Review ──> Merge ───┐
                                                 │
              ┌──────────────────────────────────┘
              │
              v
         Limit reached? ──No──> Work ──> PR ──> Review ──> Merge ───┐
              │                                                     │
              Yes                     ┌─────────────────────────────┘
              │                       │
              v                       v
         Wait for              (repeat until limit)
         next 8 AM
```

1. **8 AM cron** starts the daily N*PRs working cycle (limiting pace to preserve tokens)
2. **Agent works** - think, research, code, deliver
3. **Agent creates PR** with changes (updates `agent/state/`)
4. **PR triggers** self-review workflow
5. **Auto-merge** when approved
6. **State change triggers** next work session immediately
7. **Repeat** until MAX_PRS_PER_DAY limit reached
8. **Wait** for next 8 AM to start again

## File Structure

```
/
├── .github/workflows/
│   ├── agent-work.yml         # Work session (8 AM cron + manual dispatch)
│   ├── agent-review.yml       # Self-review on PR creation
│   ├── agent-trigger.yml      # Chains sessions after PR merge
│   └── process-outputs.yml    # Posts outputs via integrations
│
├── agent/
│   ├── config.md              # Safety limits and settings
│   │
│   ├── state/                 # Created by agent
│   │   └── current.md         # Working memory
│   │
│   ├── memory/
│   │   ├── hypotheses/        # Ideas being tested
│   │   ├── learnings/         # Validated knowledge
│   │   └── research/          # Gathered intelligence
│   │
│   ├── output/
│   │   ├── plans/             # Strategic plans
│   │   └── reports/           # Analysis summaries
│   │
│   ├── outputs/               # Content to post externally
│   │   └── x/                 # Tweet files → process-outputs.yml
│   │       └── posted/        # Archived after posting
│   │
│   └── integrations/          # External platform scripts
│       └── x/
│           ├── post.sh        # OAuth 1.0a/2.0 posting
│           └── verify.sh      # Verify credentials
│
├── CLAUDE.md                  # Agent operating instructions
├── GOALS.md                   # Goal definition and X API setup
└── README.md
```

## Requirements

### Claude Code
- `CLAUDE_CODE_OAUTH_TOKEN` or `ANTHROPIC_API_KEY` secret
- Uses Claude Personal OAuth token (`claude setup-token`) or fallback to Anthropic API Key
- Details: https://github.com/anthropics/claude-code-action/blob/main/docs/usage.md

### Integrations (optional)
See `.claude/skills/publishing/SKILL.md` for platform credentials and publishing rules.

## PDCA Methodology

The agent follows the Plan-Do-Check-Act cycle:

1. **CHECK** - Review what was planned vs what happened
2. **ACT** - Adjust based on learnings
3. **PLAN** - Define next 2-3 concrete steps
4. **DO** - Execute ONE step per session

## Safety Boundaries

- Max PRs per day: configurable (default: 2)
- No changes outside `/agent` directory
- All changes go through PR review
- Previous versions preserved in git history
- Additional limits defined in `agent/config.md`

## Getting Started

### Prerequisites
- GitHub repository with Actions enabled
- `ANTHROPIC_API_KEY` secret configured
- Branch protection rules (optional, for auto-merge)

### Manual Trigger
To start the agent manually:
```bash
gh workflow run agent-work.yml
```

### Monitor Progress
- Check `agent/state/current.md` for current status (created after first run)
- Review PRs prefixed with `[Agent]`
- Track milestones in `GOALS.md`

## Configuration

### Configurable Settings
Edit `agent/config.md` to modify these settings:

| Setting | Default | Description |
|---------|---------|-------------|
| MAX_PRS_PER_DAY | 2 | Maximum PR cycles allowed per day |

The workflow automatically reads these values from the boundaries file at runtime.

### Modify Agent Behavior
Edit `CLAUDE.md` to change how the agent operates.

### Adjust Limits
Edit `agent/config.md` to modify safety constraints.

### Change Schedule
Edit `.github/workflows/agent-work.yml` cron expressions.

## License

MIT
