# Rust Continuation Laboratory


This workspace contains executable experiments derived from a process-relational research program in which distinctions are maintained, states are moments in trajectories, admissibility is future-sensitive, and repair preserves structured possibility.

Rust is not offered as evidence that the framework is true. It is used as an unusually explicit experimental medium: ownership exposes authority, lifetimes expose dependency, enums expose alternatives, and the type system makes many hidden continuation claims inspectable.

## Running the suite

Run every experiment with:

```bash
./run-all.sh
```

Run one experiment with, for example:

```bash
cargo run -p exp10-diagnostic-coordinates
```

The workspace has no external crate dependencies.

## Experiments

01. **Distinction Machine** — see `exp01/README.md`.

02. **Identity Through Repair** — see `exp02/README.md`.

03. **Boundary-Relative Object** — see `exp03/README.md`.

04. **Reachability as Ownership** — see `exp04/README.md`.

05. **Authority Without Knowledge** — see `exp05/README.md`.

06. **Lifetime as Continuation Proof** — see `exp06/README.md`.

07. **Admissible State Space** — see `exp07/README.md`.

08. **Hierarchical Admissibility** — see `exp08/README.md`.

09. **Null Intervention** — see `exp09/README.md`.

10. **Diagnostic Coordinates** — see `exp10/README.md`.

11. **Local Repair, Global Damage** — see `exp11/README.md`.

12. **Repair Budget** — see `exp12/README.md`.

13. **Monotonic Ledger** — see `exp13/README.md`.

14. **Refusal Without Erasure** — see `exp14/README.md`.

15. **Collapse as Projection** — see `exp15/README.md`.

16. **Branch Persistence** — see `exp16/README.md`.

17. **Fair Continuation Scheduler** — see `exp17/README.md`.

18. **Persistent Generative World** — see `exp18/README.md`.

19. **Physiological Coupling** — see `exp19/README.md`.

20. **Representational Repair** — see `exp20/README.md`.

21. **Fundamental Continuation** — see `exp21/README.md`.

22. **Repair Groupoid** — see `exp22/README.md`.

23. **Shared Admissibility Budget** — see `exp23/README.md`.

24. **Observer-Relative Restorability** — see `exp24/README.md`.


## Method

Every directory contains a theoretical claim, a computational model, a predicted result, a place to record observed output, and an interpretation. Parameters are intentionally exposed in the source. The most productive use of the suite is to alter them until the printed conclusion fails, then determine whether the failure belongs to the theory, the implementation, or the chosen representation.

## Suggested sequence

Begin with Experiments 01, 02, 07, 09, 10, 11, 13, 14, 15, 16, 18, and 21. Together they form a progression from distinction through admissibility and repair to persistent history and future-sensitive viability.

Experiments 22-24 extend that progression outward: from a single system's repairs to how repairs compose across states (22), how admissibility can be shared between systems with no direct coupling (23), and how restorability depends on the observer, not just the object (24).
