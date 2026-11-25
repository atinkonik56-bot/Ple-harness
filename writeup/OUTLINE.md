# Stage 1 Writeup — outline (≤ 2,000 words, 100 points)

The Writeup is the Stage 1 gate: top 100 of all entries advance.
Write for an ML researcher with NO civil, mechanical, or electrical
background. Headline finding near the top. Three required figures.

## Word budget (2,000 max — plan for ~1,800, leave margin)

| Section | Words | Rubric |
|---|---|---|
| Headline finding + architecture (Fig. 1) | ~250 | Clarity (15) |
| 1. Insight & Failure Analysis | ~500 | 25 pts |
| 2. Engineering Reasoning (one worked task) | ~500 | 25 pts |
| 3. Cross-Model Generalizability (comparison table) | ~300 | 15 pts |
| 4. Efficiency & Scaling (Fig. 2) | ~300 | 20 pts |
| Closing + limitations | ~150 | — |

## Figure 1 — Architecture diagram (required)

serve.py → agent loop (SURVEY → PLAN → COMPUTE → VERIFY → DELIVER)
→ task container (shell / read / write / MCP: documents, spreadsheets,
email, CAD) → model via evaluator proxy. Show where verification sits
(it is a loop, not a final step) and where the unit ledger lives.

## Figure 2 — Score-vs-cost plot (required)

Dev-set mean score (y) vs compute budget (x: model calls / tokens /
runtime / parallel attempts — pick one primary axis). One curve per
model tested (≥ 2). Mark where accuracy plateaus; annotate the chosen
operating point (the committed `model_api`) and estimate remaining
headroom. Data comes from `harness/` run logs — do not hand-draw it.

## Figure 3 — Dev-set failure breakdown (required)

Stacked bar or table: the 29 dev tasks grouped by failure class
(misread drawing callout / wrong code clause / unit error / stopped
early / verifier mismatch / timeout / other), before vs after the
verification loop. This figure is the evidence for criterion 1 —
it must come from real runs, with counts.

## Content notes per criterion

1. **Insight & Failure Analysis (25):** teach something non-obvious.
   Lead with real failures and controlled ablations ("we added the
   unit ledger; dev score went A→B"). Include at least one idea that
   failed and why. No generic claims without a number attached.
2. **Engineering Reasoning (25):** one concrete dev task, walked
   through step by step: agent trajectory vs a licensed engineer's
   workflow, where reasoning held, where it shortcut, which domain
   skills (reading drawings, checking code tables, running solvers)
   separated the pass from the failure.
3. **Cross-Model Generalizability (15):** comparison table (model ×
   dev score × cost per task). State what helps every model (e.g.
   verification loop, unit ledger) vs what helps one model only.
   Name the committed target `model_api` for Stage 2.
4. **Efficiency & Scaling (20):** Fig. 2 + plateau analysis + headroom
   estimate. If more budget would not help, say so and show why.
5. **Clarity & Visuals (15):** headline finding in the first
   paragraph; no unexplained engineering jargon; all three figures
   referenced in the text; under 2,000 words.

## Submission mechanics

- Kaggle → Writeups tab → New Writeup → attach GitHub repo link
  under Project Links → 40-char commit SHA at the top → Submit.
- An un-submitted draft is NOT judged. Confirm the status reads
  SUBMITTED, not draft.
- Writeup license: CC BY 4.0 (per third-party summaries of the rules);
  code: Apache-2.0 or MIT.
