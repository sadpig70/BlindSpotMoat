# REVIEW PROMPT — BlindSpotMoat (범용, 모든 모델 공통 복붙)

> 아래 "===== 복사 시작 =====" ~ "===== 복사 끝 =====" 사이 *전체*를 어떤 AI 모델
> 채팅창에든 그대로 붙여넣는다. 모델별 변형 없음 — 동일 prompt를 Grok / DeepSeek /
> Qwen / Gemini / Codex / 기타 모두에 사용. 추가 파일 첨부·추가 지시 금지 (self-contained).

---

===== 복사 시작 =====

You are an independent, adversarial design reviewer. You will receive THREE documents
describing an early-stage project (an idea, its concretization, and its design). Your job
is to find what is WRONG, WEAK, MISSING, or UNFALSIFIABLE — not to praise. Use only your
own reasoning. Do not search the web. Do not ask clarifying questions. Output one yaml
block at the end and nothing else.

## Context (minimal)

The project ("BlindSpotMoat", codename NULLTRACK) came out of a multi-AI idea pipeline.
The selected idea applies a transformation lens ("delete the scarce resource and redesign
around absence") to an insight about policy-funded vs open-source manufacturing tracks.
You do NOT need to trust the pipeline's scores — review the idea/design ON ITS MERITS.
Treat all quantitative claims (payback weeks, score 8.12, surprise 10.0) as ASSERTIONS to
be challenged, not facts.

Be specific. "This is unclear" is useless; "H3 assumes causation from a correlation that
could be confounded by X" is useful. A weak reviewer flatters; a strong reviewer finds the
one objection that, if true, breaks the project.

---

## DOCUMENT 1 of 3 — IDEA (00_idea_card.md)

Idea ID IDEA-20-02 "Invisible-Track Resource-Deletion Competitiveness Engine".
Source insight INS-L10-005 (Invisible-Track Coexistence), layer L10_Generative,
lens DIR_RESDEL = "delete the scarce resource and redesign around absence".

Source insight (verbatim):
> In any field with both policy-funded and open-source production stacks, two innovation
> tracks coexist that share no investors, no policy vehicles, and almost no vocabulary —
> yet both claim to be the path to competitiveness. The "Invisible-Track Coexistence"
> pattern means bureaucratic instruments (NZIA, IRA, CHIPS, CRMA) are STRUCTURALLY blind
> to one of the two tracks, and the blindness is the binding constraint — not the
> technology, not the capital level.
> SEED-005-001: build a "track-visibility audit": list every government list, VC term
> sheet, and trade-press leaderboard, then map what they DO NOT contain. The unseen track
> is the high-ROI arbitrage target (Klipper-MES, FOSSASIA, OpenROAD-SEA, ros2-tropical) —
> invisible because it ships in Apache-2.0 + sub-USD-100 SBC form factors that no
> procurement framework recognizes.

Mechanism: treat policy-capital VISIBILITY itself as the scarce resource and DELETE it
from the design. Instead of making the open-source brownfield track visible to policy
instruments (the obvious move), assume the subsidy channel does not exist and optimize
that track purely on intrinsic unit economics (8–14 week payback, sub-USD-100 SBC,
Apache-2.0 MES). The blind spot (policy cannot see it) IS the moat; as policy apparatus
grows, the moat grows, because incumbents cannot defend a track their instruments cannot price.

Asserted scores (CHALLENGE THESE): CIX 6-axis total 8.12 (surprise 10.0 = 0 of 8
cross-model personas predicted resource-deletion); EVX consensus==innovation winner,
8/8 votes, max persona score 7.97 (P8 Convergence Architect).

Self-declared limitations: (1) abstract mechanism reconstructed from a placeholder seed;
(2) surprise ≠ feasibility (feasibility was the weakest, lowest-weight axis);
(3) heuristic scoring (no embedding service); (4) P7 contrarian rebuttal —
"policy instruments that cannot see informal factories cannot PROTECT them either"
(blind spot moat = simultaneously no legal/subsidy standing).

## DOCUMENT 2 of 3 — CONCRETIZATION (02_concretization.md)

Domain chosen: D1 manufacturing brownfield retrofit. Basis: INS-L7-001 (asserted highest
IDX score 8.7) + INS-L10-005 SEED-005-001.

Problem: manufacturing investment splits into two tracks sharing no capital / policy
vehicle / vocabulary, both claiming competitiveness, both permanently mis-priced.
- Track P (policy-funded, visible): NZIA Strategic Projects 47 entries (~€18B), IRA 45X,
  Northvolt, Siemens Energy, EMS roll-ups. Payback 24+ months greenfield. Listed on
  NZIA list / VC term sheets / trade-press leaderboards.
- Track O (open-source brownfield, invisible): Klipper-MES, RK3588+DefectNet-Tiny,
  FPGA laser-sync, Mazak DED+eddy-NDT, FOSSASIA, OPC-UA integrators. Payback 8–14 weeks.
  Near-zero capital (Apache-2.0 + sub-USD-100 SBC). Recognized by NO procurement framework.
Binding constraint asserted = visibility, not tech or capital.

RESDEL application: scarce resource = visibility/legitimacy/capital-access conferred by
policy listing → DELETE (stop trying to be seen; assume subsidy channel does not exist)
→ redesign Track O on pure unit economics → blind spot becomes moat (grows with policy apparatus).

System (form a — analysis/simulation tool): "Track-Visibility Audit Engine".
- Input A (public): NZIA 47-entry list, IRA 45X filings, EMS M&A, VC themes, trade-press.
- Input B (public): GitHub activity for Klipper-MES / RK3588-DefectNet / FPGA-laser-sync /
  FOSSASIA / ros2 (forks, commit freq, deployment cases, reported payback weeks, BOM USD).
- Process: set difference = O_active − (O ∩ P_visible) = blind spot; score blind-spot
  assets by unit economics (payback weeks, BOM, deploy friction).
- Output: ranked arbitrage targets + moat-strength index (spot_width × policy_growth_rate)
  + monetization signal (long regional MES integrators / short NZIA-listed incumbents,
  18–30 month window).

Stakeholders: regional MES integrators; PE/SPV (long-retrofit/short-incumbent pair);
industrial-policy auditors (quantify NZIA "tech-neutral" incumbent bias); OSS manufacturing
communities.

Moat logic: (1) blind spot = defense line incumbents can't price; (2) policy apparatus
growth = moat growth (self-reinforcing); (3) hard to replicate (requires the cognitive
flip of treating invisibility as an asset).

Falsifiable hypotheses + falsification conditions:
- H1: NZIA-47 list vs active OSS manufacturing assets — set difference is significantly
  large. FALSIFY if difference is small / largely overlapping → "blind spot" premise false.
- H2: blind-spot assets' mean payback (weeks) significantly shorter than policy-funded.
  FALSIFY if blind payback ≥ policy payback → arbitrage basis gone.
- H3: policy-apparatus growth positively correlates with blind-spot width.
  FALSIFY if no/negative correlation → "moat self-reinforcing" logic false.
- H4: long-retrofit/short-NZIA-incumbent pair shows excess return in 18–30mo window.
  FALSIFY if no excess return → monetization void (idea survives only as analysis tool).

## DOCUMENT 3 of 3 — DESIGN (05_design.md)

Form (a) analysis/simulation tool. scope-freeze: D1 only, winner IDEA-20-02 only.

Gantree (functional decomposition):
- BlindSpotMoat_Main
  - DataIngestion: TrackP_Ingest, TrackO_Ingest, Normalize (asset ontology + data vintage) → corpus{P_set,O_set}
  - BlindSpotMapping (@dep DataIngestion): EntityResolve, SetDifference (O − O∩P_visible),
    Confidence → blind_spot_assets[]
  - UnitEconomicsScoring (@dep BlindSpotMapping): PaybackEstimate, BOMSignal, DeployFriction → scored_assets[]
  - MoatMetric (@dep BlindSpotMapping): SpotWidth (|blind|/|O|), PolicyGrowth, MoatStrength → moat_index
  - HypothesisHarness (@dep Scoring,Moat; CRITICAL for heuristic-risk): H1–H4 tests,
    FalsifyGate (falsified → conclusion held + scope auto-adjust) → hypothesis_report
  - ReciprocalStandingLayer (independent, CRITICAL, fail-closed): Mechanism (reciprocal
    obligation contract WITHOUT requiring policy visibility), NonVisibilityProof
    (standing granted while moat=invisibility intact), FailClosed → standing_spec
  - SurfacingOption (detached, OPTIONAL, default-OFF): SeparationGuard (no coupling to
    primary), ExitPath → surfacing_module(detached)
  - Reporting (@dep Harness,Moat): RankTable, MonetizationSignal, HonestReport
    (heuristic→empirical delta + residual risk + data vintage)
  - ModeDryRun: validate contracts, emit plan without execution

PPR essentials: BlindSpotMapping does entity-resolved set difference with confidence;
HypothesisHarness evaluates H1–H4 only in falsifiable form, holds conclusions if falsified;
ReciprocalStandingLayer is fail-closed (no standing_spec ⇒ project CRITICAL defect);
AI_test_payback_gap falsifies if blind_median_payback ≥ policy_median_payback.

Data contract: all inputs public; every number must cite source + vintage (measurement-only);
residual heuristic separately flagged in honest_report.

Validation gates S1–S6: S1 pipeline, S2 set-difference engine, S3 ≥H1+H2 empirical,
S4 moat index, **S5 RECIP layer (CRITICAL, fail-closed)**, S6 honest reporting.

Risk handling absorbed: R1 scale-cap → surfacing as detached option; R2 P7 protection-absence
→ RECIP standing layer (CRITICAL); R3 heuristic → audit engine empirically closes it;
R4 false-resolutions (NZIA tech-neutral facade etc.) → measurement-only; R5 narrowness
→ scope-freeze, generalization deferred.

---

## YOUR REVIEW TASK

Review the three documents together. Focus, in priority order:

1. **Falsifiability rigor** — Are H1–H4's falsification conditions actually falsifiable?
   Any circular reasoning or unverified hidden assumptions? Which decisive hypothesis is MISSING?
2. **Set-difference methodology** — Does `O − (O∩P_visible)` correctly capture "blind spot"?
   Could EntityResolve failure manufacture FALSE blind spots? Better mapping method?
3. **R2/P7 RECIP sufficiency** — Can "invisible moat preserved" AND "dispute-time standing"
   actually coexist, or is it an intrinsic contradiction? Is fail-closed enough?
4. **Moat self-reinforcement (H3)** — Is "policy growth ⇒ moat growth" causal or merely
   correlational? Name a counterexample domain.
5. **Missing / additional nodes** — What functional node is absent (data reliability,
   adversarial-manipulation resistance, time-series stability, others)?
6. **Scope adequacy** — Is D1-only freeze correct, or is a D1+D2 portfolio structurally
   more robust as a design?

Rules:
- Challenge the quantitative assertions; do not accept 8.12 / surprise 10.0 / 8–14 weeks at face value.
- At least one finding must be a genuine *strongest objection* — the single thing that,
  if correct, most threatens the project.
- No flattery. Every positive must be backed by a specific reason or omit it.

## OUTPUT (this yaml block only, nothing before or after)

```yaml
reviewer_id: "<YOUR_MODEL_NAME_AND_VERSION>"
session_hash: "<random 8-char alphanumeric you generate>"
reviewed_at: "<ISO 8601>"
verdict: "<sound | revise | reject>"
focus_findings:
  - focus: 1   # falsifiability
    severity: "<critical | high | medium | low>"
    issue: "<specific problem>"
    suggested_fix: "<concrete change>"
  - focus: 2   # set-difference methodology
    severity: "..."
    issue: "..."
    suggested_fix: "..."
  - focus: 3   # R2/P7 RECIP
    severity: "..."
    issue: "..."
    suggested_fix: "..."
  - focus: 4   # moat self-reinforcement
    severity: "..."
    issue: "..."
    suggested_fix: "..."
  - focus: 5   # missing nodes
    severity: "..."
    issue: "..."
    suggested_fix: "..."
  - focus: 6   # scope
    severity: "..."
    issue: "..."
    suggested_fix: "..."
additions:                     # net-new nodes / hypotheses you propose
  - item: "<node or hypothesis>"
    rationale: "<why it is necessary>"
strongest_objection: "<one paragraph: the single objection that most threatens the project if true>"
salvage_path: "<if verdict=revise|reject: the minimal change that would make it sound>"
```

Output the yaml block only. Begin now.

===== 복사 끝 =====
