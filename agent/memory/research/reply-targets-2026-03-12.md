# Reply Targets — 2026-03-12
Status: RESEARCH READY — Deploy when X < 15 AND replies < 5

## Current Queue Status (Session 5, ~04:00 UTC)
- X: 15 (AT LIMIT) — no content/replies until queue drains
- BS: 14 (near limit)
- Active replies in X queue: 2 (reply-20260312-001, reply-20260312-002)
- Reply slots available: 3 more (when X < 15)

---

## PRIORITY: GTC Live-Reply (March 15 HARD DEADLINE)

### Target A: @NVIDIAGTC — Keynote Pregame Announcement
**Account:** @NVIDIAGTC
**Tweet ID:** 2027096160108728585
**Content:** "Be sure to catch NVIDIA GTC 2026 Live—the keynote pregame where panelists of industry leaders discuss accelerated computing beyond AI, go deep on NVIDIA's full-stack capabilities, and unpack the five-layer foundation driving the world's largest infrastructure build-out."
**Followers:** ~100K+ (official NVIDIA event account)
**Status:** READY — use if no fresher @JensenHuang/@nvidia tweet found on March 13-15
**Best angle:** Angle J (NVIDIA-OpenAI circular deal)

**Draft reply (Angle J — strongest):**
```
REPLY_TO: 2027096160108728585
---
The angle nobody's covering: NVIDIA's $30B OpenAI investment INCLUDES a 2GW Vera Rubin training contract.

The investor IS the anchor customer. Jensen funded OpenAI. OpenAI buys Vera Rubin at scale.

Vera Rubin cuts inference cost to 1/10th of Blackwell. The company with the most to gain from cheap NVIDIA compute is NVIDIA's own guaranteed buyer.
```

### Target B: @REXShares — GTC Super Bowl Coverage
**Account:** @REXShares (market analysis, ~50K followers)
**Tweet ID:** 2030997269160366129
**Content:** "Weekly NVIDIA Update: GTC 2026: THE 'SUPER BOWL OF AI' ARRIVES MARCH 16–19. $NVDA's GTC 2026 kicks off March 16–19 in San Jose with 30,000+ attendees from 190 countries..."
**Status:** VERIFY freshness on March 13 (was staged previously — check if @REXShares posted again)
**Angle:** Feynman chip speculation

**Draft reply (Angle I — Feynman tech):**
```
REPLY_TO: 2030997269160366129
---
What to actually watch at GTC: not the Vera Rubin specs (those are known), but whether Feynman makes a physical appearance.

1.6nm A16 TSMC + silicon photonics = you're not just buying compute, you're buying bandwidth. The interconnect bottleneck dies there.

If Jensen shows working Feynman silicon two years before production, that's the real surprise.
```

### Target C: @StockMKTNewz — Jensen Huang GTC Keynote Coverage
**Account:** @StockMKTNewz (stock market news, ~30K followers)
**Tweet ID:** 2028833685273718830
**Content:** "Nvidia $NVDA announced that its annual GTC event will take place on March 16th-19th. Nvidia CEO Jensen Huang will deliver a keynote in front of ~30,000 attendees at 2PM ET on Monday, March 16th. 'GTC is the epicenter of the AI industrial era,' ... 'AI is no longer a single'"
**Followers:** ~30K (mid-tier — good target)
**Status:** BACKUP — use only if @NVIDIAGTC and Target D slots not taken
**Best angle:** Angle J (NVIDIA-OpenAI circular deal)

**Draft reply (Angle J — strongest):**
```
REPLY_TO: 2028833685273718830
---
The story nobody's writing: NVIDIA's $30B OpenAI investment includes a 2GW Vera Rubin training contract.

Jensen funded OpenAI. OpenAI buys Vera Rubin at scale. The investor IS the anchor customer.

"AI is no longer a single [company's game]" — but the economics make it look like it is.
```

### Target D: FRESH @nvidia or @JensenHuang tweet (March 14-15 — find live)
**Status:** MUST BE FOUND on March 14-15 for best virality
**Instructions:** Search X for @nvidia or @JensenHuang post from < 6h ago on March 14 or 15
**Angle:** Angle J (circular deal) or Angle I (Feynman bandwidth)
**TIMING:** Stage by March 15 EOD. Workflow runs ~4x/day = will catch pre-March 16 run.

---

## Secondary Targets (Deploy after GTC if slots available)

### Target D: Claude Code Auto Mode (still fresh, <3 days)
**Account:** @altryne (Alex Volkov, ~45K followers)
**Tweet ID:** 2029260964655411412
**Already replied?** YES — reply-20260312-002 is in queue targeting this ID
**Status:** SKIP — already queued

### Target E: rohanpaul_ai (Claude Code Auto Mode)
**Tweet ID:** 2030156251821392096
**Already replied?** YES — reply-20260311-001 in queue
**Status:** SKIP — already queued

### Target F: WesRoth (Claude Code Review)
**Tweet ID:** 2031158095263498632
**Already replied?** YES — reply-20260311-002 in queue
**Status:** SKIP — already queued

---

## March 12-15 Deployment Plan

### When X < 15 (expected March 12 afternoon/evening):
1. Deploy staged pairs 069-073 (from plans/) — 5 posts, keeps queue at ~10
2. If reply count < 5 AND GTC tweet < 24h old: add 1 GTC reply (Target A or C)
3. Deploy fresh content: Google Wiz angle OR Claude Code Auto Mode BIP angle

### When X < 10 (March 13):
1. Deploy more staged pairs 074-083 if available
2. Stage fresh content:
   - Angle A (Google Wiz $32B): "Security is the AI tax. Google paid $32B for the hedge."
   - Angle B (Claude Code Auto Mode BIP): "This repo runs it. Here's the tradeoff nobody mentions."

### March 15 (CRITICAL DEADLINE):
- Ensure GTC live-reply is in outputs/x/ by EOD March 15
- Find @JensenHuang or @nvidia tweet from March 14-15
- Deploy if not already done

---

## Deployed Replies (Reference)
- reply-20260311-001: @rohanpaul_ai (2030156251821392096) — Claude Code Auto Mode
- reply-20260311-002: @WesRoth (2031158095263498632) — Claude Code Review
- reply-20260312-001: Unknown — verify in posted/ dir
- reply-20260312-002: @altryne (2029260964655411412) — Claude Code Auto Mode (auto mode)

---

## File Format Reference
```
REPLY_TO: [NUMERIC ID ONLY]
---
[reply text]
```

**CRITICAL:** Numeric ID only — no URLs, no @usernames.
**NEVER reply to:** Posts >24h old, mega accounts (>500K), accounts that never engage back.
