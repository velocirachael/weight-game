# Verified Citation Trail — K7: The Weight Game Reduces Thrashing

**Author:** Rachael (Velocirachael), with Claudio
**Date:** November 19, 2026
**Verification method:** Each source traced to arXiv primary, claims checked against abstract/paper content.

---

## Source 1: DeLoop

**Citation:** Tianle Chen, Pushkar Singh, Ketan Todi, et al. "DeLoop: Repeated Actions as Self-Supervision for Long-Horizon Agents." arXiv:2610.19376.

**What the paper says:** Qwen3-8B on CodeGym under history compression: 57.3% of tasks contained loops (agent re-issuing a tool call and getting the same observation back). DeLoop, a self-supervised method using direct preference optimization, reduced loop rate to 6.1%. Tasks also used roughly one-third as many steps with similar task success.

**What it supports for K7:** Thrashing (looping) is real, measurable, and reducible through intervention. Establishes baseline loop rates and proves an intervention can cut them.

**Verified:** Claim matches arXiv abstract and paper. Checked Nov 19, 2026.

---

## Source 2: IAL-Scan

**Citation:** Xinyi Hou, Shenao Wang, Yanjie Zhao, Haoyu Wang. "When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents." arXiv:2607.01641.

**What the paper says:** Static analysis tool tested on 6,549 LLM agent repositories. Flagged 74 potential infinite agentic loops, manual review confirmed 68 as real IAL failures across 47 projects. Precision: 91.9%.

**What it supports for K7:** Thrashing is widespread in deployed agent systems, not a lab curiosity. 47 real projects with confirmed loop failures. Establishes that thrashing is a systemic problem worth solving.

**Verified:** Claim matches arXiv abstract and paper. Checked Nov 19, 2026.

---

## Source 3: Chain-of-Thought Prompting

**Citation:** Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, Denny Zhou (Google Research, Brain Team). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." arXiv:2201.11903. Published at NeurIPS 2022.

**What the paper says:** Adding step-by-step reasoning examples to the prompt improves large model performance on arithmetic, commonsense, and symbolic reasoning tasks. PaLM 540B on GSM8K (math word problems): standard prompting 17.9%, chain-of-thought prompting 56.9%. Effect is an emergent property of model scale (helps at ~100B+ parameters).

**What it supports for K7:** Structured context in the prompt measurably changes model behavior and reduces errors. The Weight Game is a form of structured context (shaped vocabulary, reasoning scaffolding, shared definitions). If prompting structure improves reasoning at this scale, then the Weight Game's shaped context could reduce thrashing through the same mechanism. This paper establishes the principle; K7 tests whether it holds for thrashing specifically.

**Verified:** Claim matches arXiv abstract and NeurIPS paper. Key numbers confirmed from Table 1. Checked Nov 19, 2026.

---

## The Chain

1. Thrashing exists at known rates in LLM agents (Sources 1, 2)
2. Structured prompting measurably changes model behavior and reduces errors (Source 3)
3. The Weight Game is a form of structured prompting (our claim)
4. **K7 asks:** Does this specific form reduce this specific failure mode?

---

## Previously cited, still applicable elsewhere

- Hagendorff, Fabi, Kosinski. "Thinking Fast and Slow in Large Language Models." arXiv:2212.05206. Applicable to cognitive bias claims and System 1/System 2 framing, not to the thrashing reduction claim directly. Abstract does not contain the 5%-to-28% stat previously cited; needs deeper verification in full paper before reuse with that number.
