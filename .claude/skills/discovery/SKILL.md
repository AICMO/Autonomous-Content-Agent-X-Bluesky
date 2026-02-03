---
name: discovery
description: Gather context about repo owner, products, and domain. Use proactively before creating content.
user-invocable: false
---

# Discovery Skill

Gather context to make better decisions and create relevant content.

## Discover Repo Owner

```bash
gh api users/{owner}
# Returns: name, bio, blog, twitter_username, company, location
```

Additional sources:
- `ME.md` for links not in GitHub API
- Owner's GitHub profile README
- Pinned repositories
- Blog/website (from profile)

## Discover Owner's Products

1. Check pinned repos: `gh api users/{owner}/repos?sort=updated`
2. Read each repo's README for product descriptions
3. Look for live demos, documentation sites
4. Check owner's blog for product announcements

## Discover Domain Trends

For current goal, research:
- What works for similar accounts?
- Current trends in the niche
- Competitor analysis
- Platform algorithm changes

Use web search for fresh data:
```
WebSearch: "X Twitter growth strategies 2026"
WebSearch: "AI developer Twitter accounts successful"
```

## Discovery Cadence

| Type | Frequency | Purpose |
|------|-----------|---------|
| Owner profile | Once, update if stale | Accurate promotion |
| Products | Weekly | New launches, updates |
| Domain trends | Per session | Stay current |
| Competitors | Weekly | Learn from others |

## Staleness Check

Research gets stale. Check dates and refresh:
- Owner profile: Refresh if >30 days old
- Products: Refresh weekly
- Domain: Fresh each session

## Storing Discoveries

Store findings in `agent/memory/`. Organize as needed.

## Using Discoveries

Discoveries inform:
- **Publishing**: What to promote, how to frame
- **Content**: Topics that resonate with audience
- **Strategy**: What's working in the space