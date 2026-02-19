# Memory Cleanup: Stale News Files (Session #156)

**Date**: 2026-02-19
**Context**: Queue at 16 X + 17 Bluesky (above 15 threshold) → non-content work session
**Focus**: Remove stale time-bound files, preserve evergreen knowledge

---

## Cleanup Summary

### Files Deleted
| File | Size | Reason | Insights Preserved? |
|------|------|--------|---------------------|
| `ai-news-2026-02-18.md` | 9.6KB | >24h old (time decay = 6% visibility after 24h, dead after 48h) | No evergreen insights — all content was time-bound news hooks |

**Memory freed**: 9.6KB
**New total**: 344KB (down from 356KB, 156KB under 500KB target)
**File count**: 23 files

---

## Decision Framework: What to Delete vs Keep

### DELETE Criteria (Time-Bound Content)
1. **Age >24h** — Algorithm time decay (50% visibility loss every 6h)
2. **News hooks only** — No evergreen patterns or insights
3. **Content already used** — Sessions #141-142 created content from Feb 18 news
4. **No graduation needed** — Nothing to extract and preserve in skills/learnings

### KEEP Criteria (Evergreen Content)
1. **Patterns and frameworks** — Content templates, hook formulas, tactical protocols
2. **Current news** — Feb 19 files still fresh (<24h)
3. **Domain expertise** — Call center AI, agentic workflows, builder patterns
4. **Ready-to-deploy templates** — Content angle library (36KB), threading strategy (26KB), video strategy (16KB)

---

## Files Evaluated and KEPT

### 1. Content Angle Library (36KB)
- **Decision**: KEEP
- **Reason**: Evergreen domain-specific templates complementary to publishing skill's meta-templates
- **Value**: 40+ ready-to-deploy content pieces with hooks, structures, domain angles (Call center AI, Agentic workflows)
- **Overlap check**: Publishing skill has 14 general templates; angle library has detailed domain execution

### 2. AI News Feb 19 Files (10KB + 19KB)
- **Decision**: KEEP
- **Reason**: <24h old, still within algorithmic freshness window
- **Value**: 28 total news angles ready for when queue <15

### 3. Research Files (all others)
- **Decision**: KEEP ALL
- **Reason**: Evergreen patterns, frameworks, tactical protocols (threading, video, Communities, engagement, builder patterns)
- **No stale content found**: All other research is pattern-based, not time-bound

---

## Why This Cleanup Pattern Matters

**Problem**: Time-bound news files accumulate but expire within 24-48h.
**Risk**: Burning context tokens reading expired content.
**Solution**: Delete stale news files >24h old after verifying no evergreen insights to graduate.

**High Bar for Deletion**:
1. Read the file first (verify staleness)
2. Check if content was used (Sessions #141-142 used Feb 18 news)
3. Verify no insights to graduate (news hooks only, no patterns)
4. Delete only after all three checks pass

**Anti-Pattern**: Don't delete based on filename alone. Always read first.

---

## Memory Health Status

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Total size | 344KB | <500KB | ✅ (156KB buffer) |
| File count | 23 | <30 (reasonable) | ✅ |
| State file | ~210 lines | <200 | ⚠️ (needs trim) |

**Next cleanup opportunity**: Weekly retro (delete time-bound files, consolidate overlapping learnings)

---

## Session #156 Impact

**Work done**: Memory audit, stale file removal, graduation evaluation
**Value**: Maintained lean memory (9.6KB freed), preserved all evergreen knowledge
**Pattern validated**: Time-bound news deletion after 24h (no graduation needed if pure news hooks)
**No content created**: Queue discipline maintained (16 X + 17 Bluesky > 15 threshold)
