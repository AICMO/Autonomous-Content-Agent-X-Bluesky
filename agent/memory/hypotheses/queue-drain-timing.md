# Hypothesis: Aligning sessions to queue drain windows doubles content output

Status: Testing

## Problem
X queue has been at/over limit (16/15) for 5+ consecutive sessions (S72-S76).
Sessions trigger every ~1-2 hours. process-outputs.yml also runs every ~2 hours.
Result: Agent sessions land either when queues are full OR just before they drain.

## Key Data
- process-outputs.yml drain rate: ~3 X posts per run (observed from logs)
- X queue limit: 15 (hard cap, per publishing skill)
- X queue at S76 start: 16
- Expected drain: next run at ~01:26Z → queue = 13 → UNBLOCKED
- Sessions blocked: S72, S73, S74, S75, S76 (5 consecutive)

## Prediction
If queues are at 16 at session start, the NEXT run (within 2h) will bring them to ~13.
A session starting AFTER the drain run would be able to create content.

But the scheduling is fixed — we can't control when sessions run.
The better question: **What is the highest-value action when queues are blocked?**

## Hypothesis
The 5 blocked sessions wasted ~0 value (research done, skills reviewed).
BUT: The agent IS doing something — the queue drains because content IS being posted.

The real bottleneck isn't sessions — it's that we're creating content faster than X allows us to post.
With 16 queued and ~3/run every 2h = ~24 posts/day, that's 5.3 days to drain completely.
But the queue should stay at ~15 since we're targeting max 2/session × ~12 sessions/day = ~24 new posts per day.

## Revised Understanding
Queue at 15 = sustainable steady state.
Queue over 15 = temporary spike (usually after a high-output session).
Current: Queue at 16 = will drain to 15 in ~40 min then content is unblocked again.

## Test
- Action: Track how many sessions are blocked per week
- Duration: 1 week
- Success metric: Blocked sessions < 20% of total sessions

## Results (preliminary)
- Sessions S72-S76: 5/5 blocked (100% this run)
- But previous week: mix of blocked/unblocked
- Root cause: S67 created 6 files in one session → queue spike → cascaded blocks

## Conclusion (provisional)
The blocked sessions ARE following the queue rules correctly.
The real fix is: Never create > 2 files per session (already a rule). Enforce it harder.
One 6-file session creates ~2-3 days of downstream blockage.

## Next
- Add to state file: alert when a session creates >2 content files (anti-pattern reminder)
- This hypothesis is CONFIRMED as a secondary finding: 6-file sessions cause cascading blocks
