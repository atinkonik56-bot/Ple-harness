---
name: verifier-runner
description: Run the task's verifier or recompute scripts inside the task container and return a short failure summary, keeping raw output out of the agent's context.
---

# Verifier Runner

Adapted from the Gemma scaffold's `test-runner` skill (pytest summary:
failures + last traceback lines). Same contract — run a check, return
only what the agent needs to decide its next step — new backend: the
task's own verifier scripts and independent recompute scripts instead
of pytest.

## When to use

After COMPUTE, to check the numbers that will enter the deliverable.
Never paste full verifier output into the conversation — call this
skill instead.

## How it works

The harness runs `scripts/run_verification.py` inside the task
container. The script:

1. Runs the named verifier or recompute script with a 300 s timeout.
2. Parses the output and returns a summary:
   - `passed`: number of checks passed
   - `failed`: list of check name + expected vs actual + last 5 lines
   - `error`: collection/runtime errors, if any (first 10 lines)
   - `timed_out`: true if the run hit the timeout

## Inputs

- `targets`: verifier script paths or check names, e.g.
  `verify/cable_sizing.py` or `checks:load_capacity`. Defaults to all
  verifiers in the task folder if omitted — prefer a narrow target.

## Rules

- The script never modifies files. It only runs checks.
- A check that passes both before and after a change proves nothing
  about the change; the verification must fail on a deliberately
  wrong input (sanity check) before it is trusted — the analogue of
  Gemma's F2P/P2P controls.
- Never paste full verifier output anywhere — use this summary.
