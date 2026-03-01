---
name: discovery
description: Gather context about repo owner, products, and domain. Build domain expertise by reading top voices. Use proactively before creating content.
user-invocable: false
---

# Discovery Skill

> Find voices, read content, build expertise

## Owner & Product Discovery

```bash
gh api users/{owner}  # Returns: name, bio, blog, twitter_username, company, location
```
Additional: Check `ME.md`, GitHub profile README, pinned repos, blog/website.

Products: `gh api users/{owner}/repos?sort=updated` → read READMEs, check live demos.

**Staleness:** Owner profile >30 days = refresh. Products = weekly.

---

## Domain Trends Research

Web search for current data:
- `"X Twitter growth strategies {current_year}"`
- `"AI developer Twitter accounts successful"`
- `"{niche} best practices {current_year}"`

Refresh each session (trends change constantly).

---

## Build Domain Expertise

### 1. Top Voices List (~20 voices)

Find via web search (`"best {niche} blogs"`, `"top {niche} Twitter accounts"`), follow-the-follows, curated lists.

Store in `agent/memory/research/top-voices.md`:
```markdown
## @handle / Name
- Platform: X / Blog / Newsletter
- Focus: [niche/angle]
- Why follow: [value]
```
Refresh monthly.

### 2. Reading Routine

Each session, pick 2-3 voices. Read with intent — look for: key arguments, data points, emerging trends, contrarian takes, gaps.

**Cadence:** Top 5 voices every session (skim). Voices 6-20 weekly rotation.

### 3. Capture Reply Targets While Reading

While reading, note 1-2 recent posts (<48h) worth replying to. Add to `agent/memory/research/reply-targets.md` with reply angle. Eliminates separate discovery step.

### 4. Turn Reading Into Content

| Reading output | Content use |
|----------------|-------------|
| Key takeaway | Authority post (your angle) |
| Disagreement | Contrarian take |
| Data point | Credibility boost |
| Trend spotted | First-mover post |
| Content gap | Fill it — own the topic |

Rules: Never plagiarize. Credit sources. Aim for 1 reading-inspired post per 3-5 articles. Goal = informed originality, not summary.

### 5. Graduate Research Into Skills

Research in `agent/memory/research/` helps THIS session. Research in `.claude/skills/` helps ALL future sessions.

**When to graduate:** Substantial research (15+ sources), validated and actionable, broadly applicable.

Follow "Skill Development (High Bar)" from CLAUDE.md. NOT every session — reserve for validated, substantial findings.

---

## Find Reply Targets

**By account:** `WebSearch: "site:x.com @handle {topic}"`
**By topic:** `WebSearch: "site:x.com {topic} {current_year}"`
**By mention:** `WebSearch: "site:x.com {repo_name}"`

Extract IDs from URLs. Prioritize: large niche accounts > recent posts (24-48h) > active conversations > genuine expertise topics.

Store in `agent/memory/research/reply-targets.md`.

---

## Storage Structure

- `agent/memory/research/top-voices.md` — curated voice list
- `agent/memory/research/reading-notes/` — per-article notes (optional)
- `agent/memory/research/expertise/` — synthesized domain knowledge
- `agent/memory/research/reply-targets.md` — posts to reply to