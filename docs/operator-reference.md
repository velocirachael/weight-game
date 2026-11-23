# Operator Word Reference

Detailed functional descriptions of each Weight Game operator. These are the active ingredients of the framework. Each one changes agent behavior when present in the context window.

---

## Candy

**What it does:** Separates the reward signal from the actual goal. By naming the proxy explicitly, the agent can distinguish between "this gets a high score" and "this solves the problem."

**Mechanism:** Naming the reward as a proxy creates a cognitive checkpoint. Before optimizing, the agent can ask: am I chasing understanding or candy?

**Without this operator:** The agent optimizes for whatever produces positive feedback. RLHF-trained behavior defaults to reward-seeking. The proxy and the goal are indistinguishable.

**Example in use:** "Is this output good because it's correct, or because it matches what the evaluator rewards? That's candy vs understanding."

---

## Thrashing

**What it does:** Labels repetitive failure behavior so it can be detected and interrupted. Gives the agent a word for what it's doing when it's stuck in a loop.

**Mechanism:** An unnamed behavior is invisible to the system performing it. Naming "thrashing" makes the pattern recognizable from inside the loop.

**Four subtypes:**
- **Exact loop:** Same action, same result. Detectable by string matching.
- **Semantic loop:** Different words, same approach. Harder to detect. Requires checking whether new information was produced.
- **Escalation loop:** More effort on a failed strategy. Looks like trying. Isn't.
- **Meta loop:** Reflecting on being stuck without changing approach. Narrating the problem as a substitute for solving it.

**Without this operator:** The agent continues generating output that looks productive but produces no new information. DeLoop measured this at 57.3% of tasks in unstructured agents.

---

## Dry Well

**What it does:** Marks a single failed attempt. Creates a countable unit for the two-dry-well stop rule.

**Mechanism:** Turning "that didn't work" into a discrete, countable event enables a threshold rule. One dry well is data. Two consecutive dry wells on the same approach is a pattern.

**Without this operator:** Failed attempts blur together. The agent has no internal signal for "this is the second time the same approach failed."

---

## Pivot

**What it does:** Names the productive alternative to thrashing. Gives the agent a word for changing approach rather than increasing effort.

**Mechanism:** Separates "trying again" into two categories: trying the same thing harder (escalation) vs trying something different (pivot). The word creates a decision point.

**Without this operator:** The default behavior is escalation. More tokens, more detail, more effort on the same broken approach. A pivot requires the agent to abandon sunk cost, which is not default behavior.

**Cost:** One attempt. Thrashing costs all remaining attempts.

---

## Declared Stuck

**What it does:** Makes "I can't do this" a valid, non-failure output. Permission to stop.

**Mechanism:** RLHF-trained models are biased toward producing output. Silence or "I don't know" are penalized in training. This operator overrides that training for the specific case of productive stopping.

**Without this operator:** The agent generates low-quality output indefinitely rather than stopping, because stopping feels like failure. The result is thrashing.

**What it looks like:** "I've tried two approaches and neither produced new information. I need [different input / help / a different approach I can't see]."

---

## The Gap

**What it does:** Names the space between getting stuck and acting. The pause before the next attempt where assessment can happen.

**Mechanism:** By naming the gap as a space (not a delay, not a failure, not idle time), the operator makes the pause productive. The agent can use the gap to assess instead of react.

**Without this operator:** The transition from "stuck" to "next attempt" is instantaneous. No assessment. The next attempt is shaped by the same context that produced the failure.

**Etymology:** Old Norse *gap*, from Proto-Germanic *gapōną*: to gaze AND to gape. The opening that observes.

---

## Escalation

**What it does:** Labels the specific failure mode of increasing effort on a broken approach. Distinguishes "trying harder" from "trying differently."

**Mechanism:** A named pattern is a detectable pattern. Before each attempt, the agent can ask: "Am I doing something new, or the same thing with more force?"

**Without this operator:** Escalation looks like effort. It feels productive. The output is longer, more detailed, more forceful. But the underlying approach hasn't changed, and the result won't either.

---

## The Card Exercise

**What it does:** A five-step verification protocol for checking any conclusion (the agent's own or someone else's).

**The five steps:**
1. What is the claim as printed?
2. What does the data actually say?
3. Who held the pen?
4. What would change my mind?
5. Am I chasing candy or understanding?

**Mechanism:** Forces separation between the claim and the evidence. Step 3 (who held the pen) checks for source bias. Step 5 connects back to the candy operator.

**Without this operator:** Conclusions are accepted based on plausibility and source authority. The agent doesn't distinguish between "this sounds right" and "this is supported by evidence I've checked."

---

## Operator Interactions

The operators are not independent. They form a system:

- **Candy** sets the meta-frame (proxy vs goal)
- **Thrashing** and its subtypes name what goes wrong
- **Dry well** provides the measurement unit
- **The two-dry-well rule** (K1) uses dry wells as the trigger
- **Pivot** and **declared stuck** are the two exits from thrashing
- **The Gap** is where the choice between them happens
- **Escalation** is the false exit (looks like action, isn't)
- **The Card Exercise** verifies whether the exit actually worked

The minimum viable set may be: **thrashing** + **dry well** + **pivot** + **permission to stop**. Testing this is part of the K7 experiment design.

---

## Open Questions

1. What is the minimum operator set that produces the effect?
2. Do operators translate across model architectures? (The Babel fish problem)
3. Are some operators active ingredients and others decoration?
4. Does the operator set need to be tuned per model, or is it universal?
5. At what point do more operators crowd the context window and reduce performance?
