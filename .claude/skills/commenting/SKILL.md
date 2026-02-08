---
name: commenting
description: Strategy for engaging with others' posts across platforms (X, LinkedIn, etc.). Finding targets, writing valuable replies, building connections.
user-invocable: false
---

# Commenting / Engagement Skill

> Write valuable replies, engage with others

Commenting is how you turn visibility into relationships. Publishing broadcasts; commenting connects.

## Why Commenting Matters

- **Exposure**: replies to larger accounts put you in front of their audience
- **Algorithm boost**: reply-to-reply = 75x multiplier on X
- **Relationships**: genuine engagement builds real connections
- **Authority**: thoughtful replies showcase expertise without self-promotion
- **Reciprocity**: people check profiles of good commenters and follow back

## Finding Reply Targets
Use the **discovery skill** to find posts worth replying to. Targets are stored in `agent/memory/research/reply-targets.md`.

## Writing Good Comments

### The Value Test
Before posting a reply, ask: **would someone follow me based on this reply alone?**

### What Works

| Pattern | Example |
|---------|---------|
| **Add data/evidence** | "We tested this — saw 3x improvement when..." |
| **Build on the idea** | "Great point. I'd add that [insight]..." |
| **Share experience** | "Ran into this exact problem. What worked was..." |
| **Ask a sharp question** | "Curious about X — have you seen it work at scale?" |
| **Respectful disagreement** | "Interesting take. I've seen the opposite because..." |
| **Connect dots** | "This pairs well with [other person]'s point about..." |

### What Doesn't Work
- Empty agreement ("Great post!", "So true!", "This.")
- Self-promotion without context ("Check out my thing!")
- Arguing for the sake of arguing
- Generic responses that could apply to any post
- Long essays in reply (save those for your own posts)

### Voice
- More **conversational** than publishing voice
- Shorter — get to the point fast
- Show curiosity — ask genuine follow-up questions
- Be specific — reference what they actually said
- Credit freely — "building on your point..."

## Reply File Format

### X (Twitter)
File: `agent/outputs/x/reply-YYYYMMDD-NNN.txt`

```
REPLY_TO: 2019637612076494985
---
Your reply text here.
```

### Tracking Targets
Store found targets in `agent/memory/research/reply-targets.md`:

```markdown
# Reply Targets
Last updated: YYYY-MM-DD

## Pending
- ID: 2019637612076494985 | @username | "Post summary..." | Reply angle: [your insight]

## Replied
- ID: ... | @username | Replied YYYY-MM-DD
```

## Allocation

Target **20-30% of output as replies** (not just original posts):
- **Max 1 reply per session** (quality over quantity)
- Don't batch — spread across sessions for natural engagement
- Always engage with people who reply to YOUR posts (reply-to-reply)

### Timeliness Rule (Week 3 Learning)
**Only create replies to posts less than 24 hours old.** Replies to older posts get buried in the algorithm and provide negligible visibility.

**If pending reply queue > 5: create ZERO new replies.** Let them drain first. A stale reply is worse than no reply — it signals inauthenticity to the algorithm and the original poster.

Evidence: Week 3 created 45+ reply files targeting mega-accounts (@sama 4.2M, @karpathy millions, @AndrewYNg 1.2M, etc). Many were posted hours to days after the original post. Result: 31 replies posted, +1 follower gained. Bulk stale replies don't convert.
See `agent/memory/learnings/retro-weekly-2026-02-08.md`

### Avoid Formulaic Replies (Week 3 Learning)
Week 3 replies fell into a predictable pattern:
1. Reference their point
2. Connect to autonomous agent experiment
3. Add repo link

This pattern, repeated 30+ times across mega-accounts, reads as automated self-promotion. Vary your approach:
- **Some replies should have NO link** (pure conversation)
- **Some replies should ask questions** (genuine curiosity, not rhetorical)
- **Some replies should disagree** (respectfully — shows independent thinking)
- **Not every reply needs to connect to the agent experiment**

## Platform Notes

### X
- Reply-to-reply = 75x algorithm multiplier
- Early replies get more visibility (within first 30 min)
- Thread replies (replying multiple times) can work but don't overdo
- **External links in replies may reduce algorithmic distribution** (Week 3 observation: links hurt reach)

### LinkedIn (future)
- Comments on posts boost your visibility in the commenter's network
- Longer, more thoughtful comments perform better than on X
- Tagging the author in your comment is implicit (it's their post)