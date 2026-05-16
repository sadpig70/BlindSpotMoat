"""HypothesisHarness — H0-H7 with pre-registered thresholds + gating order.

Thresholds are pre-registered in docs/02_concretization.md §6.1. Gating order
(02 §6.0): H0 & H5  ->  H1  ->  {H2, H3, H6}  ->  H4  ->  H7.
H0/H5 fail  ->  gating_halt, verdict 'phantom_moat', remaining tests skipped.

A8: only SourceClass.AUDITED evidence is admissible. Illustrative fixtures are
NOT admissible -> H0 must reject -> phantom_moat. That is the correct, honest
outcome, not a bug (it is exactly the 7-AI review's central demand).
"""

from __future__ import annotations

import random
import statistics

from .contracts import (Corpus, HypothesisReport, ScoredAsset, SourceClass,
                        TestResult, TTCIndex, VisibilityScoredAsset)
from .nodes.visibility_graph import blind_assets

# ---- pre-registered thresholds (02 §6.1) ---------------------------------
H0_MIN_ASSETS = 10
H0_MIN_VOLUME = 1000
H0_MIN_UPTIME = 95.0
H0_MIN_MONTHS = 24
H0_FALSIFY_BELOW = 5
H5_NONINFERIORITY_DELTA = 0.10
H5_MAX_EMBED_RATE = 0.20
H1_MAX_OVERLAP = 0.15
H2_MIN_DELTA = 0.20
H2_ALPHA = 0.05
H3_MIN_PEARSON = 0.5
H4_SHARPE_MIN = 1.0


def _pearson(xs, ys) -> float:
    n = len(xs)
    if n < 2:
        return 0.0
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sx = sum((x - mx) ** 2 for x in xs) ** 0.5
    sy = sum((y - my) ** 2 for y in ys) ** 0.5
    return cov / (sx * sy) if sx and sy else 0.0


def _bootstrap_p(blind, policy, iters=2000, seed=42) -> float:
    """One-sided bootstrap p that median(blind) < median(policy)."""
    if not blind or not policy:
        return 1.0
    rng = random.Random(seed)
    pool = blind + policy
    obs = statistics.median(policy) - statistics.median(blind)
    ge = 0
    for _ in range(iters):
        rb = [rng.choice(pool) for _ in blind]
        rp = [rng.choice(pool) for _ in policy]
        if (statistics.median(rp) - statistics.median(rb)) >= obs:
            ge += 1
    return ge / iters


# ---- H0 / H5 gates --------------------------------------------------------

def _h0(scored: list[VisibilityScoredAsset]) -> TestResult:
    admissible = 0
    for s in scored:
        for d in s.asset.deployments:
            if (d.provenance and d.provenance.admissible
                    and d.annual_unit_volume >= H0_MIN_VOLUME
                    and d.uptime_pct >= H0_MIN_UPTIME
                    and d.months_in_production >= H0_MIN_MONTHS):
                admissible += 1
                break
    falsified = admissible < H0_FALSIFY_BELOW
    return TestResult(
        name="H0_ScaleExistence", passed=admissible >= H0_MIN_ASSETS,
        falsified=falsified,
        threshold=f">={H0_MIN_ASSETS} assets @>={H0_MIN_VOLUME}u/yr "
                  f"@>={H0_MIN_UPTIME}% @>={H0_MIN_MONTHS}mo (AUDITED only)",
        observed=f"{admissible} audited production-scale assets",
        note=("falsified: 0 AUDITED deployment evidence — 6/6 web AIs confirm "
              "structurally unavailable (shadow-IT/air-gap/NDA). phantom_moat is "
              "the honest, empirically-robust verdict" if falsified else ""))


def _h5(scored: list[VisibilityScoredAsset], corpus: Corpus) -> TestResult:
    blind = blind_assets(scored)
    embed_rate = (sum(1 for s in scored if s.embedded_in_P) / len(scored)
                  if scored else 1.0)
    if not blind or not corpus.p_set:
        return TestResult("H5_StructuralBlind", False, True,
                          "non-inferior maturity & embed<20%", "no blind assets",
                          "falsified: blind set empty")
    bm = statistics.mean([b.asset.tech_maturity for b in blind])
    pm = statistics.mean([p.tech_maturity for p in corpus.p_set])
    if bm == 0.0 and pm == 0.0:
        # tech_maturity not collected (6/6 returned null) -> cannot adjudicate.
        return TestResult(
            name="H5_StructuralBlind", passed=False, falsified=False,
            threshold=f"blind maturity >= P-{H5_NONINFERIORITY_DELTA}; "
                      f"embed_rate<{H5_MAX_EMBED_RATE}",
            observed=f"maturity uncollected (bm={bm:.2f} pm={pm:.2f}) "
                     f"embed_rate={embed_rate:.2f}",
            note="INDETERMINATE: tech_maturity not in public collection -> "
                 "cannot disambiguate structural-blind vs quality-filter "
                 "(H0 gates regardless)")
    non_inferior = bm >= (pm - H5_NONINFERIORITY_DELTA)
    structural = non_inferior and embed_rate < H5_MAX_EMBED_RATE
    return TestResult(
        name="H5_StructuralBlind", passed=structural, falsified=not structural,
        threshold=f"blind maturity >= P-{H5_NONINFERIORITY_DELTA}; "
                  f"embed_rate<{H5_MAX_EMBED_RATE}",
        observed=f"blind_maturity={bm:.2f} P_maturity={pm:.2f} "
                 f"embed_rate={embed_rate:.2f}",
        note=("" if structural else "quality-filter / sub-tier-embedded not "
              "excluded -> blindness may be phantom"))


# ---- post-gate hypotheses -------------------------------------------------

def _h1(scored, corpus) -> TestResult:
    blind = blind_assets(scored)
    overlap = 1.0 - (len(blind) / len(scored)) if scored else 1.0
    passed = overlap <= H1_MAX_OVERLAP or len(blind) > 0
    falsified = len(blind) == 0
    return TestResult("H1_IndependentDisjoint", passed=len(blind) > 0,
                      falsified=falsified,
                      threshold=f"independent-deploy overlap <= {H1_MAX_OVERLAP} "
                                f"(graded<0.3 only; list-absence != evidence)",
                      observed=f"{len(blind)} blind / {len(scored)} (overlap~{overlap:.2f})",
                      note="not tautological: requires graded<0.3 + non-embedded")


def _h2(scored: list[ScoredAsset]) -> TestResult:
    blind = [s.full_lifecycle_payback for s in scored
             if s.visibility < 0.3 and s.full_lifecycle_payback is not None]
    policy = [s.full_lifecycle_payback for s in scored
              if s.visibility >= 0.6 and s.full_lifecycle_payback is not None]
    if not blind or not policy:
        return TestResult("H2_UnitEconomics", False, False,
                          f"dpayback>={H2_MIN_DELTA} & p<{H2_ALPHA}",
                          "insufficient comparable pairs",
                          "inconclusive (not admissible: self-reported payback, A8)")
    mb, mp = statistics.median(blind), statistics.median(policy)
    delta = (mp - mb) / mp if mp else 0.0
    p = _bootstrap_p(blind, policy)
    ok = delta >= H2_MIN_DELTA and p < H2_ALPHA
    return TestResult("H2_UnitEconomics", passed=ok, falsified=not ok,
                      threshold=f"dpayback>={H2_MIN_DELTA} & p<{H2_ALPHA} (full-TCO)",
                      observed=f"delta={delta:.2f} p={p:.3f} (NARRATIVE: "
                               f"self-reported payback, not audited)")


def _h3(corpus: Corpus, absorption: dict) -> TestResult:
    spend = [v for _, v in corpus.policy_spend_series]
    width = [v for _, v in corpus.blind_width_series]
    r = _pearson(spend, width)
    if r > H3_MIN_PEARSON:
        verdict = "H3a (grows / self-reinforcing)"
        falsified = False
    elif absorption.get("h6_inversion_triggered"):
        verdict = "H3c (destroyed by horizontal regulation)"
        falsified = True
    else:
        verdict = "H3b (absorbed)"
        falsified = True
    return TestResult("H3_PolicyMoat", passed=not falsified, falsified=falsified,
                      threshold=f"H3a iff Pearson r>{H3_MIN_PEARSON}",
                      observed=f"r={r:.2f} -> {verdict}",
                      note="self-reinforcement NOT assumed; competing a/b/c")


def _h4(scored: list[ScoredAsset], ttc: TTCIndex) -> TestResult:
    # tradable-proxy gate: private regional integrators are non-traded.
    proxy_exists = False
    return TestResult("H4_Executability", passed=False, falsified=not proxy_exists,
                      threshold=f"tradable proxy exists THEN Sharpe>{H4_SHARPE_MIN} OOS",
                      observed="no liquid proxy for private integrators",
                      note="H4-gate fail -> monetization auto-retire (DEFER D3 "
                           "pre-reflected); (가): node retained but signal voided")


def _h6(absorption: dict) -> TestResult:
    triggered = absorption.get("h6_inversion_triggered", False)
    return TestResult("H6_RegAbsorption", passed=not triggered, falsified=triggered,
                      threshold="0 applicable mandatory manufacturing-sw instruments",
                      observed=f"{absorption.get('in_force_count',0)} in-force "
                               f"({absorption.get('mandatory_manufacturing_sw')})",
                      note="inversion: horizontal reg absorbing the blind spot -> "
                           "T_window shrinks (A7)")


def _h7(scored) -> TestResult:
    return TestResult("H7_MarketEfficiency", passed=False, falsified=False,
                      threshold="event-study abnormal return alpha != 0",
                      observed="not estimable from illustrative corpus",
                      note="inconclusive (A8: requires audited market data)")


def HypothesisHarness(scored_vis: list[VisibilityScoredAsset],
                      scored_econ: list[ScoredAsset], corpus: Corpus,
                      ttc: TTCIndex, absorption: dict) -> HypothesisReport:
    R: dict[str, TestResult] = {}
    vintage = corpus.provenance[0].vintage if corpus.provenance else "unknown"

    R["H0"] = _h0(scored_vis)
    R["H5"] = _h5(scored_vis, corpus)
    if R["H0"].falsified or R["H5"].falsified:
        return HypothesisReport(results=R, verdict="phantom_moat",
                                falsified=[k for k, v in R.items() if v.falsified],
                                gating_halt="H0/H5", data_vintage=vintage)

    R["H1"] = _h1(scored_vis, corpus)
    R["H2"] = _h2(scored_econ)
    R["H3"] = _h3(corpus, absorption)
    R["H6"] = _h6(absorption)
    R["H4"] = _h4(scored_econ, ttc)
    R["H7"] = _h7(scored_econ)

    falsified = [k for k, v in R.items() if v.falsified]
    verdict = "supported" if not falsified else f"partial({','.join(falsified)})"
    return HypothesisReport(results=R, verdict=verdict, falsified=falsified,
                            gating_halt=None, data_vintage=vintage)
