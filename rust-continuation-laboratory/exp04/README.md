# Experiment 04: Reachability as Ownership

## Theoretical Claim

Ownership is authority over a reachable continuation, not physical possession.

## Computational Model

This crate implements the smallest dependency-free Rust model needed to expose the distinction under examination. Run it with:

```bash
cargo run -p exp04-reachability-as-ownership
```

## Predicted Result

The printed trajectory should distinguish present-state equality from the richer structural, historical, or continuation-sensitive property named by the experiment.

## Observed Result

Record the output from a run here, together with any modifications to parameters.

## Interpretation

Treat the program as a counterexample generator and conceptual instrument, not as a proof by metaphor. The relevant question is whether implementing the claim literally produces behavior that ordinary state-transformational descriptions obscure.
