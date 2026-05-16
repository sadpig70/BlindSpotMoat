"""EntityResolve — CRITICAL (A4: promoted from plumbing to first-class node).

Adjudicated ground-truth set + fuzzy/semantic match + measured precision/recall
+ top-rank manual audit log + confidence tiering. Inaccurate resolution is the
single largest phantom-moat risk (CONV-2), hence CRITICAL + measured P/R.
"""

from __future__ import annotations

import difflib

from ..contracts import Corpus, ResolvedPairs
from ..errors import CriticalNodeFailure

# Adjudicated ground-truth O->P mapping for the illustrative corpus.
# In a real run this is a human-curated, auditable set.
_GROUND_TRUTH = {
    "O-klipper-mes": "P-mes-vendor-x",
    "O-rk3588-defectnet": "P-defect-cv-listed",
}

_FUZZY_CUTOFF = 0.62
_TIER_HIGH = 0.80


def _norm(s: str) -> str:
    return s.lower().replace("-", "").replace("_", "").replace(" ", "")


def _best_match(o, p_set):
    cand = []
    o_keys = [o.name] + list(o.aliases)
    for p in p_set:
        p_keys = [p.name] + list(p.aliases) + p.topics
        score = max(difflib.SequenceMatcher(None, _norm(ok), _norm(pk)).ratio()
                    for ok in o_keys for pk in p_keys)
        # topic-overlap boost (technology-function ontology, DeepSeek CONV-2 fix)
        shared = set(o.topics) & set(p.topics)
        if shared:
            score = max(score, 0.55 + 0.1 * len(shared))
        cand.append((score, p.asset_id))
    cand.sort(reverse=True)
    return cand[0] if cand else (0.0, None)


def EntityResolve(corpus: Corpus) -> ResolvedPairs:
    pairs: dict[str, str] = {}
    unresolved: list[str] = []
    audit_log: list[str] = []
    tp = fp = fn = 0

    for o in corpus.o_set:
        score, pid = _best_match(o, corpus.p_set)
        gt = _GROUND_TRUTH.get(o.asset_id)
        if score >= _FUZZY_CUTOFF and pid is not None:
            pairs[o.asset_id] = pid
            tier = "high" if score >= _TIER_HIGH else "low"
            if score < _TIER_HIGH:
                unresolved.append(o.asset_id)  # low-tier -> isolate, not trusted
            if gt == pid:
                tp += 1
            else:
                fp += 1
                audit_log.append(f"{o.asset_id}->{pid} (score={score:.2f},{tier}) "
                                 f"MISMATCH gt={gt}")
            # top-rank manual audit obligation
            audit_log.append(f"manual-audit: {o.asset_id}->{pid} score={score:.2f} "
                             f"tier={tier}")
        else:
            if gt is not None:
                fn += 1
                audit_log.append(f"{o.asset_id} FALSE-NEGATIVE (gt={gt}, "
                                 f"best={score:.2f}) -> phantom-blind risk")

    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0

    if not audit_log:
        raise CriticalNodeFailure("EntityResolve produced no audit log "
                                  "(CRITICAL: P/R unmeasurable)")
    return ResolvedPairs(pairs=pairs, precision=round(precision, 3),
                         recall=round(recall, 3), manual_audit_log=audit_log,
                         unresolved=unresolved)
