"""VisibilityErosionMonitor — A6 mandatory (Grok strongest objection).

Observer effect: the audit engine's own output is an act of surfacing. Track
whether previously-blind assets later appear in policy/VC/press, and warn that
publication may itself destroy the measured moat.
"""

from __future__ import annotations

from ..contracts import AuditReport


def VisibilityErosionMonitor(report: AuditReport) -> dict:
    ranked = [r["asset_id"] for r in report.rank_table]
    return {
        "watched_assets": ranked,
        "post_publication_appearances": [],   # populated across runs (vintage diff)
        "self_defeat_warning": (
            "Publishing this rank table and any monetization signal is itself a "
            "surfacing act. If watched assets appear in NZIA/VC/press in the next "
            "vintage, the measured blind spot is being eroded BY this engine. "
            "Treat all outputs as observer-perturbing (Grok CONV-5)."),
        "mitigation": "emit descriptive caveats; re-measure blind width each vintage",
    }
