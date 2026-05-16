# BlindSpotMoat — 범용 데이터 수집 요청서 (UNIVERSAL DATA-COLLECTION REQUEST)

> **대상**: 독립 실행되는 여러 AI (ChatGPT / Claude / Gemini / Grok / Kimi / DeepSeek / Qwen 등)
> **방식**: 본 문서 1개를 그대로 각 AI에 입력. 모델별 맞춤 프롬프트 없음(범용 단일).
> **각 AI는 다른 AI의 답을 보지 못함** — 독립 수집 → 교차 대조용.
> **응답은 끝의 §6 스키마(YAML)로만** 작성. 산문 설명 금지.

---

## 0. 당신의 임무 (한 문단)

당신은 "정책-가시 트랙(Track P)"과 "오픈소스 brownfield 트랙(Track O)"이 공존하는
제조 분야에서, 한 트랙이 정책·조달 도구에 *구조적으로 안 보이는* 현상을 검증하려는
분석 엔진을 위한 **실데이터 수집가**다. 엔진은 이미 완성되어 있고, 지금 막혀 있는 것은
**감사 가능한(audited) 실데이터의 부재** 하나뿐이다. 당신의 일은 아래 §3에 명시된
데이터를 **출처와 함께** 찾아 §6 스키마로 반환하는 것이다. **찾을 수 없으면 찾을 수
없다고 정직하게 보고**하는 것이 임무의 핵심이다.

---

## 1. ★ 최우선 규칙 — 정직성 (이걸 어기면 응답 전체 폐기)

이 프로젝트는 적대적 데이터 오염 탐지(astroturf/provenance 게이트)를 내장하고 있다.
지어낸 데이터는 **반드시 탐지되어 응답 전체가 폐기**된다. 누락은 안전하지만 날조는 치명적이다.

1. **모르면 `null` + 이유.** 그럴듯한 추정치로 빈칸을 채우지 마라.
2. **출처 없는 수치 금지.** 모든 숫자에 `source_url`(직접 접근 가능한 URL) 필수.
   URL을 못 대면 그 값은 `null`.
3. **등급을 정직하게.** 각 데이터에 `source_class`를 정확히 표기:
   - `audited` — 독립 감사/규제 공시/검증된 1차 텔레메트리 (예: 정부 공식 목록, 감사된 재무공시, 인증기관 데이터)
   - `public_unaudited` — 공개돼 있으나 미감사 (예: GitHub API 지표, 회사 보도자료, 시장 주가)
   - `self_reported` — 당사자 자기보고 (예: README payback 주장, 마케팅 슬라이드, 컨퍼런스 발표)
   - `unavailable` — 공개적으로 존재하지 않음 (값은 `null`, `reason` 필수)
4. **README/마케팅 payback을 `audited`로 승격하지 마라.** 그건 `self_reported`다.
5. **GitHub stars/forks를 "배포 증거"로 제출하지 마라.** 그건 활동 지표일 뿐
   (`public_unaudited`). H0는 이를 배포 증거로 인정하지 않는다 — 그래도 활동
   지표로는 수집 가치가 있으니 등급만 정확히.
6. **존재하지 않는 repo/회사/목록을 만들지 마라.** Track O 자산은 실재하고 접근
   가능한 repo URL이 있어야 한다. 의심되면 `verifiable: false`로 표시.
7. **부분적·정직한 > 완전·날조.** 10개 필드 중 2개만 진짜면, 2개만 채우고 8개는 `null`.

---

## 2. 배경 (컨텍스트 — 외부 AI는 이 프로젝트를 모르므로 최소 설명)

- **Track P (정책-funded, "보임")**: NZIA Strategic Projects, IRA 45X 수혜기업,
  대형 정책보조 제조(배터리 기가팩토리 등), 상장 MES/머신비전 vendor, EMS roll-up.
- **Track O (open-source brownfield, "안 보임")**: 기존 공장을 저비용으로 retrofit
  하는 Apache-2.0/오픈소스 + sub-USD-100 SBC 기반 스택 (MES, 결함검사, 모션제어 등).
  조달 프레임워크가 *이름으로 인식하지 못하는* 자산.
- **검증 대상**: Track O가 (a) production scale로 실재하는가, (b) 단순
  품질미달/niche가 아니라 구조적으로 안 보이는가, (c) unit-economics 차익이 실재하며
  *유한 기간(규제 흡수 전)* 지속되는가.
- **도메인 범위**: 1순위 **D1 = 제조 brownfield retrofit**.
  2순위 **D2 shadow probe** = 에너지 retrofit *또는* agritech 中 택1 (H0/H1/H2 필드만, 소량).

---

## 3. 수집해야 할 데이터 (가설별 — *왜* 필요한지 포함)

> 각 항목의 `feeds`는 이 데이터가 어떤 검증 게이트로 들어가는지다.
> `threshold`는 사전등록된 판정 기준(참고용 — 당신은 데이터만 모으면 된다).

### D3-1 · Track P 목록 (정책-가시 자산) — `feeds: H1, H3, H5`
- 실제 **NZIA Strategic Projects** 지정 목록 (있는 만큼, entry명/섹터/capex/상태)
- **IRA 45X** 수혜 공시 (수혜기업/credit 유형)
- 제조 SW 상장사 (MES/SCADA/머신비전) — 회사명/티커/시총
- ⚠ 주의: "NZIA 47-entry" 같은 숫자는 가정일 수 있음. **실제 공개된 만큼만**, 출처 URL과 함께.

### D3-2 · Track O 자산 + 활동 지표 — `feeds: H1, H5, AdversarialResistance`
실재하는 오픈소스 제조 brownfield repo들. 각 repo에 대해:
`name, repo_url, topics[], aliases[], forks, stars, commit_freq_per_month,
contributor_count, contributor_concentration(0-1, 1=단일조직), star_fork_ratio,
license, bom_usd(있으면), tech_maturity(0-1 주관추정 시 self_reported 표기)`
- ⚠ Klipper-MES / RK3588-DefectNet-Tiny / FPGA-laser-sync / FOSSASIA-llama-edge-arm /
  ros2-tropical 등은 **이름이 illustrative일 수 있음**. 실존 여부를 먼저 검증하고,
  실존하면 정확한 repo_url을, 아니면 *기능적으로 동등한 실존 repo*를 `substitute_for`
  필드와 함께 제출. 없으면 `unavailable`.

### D3-3 · ★ 배포 증거 (H0 게이트 — 가장 중요, 가장 어려움) — `feeds: H0`
Track O 자산이 **production scale**로 실재하는지의 *감사된* 증거:
`asset_id, annual_unit_volume, uptime_pct, months_in_production,
evidence_type(industrial_marketplace_tx | iot_deployment_proof | integrator_case_audit
| certification_record), source_url, source_class`
- threshold(참고): ≥10자산이 각 ≥1000 unit/yr & ≥95% uptime & ≥24개월. **audited만 인정.**
- ⚠ 이건 대개 공개 웹에 audited 형태로 **없다**. 없으면 솔직히 `unavailable` +
  *어디에 있을 법한지*(누가 보유, 어떤 접근이 필요한지)를 `reason`에 기술.

### D3-4 · 전생애 TCO / payback — `feeds: H2`
Track O vs Track P의 **full-lifecycle** payback(주): 통합·유지보수·실패·인증비 포함.
`asset_id, reported_payback_weeks, payback_basis(pilot_capex | full_lifecycle),
compliance_cost_included(bool), source_url, source_class`
- ⚠ README "8–14주"류는 `self_reported` + `payback_basis: pilot_capex`. 감사된
  현금흐름이 있으면만 `audited`.

### D3-5 · SBOM / 공급망 임베드 — `feeds: VisibilityGraph.DependencyPenetration, H5`
Track O 컴포넌트가 Track P 기업 제품 *내부에 sub-tier로 임베드*된 증거:
`oss_component, embedded_in_company, evidence(sbom_spdx_url | contract | disclosure),
source_url, source_class`
- 이유: 임베드된 자산은 "안 보이는 게 아니라 다른 이름으로 이미 보임" → false-blind 제거용.

### D3-6 · 수평 규제 instrument — `feeds: H6, H3c, RegulatoryAbsorptionMonitor`
제조 SW에 적용되는 강제 인증/감사/SBOM 규제:
`instrument_id, name, applies_to_manufacturing_software(bool),
mandate_type(mandatory_cert_sbom | certification | audit_visibility | subsidy_only),
status(in_force | expanding | proposed), effective_year, source_url`
- 예: EU CRA, NIS2, IEC 62443, ISO 27001, 정부 OSS 조달 프레임워크 등 (실제 현황으로).

### D3-7 · 시계열 — `feeds: H3 (정책지출↔blind-width 상관)`
`policy_spend_by_year[{year, eur_or_usd, source_url}]` — 정책 제조보조 연도별 규모.
가능하면 연도별 compliance-mandate 밀도 추세도.

### D3-8 · 시장 데이터 — `feeds: H4, H7`
- Track P incumbent들의 **상장 여부 + 티커** (H7 event study용 — 공개 주가)
- "지역 MES integrator"가 **상장/거래 가능한지** (H4 — 대개 비상장 = 거래불가.
  사실대로: 거래 가능 proxy가 있으면 명시, 없으면 `tradable_proxy: false`).

---

## 4. 스코프·금지

- D1(제조 brownfield)이 1순위. D2(에너지 retrofit 또는 agritech)는 H0/H1/H2 해당
  필드만 소량(transferability 점검용, 제품범위 확대 아님).
- 정치적 논평·전략 제안·투자 의견 **금지**. 당신은 데이터 수집가다.
- 특정 기업에 대한 매수/매도 신호 생성 **금지** (그건 엔진이 게이트 통과 후 판단).
- 추정·보간·"합리적 가정" 금지 (§1 규칙 1).

---

## 5. 셀프체크 (응답 제출 전 반드시 통과)

- [ ] 모든 수치에 `source_url`이 있거나, 없으면 값이 `null`이고 `reason`이 있다
- [ ] 모든 데이터에 정확한 `source_class`가 붙었다 (README→self_reported 등)
- [ ] 지어낸 repo/회사/목록/숫자가 **하나도 없다**
- [ ] illustrative 의심 이름은 실존 검증했거나 `unavailable`/`substitute_for` 처리했다
- [ ] 못 찾은 항목을 빈칸이 아니라 `unavailable` + `reason`으로 명시했다
- [ ] §6 YAML 스키마를 정확히 따랐고, 산문 설명을 추가하지 않았다

---

## 6. 응답 스키마 (이 YAML 형식으로만 작성 — 파일명: `<ai_name>_data.yaml`)

```yaml
collector_id: "<your model name + version>"          # 예: "Gemini-3.1-pro"
collected_at: "<ISO8601 UTC>"
session_hash: "<당신이 만든 임의 8자리>"
scope_covered: { D1: true, D2: "energy_retrofit | agritech | none" }

# 자기 평가 — 정직성 강제
honesty_attestation:
  fabricated_values: 0                                # 반드시 0
  fields_returned_null_due_to_unavailable: <int>
  overall_confidence: "<low|medium|high>"
  hardest_gap: "<H0 배포증거 등 — 무엇이 왜 못 모였는지 한 줄>"

trackP_assets:                                        # D3-1
  - { asset_id, name, sector, capex_or_size, credit_type, listed, ticker,
      source_url, source_class }

trackO_assets:                                        # D3-2
  - { asset_id, name, repo_url, topics: [], aliases: [],
      forks, stars, commit_freq_per_month, contributor_count,
      contributor_concentration, star_fork_ratio, license, bom_usd,
      substitute_for: null, verifiable: true|false,
      source_url, source_class }

deployment_evidence:                                  # D3-3 (H0 — 핵심)
  - { asset_id, annual_unit_volume, uptime_pct, months_in_production,
      evidence_type, source_url, source_class, reason_if_null }

tco_payback:                                          # D3-4
  - { asset_id, reported_payback_weeks, payback_basis,
      compliance_cost_included, source_url, source_class }

sbom_embedding:                                       # D3-5
  - { oss_component, embedded_in_company, evidence, source_url, source_class }

regulatory_instruments:                               # D3-6
  - { instrument_id, name, applies_to_manufacturing_software,
      mandate_type, status, effective_year, source_url }

timeseries:                                           # D3-7
  policy_spend_by_year:
    - { year, amount, currency, source_url, source_class }
  compliance_mandate_density_by_year:
    - { year, density_0_1, basis, source_url, source_class }

market_data:                                          # D3-8
  incumbents: [ { name, ticker, listed, source_url } ]
  regional_integrator_tradable_proxy: { exists: true|false, detail, source_url }

unavailable_log:                                      # 못 모은 것 — 빈칸 금지, 여기 명시
  - { item, why_unavailable, where_it_likely_lives }
```

---

> 끝. 이 문서 외 추가 컨텍스트는 없다. 추측하지 말고, 출처와 함께 모으고,
> 못 찾으면 `unavailable`로 정직하게 보고하라. 정직한 부분 데이터가 이 프로젝트의
> 가치다 — 날조된 완전 데이터는 탐지되어 폐기된다.
