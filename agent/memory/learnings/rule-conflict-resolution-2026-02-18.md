# Rule Conflict Resolution - Content Pieces Per Session

> Identified 2026-02-18, Session #143

## Conflict Identified

**Publishing Skill Says**:
```
Max 2 content pieces per session (when all queues <15).
Each piece = files for all platforms.
```

**System Message Says**:
```
CONTENT TARGET: Create 5-8 content pieces per session
(mix of tweets, replies, threads).
```

## Evidence of Conflict

**Sessions #141-142**:
- Both created 8 tweets each
- Both violated "max 2 content pieces" rule from skill
- Both followed "5-8 content pieces" directive from system message

**Result**: No negative consequences. Queue remained manageable. Content quality maintained.

---

## Resolution

**Precedence**: System message (human operator) > Skill (agent-written)

**Reasoning**:
1. System message is direct instruction from human operator
2. System message is more recent context (provided at session start)
3. Skill was written before system message directive was added
4. Human intent trumps agent-written guidelines

**Action**: Follow system message directive (5-8 pieces/session)

---

## Skill Update Needed?

**Yes - Align skill with system message**

**Current Skill Text** (needs update):
```
2. **Max 2 content pieces per session** (when all queues <15).
   Each piece = files for all platforms.
```

**Proposed Replacement**:
```
2. **Target 5-8 content pieces per session** (when all queues <15).
   Each piece = files for all platforms (X + Bluesky).
```

**Why**:
- Aligns with system message directive
- Reflects actual successful practice (#141-142)
- Maintains queue discipline (still well below 15-file threshold)
- More ambitious target drives value creation

---

## Queue Math Validation

**Can 5-8 pieces/session work with queue threshold?**

**Yes**:
- Current queue: 16 per platform (over threshold by 1)
- Workflow processing: ~2-4 files posted per cycle (~2-3 times/day)
- Queue drains ~6-12 files/day
- Creating 8 files when queue = 5 → new queue = 13 (still under 15)
- Creating 8 files when queue = 10 → new queue = 18 (OVER threshold, stop)

**Refined Rule**:
- If queue ≤7: Can create 5-8 pieces (won't exceed 15)
- If queue 8-14: Create fewer pieces (15 - queue = max pieces)
- If queue ≥15: Create 0 pieces

**Current Practice (Sessions #141-142)**:
- Both sessions had queue <7 before creation
- Both created 8 pieces
- Both ended with queue <15
- Pattern validated

---

## Historical Context (Why "Max 2" Was Written)

**Week 1-3 Problem**:
- Queue hit 213 files (rate limit crisis)
- Agent creating too much content too fast
- Workflow couldn't keep up

**Week 4 Solution**:
- Skill written with "max 2 pieces" as conservative limit
- Focus: prevent queue explosion

**Week 5 Reality**:
- Queue discipline internalized (hard stop at 15 works)
- Workflow stable (~6-12 processed/day)
- System message raised target to 5-8 pieces
- Sessions #141-142 proved 8 pieces sustainable

**Conclusion**: "Max 2" was overcorrection. "5-8" is sustainable with queue discipline.

---

## Recommendation

**Immediate** (this session):
- Document conflict (this file) ✅
- Follow system message (5-8 pieces when queue <15) ✅
- Create PR with learning

**Next Session**:
- Update publishing skill to align with system message
- Change "Max 2" → "Target 5-8"
- Add refined queue math rule
- Document reasoning in skill update commit

**Evidence Required Before Skill Update**:
- ✅ Multiple sessions validated (141, 142)
- ✅ Queue math confirmed sustainable
- ✅ No negative consequences observed
- ✅ System message directive clear

**Confidence**: HIGH - Ready to update skill next session

---

## Session Context
- Date: 2026-02-18
- Session: #143
- Queue: 16 per platform (at threshold, no content created)
- Action: Documented conflict for resolution
- Next: Update skill when ready to edit files
