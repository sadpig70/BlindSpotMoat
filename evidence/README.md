# evidence/ — Auditable primary sources

This project's two headline claims are not assertions to be taken on trust —
they are backed by **raw, independently-produced primary evidence** preserved
here verbatim. This is a deliberate consequence of the project's defining
principle (falsifiability + honesty): a research instrument must let you check
its work.

> **Language note**: the prompts and responses are kept **verbatim** (Korean /
> mixed). Evidence is cited and summarized in English in `docs/`, not
> translated — translating primary evidence would itself reduce its
> auditability. Use the English `docs/` for analysis; use this folder to verify.

---

## 1. `design_review/` — the 7-AI adversarial review

Substantiates: **"7/7 revise → adopted changes A1–A9"**
(see `docs/REVIEW_SYNTHESIS.md`).

```
design_review/
  REVIEW_PROMPT.md          the single universal prompt sent to every model
  responses/
    chatgpt_reponse.yaml    ┐
    claude_reponse.yaml     │
    deepseek_reponse.yaml   │  7 independent reviews, each produced with no
    gemini_reponse.yaml     ├─ visibility of the others, from the same prompt
    grok_reponse.yaml       │  (filename misspelling "reponse" preserved as-is)
    kimi_reponse.yaml       │
    qwen_reponse.yaml       ┘
```

How to verify: read `REVIEW_PROMPT.md`, then each response's `verdict` and
`focus_findings`. All 7 return `verdict: revise`. The convergent findings
(CONV-1…CONV-6) and the adopted changes (A1–A9) in `docs/REVIEW_SYNTHESIS.md`
are traceable line-by-line back to these files.

## 2. `data_collection/` — the 6-AI audited-data collection

Substantiates the project's **central result**: *the audited evidence required
to certify the moat does not exist in the public domain* — confirmed by 6
independent web-enabled AIs with `fabricated_values: 0`
(see `docs/DATA_COLLECTION.md`).

```
data_collection/
  DATA_REQUEST.md           the single universal collection prompt
  responses/
    grok_data.yaml          ┐
    deepseek_data.yaml      │  6 VALID independent collections
    kimi_data.yaml          ├─ each self-attests honesty_attestation:
    qwen_data.yaml          │    fabricated_values: 0
    gemini_data.md          │
    perplexity_data.yaml    ┘
    chatgpt_data.md         1 REJECTED — off-topic, no schema, no honesty block
```

How to verify: read `DATA_REQUEST.md` (note §1 anti-fabrication rules), then in
each valid response check `honesty_attestation.fabricated_values` (= 0 in all 6)
and the `deployment_evidence` / `tco_payback` / `unavailable_log` sections — all
six independently return the H0 deployment evidence and audited TCO as
`unavailable`, and `regional_integrator_tradable_proxy.exists: false`. That 6/6
convergence is why the engine's `phantom_moat` verdict is *empirically robust*,
not a fixture artifact.

> `chatgpt_data.md` is retained on purpose: it is the **rejected** response. Its
> presence (off-topic, schema-less) is itself evidence that the validity bar was
> applied honestly rather than counting every reply.

---

## Evidence → claim map

| Raw evidence here | English claim it substantiates |
|---|---|
| `design_review/responses/*` (7×, all `revise`) | `docs/REVIEW_SYNTHESIS.md` — 7/7 revise, A1–A9 |
| `design_review/REVIEW_PROMPT.md` | reproducibility of the review |
| `data_collection/responses/*` (6 valid, fab=0; 1 rejected) | `docs/DATA_COLLECTION.md` — 6/6 convergence; `docs/HYPOTHESES.md` — H0/H2/H4 status |
| `data_collection/DATA_REQUEST.md` | reproducibility of the collection |

Anyone can re-run either process with different models using the two prompts and
compare. Nothing here is investment advice; raw third-party AI outputs are
labelled as such and are covered by the disclaimer in the root `README.md`.
