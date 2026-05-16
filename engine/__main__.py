"""CLI — python -m engine --mode {dry-run,execute} [--json]

dry-run : ModeDryRun — validate data contracts / gates / thresholds only.
execute : full pipeline (fail-closed at S0 on non-audited fixtures).
"""

from __future__ import annotations

import argparse
import json
import sys

from . import __codename__, __version__
from .pipeline import dry_run, execute, report_to_dict


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="engine",
                                 description="BlindSpotMoat / NULLTRACK audit engine")
    ap.add_argument("--mode", choices=["dry-run", "execute"], default="dry-run")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args(argv)

    if args.mode == "dry-run":
        out = dry_run()
    else:
        out = report_to_dict(execute())

    if args.json:
        print(json.dumps(out, indent=2, ensure_ascii=False, default=str))
        return 0

    print(f"BlindSpotMoat ({__codename__}) v{__version__} — mode={args.mode}")
    print("=" * 68)
    if args.mode == "dry-run":
        print(json.dumps(out, indent=2, ensure_ascii=False, default=str))
        return 0

    hr = out["honest_report"]
    print(f"VERDICT        : {out['verdict']}")
    print(f"GATING HALT    : {out['gating_halt']}")
    print(f"DATA VINTAGE   : {hr['data_vintage']}")
    print("-" * 68)
    for k, v in out["hypotheses"].items():
        mark = "FALSIFIED" if v["falsified"] else ("PASS" if v["passed"]
                                                   else "INCONCLUSIVE")
        print(f"  [{mark:12}] {v['name']}")
        print(f"      threshold: {v['threshold']}")
        print(f"      observed : {v['observed']}")
        if v["note"]:
            print(f"      note     : {v['note']}")
    print("-" * 68)
    ms = out["monetization_signal"]
    print(f"MONETIZATION   : enabled={ms['enabled']} "
          f"expiry~{ms['expiry_estimate_months']}mo "
          f"half_life~{ms['half_life_months']}mo")
    if ms["void_reason"]:
        print(f"               : {ms['void_reason']}")
    print(f"TTC            : span={out['ttc_index']['illegibility_span']} "
          f"t_window={out['ttc_index']['t_window_months']}mo")
    print(f"LEGAL STANDING : fail_closed_ok={out['legal_standing']['fail_closed_ok']} "
          f"(2-layer, RECIP abandoned)")
    print("-" * 68)
    print("HONEST REPORT (S6):")
    print(f"  {hr['heuristic_to_empirical_delta']}")
    print(f"  residual risk: {hr['residual_risk']}")
    print(f"  observer-effect: {out['erosion_report'].get('self_defeat_warning','')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
