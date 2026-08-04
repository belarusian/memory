# Experiment 23: Shared Admissibility Budget

## Theoretical Claim

Admissibility can be non-local: a move can be refused for reasons that live in neither subsystem's own state, but in a constraint the subsystems merely share, without exchanging any message.

## Computational Model

Two subsystems hold a reference to the same budget but never reference each other, call each other, or observe each other's fields. One subsystem spends first; the other then attempts a move that would be admissible by every local measure it has access to. Run it with:

```bash
cargo run -p exp23-shared-admissibility-budget
```

## Predicted Result

The second subsystem's move should be refused even though nothing in its own visible state changed, because the shared account — not any local field — is what determined admissibility.

## Observed Result

Record the output from a run here, together with any modifications to parameters.

## Interpretation

Local validity checks are not sufficient evidence of admissibility whenever a constraint is shared rather than owned. The experiment is a minimal, message-free model of that failure mode: two systems can be fully decoupled in their code and still be coupled in what they are permitted to do.
