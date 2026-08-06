# The Mainstream Branch: An ML Curriculum

A dependency graph, not a linear series. Each book answers a distinct question and can be entered on its own; together they lead a reader from the field's history into its research frontier, and from there into the research branch (RSVP, Structural Semantics, Persistent Generative Worlds, and the rest).

```
        1. History
       (Why did it develop this way?)
              |
   ------------------------------
   |          |          |
2. Math    3. Neural   4. NLP
(reference  Nets from   (How do machines
 companion,  Scratch     process language?)
 consulted   (How do
 as needed)  you build
             one?)
              \          /
               \        /
          5. Training Language Models
          (How do you produce state-
           of-the-art models?)
                    |
          6. AI Systems Engineering
          (How do you deploy and
           operate them?)
                    |
          7. The research monographs
          (RSVP, Structural Semantics,
           Persistent Generative Worlds,
           Diagnostic Coordinates, ...)
```

---

## Book 1 — A History of Machine Learning
**Question: Why did machine learning develop the way it did?**

Almost entirely conceptual; minimal math. Reads more like a history of physics than a programming manual. Opens with a prologue (drafted) adapting the Swedenborg/Kant essay's thesis: every architecture in the field's history sits somewhere on the line between two failure modes — too constrained to say anything useful, or too generative to be trustworthy — and each generation's central invention is a specific answer to that tension.

**Recurring analytical tool — the bottleneck taxonomy**, reused chapter to chapter:
- Representational — what can the model express?
- Optimization — can we efficiently find good parameters?
- Data — do we have enough information to learn?
- Memory — what can the system retain or access?
- Computational — can we train and infer efficiently?
- Scaling — does performance keep improving with size?
- Interaction — how does the model obtain information beyond its parameters?
- Alignment — how do we make outputs useful and consistent with human objectives?

Each chapter closes with a short "which bottleneck(s), and what did it cost" note, so the taxonomy functions as a running scorecard rather than a static list. Chapters 5–7 (statistical learning / SVMs / graphical models) get their own bottleneck category — feature engineering — since that era wasn't superseded by a bottleneck resolution so much as outcompeted once learned representations beat hand-engineered ones.

**Chapter list (draft):**
0. Prologue — The Argument Before the Field (drafted)
1. Symbolic AI and expert systems
2. The perceptron
3. The AI winter
4. Backpropagation and multilayer networks
5. Statistical learning
6. Support vector machines and kernel methods
7. Probabilistic graphical models
8. Deep learning
9. Convolutional networks
10. Sequence models and recurrent networks
11. Attention and transformers
12. Scaling laws
13. Large language models
14. Post-training and alignment
15. Retrieval, tools, and agents
16. Open problems and future directions — names the *category* of open bottleneck (interpretability, data exhaustion, energy cost, grounding) without naming a personal proposed answer; the clean, uncontroversial handoff into Book 7

---

## Book 2 — Mathematics for Machine Learning
**Question: Why does it work?**

Not a prerequisite gate — a reference companion, consulted as needed rather than read start to end. Each chapter corresponds to concepts introduced in context elsewhere (chain rule when backprop comes up, eigenvectors when PCA or attention comes up), so readers who need the depth have somewhere to go and readers who don't can keep moving.

**Chapters (by topic, not yet sequenced):**
- Calculus for optimization
- Linear algebra for embeddings and transformers
- Probability for generative models
- Information theory for language modeling
- Numerical optimization
- Graph theory
- Statistics
- Differential equations, where relevant

---

## Book 3 — Neural Networks from Scratch
**Question: How do you build one?**

Build-oriented, mirroring the Rust and trigonometry books: each chapter culminates in constructing something. Not yet outlined chapter by chapter — candidate build sequence based on what's been discussed:
perceptron → multilayer network and backprop by hand → optimization and regularization → CNN → RNN/LSTM → attention → a tiny transformer.

---

## Book 4 — Natural Language Processing
**Question: How do machines process language?**

Not yet outlined. Candidate arc: n-grams and HMMs → word embeddings → sequence models for language → attention and transformers → retrieval → modern LLMs, each stage read against the same bottleneck taxonomy as Book 1, now at working depth.

---

## Book 5 — Training Language Models
**Question: How do you produce state-of-the-art models?**

Full lifecycle, engineering-first. Not yet outlined. Scope agreed so far: dataset collection and filtering, tokenization, pretraining objectives, distributed training, checkpointing, evaluation, fine-tuning, preference optimization (RLHF and successors).

---

## Book 6 — AI Systems Engineering
**Question: How do you deploy and operate them?**

Not yet outlined. Scope agreed so far: quantization, inference, serving, benchmarking, continual learning.

---

## Book 7 — The Research Branch
Not a new book — the existing monograph corpus (RSVP, Structural Semantics, Persistent Generative Worlds, Diagnostic Coordinates, and the reconstruction/repair cluster), positioned as where a curious reader lands after Books 1–6, entered via Book 1's closing bottleneck discussion rather than argued for anywhere in the mainstream branch itself.

---

## Design constraints holding across all six books
- Reinterpretive voice (organize by *why an idea became necessary*, not by rule-listing) is the signature; none of the books should require adopting any of the research-branch frameworks or terminology to be followed
- The Swedenborg/Kant material feeds the Book 1 prologue only as historical analogy — none of the screenplay's invented mythology (Architects, Category Plane, sentient Shadow) belongs in the nonfiction books
- Working style is serial, not parallel — Book 1 is the one with actual drafted material (prologue) and the most developed outline; it's the natural starting point
