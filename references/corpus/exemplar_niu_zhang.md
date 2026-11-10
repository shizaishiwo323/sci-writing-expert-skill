# Exemplar Style: Niu and Zhang

Use this file as the default style target when the user wants prose that is easy to read, or when drafting or revising an Introduction, Methods, Results, or Discussion. It describes how two papers organize sentences, paragraphs, and sections. It gives functional patterns with placeholders and contains no source paragraphs.

Copy the method of organization. Do not copy their scientific claims, their distinctive wording, or their section order when the user's study has a different logic.

## Exemplars

| ID | Paper | Section plan |
|---|---|---|
| E1 | Niu and Zhang (2018), Joint inversion of NMR and SIP data to estimate pore size distribution of geomaterials, *Geophys. J. Int.* 212, 1791-1805, doi:10.1093/gji/ggx501 | Introduction -> theory and its assumptions -> joint inversion method -> synthetic sample -> Berea sandstone and limitations -> conclusions |
| E2 | Niu, Zhang, and Prasad (2020), A framework for pore-scale simulation of effective electrical conductivity and permittivity of porous media in the frequency range from 1 mHz to 1 GHz, *JGR: Solid Earth* 125, e2020JB020515 | Introduction -> theoretical background -> general framework -> application to Berea sandstone -> comparison with experiment -> conclusions |

E2 is also record group P05 in `source_sentence_corpus.md`.

The author of this skill selected these papers because they are easy to read, use familiar words, avoid very long sentences, and arrange sentences, paragraphs, and sections in a clear order. In the Introduction, the first sentence opens with a general statement and each later sentence moves one step deeper.

## What the writing looks like in numbers

Counts come from automated text extraction, so treat them as approximate. Equations can distort sentence counts, so the table does not report maximum length.

| Measure | E1 | E2 | Practical target |
|---|---|---|---|
| Introduction median sentence length | about 25 words | about 23 words | 20-25 words |
| Introduction 90th percentile | about 36 words | about 40 words | below about 40 words |
| Introduction sentences over 40 words | about 5% | about 7% | rare, and only for lists or conditions that cannot be split |
| `not X but Y` constructions in the main text | 0 | 0 | avoid as a rhetorical device |
| New `-aware`, `-informed`, `-guided`, or `-enabled` labels | 0 | 0 | avoid |
| `elucidate`, `delineate`, `leverage`, `unveil`, `underscore`, `facilitate`, `pivotal`, `crucial`, `novel`, `insight` | 0 | 0 | avoid unless precise |

Hyphenated forms in both papers are field terms or ordinary modifiers, such as `pore-scale`, `low-frequency`, `water-saturated`, `solid-liquid`, and `two-step`.

## Section logic

1. Promise the order, then keep it. The last Introduction paragraph states the objective and lists the steps with `first`, `then`, and `finally`. The section headings follow that list.
2. Use theory to prepare the method. E1 ends its theory section by listing the assumptions behind each measurement. The method section then opens from those assumptions and gives the reason for a joint approach. E2 ends its background by comparing which polarization models suit porous rocks, and the framework uses those models.
3. Test in order of difficulty. E1 moves from a synthetic sample with exact models, to a synthetic sample with inaccurate models, to a real rock. E2 first compares the total response with experiment, then separates the contribution of each mechanism.
4. Separate the results from their application. E2 explains the comparison in one group of subsections and discusses possible uses in another.
5. Close in the same order as the paper. Each Conclusions section restates the method chain and then gives the main results, including the discrepancy or limit that matters. It does not add a new claim.

## Paragraph logic

Give each paragraph one job. The first sentence names the topic, and the remaining sentences develop only that topic.

### Introduction sequence

Use this sequence when it fits the study. One paragraph can cover two neighboring rows, as E1 does. The job names are diagnostic labels and do not need to appear in the text.

| Order | Job | E1 | E2 |
|---|---|---|---|
| 1 | Start with the broad need, then narrow it | why pore geometry matters and how it is usually measured | why geoelectrical methods are used and what is needed to interpret them |
| 2-3 | Explain the concepts or tools the reader needs | NMR and SIP as the promising tools | conductivity, permittivity, and how they are linked |
| 4 | Report current practice and its limits | assumptions of NMR and SIP porosimetry and when they fail | experiments, models, and pore-scale simulation |
| 5 | Name the closest prior work and the remaining gap | inversion problems, joint inversion, and the closest attempt | what simulation has covered and what remains hard |
| 6 | Explain why the gap exists and why it needs solving | missing joint treatment | thin interface layer -> fine mesh -> high cost -> need for a new method |
| Last | Objective, simplification, and road map | `In this study...` with the ordered steps | `The objective...` with scope and ordered steps |

### Sentence progression inside a paragraph

Each sentence should answer the question raised by the one before it.

```text
broad statement
-> specific example or definition
-> what this allows
-> what is required or what limits it
-> handoff to the next paragraph
```

Use these links:

- Begin with the idea the reader just met, and end with the new idea. The new idea can become the subject of the next sentence.
- Use `This`, `These`, or `Such` with a noun that names the earlier idea.
- Keep the same term for the same object. Do not vary a technical noun for style.
- Mark the relation with ordinary connectors: `Thus`, `However`, `Then`, `In addition`, `Since`, `because`, `Similarly`, `In practice`.
- End a paragraph on the topic that the next paragraph needs.

### Gap paragraph

```text
what has already been done
-> what remains difficult
-> the physical or practical reason
-> the consequence
-> what is therefore needed
```

Give the reason for the difficulty. A statement that a topic has received little attention is weak on its own.

## Sentence patterns

These patterns are common scientific forms. Replace every placeholder with the user's own content, and use a pattern only when the evidence supports it.

### Introduction

- `X is frequently used to study Y (citations).`
- `To correctly interpret X, one needs to understand Y.`
- `X quantifies a material's ability to do Y.`
- `X is related to Y through Z.`
- `In practice, some simplifications are usually made so that X can be inferred from Y.`
- `For instance, X assumes that A. However, A may not hold for B.`
- `Although X has been used to study A, it is still challenging to apply it to B. This is because C.`
- `It is therefore desirable to develop X that can do Y.`
- `One similar attempt is X, in which Y. However, Z has not been done.`
- `The objective of this study is to develop such an X.`
- `For simplicity, in this study, we only consider X.`
- `In the following, we first A. We then B. Finally, we C.`

### Definitions and terms

- Define a term before using it and say why the definition is needed: `To avoid confusion, we define X as Y.`
- Add short clarifications with `i.e.` or a brief phrase only when the reader needs them.
- Introduce a local name once and keep it: `For simplicity, we use X to refer to Y.`
- Give each symbol a plain meaning right after the equation: `where X is Y.`

### Methods

- Open a section with one sentence that states its job: `In this section, we propose X.`
- State the purpose before the operation: `To reduce X, we do Y.`
- Number the procedure when several steps depend on each other: `The first step is to do X.`
- Give the output of each step and the next step that uses it.
- Introduce an assumption directly, then give its limit: `We assume X. This assumption is usually valid when Y.`

When explaining how a parameter is obtained, follow this order:

1. state what parameter is needed and why it matters;
2. name the established method and cite it;
3. compare it briefly with other methods when the choice needs a reason;
4. give the steps for this study.

### Results

- Start with the comparison: `A comparison of X and Y shows that Z, especially for W.`
- Move through the data in a natural order, such as high to low frequency or simple to complex case.
- Report the difference and give its size: `However, the increase in X is about A, much smaller than B.`
- Keep the explanation cautious: `This discrepancy might be due to X.`
- Explain a further analysis by its purpose: `To identify the contribution of X, we also conducted Y.`
- Use a forward reference when the explanation appears later.

### Discussion and limitations

- State the job of the subsection first: `In this subsection, we discuss the limitations of X.`
- List limits with their conditions: `First, X may only be valid for Y because Z.`
- Tell the reader what follows from the limit: `In that case, X may not improve Y.`
- Keep the closing claim modest: `This work might constitute a first step towards X.`

### Conclusions

```text
what was developed or done
-> how it works, in the same order as the paper
-> what test was used
-> main agreement
-> main discrepancy and likely reason
```

## Wording habits

- Use familiar verbs: `use`, `consider`, `determine`, `show`, `apply`, `develop`, `estimate`, `compare`, `relate`.
- Keep field terms when they are the precise names. Simple wording should not replace `permeability`, `relaxation time`, or `complex conductivity`.
- Calibrate claims with `may`, `might`, `could`, `seems`, `to a certain extent`, and `fairly consistent`.
- Express contrast directly with `However`, `While`, `whereas`, `In contrast`, or `Although`.
- Explain a mechanism in a short causal sequence. A short thought experiment can help: `Consider a material with X. As Y decreases, Z occurs.`
- Split a sentence when it carries two claims, or when a definition and a comparison compete for the reader's attention.

## Do not imitate

These papers are strong models of organization and clarity, but some local language should not be copied:

- non-native grammar slips such as `Comparing to` where `Compared with` is correct, `resulted from` where `resulting from` is needed, or a singular verb with `a number of`;
- occasional inflated or unnecessary words such as `profound feature` or `utilized`;
- repeated `However` within one paragraph;
- long comma-linked sentences in equation-heavy passages.

Do not force these patterns into every paragraph. If every sentence begins with the same connector, the text becomes formulaic again.

## Quick check

1. Can a reader state the one job of each paragraph?
2. Does each sentence follow from the one before it?
3. Do the paragraphs move from broad to specific without a jump?
4. Is the gap explained by a concrete reason?
5. Does the road map match the section order?
6. Are most sentences short enough to read once, without losing necessary conditions?
7. Would a researcher in the field recognize every word and term?
8. Did the revision add any new compound label or rhetorical contrast?
9. Are all claims still within the original evidence?
