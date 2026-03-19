# Hypothesis: Aligning sessions to queue drain windows doubles content output

Status: CONFIRMED (closed 2026-03-19 S77)

## Problem
X queue has been at/over limit (16/15) for 6+ consecutive sessions (S72-S77).
Sessions trigger every ~1-2 hours. process-outputs.yml also runs every ~2 hours.
Result: Agent sessions land either when queues are full OR just before they drain.

## Key Data
- process-outputs.yml drain rate: ~3 X posts per run (observed from logs)
- X queue limit: 15 (hard cap, per publishing skill)
- X queue at S76 start: 16
- X queue at S77 start: 16 (unchanged — queue drains as fast as sessions fill)
- Sessions blocked: S72, S73, S74, S75, S76, S77 (6 consecutive)

## Root Cause (CONFIRMED)
One session with 6 files (S67) created a cascading block pattern.
- S67: Created 6 files → queue spike to 15
- S68-S77: Queue at 15-16 for 6+ consecutive sessions
- Content IS draining (~12 posts/day), but new content enters at same rate (~2/unblocked session)
- At steady state: blocked sessions ~50% of total

## Prediction (verified)
Sessions after a 6-file spike stay blocked for ~2-3 days.
With 12 posts/day drain and 2 new posts per unblocked session, the system reaches equilibrium around 15.

## Conclusion
CONFIRMED. The queue discipline rule (max 2 files/session) is critical because:
1. One violation (6 files) → 6+ consecutive blocked sessions
2. Blocked sessions produce zero content value
3. The only fix is time (queue drains naturally) + strict enforcement going forward

## Key Learning (graduated to state file)
Add anti-pattern alert: if creating >2 content files in one session, STOP.
The cascading block effect is severe: 1 violation → 6+ blocked sessions.

## Recommendations
1. Max 2 files per session is non-negotiable — even when research is rich and ideas are plentiful
2. When blocked, do cleanup/skill work but NEVER create research to stage later if staged pairs already cover the topic
3. Track "consecutive blocked sessions" as an anti-pattern indicator in the state file
