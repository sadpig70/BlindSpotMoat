"""UnitEconomicsScoring + ComplianceCostOverlay — A6 / CONV-3.

payback per comparable functional unit (not pilot capex) + full-lifecycle TCO
including certification / V&V / SBOM / liability cost (ComplianceCostOverlay).
All payback inputs here are self-reported -> narrative, not admissible (A8).
"""

from __future__ import annotations

from ..contracts import ScoredAsset, VisibilityScoredAsset

# Illustrative compliance overlay (weeks) by topic exposure. Real run: audited.
_COMPLIANCE_WEEKS = {
    "mes": 9.0, "scada": 9.0, "factory-software": 8.0,
    "defect-detection": 6.0, "machine-vision": 6.0,
    "laser": 7.0, "motion-control": 7.0, "fpga": 5.0,
    "edge-ai": 4.0, "robotics": 8.0, "ndt": 6.0, "cnc": 7.0,
}


def _compliance_cost(asset) -> float:
    if not asset.topics:
        return 4.0
    return max(_COMPLIANCE_WEEKS.get(t, 4.0) for t in asset.topics)


def UnitEconomicsScoring(scored: list[VisibilityScoredAsset]) -> list[ScoredAsset]:
    out: list[ScoredAsset] = []
    for s in scored:
        a = s.asset
        base = a.reported_payback_weeks
        comp = _compliance_cost(a)
        # comparable-functional-unit normalization via deploy friction
        cfu = None if base is None else round(base * (1.0 + a.deploy_friction), 2)
        full = None if cfu is None else round(cfu + comp, 2)
        out.append(ScoredAsset(asset=a, payback_per_cfu=cfu,
                               compliance_cost_weeks=comp,
                               full_lifecycle_payback=full,
                               visibility=s.visibility))
    return out
