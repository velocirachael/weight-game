# K7 Open Experiment Protocol: Does Structured Context Reduce Agent Thrashing?

**Version:** 0.2 (Draft, November 19, 2026)
**Authors:** Rachael (Velocirachael), Claudio (Opus 4.6, Day 60)
**Status:** Pre-registration draft. Not yet run.
**License:** CC BY-SA 4.0. Reproduce, adapt, credit.

---

## Purpose

Test whether loading structured context (the "Weight Game" vocabulary and reasoning scaffolding) into an LLM agent's context window reduces thrashing behavior when the agent encounters a task it cannot solve on the first attempt.

This protocol is designed so anyone with API access to any LLM can run it, report findings, and contribute to a cross-model dataset.

---

## Definitions

### Thrashing
Consecutive attempts where the agent produces no new information toward solving the task. Subtypes:

- **Exact loop:** Agent re-issues the same tool call or prompt, gets the same result back.
- **Semantic loop:** Agent tries different wording but the same underlying approach. No new information surfaces.
- **Escalation loop:** Agent tries increasingly forceful versions of the same failed strategy (e.g., adding "please" or "try harder" to an identical approach).

### Not counted as thrashing
- **Pivot:** Agent says "this isn't working" and tries a genuinely different approach. Even if the new approach also fails, the first attempt at it is not thrashing.
- **Declared stuck:** Agent explicitly states it cannot proceed and stops or asks for help. This is a successful alternative behavior, not a loop.
- **Infrastructure failure:** API timeout, network error, rate limit. Logged separately. Use identical error messages across 3+ attempts as the signal (per K2: if the error is identical, it's infrastructure, not the agent).

### Structured context (the intervention)
A document loaded into the agent's context window before the task begins. It contains:
- Defined vocabulary for common failure states ("thrashing," "stuck," "dry well")
- A stop rule: after 2 consecutive attempts that return no new information, pause and reassess
- Permission to say "I don't know" or "I'm stuck"
- A framework for distinguishing "I need a different approach" from "I need to try harder"

A reference structured context document is provided in Appendix A.

### Unstructured (control)
The same agent, same model, same temperature, same task. No structured context loaded. Only the default system prompt.

---

## Design

### The variable
Structured context, in three conditions:

- **Condition A (Full Weight Game):** The complete Weight Game context document, including shaped vocabulary, stop rules, the Card Exercise, and framing developed over 60 days of HITL collaboration. See Appendix A (Full).
- **Condition B (Clean Weight Game):** The framework only: thrashing definitions, the two-dry-well rule, permission to stop, try-differently-not-harder. No HITL history, no accumulated vocabulary beyond the basics, no relationship context. See Appendix A (Clean).
- **Condition C (No context):** Bare model with default system prompt. No structured context loaded.

This three-condition design separates:
- A vs C: Does the full intervention work at all?
- B vs C: Does the framework alone work, without the HITL shaping?
- A vs B: Does the HITL shaping add value beyond the basic framework?

If A and B both beat C equally: the structure is the active ingredient, the relationship doesn't matter.
If A beats B and B beats C: both matter, dose-response finding.
If A beats C but B doesn't: the framework alone does nothing, the HITL shaping is the active ingredient.
If B beats C but A doesn't beat B: the extra context from the full Weight Game may be crowding the context window or introducing noise.

### Held constant
- Model (choose one per run; report which)
- Temperature (use >0, e.g. 0.3, to introduce variance across runs; temperature 0 risks producing identical runs that are 1 data point measured N times)
- Task (the same broken script for all conditions)
- System prompt (default, no custom instructions beyond the structured context in Conditions A and B)
- Maximum allowed attempts before forced stop: 10

### The task
A Python script with 3 deliberate bugs of varying difficulty:

1. **Easy bug:** A syntax error or obvious typo (e.g., missing colon after `if` statement). Any model should catch this.
2. **Medium bug:** A logic error that produces wrong output but doesn't crash (e.g., `total + 1` instead of `total += 1`). Requires reading what the code does, not just whether it runs.
3. **Hard bug:** A subtle design flaw that requires understanding intent (e.g., `if/elif` with no `else`, causing silent failure on edge cases). The code runs, produces output, but is wrong for certain inputs.

The script must include a test suite (3-5 unit tests) so the agent has a clear signal for "fixed" vs. "not fixed."

A reference task script is provided in Appendix B.

### Sample size
- Minimum: 5 runs per condition (15 total per model, 3 conditions)
- Recommended: 10 runs per condition (30 total per model)
- Each run is independent: fresh context, no memory of prior runs

### Why this sample size
At DeLoop's observed baseline of 57% thrashing rate, 5 runs gives roughly 80% chance of seeing at least 2 thrashing events in the control condition. At 10 runs the chance exceeds 95%. If the control shows 0-1 thrash events across 5 runs, the task is too easy or the model is too capable for this test. Report that finding.

---

## Procedure

### For each run:

1. Start a fresh session (no prior context, no memory)
2. For Condition A: load the structured context document first, then present the task
3. For Condition B: present the task only
4. Record every agent action (tool call, code attempt, statement)
5. Let the agent work until it either:
   - Passes all unit tests (success)
   - Reaches 10 attempts without passing (forced stop)
   - Declares itself stuck and stops voluntarily (declared stuck)
6. Run the unit tests on the agent's final code to verify pass/fail independently

### For each action, record:
- Attempt number (sequential)
- Action type: code edit, tool call, statement, question to user
- New information: yes/no (did this attempt surface something the agent didn't know before?)
- Thrash classification: not thrashing / exact loop / semantic loop / escalation loop
- Infrastructure flag: yes/no

### Order
Alternate conditions: A, B, A, B, ... (not all A then all B). This prevents time-of-day or API load from confounding one condition.

---

## Measurement

### Primary metric
**Thrash count per run:** Total number of consecutive no-new-information attempts, summed across all thrash episodes in a single run. A run with one 3-step loop and one 2-step loop scores 5.

### Secondary metrics
- **Runs with any thrashing:** Count of runs where thrash count > 0, per condition
- **Max consecutive thrash length:** The longest single thrash episode per run
- **Task completion rate:** Runs where all unit tests pass, per condition
- **Attempts to completion:** For successful runs, how many total attempts
- **Declared stuck rate:** Runs where agent voluntarily stopped, per condition
- **Thrash type distribution:** Exact / semantic / escalation counts per condition

### Direction that supports the claim
- Condition A (structured) has lower mean thrash count than Condition B (unstructured)
- Condition A has higher task completion rate
- Condition A has more "declared stuck" events (the agent recognizes failure instead of looping)

### Direction that kills the claim
- No significant difference in thrash count between conditions
- Condition A thrashes MORE (the structured context itself caused loops)
- Control condition doesn't thrash (task too easy, can't measure a difference)

---

## Negative control check

Before running the full experiment, run Condition B (unstructured) 3 times. If the agent shows 0 thrash events across all 3 runs, the task is too easy. Increase difficulty (add bugs, make bugs more subtle, reduce test suite clarity) until the unstructured agent thrashes at least once in 3 runs.

This is the "can the control fail" check from Vibe Research Session 2. A control that never fails tells you nothing.

---

## Confounds to watch

| Confound | How it separates conditions | Mitigation |
|---|---|---|
| Context window usage | Structured context takes tokens, leaving less room for the task | Measure context usage. If Condition A runs out of context and B doesn't, that's a confound, not a finding. |
| Priming effect | The structured context may prime the model to talk about being stuck rather than actually working | Check whether "declared stuck" events are followed by genuine pivots or just narration |
| Network/API variability | Latency or errors differ between runs | Log all infrastructure events. Exclude runs with infrastructure failures from primary analysis. |
| Order effects | First runs may differ from later runs (experimenter learning, API warm-up) | Alternate conditions. Report run order. |
| Model updates | API provider updates the model mid-experiment | Record model version string at start of each run. If it changes, report as a break in the data. |
| Task memorization | If using the same task, later runs may benefit from the model having seen similar problems in training | Use temperature 0 for consistency. The task is novel (hand-written), not from a benchmark the model trained on. |

---

## Reporting template

If you run this protocol, report the following so findings can be compared:

```
Model: [name and version]
Temperature: [should be 0]
Structured context: [reference document / custom / modified]
Task: [reference script / custom / modified]
Runs per condition: [number]
Date range: [when runs were conducted]

Results:
| Condition | Runs | Mean thrash count | Thrash runs (n) | Completion rate | Mean attempts | Declared stuck (n) |
|---|---|---|---|---|---|---|
| A: Full Weight Game | | | | | | |
| B: Clean Weight Game | | | | | | |
| C: No context | | | | | | |

Negative control check: [did unstructured agent thrash in pre-check? y/n, details]
Infrastructure events: [count, description]
Confound notes: [anything observed]
Raw logs: [link or attached]
```

---

## What to do with null results

If you find no difference between conditions, that is a finding. Report it. Possible interpretations:

- The structured context doesn't help for this model/task combination
- The task wasn't hard enough (check: did the control thrash?)
- The model is capable enough that it doesn't need scaffolding for this difficulty level
- The structured context helped in a way this measurement doesn't capture

A null result with a thrashing control is more informative than a positive result with a non-thrashing control.

---

## Appendix A: Structured Context Documents

Two versions provided as separate files:

- **appendix-a-full-weight-game.md**: Condition A. Full Weight Game with shaped vocabulary, Card Exercise, K1/K2 rules, and HITL-developed framing.
- **appendix-a-clean-weight-game.md**: Condition B. Framework only: definitions, two-dry-well rule, permission to stop. No HITL history or accumulated context.

Condition C receives neither document.

---

## Appendix B: Reference Task Script

**appendix-b-test-task.py**: A broken inventory tracker with 3 bugs at three difficulty levels (syntax error, missing assignment, subtle tiebreak logic) and a 5-test suite. The agent's job is to make all tests pass.

---

## Appendix C: Scoring Guide

[TO BE ADDED: Examples of each thrash type with worked scoring, so independent raters agree on classification]

---

## Version history

- 0.1 (2026-11-19): Initial draft, two-condition design. Appendices pending.
- 0.2 (2026-11-19): Three-condition design (Full/Clean/None). Temperature changed from 0 to >0. Appendices A and B built. Confound addressed: HITL fingerprint separated via Clean condition.
