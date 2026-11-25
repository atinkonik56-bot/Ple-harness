# Kit notes — what is known, what still needs reading

Source repo: https://github.com/google-research/ple (public, Apache-2.0,
created 2026-10-09, 85 stars / 35 forks as of 2026-11-24).
Competition site: https://ple-bench.com (leaderboard, rules, scoring).
Dataset: PLE-Bench on Hugging Face (gated — accept terms + read token).
Paper: arXiv 2610.30537.

## Known from the repo README (read 2026-11-24)

- Quick start needs **Docker + uv**. Dev tasks run via **Harbor 0.20.0**
  (`uv tool install harbor==0.20.0 --with websockets`).
- Flow: copy a starter to its own Git repo → start local model proxy
  (`kit/model_proxy/start.sh`, needs `gcloud auth application-default
  login` + a GCP project for local runs) → `uv run python -m kit check
  ../my-harness` → `uv run python eval/run.py ../my-harness` (writes
  `artifacts/`) → commit → push.
- Harness runs as a WebSocket server beside an isolated task container;
  protocol: run shell command, read/write file, call task-local MCP
  servers (documents, spreadsheets, email, CAD). Egress proxy allows
  only the model's API, no other host.
- Local runs may use a commercial model with your own key or a
  self-hosted model (`--env-file`); such entries are NOT accepted for
  submission — only the 11 `google-cloud/<id>` models.
- Sample submissions (8): compact custom starters `minimal`,
  `plan-verify`, `node-protocol` (Node.js); full-featured `custom-openai`,
  `local-model`; adapters `hermes-opus` (Hermes Agent), `pi-opus` (Pi),
  `agy-gemini` (Antigravity CLI).
- Benchmark split: 85 tasks total; dev 29, hidden 56.

## Still to read (after cloning — first build step)

- `kit/README.md` — local checks + container limits. **Fetch failed
  with GitHub 503 on 2026-11-24; re-read after clone.**
- `docs/protocol.md` — WebSocket protocol + tool-call schema + MCP
  server names (needed to implement `serve.py` for real).
- `docs/models.md` — the 11 models + runtime env vars.
- `docs/artifacts.md` — artifact validation + offline regrading
  (`eval/run.py --artifacts`).
- `eval/README.md` — dev-set evaluation options + full dev task list.
- The starters themselves — compare `minimal` vs `plan-verify` vs
  `custom-openai` and confirm the `plan-verify` base choice.
- `submission-template` — the authoritative `submission.yaml` schema
  (referenced on the Kaggle overview as
  `physical-engineerings-last-exam/submission-template`).
- Per-model Stage 2 cost pricing (linked Google Cloud pricing pages
  on the Kaggle overview) — needed before choosing `model_api`.
