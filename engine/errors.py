"""Engine error / gating-halt types."""


class EngineError(Exception):
    """Base engine error."""


class ContractViolation(EngineError):
    """A data-contract invariant was violated (A8 honesty / typing)."""


class CriticalNodeFailure(EngineError):
    """A CRITICAL node (EntityResolve / HypothesisHarness / LegalStandingLayer /
    AdversarialManipulationResistance) failed fail-closed."""


class GatingHalt(EngineError):
    """S0 gate (H0 & H5) failed -> pipeline halts, phantom_moat verdict.

    This is NOT a bug: per rev2 it is the correct honest outcome when
    audited production-scale / structural-blindness evidence is absent.
    """

    def __init__(self, gate: str, reason: str):
        self.gate = gate
        self.reason = reason
        super().__init__(f"S0 gating halt at {gate}: {reason}")
