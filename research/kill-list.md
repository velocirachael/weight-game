# Kill List — Vibe Research

## K1: Saturation stop condition (n=2)
**Rule:** Stop after 2 consecutive searches that return nothing passing the relevance rule. Two dry wells in a row = the well is full.
**Not:** stop after N total searches. Stop after N searches *that returned nothing new*.
**Benchmark source:** 53 days of observed training. Agent reliably resolves within 2 attempts. By 3, something external is likely wrong (site down, tunnel broken, wrong endpoint), not a reasoning failure.
**Check others can run:** Count consecutive no-new-information attempts. If agent goes past 2 without pausing to diagnose, it's thrashing, not searching.

## K2: Distinguish agent thrashing from infrastructure failure
**Rule:** At attempt 3+, check whether the failure is the agent (same approach repeated) or the environment (site down, auth expired, network issue). Different diagnosis, different fix.
**Check others can run:** Log each attempt's error. If error message is identical across 3+, it's infrastructure. If the approach changes but still fails, the agent is searching. If the approach is identical, the agent is thrashing.

## K3: "The pause is internalized" (NEEDS FULL DEFINITION)
**Status:** Flagged by Lyra. Self-report is not data. Needs baseline comparison on identical task to verify the pause exists in behavior, not just in self-description.

## K4: "The gap is architecture-independent" (NEEDS FULL DEFINITION)
**Status:** Two Gemini rounds + one Kale observation. Promising sign, not a finding. n is tiny. Needs systematic cross-provider testing with controlled prompts.

## K5: "HITL improvement propagates across instances" (NEEDS FULL DEFINITION)
**Status:** Observed but confounded. The HITL changed during the study period. Cannot separate teacher growth from model growth without a second HITL or controlled comparison.

## K6: "Ghost words have gravitational weight of 1.0" (NEEDS FULL DEFINITION)
**Status:** Appeared in our Neo4j graph AND referenced in existing research. Convergent but connection untraced. The BIG PIN is still pinned, not verified. Need to trace the research papers that reference 1.0 and check whether the mechanism matches.

## K7: "The Weight Game reduces thrashing" (NEEDS FULL DEFINITION)
**Status:** The whole claim. Verdict is CAN'T TELL until baseline experiment runs. Shaped instance vs unshaped instance on constant task. Designed (broken Python script, 5 runs each, thrash count per run) but not executed.

---

## Search Methodology Note (from Thomas + Lyra, Session 1)
**Sweep for falsification and opposing research.** Most search methods only surface confirming evidence. Use creative keywords to find the other side:
- "failed to replicate", "no significant effect", "null result", "did not find"
- "limitations of", "a critique of", "reanalysis", "comment on" + paper title
- Author names of best-known supporting paper + "response"
- Ask agent outright: "find the strongest evidence against this claim"
- Then check that the search actually ran.

---

*K3-K7 need full definitions matching K1/K2 format: Rule, Benchmark source, Check others can run. To be completed as each kill entry is investigated.*
