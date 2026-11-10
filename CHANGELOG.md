# Changelog

## 0.3.0 — 2026-11-10

- Added `references/corpus/exemplar_niu_zhang_records.md`: 126 records from the two exemplar papers, Niu and Zhang (2018, new group P08, 59 records) and Niu et al. (2020, P05 continued, 67 records). 44 chain records take a paragraph sentence by sentence and record how each sentence links to the one before it; 82 sentence records follow the existing format. All main sections of both papers are covered. No source sentences are stored.
- Added 34 rule cards derived from these records, including new families `BKG`, `LNK`, `MAP`, `CLO`, and `STY`, and extended the `Derived from` line of six existing cards.
- Added the exemplar pass, five function tags, and paper ID P08 to the extraction protocol.
- Updated the exemplar overview, source notes, and `SKILL.md` loading rules. The 70 earlier records and the negative samples are unchanged.

## 0.2.1 — 2026-11-10

- Allowed the book PDF at the repository root in validation; other source documents remain forbidden.
- Added guidance for consulting the book when the references do not settle a question.
- Updated the notice, README, and source notes to state that the PDF is present.

## 0.2.0 — 2026-11-10

- Merged the sentence corpus, rule cards, negative samples, and extraction protocol from `academic-sentence-polisher`.
- Removed full source sentences from the public corpus while keeping 70 records.
- Added an easy-to-read writing model based on Niu and Zhang (2018) and Niu et al. (2020).
- Added readability guidance and corpus loading rules.

## 0.1.0 — 2026-06-24

- Created a comprehensive Codex Skill for SCI manuscript work.
- Added Chinese-to-English scientific translation.
- Added sentence, paragraph, section, and manuscript-level routing.
- Added IMRaD, Abstract, and Title modules.
- Added scientific-integrity and evidence-strength safeguards.
- Added target-journal adaptation, tests, validation, installation, and publishing scripts.
