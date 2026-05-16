# DESIGN — Architecture (PGF Gantree + Pipeline)

> Companion to `TECHNICAL_SPECIFICATION.md` (the master reference). This file is
> the standalone architecture view. Design version **v0.2** (post 7-AI review).

## Form

**(a) analysis / simulation tool.** Not a product, not a service. Inputs are
public-data snapshots; outputs are descriptive reports with explicit provenance.
Scope is frozen to **D1 = manufacturing brownfield retrofit** plus a thin D2
shadow probe (transferability check only).

## Gantree (functional decomposition)

```
BlindSpotMoat_Main
├─ DataIngestion                    load fixtures, tag Provenance, normalize
├─ AdversarialManipulationResistance  [CRITICAL] astroturf / dormant-fork filter
├─ SurvivorshipFilter               fold defunct repos + failure rate
├─ EntityResolve                    [CRITICAL] ground-truth + fuzzy + measured P/R
├─ VisibilityGraph                  graded 0–1 + multi-hop + DependencyPenetration
├─ UnitEconomicsScoring             payback/CFU + ComplianceCostOverlay
├─ TimeToCaptureMetric              regulatory half-life + remaining T_window
├─ TimeSeriesStabilityMonitor       ≥2 separated windows, drift alert
├─ RegulatoryAbsorptionMonitor      horizontal-reg watchlist (H3c/H6 indicator)
├─ HypothesisHarness                [CRITICAL] H0–H7 + gating order
├─ LegalStandingLayer               [CRITICAL] 2-layer spec, fail-closed
├─ SurfacingOption                  detached, default-OFF
├─ VisibilityErosionMonitor         [mandatory] observer-effect tracking
├─ Reporting                        RankTable + MonetizationSignal + HonestReport
└─ ModeDryRun                       contract/gate validation, no execution
```

## Node responsibilities

| Node | Input → Output | Notes |
|---|---|---|
| DataIngestion | fixtures → `Corpus{p_set,o_set,sbom_graph,reg_instruments,provenance[]}` | Every record gets a `Provenance`. `_derive_blind_width_series` is intentionally non-monotone so H3 self-reinforcement is never assumed. |
| AdversarialManipulationResistance | Corpus → cleaned Corpus + flags | Excludes burst-commit single-org repos, extreme contributor concentration; down-weights dormant forks. **CRITICAL** — a poisoned corpus must not reach scoring. |
| SurvivorshipFilter | Corpus → survivorship report | Failure rate + defunct payback folded in so survivors aren't cherry-picked. |
| EntityResolve | Corpus → `ResolvedPairs{pairs,precision,recall,audit_log,unresolved}` | Adjudicated ground truth + fuzzy/semantic + topic-ontology boost. Raises `CriticalNodeFailure` if P/R unmeasurable. **CRITICAL** — bad resolution is the #1 phantom-moat risk. |
| VisibilityGraph | Corpus + pairs → `VisibilityScoredAsset[]` | Graded visibility (press 0.2 / VC 0.6 / NZIA 1.0). SBOM-embedded assets are **excluded from "blind"** (false-blind guard). `blind = visibility < 0.3 AND not embedded`. |
| UnitEconomicsScoring | scored → `ScoredAsset[]` | Payback per comparable functional unit; ComplianceCostOverlay adds cert/V&V/SBOM/liability weeks. |
| TimeToCaptureMetric | scored + absorption → `TTCIndex{span,t_window,half_life}` | Moat is finite *by construction*: no half-life ⇒ no permanence claim. |
| RegulatoryAbsorptionMonitor | Corpus → absorption signal | Counts applicable mandatory manufacturing-software instruments → H6/H3c. |
| HypothesisHarness | scored + ttc + absorption → `HypothesisReport` | Evaluates H0–H7 in the gating order; halts at S0. **CRITICAL**. |
| LegalStandingLayer | — → `StandingSpec` | 2-layer: (1) standard commercial/IP/tort contract (orthogonal to illegibility); (2) dispute-only escrow/ZK reversible disclosure; + accepted-cost doc. Raises `CriticalNodeFailure` if neither layer specifiable. **CRITICAL**. |
| VisibilityErosionMonitor | report → erosion report | The engine's own output is an act of surfacing; warns the moat may be eroded *by* publication. **mandatory**. |
| Reporting | all → `AuditReport` | MonetizationSignal voided on gating halt / H4 fail. HonestReport carries the heuristic→empirical delta, provenance, residual risk. |

## Dependency graph

```
DataIngestion → AdversarialManipulationResistance → EntityResolve → VisibilityGraph
              → SurvivorshipFilter
VisibilityGraph → { UnitEconomicsScoring(+ComplianceCostOverlay), TimeToCaptureMetric }
RegulatoryAbsorptionMonitor → HypothesisHarness
{UnitEconomicsScoring, TimeToCaptureMetric, RegulatoryAbsorptionMonitor}
        → HypothesisHarness → Reporting → VisibilityErosionMonitor
LegalStandingLayer ⟂ (independent, CRITICAL, before Reporting)
SurfacingOption ⟂ (detached, default-OFF)
S0 gate (H0 & H5) fail ⇒ downstream output withheld → verdict phantom_moat
```

## Fail-closed semantics

A **CRITICAL** node failure aborts the pipeline rather than degrading silently.
**S0 gating** (`H0 & H5`) failing is *not* an error — it is the designed honest
outcome when audited existence/structural evidence is absent. `LegalStandingLayer`
currently passes (`fail_closed_ok = True`); RECIP (the original
"standing-while-invisible" idea) was abandoned because it is a logical
contradiction (see `REVIEW_SYNTHESIS.md`, CONV-1).

## Validation gates (S0–S6)

| Gate | Node | Pass condition |
|---|---|---|
| **S0** | HypothesisHarness H0&H5 | existence & structural — **fail ⇒ phantom_moat, stop** |
| S1 | DataIngestion + Adversarial + Survivorship | corpus + provenance tagged, astroturf filtered |
| S2 | EntityResolve | ground-truth + measured P/R + manual-audit log (CRITICAL) |
| S3 | VisibilityGraph | graded scores + DependencyPenetration (no boolean) |
| S4 | HypothesisHarness | gating order respected, H0·H5·H1·H2 at minimum |
| S5 | LegalStandingLayer | layer-1 OR layer-2 + accepted-cost doc (CRITICAL) |
| S6 | Reporting + VisibilityErosionMonitor | honest report + observer-effect warning |
