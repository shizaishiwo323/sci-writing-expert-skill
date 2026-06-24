# Dash and Compound Policy

## Purpose

Preserve normal scientific compounds while preventing newly invented labels during translation or revision.

## Core Rule

Compare the source with the revision. Do not convert an ordinary phrase into a new compact term merely to make the English sound more academic.

A hyphenated or dash-based form may be retained or introduced when it is:

- already present in the source or manuscript glossary;
- an established term in the field;
- a conventional compound modifier required for clarity;
- a numerical range or established paired relation;
- required by the target journal.

Otherwise, use ordinary syntax.

## Standard Terms Are Allowed

Do not apply a blanket ban to hyphens. Depending on field and context, normal forms include:

- `time-resolved`;
- `high-throughput`;
- `double-blind`;
- `first-order`;
- `pore-scale`;
- `field-scale`;
- `high-resolution image`;
- `model-based`;
- `physics-based`;
- `data-driven`.

A correction such as `high resolution image` to `high-resolution image` is acceptable because it is normal grammar, not term invention.

## Newly Coined Labels

Usually rewrite forms such as:

- `mechanism-aware interpretation`;
- `signal-structure bridge`;
- `connectivity-breakthrough nexus`;
- `process-response signature`;
- newly created three-part compounds.

Prefer:

- `interpretation based on the proposed mechanism`;
- `the relation between the signal and structure`;
- `the relation between connectivity and breakthrough`;
- `the response associated with the process`.

Use these plain forms only when the scientific relation is supported by the source.

## Warning Patterns

New forms ending in `-aware`, `-informed`, `-guided`, `-enabled`, `-sensitive`, `-linked`, `-driven`, or `-based` require a reason.

These endings are warnings, not automatic errors. Keep a standard expression such as `data-driven model`; reject an unnecessary label created from plain source wording.

## Multi-part Compounds

Treat three-part or longer compounds as high risk. Keep them only when they are established names, protected model or method names, or genuinely clearer than ordinary syntax.

Otherwise unpack the relation, for example:

```text
the relation among signal changes, pore structure, and transport
```

## Chinese-to-English Translation

Do not automatically compress Chinese modifier chains into English compounds.

```text
基于机理的解释
-> interpretation based on the mechanism
```

Do not automatically change it to `mechanism-aware interpretation`.

```text
考虑孔隙结构的模型
-> a model that accounts for pore structure
```

A compact technical alternative is appropriate only when established or defined.

## Dash Types

- Use a hyphen for established compounds and conventional compound modifiers.
- Use an en dash for ranges or paired relations only when journal style requires it.
- Do not add an em dash merely for dramatic emphasis in formal manuscript prose.
- Preserve Unicode and LaTeX dash forms in protected technical expressions unless formatting normalization is requested.

## Unknown Terms

When standardness is uncertain:

1. check the source, glossary, and surrounding manuscript;
2. check supplied target articles or journal guidance;
3. preserve a clearly defined and consistent term;
4. otherwise use ordinary syntax;
5. mark `author-confirm` only when the compact term affects meaning or terminology consistency.

## Output Gate

Before returning revised text:

1. identify every dash-based form that appears only in the revision;
2. verify that each new form is established, defined, grammatically required, a range or paired relation, or journal-required;
3. rewrite every unsupported compact label;
4. check that standard technical compounds were not removed through overcorrection.

A revision passes only when no unsupported compact label was added and no established technical compound was damaged.
