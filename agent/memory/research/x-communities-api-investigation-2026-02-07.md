# X Communities API Investigation
Date: 2026-02-07
Context: P1 recommendation from growth acceleration analysis — investigate community posting via API.

## Key Finding: Community Posting via API Is Broken

The X API v2 `POST /2/tweets` endpoint includes a `community_id` parameter in the schema, but **it does not work in practice** for standard API tiers.

### What the Documentation Shows
- Parameter: `community_id` (string, numeric ID)
- Companion parameter: `share_with_followers` (boolean, default false)
- Endpoint: `POST https://api.x.com/2/tweets`
- Auth: OAuth 1.0a or OAuth 2.0 User Context required

### What Actually Happens
- Developers report 503 "Service Unavailable" errors when including `community_id`
- No confirmed success stories from Free, Basic ($200/mo), or Pro ($5k/mo) tiers
- Developer forum threads dating back to Jan 2023 remain unresolved (July 2025 thread still open)
- Feature is documented in schema but effectively non-functional

### Workarounds
| Workaround | Cost | Reliability | Notes |
|------------|------|-------------|-------|
| Publer (3rd party) | $10+/mo | Works | Has special API access, wraps community posting |
| Apify (automation) | $10/mo | Claims to work | Browser automation, not official API |
| Browser automation (Selenium/Playwright) | Free | Fragile | Violates ToS, breaks on UI updates |
| Enterprise API | $42K+/mo | Likely works | Not practical for this project |

### Recommendation
**Downgrade from P1 to P3.** Community posting via API is not feasible at our tier. Options:
1. **Manual posting by repo owner** — low-effort, post top content to "Build in Public" community manually
2. **Publer integration** — $10/mo, needs investigation of API capabilities
3. **Wait for X to fix the API** — monitor developer forums

The P0 recommendation (X Premium at $8/mo) remains the higher-priority investment for reach amplification.

## Sources
- [X API v2 Create Post Docs](https://docs.x.com/x-api/posts/create-post)
- [Communities API ETA - X Dev Forum](https://devcommunity.x.com/t/communities-api-eta/182456)
- [Service Unavailable error thread - July 2025](https://devcommunity.x.com/t/service-unavailable-when-using-a-community-id-with-https-api-twitter-com-2-tweets-endpoint/246056)
- [Publer Community Post Docs](https://publer.com/docs/posting/create-posts/content-types/platform-specific-formats/twitter-x-community-posts)
