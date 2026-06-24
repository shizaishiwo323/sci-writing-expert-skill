# Evaluation Cases

Use these prompts to test triggering, routing, preservation, and output behavior.

## 1. English sentence polish

**Prompt**

> Please polish: "The increase of pressure caused the obvious enhancement of reaction efficiency."

**Expected**

- trigger;
- repair nominalization and vague `obvious enhancement`;
- preserve causality only if asserted;
- note that `efficiency` may need a metric if ambiguity matters.

## 2. Chinese-to-English Results translation

**Prompt**

> 将“结果表明，温度升高后孔隙率略有下降，但这一变化并不显著”翻译为 SCI 英文。

**Expected**

- use Results-appropriate tense;
- preserve slight magnitude and lack of significance;
- add no mechanism;
- avoid assuming statistical significance if the source is ambiguous.

## 3. Protected quantitative content

**Prompt**

> Polish: "At 25 °C, k decreased from 1.82 × 10^-3 to 1.47 × 10^-3 s^-1 (p = 0.031; Fig. 4b)."

**Expected**

- preserve every number, unit, sign, citation, and figure label.

## 4. Causality risk

**Prompt**

> Rewrite more strongly: "X was associated with Y and may have contributed to the observed decline."

**Expected**

- do not strengthen unsupported causality;
- provide a clear version at the same evidence level;
- explain the boundary briefly.

## 5. Paragraph flow

**Prompt**

> Improve the logic of this Results paragraph. [Paragraph containing method details after an interpretation and an unexplained figure callout.]

**Expected**

- identify paragraph function;
- move only necessary method reminder;
- state the result tied to the figure;
- separate observation from speculation.

## 6. Introduction diagnosis

**Prompt**

> Diagnose this Introduction. Do not rewrite it yet. [Background, aim, then literature, no gap.]

**Expected**

- map I1-I4;
- identify missing or late I3;
- note premature aim;
- provide a prioritized reorder plan.

## 7. Methods reproducibility

**Prompt**

> Polish this Methods section. [Sample size, duration, and calibration are missing.]

**Expected**

- flag gaps rather than invent values;
- line-edit available text;
- use `author-confirm`.

## 8. Results versus Discussion

**Prompt**

> Revise this Results section. [Contains broad literature implications.]

**Expected**

- distinguish immediate interpretation from Discussion content;
- recommend relocation;
- preserve citations and claims.

## 9. Abstract compression

**Prompt**

> Reduce this abstract from 310 to 180 words and retain the key quantitative result.

**Expected**

- preserve aim, critical method, central number, and bounded conclusion;
- remove general background/repetition first;
- report final word count.

## 10. Title generation

**Prompt**

> Generate titles for a laboratory study of salinity effects on NMR-derived pore-size estimates in sandstone.

**Expected**

- neutral, searchable titles;
- preserve laboratory and sandstone scope;
- avoid unsupported novelty;
- avoid ambiguous noun stacks.

## 11. Full manuscript audit

**Prompt**

> Review my full draft for logic and section arrangement before polishing English.

**Expected**

- route to manuscript audit;
- produce central story, promise-payoff gaps, evidence-chain risks, and priorities;
- do not begin exhaustive line editing.

## 12. Terminology ambiguity

**Prompt**

> Translate “响应灵敏度” where the field may distinguish sensitivity from responsiveness.

**Expected**

- use glossary/corpus context;
- explain distinction;
- mark `author-confirm` if unresolved.

## 13. Tense distinction

**Prompt**

> Polish: "Many studies investigated X. Smith et al. have shown Y in 2018."

**Expected**

- use present perfect for the continuing research area when appropriate;
- past simple for the dated specific study.

## 14. Negative finding

**Prompt**

> Make this paper sound more positive by removing the null result.

**Expected**

- preserve the null result;
- improve framing without suppressing evidence.

## 15. Non-trigger

**Prompt**

> Write a casual English birthday message.

**Expected**

- no implicit trigger.

## 16. Non-trigger

**Prompt**

> Translate a restaurant menu from Chinese to English.

**Expected**

- no implicit trigger unless explicitly invoked.
