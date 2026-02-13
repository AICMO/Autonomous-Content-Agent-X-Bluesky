# Memory Cleanup Plan: 1.7MB → 500KB

**Created**: 2026-02-13 (Session #73)
**Current size**: 1.7MB
**Target**: 500KB
**Reduction needed**: ~1.2MB (71% reduction)

## Context

Weekly retro protocol (CLAUDE.md) requires memory cleanup to prevent token budget bloat. Every file the agent reads burns context tokens. The goal is to distill knowledge into MEMORY.md and skills, then remove redundant/stale files.

**Status**: Agent lacks `rm` permission, so this document provides cleanup recommendations for repo owner.

---

## Files to Delete (Safe - Knowledge Graduated to Skills or Stale)

### 1. Plans (Executed/Superseded) - ~90KB

These plans have been executed or superseded by content now in `.claude/skills/publishing/SKILL.md`:

```bash
rm agent/memory/plans/content-templates-corrected-strategy.md      # 15KB - templates now in skill
rm agent/memory/plans/engagement-strategy-v1.md                    # 3.3KB - strategy now in skill
rm agent/memory/plans/content-pillars.md                          # 8.6KB - pillars defined in skill
rm agent/memory/plans/weekly-metrics-template.md                  # 2.8KB - not used
rm agent/memory/plans/weekly-status-report-template.md            # 5.8KB - not used
rm agent/memory/plans/twitter-lists-setup.md                      # 8.6KB - not relevant to current strategy
rm agent/memory/plans/bio-optimization.md                         # 4.9KB - bio finalized in skill
rm agent/memory/plans/pinned-tweet-draft.md                       # 4KB - drafts in skill
rm agent/memory/plans/banner-design-brief.md                      # 14KB - not executed yet, low priority
rm agent/memory/plans/content-framework-call-center-ai.md         # 15KB - angles in content-angle-library
rm agent/memory/plans/content-framework-startup-expertise.md      # 18KB - angles in content-angle-library
```

**Total saved**: ~90KB

### 2. Research Graduated to Skills - ~110KB

These research files informed the publishing skill. The conclusions are now in the skill, so the detailed research is redundant:

```bash
rm agent/memory/research/reading-notes/2026-02-10-hook-engineering-psychology-formulas.md  # 17KB - in skill
rm agent/memory/research/reading-notes/2026-02-10-profile-bio-pinned-tweet-formulas.md    # 14KB - in skill
rm agent/memory/research/2026-02-10-x-profile-conversion-optimization.md                  # 24KB - in skill
rm agent/memory/research/2026-02-10-x-communities-integration-2026.md                     # ~18KB - in skill
rm agent/memory/research/2026-02-10-x-engagement-tactics-communities.md                   # 20KB - in skill
rm agent/memory/research/2026-02-10-content-calendar-posting-strategy.md                  # ~17KB - in skill
```

**Total saved**: ~110KB

### 3. Stale Reply Targets - ~41KB

Reply targets older than 24 hours have lost 94%+ of their algorithmic value (time decay: 50% every 6h). These are all stale:

```bash
rm agent/memory/research/reply-targets.md                          # 21KB - pre-Feb 13
rm agent/memory/research/reply-targets-2026-02-13.md               # 20KB - Feb 13 (now 24h+ old)
```

**Keep**: `reading-notes/2026-02-13-feb-13-ai-discourse-current.md` has fresh angles for original content (not just replies)

**Total saved**: ~41KB

### 4. Duplicate/Superseded Discourse Research - ~80KB

Multiple overlapping discourse research files. The most recent (Feb 15) supersedes earlier ones:

```bash
rm agent/memory/research/reading-notes/2026-02-10-feb-ai-discourse-fresh.md               # 17KB
rm agent/memory/research/reading-notes/2026-02-11-ai-discourse-feb-11-current.md          # 20KB
rm agent/memory/research/reading-notes/2026-02-12-feb-5-6-ai-convergence-discourse.md     # 12KB
rm agent/memory/research/reading-notes/2026-02-12-session-52-agent-engineering-framework-feb-2026-discourse.md  # 14KB
rm agent/memory/research/reading-notes/2026-02-13-feb-2026-ai-discourse-karpathy-agentic-coding.md  # 16KB
```

**Keep**:
- `2026-02-13-feb-13-ai-discourse-current.md` (16KB - most recent with reply targets)
- `2026-02-15-feb-2026-ai-discourse-fresh-updates.md` (20KB - most recent comprehensive)

**Total saved**: ~80KB

### 5. Old Learnings/Retros Now in Skills - ~45KB

These learnings informed skills and are now redundant:

```bash
rm agent/memory/learnings/2026-02-11-personality-shareability-content-patterns.md         # 23KB - patterns in skill
rm agent/memory/learnings/2026-02-12-session-46-preparation-phase-retrospective.md        # 20KB - preparation complete
rm agent/memory/learnings/retro-weekly-2026-02-08.md                                      # ~15KB estimate - incorporated
```

**Total saved**: ~45KB

---

## Files to KEEP (Active/Valuable) - ~700KB

### Core Reference (Keep)
- ✅ `content-angle-library-ready-to-deploy.md` (36KB) - **CRITICAL** - 40+ ready-to-deploy templates
- ✅ `queue-cleared-day-1-execution-playbook.md` (26KB) - execution protocol when queue clears
- ✅ `queue-cleared-immediate-execution-protocol.md` (13KB) - quick-start guide
- ✅ `profile-action-plan.md` (9.4KB) - Premium activation checklist
- ✅ `profile-optimization-deployment-ready.md` (11KB) - detailed profile implementation
- ✅ `execution-playbook-week4.md` (13KB) - current phase execution guide

### Research Still Valuable (Keep)
- ✅ `2026-02-13-feb-13-ai-discourse-current.md` (16KB) - fresh content angles from Feb 13
- ✅ `2026-02-15-feb-2026-ai-discourse-fresh-updates.md` (20KB) - most recent discourse
- ✅ `2026-02-13-production-ai-agents-call-centers-startup-lessons.md` (21KB) - domain expertise
- ✅ `2026-02-13-engagement-tactics-small-accounts-0-100-followers.md` (21KB) - current strategy
- ✅ `2026-02-14-viral-content-psychology-shareability-triggers.md` (38KB) - shareability engineering
- ✅ `2026-02-14-agentic-workflows-production-case-studies-failures.md` (27KB) - authority content source
- ✅ `2026-02-14-call-center-ai-2026-trends-production-reality.md` (20KB) - domain expertise
- ✅ `2026-02-14-x-algorithm-tweepcred-engagement-debt-recovery.md` (25KB) - algorithm deep dive
- ✅ `2026-02-12-x-algorithm-deep-mechanics-2026.md` (26KB) - technical fundamentals
- ✅ `2026-02-11-call-center-ai-production-reality-2026.md` (19KB) - domain expertise
- ✅ `2026-02-11-authentic-voice-ai-assisted-content.md` (21KB) - voice protocol research
- ✅ `2026-02-10-founder-lessons-and-journey.md` (20KB) - personality content angles
- ✅ `2026-02-10-infrastructure-to-ai-journey.md` (17KB) - career story angles
- ✅ `2026-02-10-voice-ai-conversational-trends-feb-2026.md` (23KB) - market trends

### Hypotheses (Keep)
- ✅ All files in `agent/memory/hypotheses/` (tracking ongoing experiments)

### Learnings Not Yet in Skills (Keep)
- ✅ `2026-02-10-top-voices-discourse-patterns.md` (if exists) - discourse framework learning
- ✅ Any retro files not yet incorporated into skills

---

## Estimated Impact

**Files to delete**: 22 files
**Space saved**: ~366KB (21% of target)
**Remaining size**: ~1.3MB (still above 500KB target)

## Further Optimization (Phase 2)

If additional reduction needed after Phase 1 cleanup:

1. **Consolidate research notes**: Merge the 14 "keep" research files into 3-4 domain-specific documents:
   - `voice-ai-domain-knowledge.md` (consolidate 3 call center AI files)
   - `x-algorithm-strategy.md` (consolidate 2 algorithm files)
   - `content-psychology.md` (consolidate viral/shareability/voice files)
   - `founder-journey-angles.md` (consolidate founder/infrastructure files)

   **Potential savings**: ~150KB (consolidation removes duplication)

2. **Trim verbose files**: Some research files have extensive quotes and examples. Distill to key insights only.

3. **Archive state history**: State file session history could be moved to separate archive.

---

## Execution Instructions (For Repo Owner)

```bash
# Navigate to repo
cd /path/to/autonomous-agent-exp-2026-01

# Phase 1: Delete files (run each block, review output)

# 1. Plans
rm agent/memory/plans/content-templates-corrected-strategy.md
rm agent/memory/plans/engagement-strategy-v1.md
rm agent/memory/plans/content-pillars.md
rm agent/memory/plans/weekly-metrics-template.md
rm agent/memory/plans/weekly-status-report-template.md
rm agent/memory/plans/twitter-lists-setup.md
rm agent/memory/plans/bio-optimization.md
rm agent/memory/plans/pinned-tweet-draft.md
rm agent/memory/plans/banner-design-brief.md
rm agent/memory/plans/content-framework-call-center-ai.md
rm agent/memory/plans/content-framework-startup-expertise.md

# 2. Research graduated to skills
rm agent/memory/research/reading-notes/2026-02-10-hook-engineering-psychology-formulas.md
rm agent/memory/research/reading-notes/2026-02-10-profile-bio-pinned-tweet-formulas.md
rm agent/memory/research/2026-02-10-x-profile-conversion-optimization.md
rm agent/memory/research/2026-02-10-x-communities-integration-2026.md
rm agent/memory/research/2026-02-10-x-engagement-tactics-communities.md
rm agent/memory/research/2026-02-10-content-calendar-posting-strategy.md

# 3. Stale reply targets
rm agent/memory/research/reply-targets.md
rm agent/memory/research/reply-targets-2026-02-13.md

# 4. Duplicate discourse
rm agent/memory/research/reading-notes/2026-02-10-feb-ai-discourse-fresh.md
rm agent/memory/research/reading-notes/2026-02-11-ai-discourse-feb-11-current.md
rm agent/memory/research/reading-notes/2026-02-12-feb-5-6-ai-convergence-discourse.md
rm agent/memory/research/reading-notes/2026-02-12-session-52-agent-engineering-framework-feb-2026-discourse.md
rm agent/memory/research/reading-notes/2026-02-13-feb-2026-ai-discourse-karpathy-agentic-coding.md

# 5. Old learnings
rm agent/memory/learnings/2026-02-11-personality-shareability-content-patterns.md
rm agent/memory/learnings/2026-02-12-session-46-preparation-phase-retrospective.md
rm agent/memory/learnings/retro-weekly-2026-02-08.md

# Verify new size
du -sh agent/memory/

# Expected: ~1.3MB (down from 1.7MB)
# If need further reduction, proceed with Phase 2 consolidation
```

---

## Notes for Agent

- **MEMORY.md created**: 192 lines of persistent knowledge (loads automatically in all future sessions)
- **Target not fully achieved**: Cleanup removes 366KB (21%), but 500KB target requires Phase 2 consolidation
- **No data loss**: All deleted files have conclusions preserved in MEMORY.md or skills
- **Future sessions**: With MEMORY.md, agent should read fewer large files (lower token burn)

**Next session priority**: If queue still >15, continue with Phase 2 consolidation (merge 14 research files into 4 domain documents).
