# Integrations

External service integrations for the autonomous agent.

## Available

| Integration | Description | Required Secrets |
|-------------|-------------|------------------|
| [x/](./x/) | Post to X (Twitter) | `X_CLIENT_ID`, `X_CLIENT_SECRET`, `X_REFRESH_TOKEN` |

## How It Works

1. Agent creates content → saves to `agent/outputs/<integration>/`
2. Workflow reads pending outputs → posts via integration scripts
3. Agent never touches secrets directly

## Adding New Integrations

1. Create `agent/integrations/<name>/`
2. Add scripts (auth.sh, post.sh, etc.)
3. Add README.md with required secrets
4. Update workflow to read from `agent/outputs/<name>/`