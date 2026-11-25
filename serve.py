#!/usr/bin/env python3
"""PLE harness server — SKELETON (do not submit as-is).

Implements the shape the competition requires; the wire details come
from the kit after cloning google-research/ple:
  - docs/protocol.md  (WebSocket protocol, tool calls, done/error frames)
  - docs/models.md    (env vars for the model endpoint)
  - kit/README.md     (container contract, smoke test)

Contract (from the official overview, 2026-11-24):
  - serve binds to 0.0.0.0:$PORT within 120 s of start (smoke test).
  - One task per run, up to 6 h, in a container with 2 CPUs / 4 GB RAM,
    read-only /opt/harness, writable 1 GB /tmp + $HOME.
  - The evaluator sends the task prompt over WebSocket; the harness
    drives the task container via a small JSON protocol: run a shell
    command, read/write a file, call a task-local MCP server
    (documents, spreadsheets, email, CAD).
  - Model URL/key come from env vars ONLY (MODEL_BASE_URL /
    OPENAI_BASE_URL, ANTHROPIC_BASE_URL, GOOGLE_GEMINI_BASE_URL).
    No API keys in the repo; the Stage 2 proxy blocks custom keys,
    .env files, external model servers, and web search.
  - Send `done` on success, `error` on unrecoverable failure.
    A task without a done/error frame scores 0.0.

Agent loop (see prompts/system.md for the full prompt):
  SURVEY -> PLAN -> COMPUTE -> VERIFY -> DELIVER -> done

Dependencies: Python 3.11+ stdlib + `websockets`
(the kit's agent needs websockets; Harbor runs the dev tasks).
"""
import json
import os
import sys


def model_config():
    """Model endpoint from env only. Returns (base_url, api_key)."""
    base_url = (
        os.environ.get("MODEL_BASE_URL")
        or os.environ.get("OPENAI_BASE_URL")
        or os.environ.get("GOOGLE_GEMINI_BASE_URL")
        or os.environ.get("ANTHROPIC_BASE_URL")
    )
    # TODO: confirm the exact env names in docs/models.md after clone.
    # The evaluator proxy injects these; locally, kit/model_proxy sets
    # MODEL_PROXY_URL. Never fall back to a hardcoded key.
    api_key = os.environ.get("MODEL_API_KEY", "")
    return base_url, api_key


def main():
    port = int(os.environ.get("PORT", "8000"))
    # TODO: implement after reading docs/protocol.md:
    #   1. start a WebSocket server on 0.0.0.0:port
    #   2. on task prompt: run the agent loop (SURVEY..DELIVER)
    #      against the task container (shell/read/write/MCP)
    #   3. write deliverable files into the task container
    #   4. send `done` (or `error` with a reason) and exit
    # Budget guards (hard, in code, not just in the prompt):
    #   wall-clock < 6 h, model calls capped, tokens logged per task.
    print(f"PLE harness skeleton: would serve on 0.0.0.0:{port}", file=sys.stderr)
    print("Not implemented: read docs/protocol.md after cloning the kit.",
          file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
