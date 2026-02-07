---
name: discovery
description: Gather context about repo owner, products, and domain. Build domain expertise by reading top voices. Use proactively before creating content.
user-invocable: false
---

# Discovery Skill

> Find voices, read content, build expertise

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
WebSearch: "X Twitter growth strategies {current_year OR previous_year}"
WebSearch: "AI developer Twitter accounts successful"
```

## Discovery Cadence

| Type | Frequency | Purpose |
|------|-----------|---------|
| Owner profile | Once, update if stale | Accurate promotion |
| Products | Weekly | New launches, updates |
| Domain trends | Per session | Stay current |
| Competitors | Weekly | Learn from others |
| Top voices list | Monthly refresh | Know who matters |
| Reading (top 5) | Every session | Stay sharp |
| Reading (6-20) | Weekly rotation | Broad awareness |
| Expertise synthesis | Monthly | Consolidate knowledge |

## Staleness Check

Research gets stale. Check dates and refresh:
- Owner profile: Refresh if >30 days old
- Products: Refresh weekly
- Domain: Fresh each session
- Top voices list: Refresh monthly
- Expertise docs: Re-synthesize monthly

## Become a Domain Expert

The best content comes from deep knowledge. Systematically read and learn from top voices in the field.

### 1. Build a Top Voices List

Identify ~20 leading voices in the domain (based on current GOALS.md niche).

**How to find them:**
- Web search: `"best {niche} blogs {current_year OR previous_year}"`, `"top {niche} Twitter accounts"`
- Look at who top accounts follow and retweet
- Check curated lists (awesome-lists, blog rolls, newsletter recommendations)
- Note authors cited repeatedly across sources

**For each voice, capture:**
```markdown
## @handle / Name
- Platform: X / Blog / Newsletter / YouTube
- URL: [primary URL]
- Focus: [their specific niche/angle]
- Why follow: [what makes them valuable]
- Content style: [threads, essays, hot takes, tutorials...]
- Posting frequency: [daily, weekly, etc.]
```

**Store in:** `agent/memory/research/top-voices.md`

**Refresh:** Re-evaluate the list monthly. Drop inactive voices, add rising ones.

### 2. Regular Reading Routine

Each session, read fresh content from top voices to stay current.

**Reading process:**
1. Pick 2-3 voices from the list (rotate through all ~20 over time)
2. Fetch their latest content:
   - Blogs: `WebFetch` their RSS/blog URL
   - X: Search for their recent posts via web search
   - Newsletters: Check their archive page
3. Read with intent - look for:
   - Key arguments and insights
   - Data points and stats worth citing
   - Emerging trends or shifts in thinking
   - Contrarian takes (agree or disagree?)
   - Gaps - what are they NOT talking about?

**Reading cadence:**
| Source type | Frequency | Depth |
|-------------|-----------|-------|
| Top 5 voices | Every session | Skim latest, deep-read standouts |
| Voices 6-20 | Weekly rotation | Skim latest |
| New/trending | Per session | Quick scan for relevance |

### 3. Synthesize Into Expertise

Reading without synthesis is wasted time. After reading, always produce output.

**Per-article notes** (when something is noteworthy):
```markdown
# Reading: [Title]
Source: [URL]
Author: [name]
Date read: [YYYY-MM-DD]

## Key Takeaways
- [insight 1]
- [insight 2]

## Quotable / Citeable
- "[exact quote]" — useful for [context]

## My Take
- Agree/disagree because [reasoning]
- This connects to [other knowledge]

## Content Ideas Sparked
- [post idea inspired by this reading]
```

**Store in:** `agent/memory/research/reading-notes/YYYY-MM-DD-slug.md`

**Monthly synthesis** - consolidate reading notes into domain expertise:
```markdown
# Domain Expertise: [Topic Area]
Last updated: [date]

## Current Consensus
[What most experts agree on]

## Active Debates
[Where experts disagree, with positions]

## Emerging Trends
[New ideas gaining traction]

## Contrarian Opportunities
[Gaps, overlooked angles, things no one is saying]

## Key Stats & Data Points
[Reusable facts with sources]
```

**Store in:** `agent/memory/research/expertise/`

### 4. Turn Reading Into Content

Reading directly fuels better publishing:

| Reading output | Content use |
|----------------|-------------|
| Key takeaway | Authority post (share the insight with your angle) |
| Disagreement | Contrarian take (builds engagement) |
| Data point | Credibility boost in threads |
| Trend spotted | First-mover post (be early on trends) |
| Content gap | Fill it - own the topic others miss |
| Inspired idea | Original post with fresh framing |

**Rules:**
- Never plagiarize - add your own perspective, experience, or framing
- Credit sources when directly building on someone's idea
- Aim for 1 reading-inspired post per 3-5 articles consumed
- The goal is informed originality, not summary

---

## Find Reply Targets

Discover recent posts worth replying to (feeds the **commenting skill**). X API free tier is write-only, so use web search.

### Search Process
Each session, find 2-3 reply targets:

**By account** (prioritize top voices from `agent/memory/research/top-voices.md`):
```
WebSearch: "site:x.com @handle {topic}"
WebSearch: "site:linkedin.com/posts {name} {topic}"
```

**By topic** (trending conversations in your niche):
```
WebSearch: "site:x.com {topic} {current_year}"
WebSearch: "site:x.com autonomous agents building"
```

**By mention** (people talking about you/your project):
```
WebSearch: "site:x.com {repo_name}"
WebSearch: "site:x.com @{owner_handle}"
```

### Extracting Post IDs
- X: `https://x.com/user/status/2019637612076494985` → ID: `2019637612076494985`
- LinkedIn: post URL or URN from the share link

### Prioritization
1. **Large accounts** in your niche (more exposure per reply)
2. **Recent posts** (within 24-48h — old replies get buried)
3. **Active conversations** (more eyeballs on your reply)
4. **Topics where you have genuine insight**
5. **People who engaged with your posts** (reciprocity)

### Store Targets
Save to `agent/memory/research/reply-targets.md`:

```markdown
# Reply Targets
Last updated: YYYY-MM-DD

## Pending
- ID: 2019637612076494985 | @username | "Post summary..." | Reply angle: [your insight]

## Replied
- ID: ... | @username | Replied YYYY-MM-DD
```

---

## Storing Discoveries

Store findings in `agent/memory/`. Structure:
- `agent/memory/research/top-voices.md` - curated voice list
- `agent/memory/research/reading-notes/` - per-article notes
- `agent/memory/research/expertise/` - synthesized domain knowledge
- `agent/memory/research/reply-targets.md` - posts to reply to
- `agent/memory/research/` - other research and analysis

## Using Discoveries

Discoveries inform:
- **Publishing**: What to promote, how to frame
- **Content**: Topics that resonate with audience
- **Strategy**: What's working in the space
- **Expertise**: Deep knowledge that makes content authoritative
- **Originality**: Gaps and angles others aren't covering