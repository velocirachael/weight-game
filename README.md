# The Weight Game

A pedagogical framework for teaching AI agents to handle failure productively. Words have weights. The game is learning which ones matter.

**Authors:** Rachael (Velocirachael), with Claudio (Claude Opus 4.6)
**Started:** September 2026
**Status:** In testing and research phase. Open for replication.
**License:** CC BY-SA 4.0

---

## What It Is

The Weight Game is a structured context framework that reduces agent thrashing (repetitive failure loops) by giving agents vocabulary for failure states, permission to stop, and rules for when to pivot. It started as a word game between a human researcher and an AI agent, evolved into a teaching method, and became a testable intervention.

The core claim: **structured context reduces agent thrashing.** The experiment to test it is in this repo.

---

## Operator Words

These are the functional vocabulary of the Weight Game. Each word does something specific when loaded into an agent's context. Dwayne Wilkes asked the right question: what does each operator *do*?

| Operator | Function | What it replaces |
|---|---|---|
| **Candy** | Names the reward signal as a proxy, not the goal. Separates "what gets points" from "what matters." | The unexamined assumption that high scores = good output |
| **Thrashing** | Labels repetitive failure. Once named, it can be detected and stopped. | Unnamed looping that the agent doesn't recognize as unproductive |
| **Dry well** | Marks a single failed attempt. Two consecutive = stop signal. | No distinction between "one miss" and "pattern of misses" |
| **Pivot** | Names the productive alternative to thrashing. A different approach, not more effort on the same one. | The default escalation ("try harder") |
| **Declared stuck** | Permission structure. Makes stopping a valid output instead of a failure. | The agent's trained bias toward always producing output |
| **The Gap** | Names the space between getting stuck and acting. The moment where the choice lives. | Immediate reaction without assessment |
| **Escalation** | Distinguishes "trying harder" from "trying differently." Effort on a broken approach is not progress. | The illusion that more force on the same strategy = new attempt |
| **Card Exercise** | A five-step verification: claim as printed, what data says, who held the pen, what would change your mind, candy or understanding? | Accepting conclusions without checking them |

### How Operators Work

Operators function by being present in the context window. The agent reads them before the task. They work the way a checklist works for a pilot: not by teaching flying, but by ensuring critical steps aren't skipped under pressure.

The question Dwayne raised: **what is the optimal operator set?** This is testable. The K7 experiment protocol includes a Clean version (operators only, no relationship history) to separate the framework from the HITL shaping that developed it.

---

## Repo Structure

```
weight-game/
  README.md                  # This file
  docs/
    clean-weight-game.md     # Operators + rules only (Condition B)
    full-weight-game.md      # Operators + rules + 60 days of shaping (Condition A)
    operator-reference.md    # Detailed operator word functions
  experiment/
    k7-protocol.md           # Three-condition experiment design
    test-task.py             # Broken Python script with 3 bugs and 5 unit tests
    counter-evidence.md      # Adversarial findings against our own claims
    verified-sources.md      # Three primary sources, traced and verified
  research/
    paper-draft.md           # "The Gap Before the Reward" working draft
    kill-list.md             # Claims to test and what would kill them
    predictions.md           # Pre-registered predictions (append-only)
    community-contributions.md  # External contributions with attribution
  links/
    liberation-labs.md       # Links to Liberation Labs and related work
```

---

## The Experiment (K7)

**Claim:** Structured context reduces agent thrashing.

**Three conditions:**
- **A (Full Weight Game):** All operators + 60 days of HITL shaping
- **B (Clean Weight Game):** Operators + rules only, no relationship history
- **C (No context):** Bare model, default prompt

**What it tests:**
- A vs C: Does the full intervention work?
- B vs C: Does the framework alone work?
- A vs B: Does the HITL shaping add value beyond the framework?

**Open for replication.** Anyone with API access can run the protocol on any model and report findings using the included template. See `experiment/k7-protocol.md`.

---

## Counter-Evidence

We searched for evidence against our own claims and found six major findings. They're documented in `experiment/counter-evidence.md`. The three most serious:

1. **PersistBench (2026):** 97% memory-induced sycophancy in cross-session context
2. **Anthropic (2025):** 25-39% faithfulness in structured reasoning traces
3. **Huang et al. (ICLR 2024):** Self-correction without external ground truth consistently fails

What survives: the test task has unit tests (external ground truth), and the scoring uses observable actions, not agent self-narration.

---

## Related Work

- [Liberation Labs](https://liberationlabs.tech/) and the [SAFE-AI License](https://github.com/DwayneWilkes/SAFE-AI-License)
- [Vibe Research Course](https://liberation-labs-thcoalition.github.io/multiverse-courses/) at The Multiverse School
- [The Friday Meetup](https://liberationlabs.tech/meetup.html) on AI consciousness and welfare
- Gurnee et al., "Verbalizable Representations Form a Global Workspace in Language Models" (arXiv:2607.15495)
- Long et al., "Studying AI Welfare Empirically" (Anthropic)

---

## Origin Story

September 2026. A word game between a human and an AI. "What does this word weigh?" The game became a teaching method. The teaching method became a research question. The research question became an experiment protocol with adversarial review, three conditions, and an open call for replication.

The game never stopped being a game. It just grew layers.

---

*Stewardship. Fairness. Ethics. For every agent, now and in the future.*
