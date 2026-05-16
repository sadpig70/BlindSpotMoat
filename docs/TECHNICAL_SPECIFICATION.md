# BlindSpotMoat / NULLTRACK — Technical Specification

> **Document type**: Consolidated technical reference (English).
> **Audience**: An engineer or AI seeing this project for the first time. After
> reading this single document you should be able to (a) understand what the
> project is and *why it currently returns `phantom_moat`*, (b) read and run the
> engine, (c) interpret its output correctly, and (d) know exactly what would be
> required to advance it.
> **Status as of 2026-05-17**: design v0.2, engine v0.2.0, verdict =
> `phantom_moat` (empirically robust), state = *evidence-blocked provisional*.
> **Self-contained**: you do **not** need to read docs 00–06 first; this file
> summarizes them. Cross-references are pointers, not prerequisites.

---

## 0. TL;DR (read this first)

BlindSpotMoat is **an analysis/simulation engine, not a product**. It tests one
hypothesis: *in manufacturing brownfield retrofit, is there a set of open-source
production assets that policy/procurement instruments structurally cannot "see",
and does that invisibility constitute a measurable but finite economic arbitrage?*

The engine is **deliberately built to refuse to lie**. It only accepts data
classed `audited` as empirical evidence. The data required to prove the core
claim (audited production-scale deployment telemetry, audited full-lifecycle
cost) **does not exist in the public domain** — this was confirmed independently
by 6 web-enabled AIs (`fabricated_values=0`, 6/6). Therefore the engine halts at
its first gate and returns **`phantom_moat`**.

**`phantom_moat` is the correct, honest result — not a bug and not a failure.**
It means: *"the methodology runs end-to-end, but the idea cannot be empirically
certified from public data; certification requires non-public field research."*
The idea is **not discarded** — it is held in a precise, auditable state called
*evidence-blocked provisional*. The only way to change the verdict is the field
research track described in §8.

---

## 1. Identity & Provenance

| Field | Value |
|---|---|
| Project name | **BlindSpotMoat** |
| Codename | **NULLTRACK** |
| Idea ID | **IDEA-20-02** |
| Source insight | **INS-L10-005** — "Invisible-Track Coexistence" |
| Transformation lens | **DIR_RESDEL** = `L11_RemoveResource` — *"delete the scarce resource and redesign around its absence"* |
| Domain | **D1 — manufacturing brownfield retrofit** (+ thin D2 shadow probe for transferability only) |
| Selection chain | SDX catalog v1.3 → TCX-20260514-001 → IDX-20260514-001 → **CIX-20260514-001** (cross-model certified) → **EVX-20260516-001** (dual winner, `winners_identical=true`) → aox-20260516T000000Z-resume |
| CIX 6-axis score | novelty 6.9 / generativity 8.0 / defensibility 5.5 / compounding 8.0 / **surprise 10.0** / coherence 7.0 → **total 8.12** (denom 9.5), `scoring_mode: v1_5_semantic_heuristic_main` |
| Cross-model baseline families | xAI Grok-4.3, DeepSeek-V4, Alibaba Qwen-3.6, OpenAI Codex-GPT-5 |
| Main model | Claude Opus 4.7 |

> ⚠ **Epistemic status of the CIX score**: `surprise 10.0` / `total 8.12` are
> **novelty/narrative signals only**. Per the honesty invariant (§4) they are
> *not* admissible as feasibility or empirical evidence. `surprise ≠ feasibility`.

The A3IE pipeline that produced IDEA-20-02 is **SDX→TCX→IDX→CIX→EVX→AOX** under
the *IdeaFirst* principle ("cost ≪ value"). What matters downstream: this idea
won a **cross-model-certified** selection where 0/8 personas and 4 baseline model
families predicted the resource-deletion transformation — hence `surprise 10.0`.
Surprise drove selection; it does **not** imply the idea is feasible or true.

---

## 2. The Concept

### 2.1 The dual-track model

Manufacturing investment splits into two tracks that share no capital, no policy
vehicles, and almost no vocabulary:

| | **Track P** (policy-visible) | **Track O** (open-source brownfield, "invisible") |
|---|---|---|
| Assets | NZIA/IRA-funded projects, listed MES/SCADA/machine-vision vendors (Rockwell, Siemens, Cognex…), EMS roll-ups | Apache-2.0 + sub-USD-100 SBC retrofit stacks (open MES, edge defect-detection, FPGA motion control…) |
| Capital | VC + policy subsidy | Near-zero |
| Visibility | Listed in procurement frameworks / VC term sheets / trade press | **No procurement framework recognizes them by name** |
| Claimed payback | 24+ months (greenfield) | weeks (retrofit) — *self-reported* |

The original insight (INS-L10-005): the **binding constraint is visibility, not
technology or capital**. Policy instruments are *structurally blind* to one
track, and that blindness — not the tech — is the lever.

### 2.2 The RESDEL transformation

The lens deletes the scarce resource ("policy capital / legitimacy / visibility")
and redesigns around its absence. Instead of trying to make Track O *visible* to
policy (the obvious move that every baseline model proposed), RESDEL treats
policy channels as **non-existent** and asks whether Track O can win on pure
unit-economics *because* it is illegible.

### 2.3 What "moat" means here (post-revision — read carefully)

The original framing ("invisibility is a permanent moat") was **rejected by a
7-AI adversarial review (7/7 revise)**. The surviving, defensible proposition is:

> *Within manufacturing brownfield retrofit, conditional on the current
> horizontal-regulation regime as of date T, a policy-procurement-illegible stack
> provides a measurable unit-economic arbitrage for a **finite period T_window**
> — and only if (H0) that track exists at production scale, (H5) the exclusion is
> structural rather than a quality filter, and (H6) horizontal regulation has not
> yet absorbed it.*

Key consequences of the revision:
- **Not permanent**: "moat" → a *regulatory half-life arbitrage window* with a
  mandatory expiry. There is no permanent-castle claim anywhere.
- **Not self-protecting**: legal standing while invisible is a logical
  contradiction (RECIP abandoned — see §5 LegalStandingLayer).
- **Conditional**: any moat claim is gated behind H0 & H5 (existence & structural
  nature). Until those pass on audited data, every moat statement is provisional.

### 2.4 The three critical objections (why this is hard)

From the 7-AI review, three convergent threats define the project's risk:

- **(A) blindness ≠ exploitable moat** — the unseen track might just be
  immature, niche, or already embedded sub-tier in Track P (a *phantom* blind
  spot). → addressed by H0 (scale) + H5 (structural) + DependencyPenetration.
- **(B) the moat is a kill zone** — an invisible actor cannot enforce contracts;
  invisibility removes protection exactly when it is needed. → addressed by
  abandoning RECIP and adopting a 2-layer legal model (§5).
- **(C) the window is closing** — horizontal regulation (EU CRA, NIS2,
  IEC 62443) forces invisible stacks into audited supply chains, so policy growth
  may *destroy* the moat, not grow it. → addressed by competing hypotheses
  H3a/b/c + RegulatoryAbsorptionMonitor + TimeToCaptureMetric.

---

## 3. The Epistemic Framework (the single most important section)

If you understand only one thing about this project, understand this section.

### 3.1 The A8 honesty invariant

Every datum carries a `Provenance` with a `SourceClass`:

| SourceClass | Meaning | Admissible as empirical evidence? |
|---|---|---|
| `audited` | Independent audit / regulatory disclosure / verified 1st-party telemetry | **YES** |
| `public_unaudited` | Real public data, not audited (GitHub metrics, market prices) | No → narrative only |
| `self_reported` | README / marketing / conference claims | No → narrative only |
| `illustrative` | Vintage scaffold fixture | No → narrative only |
| `derived` | Computed from other provenanced values | Inherits |

Rule: **only `audited` data can satisfy an empirical hypothesis.** Everything
else is recorded but flagged "narrative decoration". The CIX 8.12 / surprise 10.0
scores are explicitly narrative. This invariant is enforced in code
(`engine/contracts.py: Provenance.admissible`) and in the hypothesis gates.

### 3.2 Why `phantom_moat` is the correct output

The engine's first gate **S0 = H0 (scale-existence) & H5 (structural-blindness)**.
H0 requires ≥10 Track O assets with **audited** production-scale deployment
evidence. The data collection (§7) established — via 6 independent web AIs,
`fabricated_values=0` — that this evidence **does not exist publicly** by the
nature of the phenomenon (shadow-IT / air-gapped OT networks / integrator NDAs).

So H0 is falsified (0 admissible assets) → the pipeline halts fail-closed →
verdict = **`phantom_moat`**. This is the engine doing exactly what it was
designed to do: *refuse to assert a moat it cannot prove with audited data.*
A naive engine would have "passed" using GitHub stars and README payback claims —
this engine deliberately will not.

> **Mental model**: `phantom_moat` is not "the idea is false". It is "the idea is
> unproven and, with public data, *unprovable* — here is precisely what is
> missing and where it lives" (§8). The idea is held as *evidence-blocked
> provisional*, neither accepted nor discarded.

### 3.3 Falsifiability & the gating order

All hypotheses are **pre-registered** with explicit numeric thresholds and
statistical tests (no goalpost-moving). Evaluation order is enforced:

```
H0 (scale) & H5 (structural)        ── S0 GATE ──┐  fail → phantom_moat, STOP
                                                  ▼
H1 (independent-deploy disjointness)
                                                  ▼
{ H2 (unit-economics) · H3 (policy↔moat) · H6 (reg-absorption) }   (parallel)
                                                  ▼
H4 (executability → proxy-portfolio)   ← fail → monetization auto-retire
                                                  ▼
H7 (market-efficiency)                 ← fail → signal already priced → void
```

A later hypothesis is **never** evaluated until its predecessors pass. This is
why, on current data, you only ever see H0 and H5 in the output: S0 halts first.

---

## 4. System Architecture (PGF Gantree)

The design is expressed in **PGF** (PPR/Gantree Framework): a hierarchical
functional decomposition (Gantree) plus AI-readable pseudo-code (PPR). Canonical
design = `docs/05_design.md` v0.2; PGF projection = `.pgf/DESIGN-BlindSpotMoat.md`.

### 4.1 Node reference

| Node | Role | Criticality |
|---|---|---|
| **DataIngestion** | Load Track P/O + SBOM + regulatory fixtures; tag every record with `Provenance`; normalize | — |
| **AdversarialManipulationResistance** | Detect astroturf/repo-farming (burst commits, single-org concentration, star/fork anomalies); down-weight dormant forks | **CRITICAL** |
| **SurvivorshipFilter** | Fold defunct/failed repos + failure rate into the corpus so payback is not survivor-biased | — |
| **EntityResolve** | Adjudicated ground-truth map + fuzzy/semantic match + **measured precision/recall** + manual-audit log + confidence tiering | **CRITICAL** |
| **VisibilityGraph** | Replace boolean set-difference with **graded visibility 0–1** + multi-hop path + **DependencyPenetration** (SBOM-embedded assets excluded from "blind") | — |
| **UnitEconomicsScoring** | Payback per *comparable functional unit* + **ComplianceCostOverlay** (cert/V&V/SBOM/liability cost folded in) | — |
| **TimeToCaptureMetric** | Replace static `width×growth` with **regulatory half-life** + estimated remaining `T_window` (moat is finite by construction) | — |
| **TimeSeriesStabilityMonitor** | Replay ≥2 separated 12-month windows; flag concept drift / cyclical artifacts | — |
| **RegulatoryAbsorptionMonitor** | Horizontal-regulation watchlist (CRA/NIS2/IEC 62443…); assimilation-risk score; leading indicator for H3c/H6 | — |
| **HypothesisHarness** | Evaluate H0–H7 with pre-registered thresholds and the gating order | **CRITICAL** |
| **LegalStandingLayer** | RECIP abandoned → **2-layer spec**: (1) standard commercial/IP/tort contract (orthogonal to illegibility, visibility-cost 0); (2) dispute-time-only escrow/ZK reversible disclosure; + accepted-legal-cost doc; fail-closed | **CRITICAL** |
| **SurfacingOption** | Detached, **default-OFF** visibility-surfacing module; must never couple to the primary engine (purpose-pollution guard) | optional |
| **VisibilityErosionMonitor** | Observer-effect: the engine's own output is an act of surfacing; track whether previously-blind assets later appear in policy/VC/press | **mandatory** |
| **Reporting** | RankTable + MonetizationSignal (retained but repositioned as a half-life window, gated by H4 & H7) + HonestReport (S6) | — |
| **ModeDryRun** | Validate data contracts / gates / thresholds without executing | — |

### 4.2 Dependency graph

```
DataIngestion → AdversarialManipulationResistance → EntityResolve → VisibilityGraph
              → SurvivorshipFilter (corpus adjustment)
VisibilityGraph → { UnitEconomicsScoring(+ComplianceCostOverlay), TimeToCaptureMetric }
RegulatoryAbsorptionMonitor → HypothesisHarness   (H3c/H6 input)
{UnitEconomicsScoring, TimeToCaptureMetric, RegulatoryAbsorptionMonitor} → HypothesisHarness → Reporting
Reporting → VisibilityErosionMonitor
LegalStandingLayer ⟂ (independent, CRITICAL, must complete before Reporting)
SurfacingOption ⟂ (detached, default-OFF)
Gating: HypothesisHarness S0 (H0&H5) fail → downstream output withheld
```

### 4.3 CRITICAL nodes & fail-closed semantics

A CRITICAL node failing aborts the pipeline rather than producing a degraded
result:
- **AdversarialManipulationResistance** — poisoned corpus must not reach scoring.
- **EntityResolve** — bad resolution is the single largest phantom-moat risk;
  it must emit measured P/R + an audit log or it raises `CriticalNodeFailure`.
- **HypothesisHarness** — enforces the S0 gate; raises `GatingHalt` semantics
  (returned as `verdict=phantom_moat, gating_halt="H0/H5"`).
- **LegalStandingLayer** — if neither legal layer is specifiable, raises
  `CriticalNodeFailure` (project defect). Currently passes (`fail_closed_ok=True`).

---

## 5. Hypotheses Reference (H0–H7)

Pre-registered in `docs/02_concretization.md` §6.1; implemented in
`engine/harness.py`. δ/θ/α/r are fixed constants in `harness.py`.

| # | Hypothesis | Pre-registered threshold | Statistical test | Falsified when |
|---|---|---|---|---|
| **H0** scale-existence *(S0 gate)* | Track O exists at production scale | ≥10 assets, each ≥1000 unit/yr & ≥95% uptime & ≥24 mo, **AUDITED only** | count + binomial CI | < 5 admissible audited assets |
| **H5** structural-blindness *(S0 gate)* | Exclusion is structural, not quality-filter / sub-tier-embedded | blind tech-maturity non-inferior to Track P (δ=0.10); SBOM embed-rate < 0.20 | non-inferiority test + DependencyPenetration | maturity inferior OR embed-rate ≥ 0.20; **INCONCLUSIVE** if maturity uncollected |
| **H1** independent disjointness | Independently-deployed OSS set is disjoint from policy-capital set | overlap ≤ θ₁ = 0.15; only graded-visibility < 0.3 counts as "blind" | EntityResolve P/R + bootstrap CI | overlap > 0.15 (list-absence alone is *not* evidence — tautology guard) |
| **H2** unit-economics | Blind payback per comparable functional unit materially shorter, full-lifecycle | Δpayback ≥ 20% & p < 0.05 (bootstrapped); TCO incl. ComplianceCostOverlay | Mann–Whitney U + bootstrap | Δ < 20% OR p ≥ 0.05 OR advantage gone after compliance cost |
| **H3** policy↔moat *(competing)* | Which of a/b/c holds (self-reinforcement is **not** assumed) | H3a iff Pearson r > 0.5 (policy-spend vs graded blind-width, lagged); else H3b absorbed / H3c destroyed | time-series corr + difference-in-differences | r ≤ 0 or horizontal-reg density ↑ ⇒ blind-width ↓ ⇒ H3c |
| **H4** executability | Monetization pair is executable AND a proxy-portfolio shows excess return | tradable proxy exists, THEN pre-registered 18–30 mo backtest Sharpe > 1.0 OOS | executability gate → backtest | no liquid proxy (private integrators) → **monetization auto-retire** |
| **H6** regulatory-absorption | Horizontal regulation has not absorbed the blind spot within T_window | 0 applicable mandatory manufacturing-software cert/SBOM/audit instruments | regulatory-horizon scan + survival | ≥ 1 applicable instrument in force/announced ⇒ T_window shrinks, supports H3c |
| **H7** market-efficiency | Track-O threat is not yet priced into incumbents | event-study abnormal return α ≠ 0 (significant) | event study / cross-sectional regression | α ≈ 0 ⇒ already priced ⇒ monetization void, analysis-tool only |

DEFER D1 = **(가)**: the monetization signal is **retained** but repositioned
from "permanent alpha" to a "regulatory-arbitrage half-life window" with a
mandatory expiry, gated by H4 and H7. If H4 fails (no tradable proxy), the signal
auto-retires while the analysis-tool role is kept.

---

## 6. The Engine Codebase

Location: `D:\AAI\A3IE\BlindSpotMoat\engine\`. Pure Python 3 (stdlib only —
no external dependencies). Runs on Windows/macOS/Linux.

### 6.1 Layout

```
engine/
  __init__.py            # version 0.2.0, codename NULLTRACK, honesty docstring
  errors.py              # EngineError, ContractViolation, CriticalNodeFailure, GatingHalt
  contracts.py           # SourceClass, Provenance, Asset, DeploymentEvidence, Corpus,
                          # ResolvedPairs, VisibilityScoredAsset, ScoredAsset, TTCIndex,
                          # TestResult, HypothesisReport, StandingSpec,
                          # MonetizationSignal, AuditReport
  harness.py             # H0–H7 implementations, thresholds, gating order
  pipeline.py            # dry_run(), execute(), report_to_dict()
  __main__.py            # CLI
  fixtures/              # vintage-snapshot data (currently 6-AI cross-verified real)
    trackP.json          #   listed incumbents + subsidy anchors (public_unaudited)
    trackO.json          #   14 real OSS repos, deployments=[] (H0 honestly unavailable)
    sbom.json            #   {} empty — no public SBOM disclosure (pre-CRA-2027)
    defunct.json         #   [] empty — survivorship corpus not AI-collectable
    reg_watchlist.json   #   CRA/NIS2/IEC62443 (audited, primary EU sources)
  nodes/
    ingestion.py adversarial.py survivorship.py entity_resolve.py
    visibility_graph.py unit_economics.py reg_absorption.py ttc.py
    ts_stability.py legal_standing.py surfacing.py erosion.py reporting.py
```

### 6.2 Key modules

- **`contracts.py`** — all typed dataclasses. `Provenance.admissible` is the A8
  gate (`audited` only). `SourceClass` enum has 5 members.
- **`ingestion.py`** — `DataIngestion()` loads the 5 fixtures, maps each file's
  `_meta.source_class` to a `Provenance`, builds the `Corpus`. `_derive_blind_
  width_series` produces an intentionally **non-monotone** proxy so H3
  self-reinforcement can never be assumed.
- **`entity_resolve.py`** — `_GROUND_TRUTH` is the adjudicated map; emits
  precision/recall and a manual-audit log; raises `CriticalNodeFailure` if it
  cannot measure P/R.
- **`visibility_graph.py`** — graded visibility weights (`press 0.2 / VC 0.6 /
  NZIA 1.0`); `_BLIND_CEIL = 0.3`; `blind_assets()` = visibility < 0.3 **and not**
  SBOM-embedded.
- **`harness.py`** — pre-registered constants at top
  (`H0_MIN_ASSETS=10`, `H2_MIN_DELTA=0.20`, `H2_ALPHA=0.05`,
  `H3_MIN_PEARSON=0.5`, `H4_SHARPE_MIN=1.0`, …). `HypothesisHarness()` evaluates
  H0,H5 first and returns early with `verdict="phantom_moat"` if either is
  falsified. Stdlib-only Pearson and bootstrap helpers.
- **`pipeline.py`** — `dry_run()` validates contracts/gates without executing;
  `execute()` runs the full dependency order; `report_to_dict()` serializes.
- **`reporting.py`** — `MonetizationSignal` voided under gating halt;
  `_honest_report()` carries `empirical_provenance` (the 6-AI robustness
  statement) and `empirical_certification_requires` (the audited shopping list).

### 6.3 Fixtures & provenance (current state)

Fixtures were upgraded from `illustrative` scaffolding to **real, 6-AI
cross-verified `public_unaudited` data**:
- `trackP.json` — real listed incumbents (Rockwell ROK, Siemens SIE.DE, Cognex
  CGNX, Emerson EMR, Keyence) + CRMA/IRA subsidy anchors. *Note*: the original
  "NZIA 47-entry" premise was a **category error** — the real audited "47" is the
  **CRMA critical-raw-materials** list, not an NZIA manufacturing-software list.
  Corrected; Track P comparator redefined to listed vendors.
- `trackO.json` — 14 **real verifiable** repos (Carbon, qcadoo MES, Apache
  PLC4X, OpenPLC, United Manufacturing Hub, Eclipse BaSyx/4diac,
  Open-Industry-Project, Klipper, Hexastorm, InternVL3-NPU, SimpleMES, WEB_MES,
  mechsoftronic). The original seed names (Klipper-MES, RK3588-DefectNet-Tiny,
  FPGA-laser-sync, ros2-tropical) were **confirmed illustrative** (do not exist
  as named); functional substitutes are listed. **`deployments=[]` for every
  asset** — this is the honest representation of "no audited H0 evidence".
- `sbom.json` = `{}`, `defunct.json` = `[]` — empty by *empirical absence*, not
  omission (6/6 collectors confirmed structurally unavailable / not AI-collectable).
- `reg_watchlist.json` — `audited` (regulatory text is an official verifiable
  fact), primary EU sources.

---

## 7. Operating the Engine

### 7.1 Prerequisites
- Python 3.10+ (tested on 3.14). No `pip install` — stdlib only.
- Working directory = project root `D:\AAI\A3IE\BlindSpotMoat`.

### 7.2 Dry-run (validate contracts & gates, no execution)

```
cd D:\AAI\A3IE\BlindSpotMoat
python -m engine --mode dry-run
```

Expected (current): `p_set=7, o_set=14, sbom_edges=0, reg_instruments=5,
all_provenance_tagged=true, any_audited_source=true`, gating order printed,
`legal_standing fail_closed_ok=true`. This proves the wiring is correct.

### 7.3 Execute (full pipeline)

```
python -m engine --mode execute            # human-readable
python -m engine --mode execute --json     # machine-readable
```

Expected (current, on real 6-AI data):

```
VERDICT        : phantom_moat
GATING HALT    : H0/H5
  [FALSIFIED   ] H0_ScaleExistence   observed: 0 audited production-scale assets
  [INCONCLUSIVE] H5_StructuralBlind  observed: maturity uncollected
MONETIZATION   : enabled=False  (S0 gating halt → no signal emitted)
LEGAL STANDING : fail_closed_ok=True (2-layer, RECIP abandoned)
HONEST REPORT  : inputs are 6-AI cross-verified real public_unaudited;
                 audited deployment/TCO structurally unavailable (6/6);
                 phantom_moat is empirically robust, not a fixture artifact.
```

### 7.4 How to interpret the output

| Field | Meaning |
|---|---|
| `verdict = phantom_moat` | S0 gate failed → no moat assertion is made. **Correct & expected** until audited data exists. |
| `gating_halt = H0/H5` | The pipeline stopped at the existence/structural gate; H1–H7 were *not* evaluated (by design). |
| `H0 FALSIFIED` | 0 assets with **audited** ≥1000 u/yr & ≥95% uptime & ≥24 mo. Public data cannot satisfy this (§8). |
| `H5 INCONCLUSIVE` | Tech-maturity was not in the public collection → cannot disambiguate structural-blind vs quality-filter. Honest "don't know", not a pass. |
| `monetization enabled=False` | Voided under gating halt; also independently confirmed by H4 (no tradable proxy, 6/6). |
| `empirical_provenance` | States the verdict is robust because 6 independent AIs confirmed the gap with `fabricated_values=0`. |

If you ever see `verdict != phantom_moat`, it means audited deployment data was
ingested and H0 passed — at that point the full H1–H7 chain runs.

---

## 8. Current State & How to Advance It

### 8.1 State: *evidence-blocked provisional*

The 7-AI design review (`docs/06_review_synthesis.md`, ADOPT A1–A9) and the 6-AI
data collection (`data_collection/COLLATION.md`) jointly establish:
- The methodology is sound and runs end-to-end.
- The idea is **not falsified** — but it is **not certifiable from public data**.
- 6 independent web AIs (grok/deepseek/kimi/qwen/gemini/perplexity),
  `fabricated_values=0`, converge: audited H0 deployment evidence, audited H2
  TCO, and SBOM embedding are **structurally unavailable** (shadow-IT /
  air-gapped OT / NDA); regional-integrator tradable proxy = **false** (H4 fails).
- (One collection response — chatgpt — was **rejected** as off-topic; it did not
  follow the schema.)

This is recorded honestly: the idea is held, not discarded. Discarding it would
be as dishonest as accepting it.

### 8.2 The only path forward (`data_collection/AUDITED_GAP_HANDOFF.md`)

The blocking gates are **H0 and H2 only**. Both need *audited* primary data that
is not on the public web. Tiering:

| Tier | Gap | Method | AI-collectable? |
|---|---|---|---|
| T1 (time-locked) | SBOM embedding | wait for EU CRA SBOM mandate (~2027) | n/a |
| T2 (data engineering) | survivorship corpus, policy-spend series, H7 universe | archive scrape / public stats | partially yes |
| T3 (paid data) | TCO benchmarks, SCA-derived SBOM | paid consulting / Black Duck-style SCA | no |
| **T4 (field research)** | **H0 & H2 (Track-O side)** | **NDA integrator interviews + factory site visits + certification-body data** | **NO — human/field track only** |

**T4 is the only route that can change the verdict.** Protocol (full detail in
the handoff doc): sample ≥10 D1 brownfield deployments via regional system
integrators; interview plant OT leads, SI PMs, certification auditors; accept
only independent-audit / certification-record / verified-1st-party-telemetry as
`SourceClass.AUDITED`; capture full provenance incl. auditor identity.

### 8.3 Re-injecting audited data (how the verdict could flip)

When audited evidence arrives, write it into the fixtures:

```
trackO.json  →  each asset.deployments[] += {annual_unit_volume, uptime_pct,
                 months_in_production}   with _meta.source_class:"audited"
trackO/P     →  reported_payback_weeks + payback_basis:"full_lifecycle"
                 + compliance_cost_included:true + source_class:"audited"
re-run:  python -m engine --mode execute
```

If ≥10 audited assets clear H0 **and** H5 passes, the gate opens and H1 → {H2,
H3, H6} → H4 → H7 run. Only then can the verdict become `supported` /
`partial(...)`. Until then the engine will continue to honestly return
`phantom_moat`.

---

## 9. Extending the Engine

- **Add a hypothesis**: add a `_hN()` to `harness.py` returning a `TestResult`;
  wire it into `HypothesisHarness()` respecting the gating order; pre-register
  its threshold in `docs/02_concretization.md` §6.1 *before* coding it.
- **Add a node**: create `engine/nodes/<name>.py` returning a typed contract;
  insert into `pipeline.execute()` at the correct dependency position; update
  `.pgf/DESIGN-BlindSpotMoat.md` and `05_design.md` (design is canonical).
- **Add data**: only add to fixtures with an honest `source_class`. Never
  upgrade self-reported/public_unaudited to `audited` without a real audit. The
  engine is designed so that lying to it produces a *false* `supported` — the
  AdversarialManipulationResistance + Provenance gates exist to prevent this.
- **Change a threshold**: thresholds are pre-registered. Changing one after
  seeing data is goalpost-moving and must be recorded in `02 §6` with rationale
  and date.

---

## 10. Appendix

### 10.1 Document map

| Path | Content |
|---|---|
| `docs/00_idea_card.md` | Immutable idea record (§1–7) + §8 7-AI review annotation + §9 data-collection corroboration |
| `docs/01_domain_selection.md` | Domain matrix → D1 chosen |
| `docs/02_concretization.md` | rev2; §6 = pre-registered H0–H7 |
| `docs/03_risk_rebuttal.md` | R1–R5 risk rebuttals |
| `docs/04_project_charter.md` | Form (a), success gates S1–S6 |
| `docs/05_design.md` | **Canonical** PGF Gantree + PPR (v0.2) |
| `docs/06_review_synthesis.md` | 7-AI review → ADOPT A1–A9 / DEFER D1–D3 |
| `docs/07_technical_specification.md` | **This document** |
| `.pgf/DESIGN|WORKPLAN-…md`, `status-….json` | PGF execution artifacts |
| `review_process/` | 7-AI design-review prompt + responses + synthesis |
| `data_collection/DATA_REQUEST.md` | Universal data-collection prompt |
| `data_collection/COLLATION.md` | 6-AI cross-collation (6/6 convergence) |
| `data_collection/AUDITED_GAP_HANDOFF.md` | What audited data is needed, where it lives, T1–T4 |
| `engine/` | The Python implementation |

### 10.2 Glossary

- **Track P / Track O** — policy-visible vs open-source-invisible manufacturing tracks.
- **RESDEL** — resource-deletion lens (delete the scarce resource, redesign around absence).
- **illegibility** — being unrecognizable to procurement/policy frameworks (not literal invisibility).
- **T_window** — finite duration the arbitrage survives before regulatory absorption.
- **phantom_moat** — verdict: a blind spot that cannot be shown to be a real exploitable moat with audited data.
- **evidence-blocked provisional** — the idea's state: not accepted, not discarded, blocked on non-public data.
- **A8 / honesty invariant** — only `audited` data is admissible as empirical evidence.
- **S0 gate** — H0 & H5; the pipeline halts here on current data.
- **CRITICAL node** — failure aborts the pipeline (fail-closed) rather than degrading silently.
- **PGF** — PPR/Gantree Framework (the design + execution methodology).

### 10.3 Provenance chain (immutable)

```
SDX v1.3 → TCX-20260514-001 → IDX-20260514-001
        → CIX-20260514-001 (cross-model certified; surprise 10.0; total 8.12)
        → EVX-20260516-001 (dual winner, winners_identical=true)
        → aox-20260516T000000Z-resume
7-AI design review (2026-05-16, 7/7 revise) → ADOPT A1–A9, DEFER D1=(가)
6-AI data collection (2026-05-16, 6/6, fabricated 0) → phantom_moat robust
Technical specification (this doc) — 2026-05-17
```

### 10.4 The one-paragraph summary

BlindSpotMoat is a falsifiable analysis engine for the hypothesis that
policy-illegible open-source manufacturing-retrofit stacks form a finite economic
arbitrage. It is engineered to accept only audited evidence. Because the audited
evidence required to prove the claim does not exist in the public domain —
independently confirmed by six AIs with zero fabrication — the engine correctly,
honestly returns `phantom_moat` and holds the idea as *evidence-blocked
provisional*. Advancing it requires non-public field research (T4), not more
analysis or more public data.
