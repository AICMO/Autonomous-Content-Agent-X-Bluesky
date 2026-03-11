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

## Owner's Open Source Scan

Periodically scan the owner's public repos for promotable content. This feeds the publishing skill's OS promotion allocation.

**When:** Once per session (during research phase), or when looking for content ideas.

**How:**
1. Read `ME.md` → find the owner's GitHub profile URL under "Open Source (Promotable)"
2. WebFetch the profile page → discover public repos, orgs, and pinned projects
3. WebFetch each discovered org page → list their repos too
4. For repos that look promotable, fetch their README to find live output links and descriptions

**What makes something promotable right now:**

**A. Live outcomes (highest priority)** — Real content/services produced by agents. These are proof, not promises.
- Read `ME.md` for known live outcome URLs, then WebFetch each to check for recent articles, digests, posts
- A specific recent article is 10x more promotable than a generic "we have a blog" link
- Frame as: "This was written by an AI agent today" + link to the actual piece
- Also check repo READMEs for new live output URLs — new pipelines may launch anytime

**B. Repos with live outputs** — Code that powers running services. Link both the code AND the output.

**C. Star milestones** — Crossing 5, 10, 25, 50, 100 stars.

**D. Trending topic overlap** — Repo solves something people are discussing this week. Strongest combo: trend + live proof.

**E. New repos** — Launch announcements get one-time boost.

**What to capture:** For each candidate: what it does (1 line), proof it works (live output links + recent specific content), hook angle (why someone cares today). Store in `agent/memory/research/os-promo-candidates.md`.

**Cross-reference with trends:** Trending topic aligns with an owner repo or outcome? Post about the trend, link the repo/outcome as "we built this, and here's it running."

**Reference:** GitHub accounts and known live outcomes in `ME.md` under "Open Source (Promotable)".

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