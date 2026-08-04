# Experiment 24: Observer-Relative Restorability

## Theoretical Claim

Restorability is a relation between an object and an observer's prior channel, not a property the corrupted object carries on its own.

## Computational Model

Two observers see byte-for-byte the same corrupted array. One kept a parity channel from before the corruption; the other kept nothing beyond the corrupted data itself. Run it with:

```bash
cargo run -p exp24-observer-relative-restorability
```

## Predicted Result

The observer with the parity channel should reconstruct the missing byte exactly; the observer without one should be unable to restore it at all, despite both looking at an identical corrupted object.

## Observed Result

Record the output from a run here, together with any modifications to parameters.

## Interpretation

Asking "is this state restorable?" without specifying "restorable by whom, with what preserved alongside it?" is underspecified. The experiment makes that dependency explicit and mechanical: restorability lives in the pairing of object and observer, not in the object in isolation.
