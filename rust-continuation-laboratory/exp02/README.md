# Experiment 02: Identity Through Repair

## Theoretical Claim

Identity is continuity preserved across perturbation, not static equality.

## Computational Model

This crate implements the smallest dependency-free Rust model needed to expose the distinction under examination. Run it with:

```bash
cargo run -p exp02-identity-through-repair
```

## Predicted Result

The printed trajectory should distinguish present-state equality from the richer structural, historical, or continuation-sensitive property named by the experiment.

## Observed Result

```
EXPERIMENT: Identity Through Repair
CLAIM: A repaired entity may differ materially while remaining the same continuation.


Comparisons
-----------
same snapshot: false
same identifier: true
same continuation: true
repair history: ["cooled State { temperature: 38.0, shape: 5 } to State { temperature: 20.0, shape: 5 }"]

Result
------
Static equality was lost; historical continuity was not.
```

No parameter modifications. The trajectory confirms the prediction: `same_snapshot` is `false` (shape permanently changed), while `same_continuation` is `true` (ID preserved, repair history grew).

## Interpretation

Treat the program as a counterexample generator and conceptual instrument, not as a proof by metaphor. The relevant question is whether implementing the claim literally produces behavior that ordinary state-transformational descriptions obscure.
