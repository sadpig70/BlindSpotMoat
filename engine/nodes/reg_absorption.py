"""RegulatoryAbsorptionMonitor — A6 (Kimi/Gemini/Qwen CONV-4/5).

Horizontal-regulation watchlist + assimilation-risk score. Leading indicator for
H3c (regulation destroys moat) and H6 (regulatory absorption inversion).
"""

from __future__ import annotations

from ..contracts import Corpus


def RegulatoryAbsorptionMonitor(corpus: Corpus) -> dict:
    instruments = corpus.reg_instruments
    applicable = [i for i in instruments
                  if i.get("applies_to_manufacturing_software")]
    mandatory = [i for i in applicable
                 if i.get("mandate_type") in
                 ("mandatory_cert_sbom", "certification", "audit_visibility")]
    # assimilation risk: share of in-force mandatory manufacturing-software regs
    in_force = [i for i in mandatory if i.get("status") in ("in_force", "expanding")]
    risk = round(len(in_force) / max(len(instruments), 1), 3)
    return {
        "applicable_instruments": [i["id"] for i in applicable],
        "mandatory_manufacturing_sw": [i["id"] for i in mandatory],
        "in_force_count": len(in_force),
        "assimilation_risk": risk,
        "h6_inversion_triggered": len(in_force) >= 1,   # >=1 -> moat T_window shrinks
        "note": ("horizontal regulation in force -> supports H3c (destroyed) over "
                 "H3a (self-reinforcing); moat is a finite window (A7)"),
    }
