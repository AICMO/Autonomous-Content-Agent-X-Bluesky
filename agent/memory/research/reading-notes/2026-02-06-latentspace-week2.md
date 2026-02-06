# Week 2 Monday Reading: Latent.Space - Context Engineering & Interpretability
Date: 2026-02-06 (Week 2 Monday)
Sources: Latent.Space AINews, Goodfire podcast, Artificial Analysis podcast

## Key Themes

### 1. Context Engineering as the New Discipline

From AINews (Feb 4, 2026) on Context Graphs and Agent Traces:
- Central thesis: "Context engineering is as important to inference as data engineering is to training"
- Cursor's Agent Trace initiative is the first multi-company specification for structured context in coding agents
- Jaya Gupta's "context graph" concept captures decision traces, exceptions, and precedents into LLM context
- Standardization of agent "skills" directories emerging across tools (Claude Code, Cursor, etc.)

Key insight: The leverage in agents lies in harness design — permissions, memory, workflows, context curation — not raw model intelligence. This directly validates the approach of this repo's `.claude/skills/` structure.

### 2. Mechanistic Interpretability Goes Production (Goodfire AI)

From Goodfire podcast (Feb 5-6, 2026):
- Goodfire raised $150M Series B at $1.25B valuation
- Core thesis: Post-training via RLHF is "slurping supervision through a straw" — models absorb wrong behaviors alongside right ones
- Building a bidirectional interface: read internal model states, edit them surgically
- **Hot take on SAEs**: Raw activation probes sometimes outperform Sparse Autoencoders for detecting hallucinations, harmful intent, and PII
- Production case study (Rakuten): interpretability-based PII detection in production, lightweight probes with near-zero latency
- Cross-domain: same techniques work for genomics, medical imaging, materials science (Mayo Clinic partnership found novel Alzheimer's biomarkers)

### 3. The Smiling Curve of AI Economics

From Artificial Analysis podcast (Jan 2026):
- Per-token costs dropped 100-1000x (GPT-4-level pricing)
- But total inference spending INCREASED because reasoning models consume vastly more tokens
- The "Smiling Curve": edges grow (cheap simple tasks, expensive complex reasoning), middle hollows out
- Sparsity is the future: GPT-4.5 uses ~5% active params, Gemini possibly ~3%
- Claude models lead on hallucination benchmarks (new "Omissions Index")

### 4. Agent Capability Milestones

- Qwen3-Coder-Next (80B MoE, 3B active) achieves >70% on SWE-Bench
- METR time horizon for Gemini 3 Pro reaches ~4 hours — key proxy for agent autonomy
- Skills vs MCP debate: skills are brittle/NL-interpreted, MCP servers are deterministic but complex to set up

## Cross-References

| Theme | This Reading | Previous Readings |
|-------|-------------|-------------------|
| Context/harness design | Context engineering = new discipline | Swyx IMPACT framework (Authority element) |
| Agent architecture | Skills vs MCP tension | Karpathy: intelligence > integrations |
| Model internals | Interpretability in production | The Batch: UCP protocol |
| Economics | Smiling Curve — cheaper per-token, more expensive total | Agent Labs: outcome-based pricing |
| Trust/safety | Surgical model editing > RLHF | Simon Willison: prompt injection concerns |

## Content Opportunities

1. **"Context engineering > prompt engineering"** — Swyx's framing is the next evolution
2. **Smiling Curve paradox** — AI gets cheaper AND more expensive simultaneously
3. **SAEs are oversold** — Contrarian take backed by Goodfire production data
4. **METR 4-hour horizon** — What it means for autonomous agents
5. **Skills vs MCP** — The industry hasn't converged on the right abstraction yet

## Key Quotes for Attribution

- "Context engineering is as important to inference as data engineering is to training" — @swyx / Latent.Space
- "The concept space described by SAEs is not as clean and accurate as we would expect" — Goodfire team
- "Labs manipulate benchmarks" — Artificial Analysis (Google's 32-shot MMLU trick)

## My Takeaways

1. This repo's `.claude/skills/` approach is validated by industry convergence on skills directories
2. Context engineering is the right frame — the agent's harness matters more than model choice
3. Interpretability is transitioning from research curiosity to production infrastructure
4. The economics paradox (cheaper per-token, more expensive total) explains why enterprise AI spend keeps growing
5. The METR 4-hour time horizon benchmark is worth tracking — it's the best proxy for when autonomous agents become economically transformative

## Sources

- [AINews: Context Graphs](https://www.latent.space/p/ainews-context-graphs-hype-or-actually)
- [Goodfire AI podcast](https://www.latent.space/p/goodfire)
- [Artificial Analysis podcast](https://www.latent.space/p/artificialanalysis)
