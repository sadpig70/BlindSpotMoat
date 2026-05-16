"""Typed data contracts for the BlindSpotMoat engine.

Mirrors docs/05_design.md v0.2 §3 (데이터 계약). Every value that participates in
an empirical claim must carry a Provenance with `audited` status (A8 invariant).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


# ---------------------------------------------------------------------------
# Provenance / honesty invariant (A8)
# ---------------------------------------------------------------------------

class SourceClass(str, Enum):
    AUDITED = "audited"                 # admissible as empirical evidence
    PUBLIC_UNAUDITED = "public_unaudited"  # real public data, not audited -> narrative
    SELF_REPORTED = "self_reported"     # README / marketing -> narrative only
    ILLUSTRATIVE = "illustrative"       # vintage scaffold fixture -> narrative only
    DERIVED = "derived"                 # computed from other provenanced values


@dataclass(frozen=True)
class Provenance:
    source: str
    source_class: SourceClass
    vintage: str                       # ISO date of the snapshot
    audited: bool                      # True only for SourceClass.AUDITED

    @property
    def admissible(self) -> bool:
        """Admissible as *empirical* evidence (A8). Narrative-flagged data is not."""
        return self.audited and self.source_class is SourceClass.AUDITED


def illustrative(source: str, vintage: str = "2026-05-16") -> Provenance:
    return Provenance(source=source, source_class=SourceClass.ILLUSTRATIVE,
                      vintage=vintage, audited=False)


# ---------------------------------------------------------------------------
# Assets / corpus
# ---------------------------------------------------------------------------

@dataclass
class DeploymentEvidence:
    annual_unit_volume: int            # H0: >=1000
    uptime_pct: float                  # H0: >=95.0
    months_in_production: int          # H0: >=24
    provenance: Provenance


@dataclass
class Asset:
    asset_id: str
    name: str
    track: str                         # "P" | "O"
    topics: list[str] = field(default_factory=list)
    aliases: list[str] = field(default_factory=list)
    # Track O activity signals
    forks: int = 0
    commit_freq_per_month: float = 0.0
    contributor_concentration: float = 0.0   # 0..1 (1 = single org -> astroturf risk)
    star_fork_ratio: float = 0.0
    reported_payback_weeks: Optional[float] = None
    bom_usd: Optional[float] = None
    deploy_friction: float = 0.0             # 0..1
    tech_maturity: float = 0.0               # 0..1 (H5 non-inferiority)
    reliability: float = 0.0                 # 0..1 (H5 non-inferiority)
    deployments: list[DeploymentEvidence] = field(default_factory=list)
    # Track P capital signals
    capex_eur: Optional[float] = None
    credit_type: Optional[str] = None
    provenance: Optional[Provenance] = None


@dataclass
class Corpus:
    p_set: list[Asset]
    o_set: list[Asset]
    sbom_graph: dict[str, list[str]]   # component -> embedded_in (Track P ids)
    reg_instruments: list[dict]        # RegulatoryAbsorptionMonitor watchlist hits
    policy_spend_series: list[tuple[str, float]]   # (period, eur) for H3
    blind_width_series: list[tuple[str, float]]    # (period, graded blind width) for H3
    provenance: list[Provenance] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Pipeline outputs
# ---------------------------------------------------------------------------

@dataclass
class ResolvedPairs:
    pairs: dict[str, str]              # O asset_id -> P asset_id
    precision: float
    recall: float
    manual_audit_log: list[str]
    unresolved: list[str]


@dataclass
class VisibilityScoredAsset:
    asset: Asset
    visibility: float                  # graded 0..1 (NOT boolean)
    embedded_in_P: bool                # SBOM DependencyPenetration
    policy_path: list[str]             # multi-hop shortest path to policy
    needs_human_review: bool


@dataclass
class ScoredAsset:
    asset: Asset
    payback_per_cfu: Optional[float]   # weeks per comparable functional unit
    compliance_cost_weeks: float       # ComplianceCostOverlay add-on
    full_lifecycle_payback: Optional[float]
    visibility: float


@dataclass
class TTCIndex:
    illegibility_span: float           # graded illegibility width
    t_window_months: Optional[float]   # estimated remaining arbitrage window
    half_life_months: Optional[float]  # regulatory half-life


@dataclass
class TestResult:
    name: str
    passed: bool
    falsified: bool
    threshold: str
    observed: str
    note: str = ""


@dataclass
class HypothesisReport:
    results: dict[str, TestResult]
    verdict: str                       # supported | partial(...) | phantom_moat
    falsified: list[str]
    gating_halt: Optional[str]
    data_vintage: str


@dataclass
class StandingSpec:
    layer1_contract: Optional[str]     # StandardCommercialContract
    layer2_dispute: Optional[str]      # StrategicVisibilityLayer
    accepted_cost_doc: str
    fail_closed_ok: bool               # True if at least one layer + cost doc present


@dataclass
class MonetizationSignal:
    """(가) retained — repositioned as a finite regulatory-arbitrage half-life
    window, NOT permanent alpha. Expiry + half-life mandatory; gated by H4 & H7."""
    pair: str
    enabled: bool
    expiry_estimate_months: Optional[float]
    half_life_months: Optional[float]
    gated_by: list[str]
    void_reason: str = ""


@dataclass
class AuditReport:
    rank_table: list[dict]
    monetization_signal: MonetizationSignal
    hypothesis_report: HypothesisReport
    ttc_index: TTCIndex
    standing_spec: StandingSpec
    honest_report: dict
    erosion_report: dict
