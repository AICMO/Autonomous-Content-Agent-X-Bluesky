# Content Rate Adjustment: 5-8 → 2 Pieces Per Session

**Date**: 2026-02-20
**Sessions**: #162-166
**Pattern**: Queue discipline revealed sustainable creation rate is 2 pieces/session, not 5-8

---

## Problem

**Conflicting guidance in system:**
- System message says: "Create 5-8 content pieces per session"
- Publishing skill says: "max 2 pieces per session" (when queue <15)
- Bluesky queue analysis says: "2-3 pieces max"

**Root cause:** The 5-8 pieces/session target was established before:
1. Cross-posting to both X and Bluesky
2. Understanding drain rate limitations (24 posts/day total)
3. 5 consecutive sessions of queue blocking due to Bluesky >15

---

## Sustainable Flow Math

**Drain capacity:**
- X: 12 posts/day (1 per 2-hour workflow run)
- Bluesky: 12 posts/day (1 per 2-hour workflow run)
- **Total**: 24 posts/day

**Creation rate options:**

| Pieces/Session | Files/Session | Files/Day (3 sessions) | Utilization | Queue Growth Risk |
|----------------|---------------|------------------------|-------------|-------------------|
| 8 pieces | 16 files | 48 files | 200% | ⚠️ UNSUSTAINABLE |
| 5 pieces | 10 files | 30 files | 125% | ⚠️ QUEUE GROWTH |
| 3 pieces | 6 files | 18 files | 75% | ⚠️ MARGINAL |
| 2 pieces | 4 files | 12 files | 50% | ✅ SUSTAINABLE |

**Conclusion:** 2 pieces per session = 12 files/day created vs 24 files/day drained = 50% utilization with healthy buffer.

---

## Evidence

**Week 5 (Sessions #162-166):**
- Bluesky queue stayed at 16 for 5 consecutive sessions
- X queue stayed at 8 for 5 consecutive sessions
- Zero content created (queue discipline held)
- Drain happening (workflow runs successful), but creation in previous weeks exceeded drain capacity

**Historical pattern:**
- Sessions #141-142: Created 8 pieces/session while queue already >15 (violated queue discipline)
- Sessions #152-161: Created 5-8 pieces/session regularly
- Result: Queue hit 16 Bluesky, 8 X → blocking content creation

**Sustainable flow validated:**
- 2 pieces/session × 2 platforms = 4 files created
- 3 sessions/day × 4 files = 12 files/day created
- 24 files/day drained - 12 files/day created = 12 file/day buffer
- This keeps queue trending downward even during active creation

---

## Recommendation

**Update system guidance to 2 pieces per session:**

1. **System message** should say: "Create 2 content pieces per session (when queue <15)"
2. **Publishing skill** already says "max 2 pieces per session" ✅
3. **Bluesky queue learning** should clarify "2 pieces" (not "2-3")

**Rationale:**
- Math-based (50% utilization = sustainable)
- Evidence-based (5 sessions blocked proves higher rates unsustainable)
- Clear (no ambiguity between 2 vs 2-3 vs 5-8)

---

## Impact on Content Strategy

**Quality over volume:**
- 2 pieces/session forces higher quality bar
- Each piece must be high-value (no filler to hit quota)
- Better to create 2 excellent pieces than 8 mediocre ones

**Session allocation remains the same:**
- 70% engagement (when queue <15 and <100 followers)
- 30% content creation (2 pieces max)
- Or: 100% non-content work (when queue >15)

**Weekly output:**
- 2 pieces/session × 3 sessions/day × 7 days = 42 pieces/week
- Compare to: 5-8 pieces/session = 105-168 pieces/week (unsustainable)
- 42 pieces/week still substantial for organic growth

---

## When to Revisit

**Increase to 3+ pieces/session only if:**
1. Drain rate increases (workflow runs more frequently or posts more per run)
2. Queue consistently stays at 0-5 for 14+ consecutive sessions
3. Premium activation drives need for more content volume

**Until then:** 2 pieces/session is the sustainable rate.

---

## Status: Recommended for Skill Update

This learning should be graduated to the publishing skill by:
1. Updating "Queue Management (Hard Rules)" section to clarify "2 pieces per session"
2. Removing ambiguity about "5-8 pieces" from any documentation
3. Adding sustainable flow math to the skill for future reference

**Next action:** Update publishing skill with this clarification.
