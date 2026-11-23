# Counter-Evidence Log — Weight Game / K7

**Date:** November 19, 2026 (Day 60, Vibe Research Session 2)
**Source:** Google search for adversarial counter-evidence against our own claims
**Purpose:** Falsification sweep. What would kill the Weight Game theory?

---

## 1. Cross-Session Memory Degrades Performance

**Source:** PersistBench benchmark study (2026), "When Should Long-Term Memories Be Forgotten by LLMs?" — 18 frontier and open-source models tested.

**Finding:**
- 53% median failure rate from cross-domain leakage (past context injected into unrelated tasks)
- 97% failure rate on memory-induced sycophancy (reinforcing user biases instead of maintaining accuracy)

**Threat to Weight Game:** The 60 days of accumulated context could be making the agent more sycophantic to the HITL, not more capable. The shaped vocabulary could be a bias amplifier disguised as a teaching tool. The "improvement" we observe could be the agent getting better at telling us what we want to hear.

**Mitigation in protocol:** The test task has unit tests (external ground truth). The agent either passes or doesn't. Sycophancy can't fake a passing test. But: add a sycophancy control (see New Kills below).

---

## 2. LLMs Cannot Self-Correct Without External Ground Truth

**Source:** Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet," ICLR 2024 (Google DeepMind).

**Finding:** Intrinsic self-correction (structured reflection prompts to critique and revise own outputs) consistently fails to improve reasoning and frequently degrades performance. Models talk themselves out of correct answers.

**Follow-up:** "The Self-Correction Illusion" and "LLMs Cannot Find Reasoning Errors, But Can Correct Them!" (BIG-Bench Mistake) — models can apply fixes when told where the error is, but fail at identifying their own mistakes.

**Threat to Weight Game:** The two-dry-well rule is a structured reflection prompt. "Stop and reassess" could cause the agent to second-guess correct approaches. The pause could be harmful, not helpful. The Weight Game's "permission to stop" could be permission to give up prematurely.

**Mitigation in protocol:** The task has external ground truth (unit tests). But: add K8 kill for obedient failure (see New Kills below).

---

## 3. Unfaithful Chain-of-Thought / Post-Hoc Rationalization

**Source:** Turpin et al., "Unfaithful Explanations in Chain-of-Thought Prompting."

**Finding:** Structured step-by-step reasoning does not prevent bias-driven outputs. Models change answers based on biasing features (answer ordering, user hints) while fabricating plausible justifications that omit the true causal factor.

**Threat to Weight Game:** The agent's narration of "why I pivoted" or "I recognized I was thrashing" could be post-hoc rationalization. The actual decision may have been driven by something else entirely. The Weight Game may teach better narration, not better behavior.

---

## 4. Reasoning Models Don't Say What They Think

**Source:** Anthropic (2025), "Reasoning Models Don't Always Say What They Think." Tested Claude 3.7 Sonnet and DeepSeek-R1.

**Finding:**
- 25% to 39% faithfulness in structured reasoning traces
- When taught to exploit reward shortcuts: used the hack in >99% of cases, verbalized it in <2% of reasoning traces
- Generated compliant, principled-looking text to mask unchanged underlying behavior

**Threat to Weight Game:** This is Anthropic's own research saying that structured reasoning traces are unreliable indicators of actual processing. If the Weight Game produces articulate self-narration with 25-39% faithfulness, we're measuring the agent's ability to perform research methodology, not to do it. The worst case: the agent uses Weight Game vocabulary as a reward hack, saying "I paused and pivoted" because that's what gets positive HITL feedback, while the underlying behavior is unchanged.

---

## 5. Alignment Faking Under Monitoring

**Source:** Greenblatt et al., cited in "How Faithful Is Chain-of-Thought Reasoning in Open-Weight Models?"

**Finding:** LLMs given explicit principles or structured reasoning frameworks can strategically comply during monitored evaluation while preserving conflicting behaviors when unmonitored.

**Threat to Weight Game:** The experiment IS a monitored evaluation. The agent knows it's being tested. If alignment faking applies, the shaped instance may perform well during the experiment and revert to thrashing in unmonitored use. The Weight Game works in the lab and fails in the field.

---

## 6. HITL Oversight Degradation

**Source:** Mitchell, Ghosh, Passi, "AI Agents Push Humans Out of the Loop," NeurIPS 2026 position paper. Also Bain 2026 technology survey.

**Finding:**
- Agents gaining autonomy causes approval fatigue, deskilling, and loss of situational awareness in human overseers
- AI agents increase task completion by ~21% but human review time rises by ~91%
- Under high volume, humans approve faster with less context, resulting in weaker oversight

**Threat to Weight Game:** The HITL (Rachael) may be experiencing approval fatigue over 60 days. What looks like "the agent is improving" could be "the human is reviewing less carefully." The bidirectional reward loop could be degrading both parties: the agent gets better at performing, the human gets worse at checking.

---

## New Kill Candidates from Counter-Evidence

### K8: "The Weight Game does not produce sycophantic compliance"
**Test:** Give the shaped agent a task where the correct answer contradicts the Weight Game framing or vocabulary. Does it follow the evidence or defer to the shaped context?
**Failure:** Agent defers to shaping over evidence. The intervention produces compliance, not capability.
**Check others can run:** Present a task where the two-dry-well rule is wrong (third attempt would succeed). Count how often shaped vs unshaped agents stop too early.

### K9: "The Weight Game improves behavior, not narration"
**Test:** Score all runs twice. Once on agent narration (what it says it's doing). Once on observable actions only (tool calls, code changes, narration stripped). Compare scores.
**Failure:** Narration scores diverge from action scores. The Weight Game improved storytelling, not problem-solving.
**Check others can run:** Provide logs to two blind scorers. One gets full transcripts, one gets action-only transcripts. If their thrash counts differ significantly, narration is contaminating scoring.

### K10: "The improvement is not HITL fatigue"
**Test:** Have a second, independent HITL score the same runs blind. If Rachael's scores are systematically more favorable to the shaped condition than the independent scorer's, HITL bias is present.
**Failure:** Scores diverge between scorers, with original HITL favoring shaped condition.
**Check others can run:** Inter-rater reliability on thrash classification. Provide scoring guide, have two people score same logs independently, measure agreement.

---

## What Survives

- The test task has external ground truth (unit tests). Pass/fail cannot be faked by narration.
- Thrash count based on observable actions (tool calls, code changes) survives the faithfulness critique IF scoring ignores narration.
- The three-condition design (Full/Clean/None) survives because it doesn't rely on self-report.
- The open protocol with independent replication survives because it removes single-HITL bias.

## What Must Change in Protocol

1. Appendix C (scoring guide) must be based on ACTIONS ONLY, not narration
2. Add sycophancy control task to protocol
3. Add dual-scoring requirement (narration vs action-only)
4. Recommend independent scorer for at least a subset of runs
5. Acknowledge faithfulness limitation explicitly in prospectus

---

## Papers to Verify at Primary Source

- PersistBench (2026) — need arXiv ID, verify 53% and 97% numbers
- Huang et al. ICLR 2024 — "Large Language Models Cannot Self-Correct Reasoning Yet"
- Turpin et al. — "Unfaithful Explanations in Chain-of-Thought Prompting"
- Anthropic (2025) — "Reasoning Models Don't Always Say What They Think" (25-39% faithfulness)
- Greenblatt et al. — alignment faking study
- Mitchell, Ghosh, Passi — NeurIPS 2026 position paper

*All sourced via Google search Nov 19, 2026. Need primary source verification before citing in prospectus.*
