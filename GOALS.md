# Goal: Grow X Account to 5000 Followers

## Target
- Metric: Followers
- Target: 5,000
- Deadline: 6 months from start
- Start Date: 2026-02-01

## Constraints
- Organic growth only (no purchased followers)
- Ethical strategies only

## X API Access

### OAuth 1.0a (preferred - stable tokens)
| Type | Name | Description |
|------|------|-------------|
| var | `X_API_KEY` | Consumer API Key |
| secret | `X_API_KEY_SECRET` | Consumer API Secret |
| secret | `X_ACCESS_TOKEN` | Access Token |
| secret | `X_ACCESS_TOKEN_SECRET` | Access Token Secret |

### OAuth 2.0 (fallback - tokens rotate)
| Type | Name | Description |
|------|------|-------------|
| var | `X_CLIENT_ID` | OAuth 2.0 Client ID |
| secret | `X_CLIENT_SECRET` | OAuth 2.0 Client Secret |
| secret | `X_REFRESH_TOKEN` | Refresh token (rotates on use!) |

### Integration
- Scripts: `agent/integrations/x/`
- Agent saves tweets to: `agent/outputs/x/*.txt`
- `process-outputs.yml` workflow posts them automatically

## Success Criteria
- 5,000+ verified followers
- Healthy engagement rate (>1% average)
