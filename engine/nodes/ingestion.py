"""DataIngestion — TrackP/O/SupplyChain ingest + AuditedProvenance + Normalize.

docs/05_design.md v0.2 §1 DataIngestion. Loads vintage-snapshot fixtures and
tags every record with Provenance. Fixtures are SourceClass.ILLUSTRATIVE, so
nothing here is admissible as empirical evidence (A8).
"""

from __future__ import annotations

import json
from pathlib import Path

from ..contracts import (Asset, Corpus, DeploymentEvidence, Provenance,
                          SourceClass)
from ..errors import ContractViolation

FIXTURES = Path(__file__).resolve().parent.parent / "fixtures"


_SC_MAP = {
    "audited": SourceClass.AUDITED,
    "public_unaudited": SourceClass.PUBLIC_UNAUDITED,
    "self_reported": SourceClass.SELF_REPORTED,
    "illustrative": SourceClass.ILLUSTRATIVE,
}


def _prov(meta: dict) -> Provenance:
    raw = meta.get("source_class")
    if raw:
        sc = _SC_MAP.get(raw, SourceClass.ILLUSTRATIVE)
    else:
        sc = SourceClass.AUDITED if meta.get("audited") else SourceClass.ILLUSTRATIVE
    return Provenance(source=meta.get("source", "unknown"), source_class=sc,
                      vintage=meta.get("vintage", "unknown"),
                      audited=(sc is SourceClass.AUDITED))


def _load(name: str) -> dict:
    path = FIXTURES / name
    if not path.exists():
        raise ContractViolation(f"missing fixture: {name}")
    return json.loads(path.read_text(encoding="utf-8"))


def DataIngestion() -> Corpus:
    p_raw = _load("trackP.json")
    o_raw = _load("trackO.json")
    sbom_raw = _load("sbom.json")
    reg_raw = _load("reg_watchlist.json")

    p_prov = _prov(p_raw["_meta"])
    o_prov = _prov(o_raw["_meta"])

    p_set: list[Asset] = []
    for a in p_raw["assets"]:
        p_set.append(Asset(asset_id=a["asset_id"], name=a["name"], track="P",
                            topics=a.get("topics", []), aliases=a.get("aliases", []),
                            capex_eur=a.get("capex_eur"),
                            credit_type=a.get("credit_type"),
                            tech_maturity=a.get("tech_maturity", 0.0),
                            reliability=a.get("reliability", 0.0),
                            reported_payback_weeks=a.get("reported_payback_weeks"),
                            provenance=p_prov))

    o_set: list[Asset] = []
    for a in o_raw["assets"]:
        deps = [DeploymentEvidence(annual_unit_volume=d["annual_unit_volume"],
                                   uptime_pct=d["uptime_pct"],
                                   months_in_production=d["months_in_production"],
                                   provenance=o_prov)
                for d in a.get("deployments", [])]
        o_set.append(Asset(asset_id=a["asset_id"], name=a["name"], track="O",
                           topics=a.get("topics", []), aliases=a.get("aliases", []),
                           forks=a.get("forks", 0),
                           commit_freq_per_month=a.get("commit_freq_per_month", 0.0),
                           contributor_concentration=a.get("contributor_concentration", 0.0),
                           star_fork_ratio=a.get("star_fork_ratio", 0.0),
                           reported_payback_weeks=a.get("reported_payback_weeks"),
                           bom_usd=a.get("bom_usd"),
                           deploy_friction=a.get("deploy_friction", 0.0),
                           tech_maturity=a.get("tech_maturity", 0.0),
                           reliability=a.get("reliability", 0.0),
                           deployments=deps, provenance=o_prov))

    blind_width_series = _derive_blind_width_series(p_raw["policy_spend_series"])

    return Corpus(
        p_set=p_set,
        o_set=o_set,
        sbom_graph={k: list(v) for k, v in sbom_raw.get("edges", {}).items()},
        reg_instruments=reg_raw["instruments"],
        policy_spend_series=[(p, float(v)) for p, v in p_raw["policy_spend_series"]],
        blind_width_series=blind_width_series,
        provenance=[p_prov, o_prov, _prov(sbom_raw["_meta"]), _prov(reg_raw["_meta"])],
    )


def _derive_blind_width_series(spend_series) -> list[tuple[str, float]]:
    """Illustrative graded-blind-width proxy per period (DERIVED, narrative).

    Intentionally NOT monotone-with-spend so H3 cannot be assumed self-reinforcing.
    """
    out = []
    for i, (period, _) in enumerate(spend_series):
        # widens early, then compresses as horizontal-reg density rises (H3c shape)
        w = max(0.05, 0.45 - 0.06 * i)
        out.append((period, round(w, 3)))
    return out
