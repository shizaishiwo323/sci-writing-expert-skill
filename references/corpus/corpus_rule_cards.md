# Corpus Rule Cards

These cards compress the sentence records in `source_sentence_corpus.md` and `exemplar_niu_zhang_records.md` into executable rules. The first group (DEF-01 to IMP-04) covers sentence-level polishing and must not change paragraph structure. The second group, added from the exemplar records, also covers how sentences, paragraphs, and sections follow one another. No card may change scientific logic, evidence, citations, variables, equations, or figure labels.

Card families: `DEF` definitions, `GAP` gaps, `AIM` aims, `MET` methods, `ASS` assumptions and limits, `RES` results, `CON` comparisons, `IMP` interpretation, `BKG` background and openings, `LNK` links between sentences and sections, `MAP` road maps, `CLO` Conclusions and abstracts, `STY` surface forms.

Each rule card includes `Derived from` so the rule can be traced back to specific corpus records. Do not add future rules without this mapping.

## DEF-01: Define central terms at first meaningful use

**Derived from:** P01-S01, P05-S03, P06-S02, P05-S13

**Problem addressed:** AI-style writing often introduces a fancy noun or named framework without telling the reader what it means.  
**Rule:** If a term is central and not self-explanatory, define it immediately with a short appositive, relative clause, or `where` clause.  
**Preferred patterns:**
- `This relation, known as X, relates A to B through C.`
- `Here, X means Y.`
- `X, with condition C, means that A is higher than B.`
**Avoid:** New labels such as `mechanism-diagnostic bridge` unless the label is defined and necessary.  
**Skill instruction:** Add or preserve definitions for central terms; do not define common terms just to sound formal.

## DEF-02: Pair equations and symbols with plain-language meaning

**Derived from:** P01-S05, P02-S04, P04-S04, P06-S03, P07-S03

**Problem addressed:** Polishing can make formula sentences cleaner but accidentally remove the meaning of symbols.  
**Rule:** Keep equations, variables, inequalities, and ranges intact; simplify only the surrounding prose.  
**Preferred patterns:**
- `Here, X = A/B, where A is ... and B is ...`
- `The X number compares A to B and can be defined as X = ...`
- `X has values ..., where X denotes ...`
**Avoid:** Rewriting equations, deleting units, or replacing variables with vague pronouns.  
**Skill instruction:** Treat equations and variable definitions as protected content.

## DEF-03: Define regimes through observable behavior

**Derived from:** P02-S08, P03-S01, P06-S04, P07-S03

**Problem addressed:** AI often treats regime labels as self-explanatory.  
**Rule:** When a sentence introduces a regime, state the behavior, condition, or observation that defines it.  
**Preferred patterns:**
- `The X pattern is characterized by Y at Z.`
- `For small X, Y occurs in regime Z, where criterion C holds.`
- `This process is known as X and can be described by Y.`
**Avoid:** `X is a critical regime` without saying what physically identifies it.  
**Skill instruction:** Keep regime labels tied to their physical or measurable criteria.

## GAP-01: Acknowledge existing capability before naming the hard case

**Derived from:** P04-S01, P07-S01, P05-C07

**Problem addressed:** AI gap sentences often make prior work sound useless.  
**Rule:** Use concession when the method works in one setting but remains difficult in another.  
**Preferred patterns:**
- `Although X can provide insight into A, its application to B remains challenging.`
- `While X can provide insight into A, interpreting X in B remains challenging.`
**Avoid:** `Previous studies failed to...` unless the source explicitly says so.  
**Skill instruction:** Preserve balanced gap framing and avoid dismissive language.

## GAP-02: Make the missing piece specific

**Derived from:** P01-S02, P04-S02, P07-S02

**Problem addressed:** Vague gaps such as `little is known` do not help the reader.  
**Rule:** Name the unresolved relation, mechanism, metric, scale, condition, or variable.  
**Preferred patterns:**
- `How X changes with Y, and how this change can be observed and quantified, remains unresolved.`
- `A physical understanding of X remains limited because Y is not well constrained.`
**Avoid:** `This remains a major challenge` without a specific missing element.  
**Skill instruction:** Replace broad unknowns with concrete unresolved questions.

## GAP-03: State scope limitations, not literature failure

**Derived from:** P02-S01, P03-S03

**Problem addressed:** AI gap language often overstates by saying prior studies `ignored` or `failed`.  
**Rule:** Describe what prior studies mainly focused on and what assumption remains untested.  
**Preferred patterns:**
- `Most studies on X have focused on cases where Y remains constant.`
- `Existing classifications often rely on Y rather than Z.`
**Avoid:** `Previous studies failed to consider...` unless directly supported.  
**Skill instruction:** Use scope-based gap wording for literature review sentences.

## GAP-04: Use exclusivity words only with evidence

**Derived from:** P02-S01, P03-S03, P07-S02

**Problem addressed:** Words such as `solely`, `no study`, and `only` can overclaim.  
**Rule:** Retain exclusivity only when the original literature review supports it; otherwise downgrade.  
**Preferred patterns:**
- `often relies on`
- `has primarily focused on`
- `few studies have examined`
**Avoid:** `no study has shown` when the author cannot verify the full literature.  
**Skill instruction:** Downgrade high-risk gap claims unless the user confirms the literature basis.

## AIM-01: Say what the study does before why it matters

**Derived from:** P01-S03, P06-S01, P08-S02

**Problem addressed:** AI often turns study aims into promotional contribution claims.  
**Rule:** Aim sentences should name method, object, and target relation.  
**Preferred patterns:**
- `Here, we use X to obtain Y and analyze Z.`
- `This study aims to understand whether model X remains applicable under Y.`
**Avoid:** `This study provides unprecedented insight into...`  
**Skill instruction:** Keep aim sentences procedural, direct, and bounded.

## AIM-02: Define a new metric by operation and output

**Derived from:** P02-S02, P02-S05

**Problem addressed:** New metric names can sound like decorative frameworks.  
**Rule:** When introducing a metric, state what it segments, measures, calculates, or compares.  
**Preferred patterns:**
- `We propose X, which segments A to calculate B.`
- `We use X to determine Y.`
**Avoid:** `a powerful X-based framework` without operational content.  
**Skill instruction:** If a new term is necessary, immediately attach what it does.

## AIM-03: Keep framework claims concrete

**Derived from:** P05-S02, P05-S06

**Problem addressed:** `framework` can become a fancy placeholder.  
**Rule:** Use `framework` only when the sentence specifies the processes included and quantities produced.  
**Preferred patterns:**
- `We develop a framework to consider X in Y, enabling calculation of Z.`
- `The framework is outlined in Figure X, and the details are discussed below.`
**Avoid:** `a comprehensive framework for new understanding` without inputs and outputs.  
**Skill instruction:** Replace empty framework language with concrete method-output wording.

## MET-01: Use direct verbs for method steps

**Derived from:** P02-S05, P04-S05, P05-S05

**Problem addressed:** AI often turns simple method actions into nominalized prose.  
**Rule:** Prefer verbs such as `use`, `segment`, `calculate`, `scan`, `extract`, and `compare`.  
**Preferred patterns:**
- `We segment X along Y and calculate Z.`
- `Samples were scanned at X resolution, and Y segmentation was performed on Z.`
**Avoid:** `the implementation of segmentation was conducted`.  
**Skill instruction:** Convert heavy nominalizations into direct method verbs.

## MET-02: Preserve reproducibility details

**Derived from:** P01-S04, P04-S05, P07-S08

**Problem addressed:** Concision edits can remove parameters needed for reproducibility.  
**Rule:** Keep resolution, ranges, units, boundary conditions, sample states, and figure references.  
**Preferred patterns:**
- `X varies from A to B, defined by criteria C and D.`
- `Samples were scanned at X resolution.`
**Avoid:** Removing numeric values to make the sentence smoother.  
**Skill instruction:** Protect all numerical and procedural details.

## MET-03: Explain model representation, not model ambition

**Derived from:** P03-S04, P07-S05

**Problem addressed:** AI method prose often adds unnecessary claims about what the model enables.  
**Rule:** A model sentence should say what the model represents and how.  
**Preferred patterns:**
- `The X model represents Y as Z.`
- `We use A and B models to represent X.`
**Avoid:** `This model captures the full complexity of...` unless explicitly supported.  
**Skill instruction:** Keep representation language modest and literal.

## MET-04: Link simplified methods to intended scope

**Derived from:** P06-S05, P07-S04, P07-S05

**Problem addressed:** Simplified models can be polished into overconfident descriptions.  
**Rule:** State what the simplified model is intended to mimic or capture.  
**Preferred patterns:**
- `We use simplified models to mimic X, aiming to capture Y.`
- `While X is complex in natural systems, we use idealized Y in the simulation.`
**Avoid:** Claiming that a simplified model fully represents natural complexity.  
**Skill instruction:** Preserve the intended level of simplification.

## ASS-01: State the condition that justifies a simplification

**Derived from:** P03-S06, P05-S07, P08-S18

**Problem addressed:** AI sometimes deletes the reason an assumption is acceptable.  
**Rule:** Keep the parameter range, scale relation, or physical condition that supports an assumption.  
**Preferred patterns:**
- `For the range of X considered here, Y is small relative to Z, allowing us to neglect A.`
- `This model is only valid for X with condition C.`
**Avoid:** `We neglect A` without the condition.  
**Skill instruction:** Never remove assumption boundaries.

## ASS-02: Acknowledge excluded factors without adding new conclusions

**Derived from:** P02-S10, P04-S10

**Problem addressed:** AI may turn limitations into speculative discussion.  
**Rule:** Name what the study focuses on and which factor remains outside that focus.  
**Preferred patterns:**
- `While this study focuses on X, Y remains an important factor that can influence Z.`
- `X may be less suitable for Y where Z is not available.`
**Avoid:** Expanding a limitation into a new mechanism.  
**Skill instruction:** Keep out-of-scope factors as limitations or context.

## ASS-03: Pair limitation with scope, not reassurance

**Derived from:** P03-S10, P05-S10

**Problem addressed:** AI often softens limitations until they disappear.  
**Rule:** A limitation can be followed by relevance, but the constraint must remain visible.  
**Preferred patterns:**
- `Although this study is based on X, Y has also been observed in Z.`
- `This may be due to X, which cannot represent Y.`
**Avoid:** `This limitation does not affect the conclusions` unless explicitly shown.  
**Skill instruction:** Preserve limitations and avoid over-reassuring language.

## RES-01: Report observation before interpretation

**Derived from:** P03-S07, P04-S06

**Problem addressed:** AI result sentences often jump to mechanism before the result is clear.  
**Rule:** State the measured or observed change first; add interpretation only if already present.  
**Preferred patterns:**
- `With decreasing X, Y decreases more than Z, reflecting A.`
- `As seen in Figure X, Y changes from A to B.`
**Avoid:** Starting with `This proves that...`  
**Skill instruction:** Keep result-first ordering.

## RES-02: Preserve comparison baselines

**Derived from:** P06-S07, P07-S08

**Problem addressed:** Polishing can make comparisons smoother but less precise.  
**Rule:** Keep baseline condition, comparison condition, direction of change, and variables.  
**Preferred patterns:**
- `Compared with X at condition A, X at conditions B and C shows Y.`
- `For X cases, Y varied considerably despite minor changes in Z.`
**Avoid:** `Y changed across cases` when the baseline matters.  
**Skill instruction:** Do not drop the reference condition in comparison sentences.

## RES-03: State both changed and unchanged quantities

**Derived from:** P01-S06, P07-S06

**Problem addressed:** AI may simplify contrastive results by reporting only the change.  
**Rule:** If one variable changes and another remains stable, preserve both.  
**Preferred patterns:**
- `From A to B, X increases, while Y remains unchanged.`
- `At A, X remains nearly constant; as Y changes, X increases.`
**Avoid:** `X changes with Y` when the unchanged part is important.  
**Skill instruction:** Preserve negative or stable results because they often control interpretation.

## RES-04: Anchor figure sentences to the key visual information

**Derived from:** P03-S09, P04-S08

**Problem addressed:** Figure references can become empty signposts.  
**Rule:** State what the figure shows, including the trend, transition, or contrast.  
**Preferred patterns:**
- `Figure X shows that A leads to B, while C results in D.`
- `In Figure X, A represents ..., while B corresponds to ...`
**Avoid:** `Figure X clearly illustrates the mechanism` without saying what is shown.  
**Skill instruction:** Keep figure labels and add only the observed content already present.

## RES-05: Keep magnitude words proportional to data

**Derived from:** P01-S06, P02-S06, P06-S10, P05-S35

**Problem addressed:** AI overuses `dramatically`, `significantly`, and `substantially`.  
**Rule:** Use magnitude words only when supported by numeric values, figure trends, or original wording.  
**Preferred patterns:**
- `increases`
- `decreases`
- `varies considerably` only with a clear comparison
**Avoid:** `remarkably`, `fundamentally`, `profoundly` unless the paper explicitly supports them.  
**Skill instruction:** Downgrade unsupported intensifiers to neutral trend verbs.

## CON-01: Compare matched objects

**Derived from:** P02-S07, P06-S10

**Problem addressed:** AI comparison sentences can compare mismatched scales or concepts.  
**Rule:** Use contrast structures only for comparable regimes, cases, variables, or models.  
**Preferred patterns:**
- `Unlike A, where X occurs, B involves Y.`
- `Compared to A, B has a stronger influence on C.`
**Avoid:** Comparing a method with a result or a mechanism with an application.  
**Skill instruction:** Check that both sides of a comparison are parallel.

## CON-02: Use contrast to clarify mechanism, not to dramatize

**Derived from:** P03-S09, P07-S07

**Problem addressed:** AI turns contrasts into rhetorical emphasis.  
**Rule:** Let the contrast identify a physical or methodological difference.  
**Preferred patterns:**
- `A leads to B, while C results in D.`
- `A remains constant, whereas B varies with C.`
**Avoid:** `in stark contrast` unless the data justify a stark difference.  
**Skill instruction:** Prefer neutral contrast words such as `whereas`, `while`, and `compared with`.

## CON-03: Keep concessive uncertainty in classification

**Derived from:** P02-S09, P06-S04

**Problem addressed:** Gradual regime boundaries are often polished into hard categories.  
**Rule:** Preserve markers such as `subtle`, `features of`, `approximately`, and `roughly`.  
**Preferred patterns:**
- `Although the boundary is subtle, X exhibits features of Y.`
- `The pattern is roughly uniform.`
**Avoid:** Converting partial classification into definitive labels.  
**Skill instruction:** Do not remove uncertainty markers from regime-classification sentences.

## IMP-01: Use tentative verbs for inference

**Derived from:** P01-S08, P01-S09, P05-S09, P08-C11, P05-S42

**Problem addressed:** AI often upgrades `suggests` to `demonstrates` or `proves`.  
**Rule:** Use tentative verbs when moving from result to mechanism, discrepancy explanation, or broader relation.  
**Preferred patterns:**
- `This trend suggests that there might be a relation between X and Y.`
- `This discrepancy might be due to X.`
- `This behavior is consistent with Y.`
**Avoid:** `proves`, `confirms`, `establishes` unless the original evidence is decisive.  
**Skill instruction:** Preserve or restore the original evidence strength.

## IMP-02: Name the mechanism only if it is already present

**Derived from:** P03-S08, P06-S08

**Problem addressed:** AI polishers invent mechanism to make sentences sound deeper.  
**Rule:** Clarify existing mechanism language but do not add new causal processes.  
**Preferred patterns:**
- `X forms due to Y, based on feedback between A and B.`
- `This is expected because A rather than B controls C.`
**Avoid:** Adding `thereby revealing a feedback mechanism` when the original did not state one.  
**Skill instruction:** If mechanism is uncertain, mark `author-confirm`.

## IMP-03: Keep broad relations bounded by domain and evidence type

**Derived from:** P01-S10, P06-S09

**Problem addressed:** Local results can be polished into universal conclusions.  
**Rule:** Preserve phrases such as `for granular materials`, `in simulations`, `under these conditions`, and `for the tested cases`.  
**Preferred patterns:**
- `Our numerical results suggest that, for X, a relation might exist between A and B.`
- `This indicates that applicability depends on Y.`
**Avoid:** Removing scope qualifiers to make a sentence shorter.  
**Skill instruction:** Do not broaden local evidence.

## IMP-04: State practical meaning through the specific error or use case

**Derived from:** P04-S09, P07-S10

**Problem addressed:** AI implication sentences often become generic `new insights` claims.  
**Rule:** Name the interpretation error avoided, the metric tracked, or the application condition.  
**Preferred patterns:**
- `This pattern ensures that X does not exceed Y, avoiding Z.`
- `This trend reflects X and indicates that Y can track Z.`
**Avoid:** `These findings provide important insights into...`  
**Skill instruction:** Replace generic contribution language with the concrete function of the result.

---

# Cards added from the exemplar records

The cards below are derived from `exemplar_niu_zhang_records.md` (record groups P08 and P05-C/P05-S11 onward). They cover how sentences follow one another and how paragraphs and sections are arranged, as well as single-sentence patterns. They may reorder sentences inside a paragraph when that repairs the logic. They still must not add facts, mechanisms, citations, or claims.

## BKG-01: Open with what is used or what controls, not with importance

**Derived from:** P08-C01, P08-S05, P08-S07, P05-C01, P05-S11

**Problem addressed:** Openings such as `X has attracted increasing attention` say nothing the reader can use.  
**Rule:** Make the first sentence a plain statement about the study's object: what it controls, or what a method family is used for. Then narrow one step per sentence.  
**Preferred patterns:**
- `X plays an important role in controlling Y in Z (general source).`
- `X methods are frequently used in F to study A and B (sources).`
**Avoid:** Opening on the growth of a field, or on an object broader than the one the paper studies.  
**Skill instruction:** Rewrite an attention-based opening as a statement of use or control, using only the author's content.

## BKG-02: End the first paragraph on the requirement that the paper serves

**Derived from:** P05-C01, P05-S12, P08-C01

**Problem addressed:** A first paragraph that lists applications leaves the reader without a direction.  
**Rule:** Close the opening paragraph with what must be known or measured in order to do the practical task. The terms in that sentence should be the topics of the next paragraphs.  
**Preferred patterns:**
- `To correctly interpret X, one needs to understand Y and its controlling factors such as A and B.`
- `X can be measured directly by A. In addition, indirect methods can be used.`
**Avoid:** Ending the paragraph on a citation list.  
**Skill instruction:** Check that the last sentence of paragraph 1 names the concepts that paragraphs 2 and 3 develop.

## BKG-03: Teach each needed concept in its own short paragraph

**Derived from:** P05-C02, P05-C03, P05-S13, P05-S14, P08-C02

**Problem addressed:** Concepts are often introduced inside the literature review, where the reader meets them half-defined.  
**Rule:** Give each central concept or tool a paragraph: a functional definition, then one sentence per component or per step from signal to result. Paired concepts get paragraphs of the same shape.  
**Preferred patterns:**
- `X quantifies a material's ability to do Y.`
- `For A, X is of the order of V, and thus A is usually considered B.`
- `In addition to A, B also contributes, especially in C.`
**Avoid:** Two components in one sentence; tutorial detail that the target journal's readers do not need.  
**Skill instruction:** When a concept paragraph is tangled, order it as definition, components one by one, and the fact that raises the paper's question.

## BKG-04: Review earlier work by what each model relates

**Derived from:** P05-C05, P05-S17, P05-S19

**Problem addressed:** Review sentences often name a study and praise it without saying what it found or relates.  
**Rule:** Describe a cited model or tool by its inputs, outputs, and the relation it gives. End the review paragraph on the recent work nearest the study.  
**Preferred patterns:**
- `The most widely used model is probably M (source), which relates X to Y through Z.`
- `In T, A can be calculated from B. Such simulations allow us to explore C.`
**Avoid:** `robust`, `powerful`, and `significant progress` without content.  
**Skill instruction:** Replace praise in review sentences with what the cited work relates or calculates.

## LNK-01: Begin with the known, end with the new, and reuse the new as the next subject

**Derived from:** P08-C01, P08-S06, P08-S08, P05-C07, P05-C01, P05-S41

**Problem addressed:** Sentences that are each correct can still read as a list because nothing ties one to the next.  
**Rule:** Put the new information at the end of a sentence. Open the next sentence with that information, usually as `This`, `These`, or `Such` plus a noun that names it.  
**Preferred patterns:**
- `... described by A, B, and C. These parameters are used to ...`
- `... will underestimate X. This underestimate has been reported in ...`
- `... include A, B, and C. Such tests provide ...`
**Avoid:** A bare `This` with no noun; a new synonym for a term the reader has just learned.  
**Skill instruction:** For each sentence, find the word that connects it to the previous one. If there is none, reorder the sentence or add a naming noun.

## LNK-02: Let each sentence answer the question the previous one raises

**Derived from:** P08-C04, P08-S14, P05-C07, P05-C04, P05-S25, P08-C03

**Problem addressed:** Paragraphs jump from background to aim and leave the reasoning to the reader.  
**Rule:** Order a paragraph so that each sentence answers the reader's next question: why is this needed, what goes wrong, how is it handled, has it been done, what is missing.  
**Preferred patterns:**
- `X is needed to obtain Y. However, X is limited by A. To reduce this problem, B has become common because C. This led us to consider D.`
- `In principle, ... Consider ... This means ... Mathematically, ...`
**Avoid:** Filling a missing step with a fact the author did not give.  
**Skill instruction:** Name the question each sentence answers. Where a question is skipped, ask the author for the missing step.

## LNK-03: Use the same order of moves for parallel items

**Derived from:** P08-C02, P05-C13, P08-S23, P05-C02, P05-C03, P05-S26

**Problem addressed:** Parallel methods, mechanisms, or cases are described in different orders, so the reader cannot compare them.  
**Rule:** Describe sibling items with the same sequence of moves and the same key terms. Vary only what really differs.  
**Preferred patterns:**
- `A measures P ... can be decomposed to obtain Q ... which is related to R. B measures S ... can be decomposed to obtain Q ...`
- `For A, X is B, and therefore Y equals C. For D, X is E, and therefore Y equals F.`
**Avoid:** Forcing unequal items into identical sentences; identical wording across more than three or four siblings.  
**Skill instruction:** Align the order of sibling descriptions before polishing their sentences.

## LNK-04: Start a section from the result of the previous one

**Derived from:** P08-C07, P05-C19, P05-C21, P05-C11

**Problem addressed:** Sections start cold, and the reader does not see why the method follows from the theory.  
**Rule:** Open a section or step with a short phrase that restates what the previous one established, then give the consequence. End a background subsection by saying what it means for the present method.  
**Preferred patterns:**
- `As discussed, X involves several assumptions. Since these are difficult to justify for M, ... To reduce this uncertainty, we suggest Z.`
- `After step N, B now has an apparent X.`
- `In this method, however, H is represented directly because I. Thus, no separate model of X is required.`
**Avoid:** `As discussed` when the earlier section did not establish the point. A `not required` statement that can be read as omission.  
**Skill instruction:** Add a bridge only from content the earlier section already contains.

## LNK-05: Mark the relation with a plain connector, and vary its position

**Derived from:** P05-S15, P08-C03, P05-C16, P08-C12, P05-C20

**Problem addressed:** Either no connectors, or the same one at the head of every sentence.  
**Rule:** Use ordinary connectors for the actual relation: `Thus`, `However`, `In addition`, `Similarly`, `Instead`, `That is`, `In that case`, `In practice`, `In particular`. Place `however` after the subject when several contrasts fall close together.  
**Preferred patterns:**
- `The effective X of M, however, depends on D.`
- `That is, C gains an extra B.`
- `In that case, X may not improve E.`
**Avoid:** `Moreover`, `Furthermore`, and `Notably` used as decoration; three sentence-initial `However` in one paragraph.  
**Skill instruction:** Check that each connector states a real relation. Delete it or change it if it does not.

## LNK-06: Use forward and backward pointers sparingly and exactly

**Derived from:** P05-S16, P05-S38, P08-S43, P05-C24, P05-C25

**Problem addressed:** Explanations are repeated in several places, or a claim is made long before its support.  
**Rule:** Point once to the section that explains a deferred topic. When two plots show equivalent quantities, discuss one and state that the discussion holds for the other.  
**Preferred patterns:**
- `..., both of which are reviewed in Section N.`
- `(discussed in Section N)`
- `Our discussion of X in Figure Na also holds for Y in Figure Nb.`
**Avoid:** The same parenthetical pointer three times in one paragraph; `will be discussed` without a section number.  
**Skill instruction:** Keep one pointer per deferred topic and verify the section or equation number.

## MAP-01: End the Introduction with objective, scope, and ordered steps

**Derived from:** P08-C05, P05-C08, P05-S22, P08-S17

**Problem addressed:** Aims are stated without scope, and the reader cannot predict the structure.  
**Rule:** State the objective as the answer to the need just given. Limit the scope in one sentence. List what the paper does with `first`, `then`, and `finally`, in the order of the headings. Add a problem-solution pair only for a method step that later gets its own section.  
**Preferred patterns:**
- `The objective of this study is to develop such an X for Y. For simplicity, in this study, we only consider A.`
- `In the following, we first review A. We then develop B. Finally, we demonstrate B by applying it to C.`
- `In B, one important aspect is D. We propose E to handle it.`
**Avoid:** A road map that differs from the headings; a road map in a short letter where space is limited.  
**Skill instruction:** Compare the road map with the headings and report any mismatch to the author.

## MAP-02: Tell the reader the job of a section in its first sentence

**Derived from:** P05-C17, P08-C06, P08-C12, P08-S35, P05-C22

**Problem addressed:** Sections begin with details, so the reader does not know what to look for.  
**Rule:** Begin a section or subsection with one sentence that says what it does. For a method section, follow with the design in miniature: what is included, the main simplification and its reason, and the order of operations.  
**Preferred patterns:**
- `In this section, we propose X for Y (Figure N). In particular, both A and B are considered.`
- `To reduce C, A is not modeled from first principles. Instead, ...`
- `In this subsection, we discuss the limitations of X.`
**Avoid:** Repeating the Introduction's road map word for word; a job sentence for every short subsection.  
**Skill instruction:** If a long section starts with detail, write a job sentence from the author's own headings and steps.

## CLO-01: Write Conclusions as a replay in the paper's own order

**Derived from:** P08-C14, P05-C28, P05-S45, P05-S46, P05-S47

**Problem addressed:** Conclusions either repeat the abstract or add claims the paper did not test.  
**Rule:** First retrace the method steps in order. Then give an overall verdict with a qualifier and the range tested. Then give each main finding and each mismatch with its likely cause, in the order of the Results.  
**Preferred patterns:**
- `In this study, we developed X for Y. ... By doing so, both A and B can be considered.`
- `A comparison of F and G shows that the spectra in general agree very well between H and I.`
- `At A, B contributes substantially to X. If overlooked, ...`
- `This may be due to M.`
**Avoid:** A general verdict without the exceptions that follow it; closing on `applicability and usefulness`.  
**Skill instruction:** Check each sentence of the Conclusions against the body. Flag any claim that has no source there.

## CLO-02: Build the abstract one stage per sentence

**Derived from:** P08-C15, P05-C29, P08-S01, P08-S02, P08-S03

**Problem addressed:** Abstracts pack several stages into long sentences.  
**Rule:** Give one short sentence to each stage: need, usual practice or requirement, difficulty, what the study does, how, test, main result, result under a harder condition, and a bounded closing. Draw the first sentences from the Introduction's topic sentences.  
**Preferred patterns:**
- `In these applications, X is usually done separately, which may be inadequate to Y.`
- `In this study, we propose X to estimate Y from A and B.`
- `Even when X is incomplete, Y can still capture Z, including A and B.`
**Avoid:** Stating validation twice; `powerful`, `valuable`, and `useful` as closing words.  
**Skill instruction:** Split overloaded abstract sentences by stage and keep every condition.

## DEF-04: Explain first, name second, and keep the name

**Derived from:** P08-S09, P05-S27, P05-S28, P08-S21, P05-C12

**Problem addressed:** A label appears before the reader knows what it refers to.  
**Rule:** Explain the process or method, then give its name in an appositive or a short naming sentence. Mark a paper-specific name with `in this study` or `in this paper`, and do not vary it afterward.  
**Preferred patterns:**
- `The increase, known as N, has been observed in A.`
- `For simplicity, in this study we use 'N' to refer to the method of doing B.`
- `..., forming F.`
**Avoid:** `termed as`; many local names; a new compound label that no source uses.  
**Skill instruction:** Where a term precedes its explanation, reverse the order if the paragraph allows it.

## DEF-05: State the ambiguity before the definition

**Derived from:** P05-C09, P05-S24, P05-C14, P05-C19, P08-S20

**Problem addressed:** Terminology paragraphs read as arbitrary rules.  
**Rule:** Say which competing usages or confusable quantities exist, then define with a purpose phrase. Close a definitions section by tying each term to its symbol and equation. Warn against the nearest confusable quantity by name.  
**Preferred patterns:**
- `Other terms such as C and D are also used in the literature. To avoid confusion, we define A through E.`
- `In this study, T1 refers to S1 in Equation i.`
- `Thus, Q' should not be confused with R, which exists even at S.`
- `In practice, models considering only A are usually termed N1. This is because D.`
**Avoid:** A terminology paragraph where the field has one settled usage.  
**Skill instruction:** Keep purpose phrases such as `To avoid confusion` and `To distinguish A from B`; they carry the reason for the definition.

## DEF-06: Introduce every equation by the operation that produces it

**Derived from:** P05-C10, P08-S18, P08-S19, P08-S43, P08-S22

**Problem addressed:** Equations appear without a statement of where they come from or when they hold.  
**Rule:** Lead into an equation with the operation (`Inserting`, `Combining`, `If we define`, `Assuming`). State the condition for dropping a term before dropping it. State the limit of an equation right after it. A simple case can introduce a mechanism before the general equation.  
**Preferred patterns:**
- `Inserting Equation i into Equation j yields ...`
- `Compared with A, B could dominate C, such that term D could be dropped.`
- `It should be noted that X could be important if Y. In that case, Equation N might be insufficient.`
- `Consider X filled with Y. After applying Z, ...`
**Avoid:** Editing the equation itself; removing `where` definitions.  
**Skill instruction:** Edit only the lead-in and follow-up sentences of an equation.

## GAP-05: Build the gap from an assumption and the condition under which it fails

**Derived from:** P08-C03, P08-S11, P08-S12, P08-S13, P08-S10

**Problem addressed:** Gaps stated as `X is limited` give the reader nothing to check.  
**Rule:** Say what practice assumes and what the assumption makes possible. Then give the materials or conditions in which it may fail, with sources. Close with the consequence for the quantity of interest.  
**Preferred patterns:**
- `In practice, some simplifications are usually made so that X can be inferred from Y.`
- `For instance, M assumes (1) that A and (2) that B. However, these assumptions may not hold for C (sources).`
- `These approximate relations may cause errors in the estimated X.`
**Avoid:** Stating the consequence without the failing condition.  
**Skill instruction:** Convert a vague limitation to assumption, failure condition, and consequence when the author's text or citations supply them. Otherwise mark `author-confirm`.

## GAP-06: Argue the gap as a causal chain that ends in a need

**Derived from:** P05-C07, P05-S20, P05-S21, P05-C06, P05-S18

**Problem addressed:** `It remains challenging` with no reason, followed by an aim.  
**Rule:** Give what the approach already does, what remains hard, the physical or practical reason with its scale, the consequence, and then the need. State an imbalance in the literature together with its reason.  
**Preferred patterns:**
- `Although X has been used to study A and B, applying it to C is still challenging. This is because C occurs at scale E.`
- `Considering that G is relatively large, the cost is very high. It is therefore desirable to develop methods that can include C in X.`
- `While the effect of A has been extensively studied, the influence of B is less explored because C is difficult.`
**Avoid:** A need sentence placed before its reason; `extremely` without numbers.  
**Skill instruction:** Ask the author for the reason and the consequence behind any bare `challenging`, and write them as separate short sentences.

## GAP-07: Place the closest earlier study next to the aim and name the one missing step

**Derived from:** P08-C04, P08-S15, P08-S16, P05-C15, P05-S29

**Problem addressed:** Novelty is claimed against the whole literature, which no author can defend.  
**Rule:** Credit the nearest study in one sentence and state the single step it did not take in the next. For a workaround in common use, say what it lacks. If the study then uses the same workaround, say so openly.  
**Preferred patterns:**
- `One similar attempt is the work of A, in which B and C were used to estimate D. However, in that study, B and C were processed separately.`
- `Equations developed for Y have been used for X by replacing E with F, but no physical justification is provided.`
- `Note that Equations i and j are modified from Author (year) by replacing A with B.`
**Avoid:** `still not ... yet`; `no study has`; `Few works have been done`.  
**Skill instruction:** Keep credit and limitation in separate sentences, and never strengthen `few` to `no`.

## MET-05: Explain how a parameter is obtained in four parts

**Derived from:** P05-C18, P05-C22, P08-S39, P08-S40

**Problem addressed:** Parameter paragraphs describe an algorithm in detail and never say why the parameter is needed.  
**Rule:** Give, in this order: what must be determined and from what; why it is needed (to validate an earlier stage, or as input to a later one); which part is hard and which established method is used, with citations; the alternative and its drawback. Attach to each reported value the way it was determined.  
**Preferred patterns:**
- `The first step is to determine X by analyzing Y. One purpose of this step is to validate D. In addition, A is needed in E.`
- `While F is relatively easy to calculate, the determination of A is not straightforward. In this study, we use G (sources).`
- `H can also be used, but additional assumptions are involved.`
- `The surface area is B as determined by C.`
**Avoid:** Describing the internals of a published algorithm; a value with no method attached.  
**Skill instruction:** Check a parameter paragraph for what, why, how, and why not the alternative. Ask the author for any missing part.

## MET-06: Give each chosen value a support clause

**Derived from:** P05-C23, P05-S30, P05-S33, P05-S32, P08-S41

**Problem addressed:** Simulation settings are listed as bare numbers.  
**Rule:** Support each chosen value in one of three ways: it corresponds to a typical physical quantity, it is close to a published value, or it is consistent with another parameter under a named relation. State what software was used and how it was changed. Say which parts of a demonstration are replaceable, and where settings differ between the cases being compared.  
**Preferred patterns:**
- `X is V1, which corresponds to a typical A of B.`
- `X is V2, which is close to the value reported in C.`
- `X is V3, which is consistent with D according to the E equation.`
- `We emphasize that the models used here are for demonstration only. Other models may also be used.`
**Avoid:** `if consider`; a wrong equation cross-reference; values with no support.  
**Skill instruction:** Mark unsupported parameter values `author-confirm` and verify every equation number cited.

## MET-07: Describe dependent steps by input and output

**Derived from:** P08-C09, P08-S30, P05-C19, P05-C20, P05-C21, P05-S31, P05-S34

**Problem addressed:** Multi-step procedures are written as one block, so the reader cannot see what feeds what.  
**Rule:** Mark the start of each step. Say what is held fixed, what is varied, and what the step yields. Use `Similarly` when a later step repeats the logic of an earlier one. Before a correction, say what the raw output contains and why that part is removed. For the central step, add a plain restatement with `That is`.  
**Preferred patterns:**
- `First, A is fixed. Then, X is carried out with B varying over C. The second step is to determine A. Similarly, ...`
- `Note that Q also contains A, which is not influenced by B. To determine C, A needs to be subtracted.`
- `That is, C gains an extra B in addition to its own value.`
**Avoid:** Step markers on single simple actions.  
**Skill instruction:** Number steps only when a later step uses an earlier result.

## MET-08: Justify a choice by naming the alternatives

**Derived from:** P08-C08, P08-S28, P08-S34, P05-C20, P08-S32, P08-S31, P08-S33

**Problem addressed:** A method is named without a reason, or praised without comparison.  
**Rule:** Say how many options exist, describe each by what it assumes, choose one, and give the reason: fit to the physical situation, or the cost of the ideal option. Give the purpose of each transformation or implementation detail that affects the result.  
**Preferred patterns:**
- `In practice, there are two types of approach to X: A and B. A assumes C. Alternatively, B assumes E. In this study, we apply A.`
- `It would be better to do X using Y. However, Y is computationally costly.`
- `W1 has long been used for M1 because D. However, for M2, E, and hence W2 is the logical choice.`
- `The use of X is to ensure Y.`
**Avoid:** `always better`; describing unused options at length.  
**Skill instruction:** When a choice has no stated reason, ask for the alternative and the reason. Do not supply them.

## ASS-04: Give each assumption a unit: statement, valid case, failing case

**Derived from:** P08-C06, P08-S26, P08-S27, P05-S23, P08-S19

**Problem addressed:** Assumptions are listed without saying when they hold.  
**Rule:** For each assumption, state it, give its origin if needed, say when it is valid, and say when it may fail. Order assumptions by importance. Make implicit assumptions explicit and restate them in physical terms.  
**Preferred patterns:**
- `In X, it is assumed that A. This assumption is usually valid if B.`
- `For D, this assumption is approximately valid. However, for E, it might break down.`
- `Lastly, although not stated explicitly, X uses Y, which assumes Z. That is, W does not occur during V.`
- `Note that this type of model is only valid for C.`
**Avoid:** Supplying a validity condition the author did not state; `clearly valid` outside an exact case.  
**Skill instruction:** Group scattered assumptions by method and keep the three grades: valid, approximately valid, and unresolved.

## ASS-05: Say plainly what the study leaves out and what it does in its place

**Derived from:** P08-S24, P08-S25, P05-S22, P05-C08, P05-C11

**Problem addressed:** Scope limits are hidden or softened.  
**Rule:** State the scope with `only`. State what is not addressed and what is done in its place. When a lumped parameter absorbs an effect, say it is considered `to a certain extent`.  
**Preferred patterns:**
- `For simplicity, in this study, we only consider A.`
- `In this study, we will not address X; instead, we simplify Y by using Z.`
- `Since X and Y are both optimized, to a certain extent, the effects of Z are also considered.`
**Avoid:** Removing `only`; using a scope statement to avoid a question the conclusion depends on.  
**Skill instruction:** Preserve scope statements and partial-treatment hedges exactly.

## ASS-06: Give each limitation its cause, the cases affected, and its consequence

**Derived from:** P08-C12, P08-C13, P05-S43

**Problem addressed:** Limitation paragraphs are apologetic or vague.  
**Rule:** Announce the limitations subsection. For each limit, give the assumption behind it, the materials or conditions affected, and what it means for the method's result. State the size of whatever limits the model.  
**Preferred patterns:**
- `First, Y may only be valid for A because it assumes B. Therefore, for C, Y may not describe D. In that case, X may not improve E.`
- `This could be because D only covers a small fraction of E (about V).`
**Avoid:** Limits without conditions; reassurance that the conclusions are unaffected.  
**Skill instruction:** Pair every limitation with a condition and a consequence, and keep the author's modal verbs.

## RES-06: Report in the order result, deviation, comparison, cause

**Derived from:** P08-C10, P08-C11, P05-C24, P05-S35, P08-S36

**Problem addressed:** Results paragraphs mix description and explanation, or report only agreement.  
**Rule:** State the main result. Report its deviation even when small. Compare with the reference cases. Give the cause last. When magnitudes are compared, give both numbers. Introduce a side test by the question it asks.  
**Preferred patterns:**
- `As shown in Figure N, A recovers X. The positions of Y are close to the true values, although Z is slightly smaller. In contrast, B gives W.`
- `However, the increase in A is only about V1, much smaller than that in B (about V2).`
- `We also tested whether X can estimate Y by allowing Y to change during Z.`
**Avoid:** `Clearly`, `successfully`, and `perfectly` without exact support.  
**Skill instruction:** Keep the order, and add the two values to any `much larger` or `much smaller` if the author can supply them.

## RES-07: Walk along the axis in one direction

**Derived from:** P05-C25, P05-S37, P05-C28, P05-C26

**Problem addressed:** Descriptions of a curve jump between ranges.  
**Rule:** Describe a spectrum or curve from one end to the other. Open each sentence with the range it covers. Report agreement and disagreement range by range. Interpret a value by comparing it with a known reference.  
**Preferred patterns:**
- `At A, X is nearly constant, about V1 for the experiment and V2 for the simulation.`
- `When the frequency is decreased to B, ... As the frequency is further decreased, ... When the frequency is lower than D, ...`
- `These values are close to R, implying that S in this range.`
**Avoid:** `sharply` unless the plot shows it; `orders` for `orders of magnitude`.  
**Skill instruction:** Reorder a scattered curve description along its axis and keep every range and number.

## RES-08: State overall agreement with a qualifier, then where it ends

**Derived from:** P05-S46, P08-C11, P05-C24, P05-C28

**Problem addressed:** `Good agreement` hides ranges where the model fails.  
**Rule:** Give the overall verdict with a qualifier such as `in general` and the range compared. Follow it at once with the ranges where agreement holds and where it does not.  
**Preferred patterns:**
- `A comparison of A and B shows that X in general agrees very well between V1 and V2.`
- `Z agrees with the measurements only at A and B. At C, Z is much smaller than measured.`
- `... shows that A follows the general trend of X, especially for C.`
**Avoid:** A qualifier with no exceptions stated nearby.  
**Skill instruction:** If a text claims general agreement, check that the mismatches reported elsewhere are still present.

## RES-09: Isolate contributions one at a time, one paragraph each

**Derived from:** P05-C26, P05-S39, P08-S35, P08-S37

**Problem addressed:** The role of each component in a combined result is asserted without being shown.  
**Rule:** Introduce the additional analysis by its purpose and its single change. Give each component a paragraph with result, mismatch, and tentative cause. Define test cases by the one condition that differs.  
**Preferred patterns:**
- `To identify the relative contribution of each X, we also conducted simulations that consider only one X at a time.`
- `Two cases were tested. In Case 1, A. In Case 2, B.`
- `For comparison, X is also shown.`
**Avoid:** `the former` and `the latter` when the reader has to search for the antecedent.  
**Skill instruction:** State the purpose of an added analysis at the start of its first sentence.

## CON-04: Grade suitability case by case

**Derived from:** P05-C16, P05-C15, P08-S42

**Problem addressed:** Model comparisons reduce to right and wrong.  
**Rule:** When choosing among models, say for each class of case how well each model fits, in graded words, with the reason in the same sentence. Present an alternative by the one relation in which it differs.  
**Preferred patterns:**
- `For A, it is intuitive to apply X because B. For C, it still seems reasonable, although D. For E, however, it is questionable. Instead, Y seems more appealing because G.`
- `Different from A, which relates B to C, D suggests that B may also be controlled by E.`
**Avoid:** Flattening the grades to `suitable` and `unsuitable`; a graded word with no reason.  
**Skill instruction:** Keep graded suitability wording and its reasons.

## CON-05: Compare with earlier work through the element it lacked

**Derived from:** P05-S41, P05-C26, P05-S42

**Problem addressed:** Literature comparisons say only that results are `consistent with previous studies`.  
**Rule:** State what happens when a component is omitted, connect that to earlier studies that omitted it, show the result with the component included, and state the implication with a modal.  
**Preferred patterns:**
- `If A is not accounted for, the combination of B and C will underestimate X at D. This underestimate has been reported in earlier studies that did not consider A (source).`
- `This implies that A could be a significant contributor to X.`
**Avoid:** Changing `could be` to `is` on the basis of one sample.  
**Skill instruction:** Keep the counterfactual sentence and the link to earlier studies; they are the evidence for the claim.

## IMP-05: After a tentative cause, show that it predicts the direction of the mismatch

**Derived from:** P05-S36, P05-S40, P05-C24, P08-S38, P08-S29

**Problem addressed:** Discrepancies are explained by causes that would not produce the observed error.  
**Rule:** Name the discrepancy, offer the cause with `might be due to` or `One possible explanation`, then add one sentence that shows why this cause gives an error in the observed direction. Use direct attribution only when the study design isolates the cause. Use `support` language for agreement with a single dataset.  
**Preferred patterns:**
- `This discrepancy might be due to F. Since E is associated with G, ignoring G underestimates H.`
- `One possible explanation for this difference is that C, and thus D could be overlooked.`
- `This is attributed to the use of Y.` (only when Y is the one variable changed)
- `The data lend additional support to the relation between X and Y.`
**Avoid:** Shortening `One possible explanation is` to `This is because`.  
**Skill instruction:** Check that each proposed cause is consistent with the sign of the discrepancy. If the author gave no mechanism, do not add one.

## IMP-06: State applications and outlook as bounded next steps

**Derived from:** P08-S04, P08-C13, P05-C27, P05-S44

**Problem addressed:** Closing paragraphs promise more than the study delivered.  
**Rule:** Derive each application from a property of the method and give one example. Tie the first application back to the need stated in the Introduction. Present a larger goal as a possible first step.  
**Preferred patterns:**
- `Because A can be easily included in X, it can be used to evaluate B. One example is to compare C and D.`
- `Thus, it is necessary to assess X for a given Z, and this approach is suited to that purpose.`
- `This work might be a first step towards X.`
**Avoid:** `attractive`, `useful tool`, and `comprehensive` as self-description.  
**Skill instruction:** Replace self-praise with the specific use and its example.

## STY-01: Learn the exemplar's organization, not its slips

**Derived from:** P08-S44, P05-S48

**Problem addressed:** Imitating a model paper can copy its non-native forms and occasional inflated words.  
**Rule:** Keep the function of the sentence and correct the form.  
**Preferred patterns:**
- `Compared with` (not `Comparing to`, `Comparing with`, or `if compared to`)
- `used` (not `utilized`); `resulting from` (not `resulted from`)
- `we suggest upscaling` (not `we suggest to upscale`)
- `orders of magnitude`; `of the order of`; `systematically low`; `considerably lower`
- `One notable feature` or `The main feature` (not `profound feature`)
- `although` or `even though` (not `despite that`)
**Avoid:** `powerful tool`, `valuable`, `perfectly`, `clearly`, and `extremely` without support.  
**Skill instruction:** Apply these corrections whenever a draft imitates the exemplar's wording.
