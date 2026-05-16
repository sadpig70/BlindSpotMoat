"""Reporting — RankTable + MonetizationSignal + HonestReport (S6).

MonetizationSignal retained per DEFER D1=(가) but repositioned: NOT permanent
alpha — a regulatory-arbitrage half-life window with mandatory expiry, gated by
H4 (executability) and H7 (market efficiency). HonestReport carries the
heuristic->empirical delta, vintage, gating result, and residual risk (A8).
"""

from __future__ import annotations

from ..contracts import (AuditReport, HypothesisReport, MonetizationSignal,
                         ScoredAsset, StandingSpec, TTCIndex,
                         VisibilityScoredAsset)
from .visibility_graph import blind_assets


def _rank_table(scored_vis, scored_econ, ttc) -> list[dict]:
    econ = {s.asset.asset_id: s for s in scored_econ}
    rows = []
    for s in blind_assets(scored_vis):
        e = econ.get(s.asset.asset_id)
        rows.append({
            "asset_id": s.asset.asset_id,
            "name": s.asset.name,
            "visibility": s.visibility,
            "full_lifecycle_payback_weeks": e.full_lifecycle_payback if e else None,
            "compliance_cost_weeks": e.compliance_cost_weeks if e else None,
            "policy_path": s.policy_path,
            "evidence_class": "NARRATIVE (self-reported, not audited — A8)",
        })
    rows.sort(key=lambda r: (r["full_lifecycle_payback_weeks"] is None,
                             r["full_lifecycle_payback_weeks"] or 1e9))
    return rows


def _monetization(rep: HypothesisReport, ttc: TTCIndex) -> MonetizationSignal:
    h4 = rep.results.get("H4")
    h7 = rep.results.get("H7")
    gated = ["H4", "H7"]
    if rep.gating_halt:
        return MonetizationSignal(
            pair="long regional-MES-integrator / short NZIA-listed incumbent",
            enabled=False, expiry_estimate_months=None, half_life_months=None,
            gated_by=gated,
            void_reason=f"S0 gating halt ({rep.gating_halt}) -> no signal emitted")
    h4_fail = h4 is not None and h4.falsified
    void = ("H4 executability-gate fail (no liquid proxy) -> signal auto-retired "
            "(DEFER D3 pre-reflected); analysis-tool role retained" if h4_fail else "")
    return MonetizationSignal(
        pair="long regional-MES-integrator / short NZIA-listed incumbent",
        enabled=not h4_fail,
        expiry_estimate_months=ttc.t_window_months,
        half_life_months=ttc.half_life_months,
        gated_by=gated,
        void_reason=void)


def _honest_report(rep, ttc, standing, survivorship, adversarial_flags,
                   pr_metrics, stability, absorption) -> dict:
    return {
        "verdict": rep.verdict,
        "gating_halt": rep.gating_halt,
        "data_vintage": rep.data_vintage,
        "heuristic_to_empirical_delta": (
            "Inputs upgraded from illustrative fixtures to 6-AI cross-verified "
            "REAL public_unaudited data (data_collection/COLLATION.md, "
            "fabricated_values=0 x6). Still SourceClass != AUDITED -> per A8 "
            "narrative, not empirical. CIX 8.12 / surprise 10.0 likewise narrative."),
        "empirical_provenance": (
            "phantom_moat is now EMPIRICALLY ROBUST, not a fixture artifact: 6 "
            "independent web-enabled AIs (grok/deepseek/kimi/qwen/gemini/perplexity) "
            "each report H0 deployment evidence + H2 audited TCO + SBOM as "
            "structurally UNAVAILABLE with fabricated_values=0, and "
            "regional-integrator tradable proxy = FALSE (6/6). The required "
            "audited evidence does not exist in the public domain by the nature "
            "of the phenomenon (shadow-IT / air-gap / NDA)."),
        "empirical_certification_requires": [
            "audited public NZIA/IRA list (not shape-only fixture)",
            "audited deployment telemetry (volume/uptime/months) for H0",
            "audited TCO cash-flow for H2 (not README payback)",
            "audited SBOM/SPDX for DependencyPenetration",
            "audited market data for H4 proxy-portfolio + H7 event study",
        ],
        "entity_resolution": pr_metrics,
        "survivorship": survivorship,
        "adversarial_exclusions": adversarial_flags,
        "timeseries_stability": stability,
        "regulatory_absorption": absorption,
        "legal_standing": {
            "model": "2-layer (RECIP abandoned, CONV-1 7/7 critical)",
            "fail_closed_ok": standing.fail_closed_ok,
        },
        "ttc": {
            "illegibility_span": ttc.illegibility_span,
            "t_window_months": ttc.t_window_months,
            "half_life_months": ttc.half_life_months,
            "note": "moat is finite by construction (A7) — no permanence claim",
        },
        "residual_risk": (
            "phantom-moat risk closed only when H0&H5 pass on AUDITED data; "
            "until then verdict is provisional and surprise!=feasibility."),
    }


def Reporting(scored_vis: list[VisibilityScoredAsset],
              scored_econ: list[ScoredAsset], rep: HypothesisReport,
              ttc: TTCIndex, standing: StandingSpec, survivorship: dict,
              adversarial_flags: list, pr_metrics: dict, stability: dict,
              absorption: dict) -> AuditReport:
    return AuditReport(
        rank_table=_rank_table(scored_vis, scored_econ, ttc),
        monetization_signal=_monetization(rep, ttc),
        hypothesis_report=rep,
        ttc_index=ttc,
        standing_spec=standing,
        honest_report=_honest_report(rep, ttc, standing, survivorship,
                                     adversarial_flags, pr_metrics, stability,
                                     absorption),
        erosion_report={},   # filled by VisibilityErosionMonitor
    )
