# Protected Content and Evidence

## Purpose

Prevent fluent editing from altering scientific content.

## 1. Build a protection map

### Exact tokens

Preserve exactly unless correction is explicitly requested:

- numbers, ranges, percentages, p-values, confidence intervals, sample sizes;
- signs, inequalities, exponents, subscripts, superscripts, and significant figures;
- units and unit spacing;
- equations, LaTeX, variable names, code identifiers, and model names;
- citations, reference order, DOI strings, figure/table/equation labels;
- chemical formulas, gene/protein names, species names, and abbreviations.

### Semantic constraints

Record:

- agent: who performed or observed the action;
- object: what was measured, changed, or compared;
- direction: increase/decrease, higher/lower, positive/negative;
- baseline or comparator;
- tested conditions, population, material, spatial scale, and time scale;
- whether the statement is descriptive, associative, causal, predictive, or normative;
- degree of certainty;
- whether the claim belongs to this study or prior work.

## 2. Evidence-strength ladder

```text
direct observation or formal derivation
> robust result under stated conditions
> interpretation supported by converging evidence
> indication or association
> plausible possibility
> speculation
```

A revision must remain on the same rung unless the user supplies justification.

Unsafe strengthening includes:

- `was associated with` -> `caused`
- `suggests` -> `demonstrates`
- `may improve` -> `improves`
- `under the tested conditions` -> an unrestricted statement
- `one possible explanation` -> `the mechanism`
- `higher` -> `significantly higher` without support
- `consistent with` -> `confirms`

Unsafe weakening includes removing a supported quantitative result or turning a formal result into vague speculation.

## 3. Ownership of claims

Keep the source of each claim visible:

- cited study: author/citation in the sentence or unambiguous local context;
- accepted knowledge: present-tense factual statement, with citation where required;
- present study: `we`, `this study`, `our analysis`, or clear section context;
- inference: an explicit signal such as `suggests`, `is consistent with`, or a modal.

Do not let an agentless passive make another study's work look like the current authors' work.

## 4. Data and figure integrity

When revising Results:

- distinguish absolute and relative change;
- distinguish percentage points from percent change;
- retain variability and uncertainty;
- keep the same comparator and denominator;
- do not call a pattern monotonic, linear, stable, or negligible without support;
- ensure textual values agree with supplied tables and figures.

If prose and data conflict, flag the conflict rather than silently choosing one.

## 5. Citation integrity

Do not:

- invent a reference;
- move a citation so it appears to support a different claim;
- merge sentences in a way that broadens citation scope;
- imply consensus from a single study;
- remove the cited author when attribution is needed.

When splitting or combining sentences, preserve citation-to-claim alignment.

## 6. `author-confirm` protocol

Use when:

- a term has more than one field-specific meaning;
- a causal interpretation is plausible but unstated;
- a numerical inconsistency appears;
- a cited claim cannot be attributed safely;
- a limitation or implication requires new scientific information;
- grammar can be repaired only after choosing between scientific interpretations.

Format:

```text
author-confirm: Does X refer to ... or ...? The revision currently uses the more conservative interpretation.
```
