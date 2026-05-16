# REVIEW SYNTHESIS — 7-AI Adversarial Design Review

> Before implementation, the idea + concretization + design were sent to **7
> independent AIs** (ChatGPT-5.5, Claude-4.7, DeepSeek, Gemini, Grok, Kimi, Qwen)
> for adversarial review under a single universal prompt. Each reviewed
> independently. This document records the convergent findings and the changes
> adopted into the design (v0.1 → v0.2). Korean originals: `_legacy/`.

## Verdict: 7/7 "revise" (0 reject, 0 sound)

Not discarded, but **substantial redesign required**. Three fatal convergences:

- **(A) blindness ≠ exploitable moat** — the unseen track may simply be
  immature, niche, or already embedded sub-tier in Track P. (H0/H5 were unproven
  existence assumptions.)
- **(B) the moat is a kill zone** — 7/7 critical. An invisible actor cannot
  obtain legal standing; "standing while invisible" is a logical contradiction.
  The original RECIP (ReciprocalStandingLayer) was magical thinking.
- **(C) the window is closing** — the moat is not permanent; it is a *shrinking
  regulatory window*. The H3 causal arrow ("policy growth ⇒ moat growth") may be
  inverted: horizontal regulation (EU CRA, NIS2, IEC 62443) destroys it.

## Cross-agreement (≥2 reviewers; most 7/7)

| Code | Severity | Finding |
|---|---|---|
| CONV-1 | CRITICAL 7/7 | RECIP is contradictory — legal standing needs an identifiable entity + jurisdiction, incompatible with invisibility. |
| CONV-2 | CRITICAL 7/7 | Boolean set-difference manufactures phantom blind spots (entity-resolution failure, sub-tier OSS embedded in Track P, "marginal" vs "structurally blind" indistinguishable). |
| CONV-3 | CRITICAL 7/7 | H1–H4 not falsifiable: no thresholds, H1 tautological, H2 category error, H4 a Schrödinger window. CIX/surprise scores are "marketing copy". |
| CONV-4 | HIGH 7/7 | H3 confuses correlation with causation; unanimous counterexamples (EU CRA, NIS2/CISA, MiCA, government OSS procurement). |
| CONV-5 | HIGH 7/7 | Missing load-bearing nodes (adversarial resistance, survivorship, compliance cost, time-series stability, visibility-erosion/observer-effect, regulatory absorption). |
| CONV-6 | MEDIUM 7/7 | D1-only scope cannot separate a structural mechanism from a domain fluke. |

## Adopted changes (A1–A9)

| # | Change |
|---|---|
| **A1** | Redefine "moat": "complete invisibility" → *policy-procurement illegibility within a regulatory regime as of date T, of bounded duration T_window*. Demote "any field" / "permanent moat" language. |
| **A2** | Abandon RECIP → **2-layer LegalStandingLayer**: (1) standard commercial/IP/tort contract (orthogonal to illegibility); (2) dispute-time-only escrow/ZK reversible disclosure. Document accepted legal cost. |
| **A3** | Boolean set-difference → **VisibilityGraph**: graded visibility 0–1 + multi-hop graph + DependencyPenetration (SBOM-traced OSS embedded in Track P excluded from "blind"). |
| **A4** | **EntityResolve promoted to a CRITICAL first-class node** with adjudicated ground truth + measured precision/recall + mandatory manual audit. |
| **A5** | Hypotheses redesigned with pre-registered numeric thresholds + statistical tests: add **H0** (scale-existence gate), redefine H1, H2 (payback per comparable functional unit + compliance), competing **H3a/b/c**, H4 executability gate, **H5** controlled-blindness, **H6** regulatory-absorption, **H7** market-efficiency. |
| **A6** | Add 6 nodes: AdversarialManipulationResistance, SurvivorshipFilter, ComplianceCostOverlay, TimeSeriesStabilityMonitor, VisibilityErosionMonitor (observer-effect), RegulatoryAbsorptionMonitor. |
| **A7** | Moat metric: static `width × growth` → **Time-to-Capture / regulatory half-life**. Monetization reframed from "permanent alpha" to "regulatory-arbitrage half-life window". |
| **A8** | **Honesty invariant**: every numeric claim needs an audited source; CIX 8.12 / surprise 10.0 are *narrative decoration* excluded from empirical reasoning. |
| **A9** | Scope: D1 + a thin D2 shadow probe (transferability only). D1-alone conclusions explicitly downgraded to "manufacturing-plausible only". |

**Deferrals**: D1 (monetization removal) → resolved as option **(가)**: retained
but repositioned per A7. D2 (concrete StrategicVisibility legal entity) → design-
stage candidate. D3 (drop H4 trading thesis) → pre-reflected in the H4
executability gate (auto-retires on failure). **Rejected: none** — every
critical/high finding was absorbed.

## Surviving proposition (post-revision)

> *Within manufacturing brownfield retrofit, conditional on the current
> horizontal-regulation regime, a policy-procurement-illegible stack provides a
> measurable unit-economic arbitrage for a finite period T_window — only if (H0)
> the track exists at production scale, (H5) the exclusion is structural rather
> than a quality filter, and (H6) horizontal regulation has not yet absorbed it.*

Falsifiable · monetization has an explicit expiry · the RECIP contradiction is
removed · phantom-moat is defended against. This is what the 7 reviews converged
on as the *defensible residual form*.
