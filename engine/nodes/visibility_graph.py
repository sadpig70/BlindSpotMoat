"""VisibilityGraph — A3 (replaces boolean set-difference; CONV-2 7/7).

Graded visibility 0..1 (NOT boolean), multi-hop graph, and DependencyPenetration:
OSS embedded sub-tier inside a Track P entity (per SBOM) is excluded from blind
(false-blind guard — Qwen strongest objection).
"""

from __future__ import annotations

from ..contracts import Corpus, ResolvedPairs, VisibilityScoredAsset

# graded visibility weights (02 §6.1 / Kimi CONV-2): press .2 / VC .6 / NZIA 1.0
_W_TRADE_PRESS = 0.2
_W_VC = 0.6
_W_NZIA = 1.0
_BLIND_CEIL = 0.3        # H1: only graded-visibility < 0.3 counts as 'blind'
_BOUNDARY = 0.05         # near-threshold -> human review


def _graded_visibility(o, corpus: Corpus, pairs: dict) -> float:
    """Max visibility surface the asset is exposed through (0..1)."""
    v = 0.0
    if o.asset_id in pairs:                       # resolved to a listed P entity
        v = max(v, _W_NZIA)
    for p in corpus.p_set:
        if set(o.topics) & set(p.topics):         # topic appears on a listed track
            if p.credit_type and "NZIA" in p.credit_type:
                v = max(v, _W_VC)                 # adjacent, not directly listed
            else:
                v = max(v, _W_TRADE_PRESS)
    # popularity as a weak trade-press proxy
    if o.forks >= 1000:
        v = max(v, _W_TRADE_PRESS)
    return round(min(v, 1.0), 3)


def _policy_path(o, corpus: Corpus, pairs: dict) -> list[str]:
    """Multi-hop: asset -> component -> integrator -> deployment -> procurement -> policy."""
    path = [o.asset_id]
    embed = corpus.sbom_graph.get(o.asset_id)
    if embed:
        path += ["component", embed[0], "procurement", "policy"]
    elif o.asset_id in pairs:
        path += ["integrator", pairs[o.asset_id], "policy"]
    return path


def VisibilityGraph(corpus: Corpus, pairs: ResolvedPairs) -> list[VisibilityScoredAsset]:
    out: list[VisibilityScoredAsset] = []
    for o in corpus.o_set:
        embedded = o.asset_id in corpus.sbom_graph      # DependencyPenetration
        v = _graded_visibility(o, corpus, pairs.pairs)
        out.append(VisibilityScoredAsset(
            asset=o,
            visibility=v,
            embedded_in_P=embedded,
            policy_path=_policy_path(o, corpus, pairs.pairs),
            needs_human_review=abs(v - _BLIND_CEIL) <= _BOUNDARY,
        ))
    return out


def blind_assets(scored: list[VisibilityScoredAsset]) -> list[VisibilityScoredAsset]:
    """'Blind' = low graded visibility AND not embedded sub-tier in Track P."""
    return [s for s in scored
            if s.visibility < _BLIND_CEIL and not s.embedded_in_P]
