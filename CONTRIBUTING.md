# Contributing

This repository is the working record of a geometry-first physics research program. It is offered for collaboration — but the *method* is the point, so contributions are held to the same standing rules the record was built under. Please read these before opening an issue or a pull request.

## The standing honesty rules

These are non-negotiable. They are why the record is worth reading even where the physics failed.

1. **Tag every claim.** Each assertion carries exactly one tag:
   - `[proved]` — proved here, with the proof in the same document.
   - `[established (others')]` — a known result, **with citation**.
   - `[conjecture]` — believed, not proved. Say so.
   - `[interpretation]` — a reading of a result, not a result.
   - `[fitted]` — obtained by fitting to data, not derived.
2. **Pre-register predictions with kill conditions.** A prediction states, in advance, the observation or computation that would falsify it. Predictions added after the relevant data are not predictions.
3. **Report negative results plainly.** No-go results, failed routes, and dead ends are stated, not buried and not tuned away. A negative result is a result.
4. **Honor kill tests when they fire.** If a pre-registered kill condition is met, the claim dies in the record. It is not quietly rescoped.
5. **No fabricated numbers, assignments, or derivations.** Compute it, cite it, or write "unknown." Never invent a figure to fill a gap.

A contribution that violates these will be asked to revise before it can be merged, regardless of whether the underlying physics or math is interesting.

## Where to put things

- **Discussions** — open-ended ideas, questions about the framework, "has anyone considered…". Start here if you are not sure.
- **Issues** — a specific, actionable item: a claimed error, a proposed calculation, or an attack on one of the open problems in [`notes/QUESTIONS-2026-07-19.md`](notes/QUESTIONS-2026-07-19.md). Each open problem there names what dies if the answer is wrong — good issues do the same.
- **Pull requests** — corrections, new calculations, new phase documents, or reproducible scripts.

## Practical conventions

- **New computations** go in `scripts/` as self-contained Python (standard library plus `sympy`/`numpy` where noted). No hidden inputs; a reader should be able to run the script and reproduce the number. See existing `scripts/*_calc.py` for the style.
- **New prose** goes in the matching folder (`phases/`, `notes/`, `reviews/`, …). Match the surrounding tone and the tagging discipline above.
- **Cite your sources.** External results need a reference a reader can follow.
- **Keep the layout intact.** The folder scheme is documented in the README's "Repository layout" table; new files should land in the right folder, and cross-references should use the folder-qualified path.
- **Math and negative results are equally welcome.** A clean refutation of a live claim is one of the most valuable contributions you can make here.

## Reviewing others' contributions

Referee-style critique is explicitly invited — four adversarial red-team campaigns are preserved in `reviews/`, and that spirit continues. Be specific, be adversarial about the claim (not the person), and default to "refuted / unknown" when the evidence is not there.

## Code of conduct

Be direct about ideas and kind to people. Attack claims, not contributors. That is the whole of it.
