---
name: doc-locator
description: Rank the project files most likely to contain the governing clause, table, drawing callout, or calculation a task needs, using BM25 over extracted document text. Use before reading files in full.
---

# Doc Locator

Adapted from the Gemma scaffold's `locator` skill (BM25 over Python
files, gold file in top 5 for ~70% of tasks). The corpus here is
different — project documents, drawing text, code/standard clauses,
spreadsheets — but the mechanism is the same: rank first, read second.

## When to use

First step of SURVEY, before any full read. Give it the words from
the task: element names, clause numbers, drawing callouts, quantities,
material grades, load cases.

## How it works

The harness runs `scripts/locate.py` inside the task container. The
script:

1. Walks the project folder for readable text: `.txt`, `.md`, `.csv`,
   extracted PDF text, extracted CAD/DXF text, spreadsheet exports
   (skipping the deliverable folder and any binary blobs).
2. Tokenizes each file (identifiers split on `_` and camelCase, plus
   raw words, lowercased; clause numbers like `5.2.1` and units like
   `kN/m` kept as tokens).
3. Scores each file against the query terms with BM25 (k1=1.5, b=0.75).
4. Returns the top 5 files with scores, plus the top matching line
   numbers for the strongest term in each file.

## Inputs

- `query`: space-separated terms from the task, e.g.
  `beam B12 shear capacity AISC 360 Table J3.1`.
- `top_n`: how many files to return (default 5).

## Output

JSON: `{"results": [{"file": str, "score": float, "lines": [int]}]}`.

Read the top files first. If none of them look relevant, grep for a
different identifier or clause number instead of reading more files
at random. Quote the governing clause in your working notes before
you use its numbers.
