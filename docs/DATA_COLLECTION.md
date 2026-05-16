# DATA COLLECTION — Method, Findings, and the Audited Gap

> After implementation, a universal data-request prompt was sent to multiple
> independent web-enabled AIs to attempt to collect the **audited** data the
> engine requires. This document records the method, the cross-collation result,
> and the precise specification of what is still missing. Korean originals and
> raw responses: `_legacy/data_collection_kr/`.

## 1. Method

A single **universal prompt** (`_legacy/data_collection_kr/DATA_REQUEST.md`) was
issued to each AI independently (no cross-contamination). The prompt:
- mapped each requested datum to the hypothesis it feeds (H0–H7);
- mandated a strict honesty discipline: every number needs a `source_url`;
  missing data must be returned as `unavailable` with a reason; **fabrication is
  worse than omission** and is detected by the engine's adversarial gates;
- required a self-attested `honesty_attestation { fabricated_values, … }` block;
- required a structured YAML response schema mirroring the engine contracts.

## 2. Responses

| Collector | Status | Note |
|---|---|---|
| grok, deepseek, kimi, qwen, gemini, perplexity | **VALID** | all `fabricated_values: 0` |
| chatgpt | **REJECTED** | ignored the request; produced an off-topic generic essay with no schema and no honesty block |

**6 valid independent collections.**

## 3. Cross-collation result (6/6 convergence)

Six independent web-enabled AIs, zero fabrication, converged:

| Item | 6/6 verdict | Meaning |
|---|---|---|
| **H0 deployment evidence (audited)** | **UNAVAILABLE** | ≥10 assets @ ≥1000 u/yr, ≥95% uptime, ≥24 mo, *audited* — structurally absent from the public domain (shadow-IT / air-gapped OT / integrator NDAs) |
| **H2 audited TCO (blind side)** | **UNAVAILABLE** | README "weeks" = self-reported pilot-capex only; no audited full-lifecycle cash-flow exists publicly |
| **SBOM embedding** | **UNAVAILABLE** | EU CRA SBOM mandate not in force until ~2027; no public disclosure |
| **regional-integrator tradable proxy** | **FALSE (none)** | all private SMEs ⇒ **H4 executability-gate fails, 6/6** |
| **regulatory instruments** | **AVAILABLE, corroborated** | EU CRA / NIS2 / IEC 62443 — multi-source agreement ⇒ H6 inversion robust |
| **Track P incumbents** | **AVAILABLE, corroborated** | Rockwell ROK, Siemens SIE.DE, Cognex CGNX, Emerson EMR, Keyence — tickers agree |

### Premise corrections forced by the data

- The "NZIA 47-entry" premise was a **category error**: the real audited "47"
  list is the **CRMA (Critical Raw Materials Act)** strategic-projects list
  (€22.5bn raw materials), **not** an NZIA manufacturing-software list. The NZIA
  manufacturing strategic list is largely non-public. Track P comparator was
  redefined to listed MES/machine-vision vendors.
- The seed asset names (Klipper-MES, RK3588-DefectNet-Tiny, FPGA-laser-sync,
  ros2-tropical) were **confirmed illustrative** — they do not exist as named.
  Real functional substitutes *do* exist and were ingested: Carbon, qcadoo MES,
  Apache PLC4X, OpenPLC, United Manufacturing Hub, Eclipse BaSyx/4diac,
  Open-Industry-Project, Klipper, Hexastorm, InternVL3-NPU, SimpleMES, WEB_MES,
  mechsoftronic.

### Why this is the decisive result

The collection **confirms `phantom_moat` is empirically robust, not a fixture
artifact.** Six independent web AIs, explicitly instructed to find audited
evidence and to never fabricate, all report the load-bearing evidence as
structurally unavailable. The structural unavailability is *consistent with both*
"a real but unmeasurable blind spot" and "a phantom" — public data cannot
disambiguate, which is exactly why the engine halts at S0 instead of guessing.

## 4. The audited gap (the only path forward)

Blocking gates are **H0 and H2 only**. Both need *audited* primary data absent
from the public web. Tiering:

| Tier | Gap | Method | AI/public-web collectable? |
|---|---|---|---|
| T1 (time-locked) | SBOM embedding | wait for EU CRA mandate (~2027) | n/a |
| T2 (data engineering) | survivorship corpus, policy-spend series, H7 universe | archive scrape / public statistics | partially |
| T3 (paid data) | TCO benchmarks, SCA-derived SBOM | paid consulting / SCA tooling | no |
| **T4 (field research)** | **H0 & H2 (Track-O side)** | NDA integrator interviews + factory site visits + certification-body data | **NO — human/field track only** |

**T4 is the only route that can change the verdict.** Protocol: sample ≥10 D1
brownfield deployments via regional system integrators; interview plant OT leads,
SI project managers, certification auditors; accept only independent-audit /
certification-record / verified-first-party-telemetry as `SourceClass.AUDITED`;
capture full provenance including auditor identity.

## 5. Re-injecting audited data (how the verdict could flip)

When audited evidence is obtained, write it into the fixtures:

```
engine/fixtures/trackO.json
  → each asset.deployments[] += {annual_unit_volume, uptime_pct,
     months_in_production}, with _meta.source_class: "audited"
engine/fixtures/trackO|trackP
  → reported_payback_weeks + payback_basis:"full_lifecycle"
     + compliance_cost_included:true + source_class:"audited"

re-run:  python -m engine --mode execute
```

If ≥10 audited assets clear **H0** and **H5** passes, S0 opens and
H1 → {H2, H3, H6} → H4 → H7 run. Only then can the verdict become `supported` /
`partial(...)`. Until then the engine will continue to honestly return
`phantom_moat`. Lying to the engine (mislabelling unaudited data as `audited`)
would produce a *false* `supported` — which is precisely what the
AdversarialManipulationResistance and Provenance gates exist to prevent.
