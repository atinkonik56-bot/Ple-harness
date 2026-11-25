# Local evaluation harness (plan)

CPU-only replica of the PLE dev-set evaluation, adapted from the Gemma
scaffold's `harness/local_eval.py` (task loader, F2P/P2P controls,
JSONL results, exclude-misbehaving-tasks rule).

## The problem

The official path — `uv run python eval/run.py ../my-harness` — runs
dev tasks in Docker containers via Harbor. **This VM has no Docker
and no GPU**, and Kaggle notebooks cannot run Docker either. So the
official eval cannot run here. This harness covers what CAN be done
locally; real dev-task runs need a Docker host (see PLAN.md §7 gap 1:
cheap cloud VM, or GitHub Actions on the submission repo).

## What to build here

1. **Mock task container** — a tiny local stand-in for the evaluator:
   feeds a task prompt to `serve.py` over a local WebSocket, answers
   the harness's shell/read/write/MCP calls against a plain folder,
   records every call, and checks that `serve.py` binds fast, writes
   files, and sends `done`. Proves the server mechanics without
   Docker. (Analogue: Gemma's `sample_task.jsonl` + `sample_repo/`.)
2. **Synthetic 1-task fixture** — a miniature engineering task (e.g.
   a beam load check with a known answer) with its own verifier
   script. The harness must produce the right number; a deliberately
   wrong answer must fail the verifier (the F2P/P2P control idea:
   validate the instrument before measuring the agent).
3. **Artifact checker** — mirrors `kit artifacts` locally: artifacts/
   unpacked, ≤ 512 MiB, ≤ 10,000 files, no symlinks, no LFS; every
   dev-task output present and re-scoreable.
4. **Run logger (JSONL)** — per task: model, calls, tokens, runtime,
   verifier score, judge score (local stand-in), cost estimate.
   This is the raw material for the writeup's score-vs-cost plot and
   failure breakdown. Record the model + harness commit with every run.

## Rules (from Gemma, kept)

- A dev task whose verifier misbehaves is reported EXCLUDED, never
  silently scored.
- Keep **5 of the 29 dev tasks** out of all design decisions (holdout);
  validate on them only at the end.
- Real agent runs (model + Harbor + Docker) happen where Docker
  exists, not here.
