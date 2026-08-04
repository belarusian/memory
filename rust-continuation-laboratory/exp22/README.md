# Experiment 22: Repair Groupoid

## Theoretical Claim

Repair operations compose like a groupoid, not a group: each defined repair is invertible on its own domain, but there is no single symmetry relating every admissible state to every other one.

## Computational Model

Shapes stand in for states, and morphisms stand in for repairs, each defined only between two specific shapes and invertible exactly where defined. Composition chains two morphisms through a shared intermediate shape, exactly as groupoid morphisms compose. Run it with:

```bash
cargo run -p exp22-repair-groupoid
```

## Predicted Result

A state should be repairable to some targets directly, to others only through composition, and to at least one target not at all — with round-trip invertibility holding wherever a repair is defined.

## Observed Result

Record the output from a run here, together with any modifications to parameters.

## Interpretation

A group would license moving between any two states via some element and its inverse. A groupoid only licenses movement along the arrows that were actually built, composed as far as they reach. The experiment is a warning against importing group-theoretic intuitions — "everything is reachable from everything, symmetrically" — into a setting where admissibility was never total to begin with.
