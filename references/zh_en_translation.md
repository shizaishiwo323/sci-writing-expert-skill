# Chinese-to-English Scientific Translation

## Goal

Produce natural scientific English that preserves the Chinese scientific proposition, evidence strength, and rhetorical role.

Translation is not word substitution. Reconstruct the sentence in the conventional grammar of the target section.

## 1. Workflow

### A. Parse the proposition

Identify:

- topic and main claim;
- actor or logical subject;
- action or relation;
- object;
- conditions and scope;
- evidence source;
- comparison or causal direction;
- uncertainty and degree;
- rhetorical function.

### B. Choose an English subject

Prefer a concrete subject:

- `This study...`
- `The proposed method...`
- `The results...`
- `Figure 3...`
- `Increasing temperature...`
- `Previous studies...`

Do not repeatedly translate `本文`, `本研究`, `可以看出`, or `研究发现` as empty framing when a more informative subject is available.

### C. Choose section-appropriate tense

- Introduction background: present simple.
- Specific prior study: past simple.
- Current body of research: present perfect.
- Study-specific procedure: usually past simple.
- Study result: usually past simple.
- General relationship: present simple only when justified.
- Interpretation: calibrated reporting verb or modal.

### D. Rebuild information order

Prefer:

```text
known/contextual information -> new information
condition -> main proposition
main clause -> bounded qualification
clear cause -> effect or effect -> cause
```

Keep subject and main verb reasonably close.

### E. Remove source-language artifacts

Watch for:

- empty openers;
- repeated abstract subjects;
- long strings of prepositional phrases;
- overpacked noun stacks;
- excessive passive voice;
- vague evaluative phrases;
- multiple logical relations joined only by commas.

### F. Back-check

Verify:

- no condition was omitted;
- comparison direction is unchanged;
- causality was not strengthened;
- certainty and time reference remain accurate;
- negation is preserved;
- claim ownership is correct.

## 2. High-risk Chinese patterns

### `随着……的发展`

Do not automatically write `With the continuous development of...`.

Use a substantive form:

- `Recent advances in X have enabled...`
- `X is increasingly used for...`
- or omit the framing.

### `越来越多`

Avoid `more and more` in formal prose.

Possible choices:

- `an increasing number of`
- `has received increasing attention`
- `is increasingly used`

Do not imply a measured trend without support.

### `对……进行了研究/分析/测试`

Prefer a direct verb:

- `We investigated X.`
- `X was analyzed using Y.`
- `The study evaluated X under Y conditions.`

### `结果表明`

Choose by evidence:

- `The results showed that...` for a completed observation.
- `The results indicate that...` for a supported current interpretation.
- `These findings suggest that...` for a cautious inference.

Do not use `prove` unless there is formal proof.

### `可以看出/由图可知`

Prefer:

- `Figure 2 shows that...`
- `As shown in Figure 2, ...`
- or state the result directly.

Avoid `It can be seen that` when a direct construction is clearer.

### `具有重要意义`

Do not write `has important significance`.

State the specific supported value:

- `This finding helps explain...`
- `The method may improve...`
- `The result provides evidence for...`

If no concrete implication is supplied, omit or mark `author-confirm`.

### `为……提供理论依据/参考`

Avoid `theoretical basis` unless a theory is actually established.

Possible calibrated forms:

- `provides evidence for`
- `provides a basis for`
- `may inform`

### `在一定程度上`

Identify what is limited:

- magnitude: `partly`, `to some extent`;
- conditions: state the actual boundary;
- uncertainty: use a modal or cautious reporting verb.

### `首次`

Use `for the first time` only after literature verification. Otherwise mark `author-confirm`.

## 3. Terminology

Use, in order:

1. the user's approved glossary;
2. terminology already defined in the manuscript;
3. stable usage in target articles;
4. a recognized field-standard term.

When two translations have different meanings, provide the safer version and explain the alternative briefly.

## 4. Default output

```text
Translation:
...

Notes:
- terminology or ambiguity note, only if needed;
- claim-strength note, only if needed.
```

Do not include a literal translation unless requested.
