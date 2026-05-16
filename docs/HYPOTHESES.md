# HYPOTHESES — Pre-registered H0–H7

> All thresholds are **pre-registered** (fixed before seeing data) to prevent
> goalpost-moving. Implemented in `engine/harness.py`; constants live at the top
> of that file. Changing any threshold after seeing data must be recorded with
> rationale and date — that is the anti-fudge contract.

## Gating order (enforced)

```
H0 (scale) & H5 (structural)        ── S0 GATE ──┐  either falsified → phantom_moat, STOP
                                                  ▼
H1 (independent-deploy disjointness)
                                                  ▼
{ H2 (unit-economics) · H3 (policy↔moat) · H6 (reg-absorption) }   parallel
                                                  ▼
H4 (executability → proxy-portfolio)   fail → monetization auto-retire
                                                  ▼
H7 (market-efficiency)                 fail → signal already priced → void
```

A hypothesis is **never** evaluated until its predecessors pass. On current data
only H0 and H5 appear in the output because S0 halts the pipeline first — this is
by design.

## Specification

| # | Hypothesis | Pre-registered threshold | Test | Falsified when |
|---|---|---|---|---|
| **H0** scale-existence *(S0 gate)* | Track O exists at production scale | ≥10 assets, each ≥1000 unit/yr **and** ≥95% uptime **and** ≥24 months in production — **AUDITED source only** | count + binomial CI | < 5 admissible audited assets |
| **H5** structural-blindness *(S0 gate)* | Exclusion is structural, not a quality filter / sub-tier embed | blind tech-maturity non-inferior to Track P (margin δ = 0.10) **and** SBOM embed-rate < 0.20 | non-inferiority + DependencyPenetration | maturity inferior, OR embed-rate ≥ 0.20. **INCONCLUSIVE** if maturity uncollected (honest "don't know", not a pass) |
| **H1** independent disjointness | Independently-deployed OSS set disjoint from policy-capital set | overlap ≤ θ₁ = 0.15; only graded-visibility < 0.3 counts as "blind" | EntityResolve P/R + bootstrap CI | overlap > 0.15. (List-absence alone is **not** evidence — tautology guard.) |
| **H2** unit-economics | Blind payback per comparable functional unit materially shorter, full-lifecycle | Δpayback ≥ 20% **and** p < 0.05 (bootstrapped); TCO must include ComplianceCostOverlay | Mann–Whitney U + bootstrap | Δ < 20%, OR p ≥ 0.05, OR advantage vanishes after compliance cost |
| **H3** policy↔moat *(competing — self-reinforcement NOT assumed)* | Determine which of a/b/c holds | **H3a** iff Pearson r > 0.5 (policy-spend vs graded blind-width, lagged); else **H3b** absorbed / **H3c** destroyed | time-series correlation + difference-in-differences | r ≤ 0, or horizontal-reg density ↑ ⇒ blind-width ↓ ⇒ H3c |
| **H4** executability | Monetization pair executable **and** proxy-portfolio shows excess return | a tradable proxy exists, THEN pre-registered 18–30 month backtest Sharpe > 1.0 out-of-sample | executability gate → backtest | no liquid proxy (private integrators) ⇒ **monetization auto-retire** |
| **H6** regulatory-absorption | Horizontal regulation has not absorbed the blind spot within T_window | 0 applicable mandatory manufacturing-software cert/SBOM/audit instruments | regulatory-horizon scan + survival | ≥ 1 applicable instrument in force/announced ⇒ T_window shrinks, supports H3c |
| **H7** market-efficiency | Track-O threat not yet priced into incumbents | event-study abnormal return α ≠ 0 (significant) | event study / cross-sectional regression | α ≈ 0 ⇒ already priced ⇒ monetization void, analysis-tool only |

## The monetization signal (DEFER D1 = option (가))

The long/short "monetization signal" was **retained but repositioned**: it is no
longer "permanent alpha". It is a *regulatory-arbitrage half-life window* with a
mandatory expiry, **gated by H4 and H7**. If H4 fails (no tradable proxy — the
current, 6/6-confirmed reality), the signal **auto-retires** and the engine keeps
only its analysis-tool role. It is never an investment recommendation.

## Current evaluation (real 6-AI data)

- **H0 → FALSIFIED**: 0 assets with audited production-scale deployment evidence.
  6 independent web AIs confirmed this is structurally unavailable publicly.
- **H5 → INCONCLUSIVE**: tech-maturity not in any public collection → cannot
  disambiguate structural-blind vs quality-filter.
- **S0 halts.** H1–H7 are not evaluated. Verdict = `phantom_moat`.

To change this, audited deployment + TCO data must be ingested (see
`DATA_COLLECTION.md §4`); only then do H1 → {H2,H3,H6} → H4 → H7 run.
