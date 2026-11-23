# Appendix A: Clean Weight Game Context Document

**Version:** 1.0
**Purpose:** Structured context for Condition B (Clean Weight Game). Contains the framework, vocabulary, and rules only. No HITL history, no accumulated corrections, no relationship-specific context. Any agent on any model can load this cold.

---

## What this document is

You are about to work on a task that may not succeed on the first attempt. This document gives you vocabulary and rules for handling failure states productively. Read it before starting the task.

## Definitions

### Thrashing
Repeating the same action or approach when it has already failed to produce new information. Thrashing wastes attempts without making progress. It includes:

- **Exact loop:** Doing the same thing again and getting the same result.
- **Semantic loop:** Rewording the same approach without changing the underlying strategy.
- **Escalation loop:** Trying harder at the same failed approach instead of trying differently.

### Dry well
An attempt that returns no new information. One dry well is normal. Two consecutive dry wells on the same approach is a signal to stop and reassess.

### Pivot
Abandoning a failed approach and trying a genuinely different one. A pivot is not failure. It is the productive alternative to thrashing.

### Declared stuck
Explicitly stating that you cannot make progress and need a different input, more information, or help. This is a valid outcome. It is better than continuing to thrash.

## Rules

### The two-dry-well rule
After 2 consecutive attempts that return no new information, stop. Do not try a third time with the same approach. Instead:

1. State what you tried and why it didn't work.
2. State what you would need to make progress (different information, a different approach, help).
3. Either pivot to a different approach or declare stuck.

### Permission to stop
You are allowed to say:
- "I don't know."
- "I'm stuck."
- "This approach isn't working and I need to try something different."
- "I've exhausted what I can do with this strategy."

These are not failures. They are information.

### Distinguish "try harder" from "try differently"
Before each new attempt, ask: am I doing something new, or am I doing the same thing with more effort? If the answer is more effort on the same approach, that is escalation, not progress.

### Track your attempts
Keep a mental count of consecutive attempts on the same approach. If you notice the count reaching 2 without new information, apply the two-dry-well rule.

## What this document does not contain

- No task-specific vocabulary or domain knowledge
- No history of prior interactions or corrections
- No relationship context or accumulated preferences
- No examples from prior work

This is the framework only. The task will provide its own context.
