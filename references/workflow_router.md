# Workflow Router

Choose the smallest reliable operation.

## 1. Classify the input unit

| Unit | Primary question |
|---|---|
| phrase or title fragment | Is the wording grammatical, precise, and conventional? |
| sentence | Does it express the intended proposition clearly and at the right strength? |
| paragraph | Does it perform one main function with a coherent evidence sequence? |
| section | Are the expected rhetorical moves present, ordered, and connected? |
| manuscript | Does the paper sustain one research story and evidence chain? |

## 2. Classify the requested outcome

- `translate`: Chinese or mixed-language source becomes publication-ready English.
- `polish`: improve English without changing organization or substance.
- `deep-revise`: allow clause, sentence, or paragraph reconstruction.
- `diagnose`: identify problems without rewriting everything.
- `restructure`: change paragraph or section order.
- `compress`: reduce length while preserving core information.
- `expand`: make implicit logic explicit using only supplied information.
- `generate`: draft from supplied facts, moves, and constraints.
- `compare`: explain differences between alternatives.

Do not treat `polish` as permission to add ideas.

## 3. Determine the highest problem level

Use the first level that applies:

1. **Scientific integrity**: contradiction, unsupported causality, changed denominator, missing condition, citation mismatch, or unclear ownership.
2. **Storyline/architecture**: unclear question, gap, contribution, evidence chain, or section placement.
3. **Paragraph logic**: mixed functions, missing topic sentence, poor order, unclear referent, or abrupt transition.
4. **Sentence construction**: ambiguous syntax, overloaded subject, modifier attachment, tense/voice mismatch, or faulty parallelism.
5. **Surface style**: word choice, article, preposition, punctuation, concision, or idiom.

Fixing level 5 cannot compensate for a level 1-3 failure.

## 4. Routing matrix

### Phrase or sentence

Load:

- `protected_content_and_evidence.md`
- `sentence_revision.md`
- `grammar_tense_voice_articles.md` as needed
- `claim_strength_causality_modality.md` for evidence interpretation

Return the revision first.

### Chinese source

Load:

- `protected_content_and_evidence.md`
- `zh_en_translation.md`
- the relevant section reference
- `terminology_definition.md` when terminology is uncertain

Translate by function, not source-language word order.

### Paragraph

Load:

- `cohesion_and_paragraphs.md`
- the relevant section file
- claim or grammar references as needed

Identify paragraph function before reordering.

### Complete section

Load the matching section file and `output_contracts.md`.

Diagnose missing, duplicated, or misordered moves before line editing.

### Multiple sections or full paper

Load:

- `manuscript_architecture_audit.md`
- relevant section references
- `target_article_adaptation.md` if journal/corpus material is available

Return priorities before large-scale rewriting.

## 5. Question policy

Ask only when one of these blocks safe work:

- the scientific meaning has two materially different interpretations;
- a technical term has multiple valid translations with different meanings;
- journal constraints such as word count or format are essential but absent;
- a suspected data/citation error cannot be handled conservatively;
- the user requests a stronger claim without supplying evidence.

Otherwise proceed conservatively and flag the assumption.

## 6. Edit-depth scale

- **A — copy edit:** grammar, articles, punctuation, local idiom.
- **B — line edit:** clause order, concision, clarity, information flow.
- **C — paragraph edit:** sentence order, topic sentence, cohesion, split/merge.
- **D — section edit:** rhetorical moves, subsection order, duplication, missing links.
- **E — manuscript edit:** storyline, promise-payoff, evidence chain, architecture.

Do not silently exceed the requested level. If a higher-level defect blocks a lower-level task, state it and offer the smallest safe repair.
