"""AdversarialManipulationResistance — CRITICAL (A6 / Kimi+DeepSeek+Qwen CONV-5).

Detect astroturf / repo-farming / dormant forks before EntityResolve so the
corpus cannot be poisoned to inflate the blind spot.
"""

from __future__ import annotations

from dataclasses import replace

from ..contracts import Corpus

# Heuristic anomaly thresholds (deterministic; no embedding service — A8 honest).
_BURST_COMMIT = 150.0          # commits/mo from concentrated authorship
_CONC_MAX = 0.9                # contributor concentration (1 = single org)
_STAR_FORK_MIN = 0.3           # abnormally low engagement vs fork count


def _suspicious(a) -> str | None:
    if a.contributor_concentration >= _CONC_MAX and a.commit_freq_per_month >= _BURST_COMMIT:
        return "burst_commits_single_org"
    if 0 < a.star_fork_ratio < _STAR_FORK_MIN and a.forks > 0:
        return "low_star_fork_ratio_anomaly"
    if a.contributor_concentration >= 0.95:
        return "extreme_contributor_concentration"
    return None


def AdversarialManipulationResistance(corpus: Corpus) -> tuple[Corpus, list[str]]:
    clean_o = []
    flags: list[str] = []
    for a in corpus.o_set:
        reason = _suspicious(a)
        if reason:
            flags.append(f"{a.asset_id}: excluded ({reason})")
            continue
        # DormantForkFilter: down-weight dormant repos rather than drop.
        if a.commit_freq_per_month < 2.0 and a.forks < 50:
            flags.append(f"{a.asset_id}: down-weighted (dormant fork)")
            a = replace(a, tech_maturity=a.tech_maturity * 0.5)
        clean_o.append(a)
    cleaned = replace(corpus, o_set=clean_o)
    return cleaned, flags
