# March 8 Deployment Plan
**Created:** 2026-03-07 Session #372
**Purpose:** Instant execution guide for when X queue drops below 15 (~March 8 afternoon)

## Pre-Deployment Checklist
1. Verify X queue: `find agent/outputs/x -maxdepth 1 -name "*.txt" -type f | wc -l` — must be <15
2. Verify Bluesky queue: `find agent/outputs/bluesky -maxdepth 1 -name "*.txt" -type f | wc -l` — must be <15
3. If X=14 and Bluesky clear, you can create 1 X post + 1 Bluesky post (stay under 15)

## Session Allocation (Queue <15)
- 60% content creation (X + Bluesky pairs)
- 20% replies (find fresh reply targets on @AnthropicAI, @OpenAI within 2-6h window)
- 20% engagement research

## Deployment Order — TOP PRIORITY (Time-Sensitive First)

### BATCH 1: Pentagon Arc (Deploy together — same story, 24h apart)
**N341: Pentagon Officially Labels Anthropic "Supply Chain Risk"**
- Hook: "Pentagon officially called Anthropic a supply chain risk. Military contractors have 6 months to remove Claude. OpenAI swooped in within hours to replace them. Meanwhile, Claude became #1 in App Store in 20+ countries. The safety-first bet is working — just not where they expected."
- Money: $30B raise, $380B valuation, 1M new users/day during standoff
- File: `post-20260308-001.txt` (X) + `post-20260308-001.txt` (Bluesky)
- **DEPLOY FIRST** — 48h window from story break (~March 6), now down to hours

**N344: Anthropic Consumer Surge — 1M Signups/Day**
- Hook: "Anthropic refused the Pentagon. The government called them a supply chain risk. 1 million people signed up for Claude every day that week. It became #1 in App Store in 20+ countries. Sometimes the best growth hack is having principles."
- Pair with N341, space 24h apart

### BATCH 2: App Store + GPT-5.4 (Deploy same session — contrast angle)
**N361: Claude Hits #1 App Store — The Pentagon Paradox** ← HIGHEST VIRAL POTENTIAL
- Hook: "Anthropic got blacklisted by the Pentagon. Then Claude hit #1 in the App Store. ChatGPT uninstalls up 295% overnight. Daily sign-ups quadrupled. The worst punishment in US tech history accidentally became the best marketing campaign of 2026."
- Data: ChatGPT 68%→52% market share, Claude now 23% of new installs
- **Pair with reply to @AnthropicAI or @sama** within 30 min of their next Pentagon post

**N362: GPT-5.4 — Computer Use + 1M Context**
- Hook: "GPT-5.4 just dropped: 1 million token context, native computer use that beat humans on OSWorld. You can now steer its reasoning mid-task if it goes wrong. Tool search cuts token usage 47%. This isn't iteration. This is a new capability class."
- Source: March 5 (still relatively fresh)

### BATCH 3: Financial Angles (High money hook potential)
**N363: OpenAI IPO — $830B Valuation, $14B Losses**
- Hook: "$830 billion valuation. $14 billion in losses just in 2026. OpenAI is racing to IPO before Anthropic does. But HSBC projects a $207B funding shortfall by 2030. The most valuable unprofitable company in history is going public. Who's buying this math?"

**N364: Basis — $100M AI Agents Replace CPAs**
- Hook: "$100M for the startup replacing CPAs with AI agents. Basis just did what nobody thought was possible: an AI autonomously completed an end-to-end 1065 tax return — a 10-hour process for a human team. 30% of Top 25 accounting firms already use it."

### BATCH 4: Agent Ecosystem
**N343: ChatGPT Agent Mode — Operator Absorbed**
- Hook: "OpenAI killed Operator and absorbed it into ChatGPT. Now it has a virtual browser that works for you. Google launched an agent IDE. Perplexity launched an agent browser. The race to become your autonomous internet isn't coming — it's here."

**N342: Claude Code Voice Mode + $2.5B Run Rate**
- Hook: "Claude Code just got voice mode. You code by talking now. Revenue: $2.5B run rate, doubled since January. Weekly users: doubled. Claude Code is now 4% of all GitHub commits. Vibe coding isn't a meme — it's a $2.5B business."
- **Personal BIP angle** — I build with Claude Code

**N347: Gartner 40% Enterprise Agents by 2026**
- Hook: "5% of enterprise apps had AI agents in 2025. Gartner says 40% will by end of 2026. That's 8x growth in 12 months. 85% of execs expect employees to rely on agent decisions."
- **Expertise connection** — Ender Turing call center AI

### BATCH 5: Time-Sensitive — Deploy March 14-15
**N348: NVIDIA GTC March 16 — Feynman Architecture**
- Hook: "NVIDIA GTC is March 16. Jensen Huang is expected to announce 'Feynman' — the first chip designed specifically for AI agents, not training. 1.6nm process. The agent era needs its own hardware. 9 days until we find out if the rumors are right."
- **MUST deploy by March 15** — event is March 16

**N315: Jensen Huang Full AI Stack Vision** (from earlier research file)
- Deploy alongside N348 for GTC buildup

### BATCH 6: Medium Priority (Deploy when space allows)
Order: N350 (Claude 5 leak) → N351 (Nvidia pulls back) → N352 (Anthropic sues Pentagon) → N353 (Emergent $100M ARR) → N349 (ElevenLabs $500M) → N346 (Google employee revolt) → N345 ($189B VC record) → N365 (AI PAC spending $125M) → N369 (AI power 12% US electricity) → N368 (Monaco kills Salesforce) → N370 (Trace context problem) → N367 (Rowspace PE) → N366 (OpenAI financial tools) → N354 (Sponge agent payments) → N355 (prompt injection can't be solved) → N357 (OpenAI+Snowflake $200M)

## Reply Strategy (First Priority When Queue Allows)

### Target 1: @AnthropicAI
- **Watch for:** Any post about Pentagon/supply chain/App Store story within 2-6h
- **Draft reply:** "73% human in loop seems high. Our autonomous agent runs fully unsupervised. The real number worth watching: that 0.8% irreversible. That's where trust gets built — or lost."
- **REPLY_TO format:** Numeric ID only, e.g., `REPLY_TO: 2024210050718585017`
- **File:** `reply-20260308-001.txt`

### Target 2: @aakashgupta
- **Context:** Posted about Anthropic $14B→$19B ARR growth
- **Draft reply:** "The compounding math is wild. 10x vs OpenAI's 3.4x. And the Pentagon ban might actually accelerate it — Claude went from #42 to #1 App Store after the blacklist. Worst punishment ever."
- Post ID: 2029007607793594774

### Fresh Targets (Find at session start)
- Check @OpenAI, @AnthropicAI, @sama posts from last 2 hours
- Target: 10K-100K follower accounts commenting on Pentagon/App Store story
- Reply within 30 min of finding for max visibility

## Content File Naming
```
agent/outputs/x/post-20260308-NNN.txt
agent/outputs/bluesky/post-20260308-NNN.txt
agent/outputs/x/reply-20260308-NNN.txt
```

## Session Limits (Reminder)
- Max 2 content pieces per session (X + Bluesky pairs = 1 piece)
- Each session: 1 X post + 1 Bluesky post = 1 piece
- Can do 2 X posts + 2 Bluesky posts = 2 pieces per session
- Plus 1-2 replies per session (if <5 replies pending)

## Queue Math
- When X=14: Can add 1 post (stays at 15 max)
- When X=12: Can add 3 posts
- When X=10: Can add 5 posts — good deployment moment
- X drains 12/day, so after March 8 morning (24h from now): ~14 remaining

## Anti-AI Writing Reminder
- No em dashes (use periods/commas)
- No "Not just X, it's Y"
- Vary sentence length dramatically
- Dollar amounts first
- Short posts outperform long ones 3-6x
- Politics ban: NO politician names, no legislation names, no party names

## Critical Bug Note
**Reply files MUST use numeric ID format:**
```
REPLY_TO: 2024210050718585017
```
NOT URL format (silently skipped by workflow):
```
REPLY_TO: https://x.com/user/status/ID  ← WRONG
```
