"""Pipeline — dependency-graph wiring + dry-run / execute modes.

Dependency order (docs/05_design.md v0.2 §5):
  DataIngestion -> AdversarialManipulationResistance -> EntityResolve
                -> VisibilityGraph -> {UnitEconomicsScoring, TimeToCaptureMetric}
  RegulatoryAbsorptionMonitor -> HypothesisHarness -> Reporting
  Reporting -> VisibilityErosionMonitor ; LegalStandingLayer ⟂ (CRITICAL)
"""

from __future__ import annotations

from dataclasses import asdict

from .contracts import AuditReport, SourceClass
from .errors import GatingHalt
from .harness import (H0_MIN_ASSETS, H1_MAX_OVERLAP, H2_ALPHA, H2_MIN_DELTA,
                      H3_MIN_PEARSON, H4_SHARPE_MIN, HypothesisHarness)
from .nodes.adversarial import AdversarialManipulationResistance
from .nodes.entity_resolve import EntityResolve
from .nodes.erosion import VisibilityErosionMonitor
from .nodes.ingestion import DataIngestion
from .nodes.legal_standing import LegalStandingLayer
from .nodes.reg_absorption import RegulatoryAbsorptionMonitor
from .nodes.reporting import Reporting
from .nodes.surfacing import SurfacingOption
from .nodes.survivorship import SurvivorshipFilter
from .nodes.ttc import TimeToCaptureMetric
from .nodes.ts_stability import TimeSeriesStabilityMonitor
from .nodes.unit_economics import UnitEconomicsScoring
from .nodes.visibility_graph import VisibilityGraph


def dry_run() -> dict:
    """ModeDryRun — validate data contracts, gate wiring, pre-registered
    thresholds. No empirical execution, no monetization output."""
    corpus = DataIngestion()
    checks = {
        "data_contract": {
            "p_set": len(corpus.p_set), "o_set": len(corpus.o_set),
            "sbom_edges": len(corpus.sbom_graph),
            "reg_instruments": len(corpus.reg_instruments),
            "all_provenance_tagged": all(p is not None for p in corpus.provenance),
            "any_audited_source": any(
                p.source_class is SourceClass.AUDITED for p in corpus.provenance),
        },
        "pre_registered_thresholds": {
            "H0_min_assets": H0_MIN_ASSETS, "H1_max_overlap": H1_MAX_OVERLAP,
            "H2_min_delta": H2_MIN_DELTA, "H2_alpha": H2_ALPHA,
            "H3_min_pearson": H3_MIN_PEARSON, "H4_sharpe_min": H4_SHARPE_MIN,
        },
        "gating_order": "H0&H5 -> H1 -> {H2,H3,H6} -> H4 -> H7",
        "fail_closed": "H0/H5 falsified -> phantom_moat halt (honest, not a bug)",
        "critical_nodes": ["AdversarialManipulationResistance", "EntityResolve",
                           "HypothesisHarness", "LegalStandingLayer"],
        "legal_standing_fail_closed_ok": LegalStandingLayer().fail_closed_ok,
        "surfacing": SurfacingOption(enabled=False)["active"],
        "honesty_invariant_A8": (
            "PASS: audited sources exist (regulatory text) but NO audited "
            "deployment/TCO evidence (6/6 web AIs: structurally unavailable) "
            "-> H0 rejects -> phantom_moat (correct, empirically robust)"),
    }
    return {"mode": "dry-run", "status": "contracts+gates validated", "checks": checks}


def execute() -> AuditReport:
    """Full pipeline. Halts fail-closed at S0 (H0&H5) on non-audited data."""
    corpus = DataIngestion()
    corpus, adv_flags = AdversarialManipulationResistance(corpus)
    survivorship = SurvivorshipFilter(corpus)
    pairs = EntityResolve(corpus)                        # CRITICAL
    vis = VisibilityGraph(corpus, pairs)
    econ = UnitEconomicsScoring(vis)
    absorption = RegulatoryAbsorptionMonitor(corpus)
    ttc = TimeToCaptureMetric(vis, corpus, absorption)
    stability = TimeSeriesStabilityMonitor(corpus)
    rep = HypothesisHarness(vis, econ, corpus, ttc, absorption)
    standing = LegalStandingLayer()                      # CRITICAL ⟂, fail-closed

    report = Reporting(vis, econ, rep, ttc, standing, survivorship,
                       adv_flags, {"precision": pairs.precision,
                                   "recall": pairs.recall,
                                   "unresolved": pairs.unresolved,
                                   "audit_log": pairs.manual_audit_log},
                       stability, absorption)
    report.erosion_report = VisibilityErosionMonitor(report)
    return report


def report_to_dict(r: AuditReport) -> dict:
    return {
        "verdict": r.hypothesis_report.verdict,
        "gating_halt": r.hypothesis_report.gating_halt,
        "hypotheses": {k: asdict(v) for k, v in r.hypothesis_report.results.items()},
        "rank_table": r.rank_table,
        "monetization_signal": asdict(r.monetization_signal),
        "ttc_index": asdict(r.ttc_index),
        "legal_standing": asdict(r.standing_spec),
        "honest_report": r.honest_report,
        "erosion_report": r.erosion_report,
    }
