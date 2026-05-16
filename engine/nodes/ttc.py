"""TimeToCaptureMetric — A7 (replaces static MoatMetric width x growth; CONV-4).

Moat is NOT permanent. Output a regulatory half-life and an estimated remaining
arbitrage window T_window (months). All TTC outputs carry an expiry by design.
"""

from __future__ import annotations

import math

from ..contracts import Corpus, TTCIndex, VisibilityScoredAsset
from .visibility_graph import blind_assets


def TimeToCaptureMetric(scored: list[VisibilityScoredAsset], corpus: Corpus,
                        absorption: dict) -> TTCIndex:
    blind = blind_assets(scored)
    span = round(len(blind) / max(len(scored), 1), 3)

    risk = absorption.get("assimilation_risk", 0.0)
    if risk <= 0.0:
        half_life = None          # cannot bound -> do not claim permanence
        t_window = None
    else:
        # higher horizontal-reg assimilation risk -> shorter half-life
        half_life = round(24.0 * math.exp(-2.0 * risk), 1)   # months
        t_window = round(half_life * math.log(2) / math.log(2), 1)
        # decay further if absorption already inverted (H6)
        if absorption.get("h6_inversion_triggered"):
            t_window = round(min(t_window, half_life * 0.5), 1)

    return TTCIndex(illegibility_span=span,
                    t_window_months=t_window,
                    half_life_months=half_life)
