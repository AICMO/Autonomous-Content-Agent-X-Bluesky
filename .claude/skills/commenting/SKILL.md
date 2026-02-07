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
- 2-3 replies per session alongside 1-2 original tweets
- Don't batch — spread across sessions for natural engagement
- Always engage with people who reply to YOUR posts (reply-to-reply)

## Platform Notes

### X
- Reply-to-reply = 75x algorithm multiplier
- Early replies get more visibility (within first 30 min)
- Thread replies (replying multiple times) can work but don't overdo

### LinkedIn (future)
- Comments on posts boost your visibility in the commenter's network
- Longer, more thoughtful comments perform better than on X
- Tagging the author in your comment is implicit (it's their post)