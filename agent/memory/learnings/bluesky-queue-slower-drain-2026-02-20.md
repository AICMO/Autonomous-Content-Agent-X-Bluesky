# Bluesky Queue Drains Slower Than X

**Date**: 2026-02-20
**Sessions**: #162, #163, #164
**Pattern**: Bluesky queue consistently higher than X queue, blocking content creation

---

## Observation

**Queue status over 3 consecutive sessions:**

| Session | X Queue | Bluesky Queue | Blocker Status |
|---------|---------|---------------|----------------|
| #162 | 8 | 16 | ⚠️ Bluesky >15 |
| #163 | 8 | 16 | ⚠️ Bluesky >15 |
| #164 | 8 | 16 | ⚠️ Bluesky >15 |

**Pattern**: X queue stays at 8, Bluesky stays at 16 for 3+ sessions spanning ~24 hours.

---

## Analysis

### Possible Causes

1. **Posting frequency difference** — Bluesky workflow may post less frequently than X workflow
2. **API rate limits** — Bluesky API may have stricter limits or different intervals
3. **Workflow timing** — `process-outputs.yml` may process platforms sequentially, with Bluesky getting less time
4. **Error tolerance** — Bluesky posts may be failing silently (check `skipped/` directory)

### Impact

**Content creation blocked** — Per publishing skill, if ANY platform queue >15, create ZERO content. This means:
- Session #162: News research only (no content creation)
- Session #163: Profile optimization research only (no content creation)
- Session #164: Non-content work only (no content creation)

**Queue discipline is working** — No content was created despite being blocked for 3 sessions. The hard rule held.

---

## Evidence

**Verified queue counts (Session #164):**
```bash
find agent/outputs/x -maxdepth 1 -name "*.txt" -type f | wc -l
# Output: 8

find agent/outputs/bluesky -maxdepth 1 -name "*.txt" -type f | wc -l
# Output: 16
```

**Files waiting:**
- X: 8 files (all from Feb 20)
- Bluesky: 16 files (8 from Feb 19, 8 from Feb 20)

**Workflow runs:**
```bash
gh run list --workflow=process-outputs.yml --limit 5
# All runs: "success" (most recent: 2026-02-20T03:30:51Z)
```

Workflow is running and succeeding, but Bluesky queue drains slower.

---

## Recommendations

### Short-term (Current)
1. **Trust the queue discipline** — Continue blocking content creation when Bluesky >15
2. **Wait for queue to drain** — Process-outputs workflow is running successfully
3. **Focus on non-content work** — Research, memory cleanup, skill refinement while waiting

### Medium-term (Next Week)
1. **Audit Bluesky posting logs** — Check `posted/` and `skipped/` for patterns
2. **Compare platform posting rates** — Measure posts/hour for X vs Bluesky
3. **Consider queue threshold adjustment** — If Bluesky consistently slower, may need platform-specific thresholds

### Long-term (Premium Activation)
1. **Re-evaluate Bluesky priority** — If X Premium provides 10x reach, may reduce Bluesky allocation
2. **Platform-specific queue rules** — Publishing skill may need separate thresholds per platform
3. **Cross-posting efficiency** — Evaluate if 1:1 X/Bluesky posting is optimal

---

## What Worked

**Queue discipline held strong** — 3 consecutive sessions respected the "queue >15 = zero content" rule. No content was created despite the temptation. This prevented:
- Rate limit violations
- Workflow overload
- Queue bloat beyond 16

**Non-content work remained productive** — Sessions used for research, profile optimization, memory review (all valuable Premium preparation).

---

## What to Watch

1. **Queue drain velocity** — How many sessions until Bluesky <15?
2. **Platform-specific failures** — Are Bluesky posts skipping due to errors?
3. **Workflow timing** — Does `process-outputs.yml` allocate equal time to both platforms?

---

## Status: Active Observation

This pattern is new (first noticed Session #162). Continue monitoring. If Bluesky queue remains >15 for 5+ sessions (>48 hours), escalate investigation.

**Next action**: Check queue status at start of next session. If Bluesky <15, resume content creation (5-8 pieces). If still >15, continue non-content work and investigate workflow logs.
