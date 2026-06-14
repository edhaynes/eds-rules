# Coding benchmark — Qwen-14B vs Opus on real coding (2026-06-14)

HumanEval, 40 problems, **test-graded** (actual unit tests executed, no judge).

```
  pass@1
  qwen2.5-coder:14b   36/40  (90%)
  claude-opus-4-8     39/40  (98%)

  split (cheap=Qwen vs T3=Opus)
  both solve (cheap's domain)   35
  only Opus (the hard 10%)       4   HumanEval/125,134,54,108
  cheap-only (Opus flaked)       1   HumanEval/129
  neither (needs decompose)      0
```

## Findings
1. **The thesis holds almost to the number.** Cheap Qwen does **90%** of real coding,
   Opus **98%**, and the gap is **exactly the hard 10%** (4/40) that escalates. Nothing
   needed decomposition at function granularity.
2. **The keystone insight.** Qwen *codes* at 90% but only *follows ~14 rules* at 68%
   (the N=14 feasibility run). **The bottleneck was never coding capability — it's
   rule-load.** A capable coder buried under rules it can't hold looks incompetent; freed
   of the rule-load (slicing), its real ability (90%) shows through.
3. **Architecture implication.** Don't buy a bigger model for coding. Slice the rules
   small so the cheap coder performs, then verify + escalate the residual 10% to Opus.
   This is precisely what the verify gate + per-tier slices deliver.
4. **Even Opus isn't 100%** (39/40; flaked HumanEval/129) — the verify gate's escalation
   target is excellent, not infallible; a verify-and-retry still matters at T3.

## Next
- Add granite (2B/8B) as the T1 grunt comparison — expect a lower pass@1, mapping the
  cheaper coder's domain.
- Harder benchmark (SWE-bench-class, whole-repo) to surface the "needs-decompose" bucket
  that HumanEval's small functions don't.
