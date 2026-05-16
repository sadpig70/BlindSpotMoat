"""SurvivorshipFilter — A6 (DeepSeek/Kimi CONV-5).

Archive-scrape defunct repos and report failure rate so payback corpus is not
cherry-picked from best-case survivors.
"""

from __future__ import annotations

from .ingestion import _load


def SurvivorshipFilter(corpus) -> dict:
    raw = _load("defunct.json")
    defunct = raw["defunct"]
    n_alive = len(corpus.o_set)
    n_dead = len(defunct)
    total = n_alive + n_dead
    failure_rate = round(n_dead / total, 3) if total else 0.0
    dead_payback = [d["reported_payback_weeks"] for d in defunct
                    if d.get("reported_payback_weeks") is not None]
    return {
        "alive": n_alive,
        "defunct": n_dead,
        "failure_rate": failure_rate,
        "defunct_payback_weeks": dead_payback,
        "abandon_reasons": sorted({d["abandon_reason"] for d in defunct}),
        "note": ("survivorship-adjusted: defunct payback must be folded into any "
                 "H2 comparison; failure_rate is a lower bound (illustrative)"),
    }
