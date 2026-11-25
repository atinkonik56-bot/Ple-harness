# Kaggle PLE Hackathon — prep repo

**Competition:** Google — Agent Harness on Physical-Engineering's Last Exam (PLE)
**Link:** https://www.kaggle.com/competitions/physical-engineerings-last-exam
**Prizes:** $400K (1st $250K / 2nd $100K / 3rd $50K)
**Deadline:** Tue 5 Jan 2027 23:59 UTC = Wed 6 Jan 2027 06:59 WIB
**Status:** prep only (2026-11-24). Mohammad has NOT joined yet — he joins on Kaggle from his phone.

Read `PLAN.md` first — it has the full picture: what the competition wants, the harness design, the reuse map from the Gemma scaffold, the timeline, the gaps, and what Mohammad needs to do.

## Layout

| Path | What it is |
|---|---|
| `PLAN.md` | The plan (approach, reuse map, timeline, gaps, his action list) |
| `submission.yaml` | TEMPLATE — `model_api` placeholder; validate against the kit's submission-template after cloning `google-research/ple` |
| `serve.py` | SKELETON — WebSocket harness server outline; implement against `docs/protocol.md` after cloning the kit |
| `prompts/system.md` | Draft v0 agent system prompt (Gemma 5-phase loop, re-mapped to engineering tasks) |
| `skills/doc-locator/` | Adapted from Gemma `skills/locator` — BM25 over project docs/drawings/code text |
| `skills/verifier-runner/` | Adapted from Gemma `skills/test-runner` — run verifier scripts, summary only |
| `harness/` | Local eval plan: mock task container + artifact checks (no Docker in this VM) |
| `writeup/OUTLINE.md` | Stage 1 Writeup outline mapped to the 100-point rubric |
| `docs/kit-notes.md` | What is known about the kit so far + what still needs reading after clone |

## What is NOT here (yet)

- The kit itself — clone `google-research/ple` first (build step 1).
- The 29 dev tasks — gated Hugging Face dataset; needs his HF account + terms + read token.
- A working harness — `serve.py` is a skeleton until the kit protocol is read.
- Any Kaggle join/submit — forbidden in prep; he joins from his phone.
