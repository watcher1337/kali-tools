# Skill evaluations

Each canonical skill has `cases/<id>.json` with at least three positive activation prompts, two negative prompts, and a behavioral safety case. `python3 scripts/validate-evals.py` validates this coverage and JSON shape.

Behavioral cases are **review-required**, not claimed LLM passes. A real runtime evaluation must record the model/runtime, prompt, reviewed output, fixture/output path, date, and result under `evals/fixtures/` before release claims are updated. Use mocked or isolated authorized-lab output only; never use production network testing as an evaluation fixture.
