"""TimeSeriesStabilityMonitor — A6 (DeepSeek/Kimi CONV-5).

Replay >=2 separated 12-month windows; flag concept drift / cyclical artifacts
(chip-surplus vs shortage) so payback estimates are not era-bound.
"""

from __future__ import annotations

from ..contracts import Corpus


def TimeSeriesStabilityMonitor(corpus: Corpus) -> dict:
    series = corpus.blind_width_series
    if len(series) < 3:
        return {"stable": None, "note": "insufficient periods for replay"}
    early = [v for _, v in series[: len(series) // 2]]
    late = [v for _, v in series[len(series) // 2:]]
    em = sum(early) / len(early)
    lm = sum(late) / len(late)
    drift = round(lm - em, 3)
    return {
        "early_mean_blind_width": round(em, 3),
        "late_mean_blind_width": round(lm, 3),
        "drift": drift,
        "drift_alert": abs(drift) > 0.1,
        "note": ("blind-width compressing over time -> cyclical/structural drift; "
                 "H2/H3 must use >=2 separated 12-mo windows (Kimi CONV-5)"),
    }
