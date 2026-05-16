"""LegalStandingLayer — A2 / CONV-1 (7/7 critical). Replaces ReciprocalStandingLayer.

RECIP ("standing while invisible") is a logical contradiction. Replace with 2
layers + an explicit accepted-cost doc. This is a SPEC EMITTER (not runnable
business logic): it emits the standing specification and a fail-closed verdict.
"""

from __future__ import annotations

from ..contracts import StandingSpec
from ..errors import CriticalNodeFailure

_LAYER1 = (
    "StandardCommercialContract: identifiable legal entity enters standard "
    "commercial / IP / tort contracts. Orthogonal to procurement-illegibility "
    "(visibility cost = 0): being commercially contractable does NOT make the "
    "stack legible to NZIA/IRA procurement frameworks."
)
_LAYER2 = (
    "StrategicVisibilityLayer (dispute-time only): reversible minimal disclosure "
    "to a trusted escrow / confidential-arbitration / ZK-proof venue, invoked "
    "ONLY on dispute. Preserves operational illegibility outside disputes."
)
_ACCEPTED_COST = (
    "AcceptedLegalCost: the moat is explicitly NOT a protected permanent castle. "
    "It is a finite-window arbitrage that ACCEPTS bounded legal vulnerability as a "
    "stated cost. Stakeholder value proposition reflects this (DEFER D1=(가): "
    "monetization retained but repositioned as a regulatory half-life window)."
)


def LegalStandingLayer() -> StandingSpec:
    layer1 = _LAYER1
    layer2 = _LAYER2
    fail_closed_ok = bool((layer1 or layer2) and _ACCEPTED_COST)
    if not fail_closed_ok:
        raise CriticalNodeFailure(
            "S5 fail-closed: neither standing layer specifiable -> project defect")
    return StandingSpec(layer1_contract=layer1, layer2_dispute=layer2,
                        accepted_cost_doc=_ACCEPTED_COST,
                        fail_closed_ok=fail_closed_ok)
