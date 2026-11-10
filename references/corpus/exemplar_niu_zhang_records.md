# Exemplar Records: Niu and Zhang

Record-level corpus for the two exemplar papers described in `exemplar_niu_zhang.md`. That file gives the overall model of organization; this file gives the individual records behind it. The rules distilled from these records are in `corpus_rule_cards.md`.

Load this file when you need a worked model for a specific move: an opening paragraph, a gap paragraph, a road map, a parameter paragraph, a model-data comparison, a limitation, or a Conclusions paragraph. For routine editing, the rule cards are enough.

## How to read the records

This repository is public, so no record contains a source sentence. Each record gives a **source pointer** (page, section, paragraph, sentence) so the wording can be checked in the paper, and a **reusable pattern** with placeholders. Words in backticks inside the moves are short connectors or frames taken from the paper to show how the sentence starts.

There are two kinds of record:

- **Chain records (`Pxx-Cnn`)** cover a paragraph or a run of sentences. `Sentence-by-sentence moves` lists what each sentence does, and `Sentence link` explains how each sentence is tied to the one before it.
- **Sentence records (`Pxx-Snn`)** cover one sentence or an adjacent pair, in the same format as `source_sentence_corpus.md`, with `Source pointer` and, where useful, `Sentence link` added.

`Reader mark` reports that the skill author underlined or annotated the passage in their own copy. Treat marked records as the first choice when several records fit.

Function tags follow `extraction_protocol.md`. Besides the eight original tags, these records use `BKG` (background or opening statement), `LNK` (link between sentences, paragraphs, or sections), `MAP` (road map or statement of a section's job), `CLO` (closing summary), and `STY` (surface forms to correct).

Records marked `caution` have a useful function but contain wording that should be corrected or toned down; the `Risk when misused` field says what to change.

## Index

| Need | Records |
|---|---|
| Opening paragraph of an Introduction | P08-C01, P05-C01, P08-S05, P05-S11, P05-S12 |
| Explaining the concepts or tools the reader needs | P08-C02, P05-C02, P05-C03, P05-C04, P05-S13 |
| Reviewing earlier work | P05-C05, P05-C06, P05-S17, P05-S18 |
| Gap paragraph | P08-C03, P08-C04, P05-C07, P05-C15, P08-S12, P08-S16, P05-S20, P05-S21 |
| Objective, scope, and road map | P08-C05, P05-C08, P08-S17, P05-S22 |
| Terms, definitions, and names | P05-C09, P05-C12, P05-C14, P08-S09, P08-S20, P05-S24, P05-S27, P05-S28 |
| Introducing equations and derivations | P05-C10, P08-S18, P08-S19, P08-S43 |
| Assumptions and their validity | P08-C06, P08-S24 to P08-S27, P05-S23, P05-S29 |
| From theory to method; opening a method section | P08-C07, P05-C11, P05-C16, P05-C17 |
| Justifying a choice of method or model | P08-C08, P05-C16, P05-C20, P08-S34 |
| Obtaining a parameter; giving parameter values | P05-C18, P05-C23, P05-S30, P05-S31, P08-S40 |
| Method steps in order | P08-C09, P05-C19, P05-C20, P05-C21, P05-C22 |
| Describing parallel cases, mechanisms, or models | P08-C02, P05-C13, P08-S23 |
| Setting up test cases and extra analyses | P08-S35, P08-S36, P05-S39 |
| Reporting and comparing results | P08-C10, P08-C11, P05-C24, P05-C25, P05-S35, P05-S37, P05-S46 |
| Explaining a discrepancy | P05-C24, P05-C26, P08-S38, P05-S36, P05-S40, P05-S43 |
| Comparing with the literature | P05-C26, P05-S41, P08-S16 |
| Limitations | P08-C12, P08-S41, P05-S32 |
| Applications and outlook | P08-C13, P05-C27, P08-S04, P05-S44 |
| Conclusions | P08-C14, P05-C28, P05-S45, P05-S47 |
| Abstract | P08-C15, P05-C29, P08-S01 to P08-S03 |
| Wording not to copy | P08-S44, P05-S48 |

---

# P08: Joint Inversion of NMR and SIP Data (E1)

## Paper-Level Notes

**Source:** Niu and Zhang (2018), *Geophys. J. Int.* 212, 1791-1805, doi:10.1093/gji/ggx501.  
**Strength of writing:** Familiar words, short causal steps, assumptions stated with the conditions under which they fail, and a road map that the headings follow.  
**Useful for this skill because:** It shows how a method paper can move from a broad need to a specific gap without one long or decorative sentence.

## Paragraph chains

## P08-C01

**Source pointer:** p. 1791-1792, §1 ¶1, sentences 1-7  
**Section:** Introduction  
**Function tag:** LNK + BKG  
**Score:** 10/10  
**Use status:** positive  
**Reader mark:** note: this paragraph gives the importance of pore size and its uses

**Local context:** Opening paragraph. It goes from why pore space matters to how pore geometry is measured, and stops where geophysical methods can enter.  
**Sentence-by-sentence moves:**
1. General claim: one object controls one process, with a textbook citation.
2. Narrow to a class of materials and list the quantities that describe the object.
3. `These parameters` picks up the list and says what they are used for.
4. `For instance` gives two uses in parallel clauses joined by a semicolon.
5. The object returns as subject and the topic turns to measurement: direct methods with examples.
6. `In addition` adds the second class of measurement, indirect methods.
7. `One example ...; another example ...` names two members of that class.

**Why it works:** Every sentence begins with something the reader has already met, and only one new idea arrives at a time.  
**Sentence link:** The list at the end of sentence 2 becomes the subject of sentence 3 through a summary noun. The word `methods` at the end of the paragraph prepares the next paragraph, which opens on a further family of methods.  
**Transferable rule:** Open with the object of the study, describe it, say why the description is useful, then say how it is obtained.  
**Reusable pattern:** `X controls Y (general source). For M, X is usually described by A, B, and C. These parameters are used to estimate Z. For instance, ...; ... X can be measured directly by D. In addition, indirect methods can be used. One example is E; another example is F.`  
**Risk when misused:** The opening becomes generic if X is broader than the object the paper studies.  
**Skill-ready instruction:** When an Introduction opens abruptly, rebuild its first paragraph in this order: object, description, use, measurement. Add no facts the author did not supply.

## P08-C02

**Source pointer:** p. 1791-1792, §1 ¶2, sentences 1-11  
**Section:** Introduction  
**Function tag:** LNK + BKG  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** note: geophysical methods for pore size and the principles of the two tools are introduced here

**Local context:** Narrows from geophysical methods in general to two tools, then explains each tool from signal to pore size.  
**Sentence-by-sentence moves:**
1. The family of methods is attractive, and the reasons follow in a `mainly due to` phrase.
2. `Another advantage` adds one more reason in its own short sentence.
3. The two most useful tools are named.
4. Tool 1: what it measures. 5. What the signal is proportional to. 6. How the curve is decomposed and how the result relates to pore size.
7. Tool 2: what it measures. 8. What controls the response at the frequencies of interest. 9. How the spectrum is decomposed. 10. How the result relates to pore size.
11. `For simplicity` introduces one short local name for each use of the tools.

**Why it works:** Both tools are explained in the same order, so the second explanation is easy once the first is understood.  
**Sentence link:** The named tools at the end of sentence 3 become the topics of the two later blocks. Inside each block, the output of one sentence (a curve, a spectrum, a distribution) is the subject of the next. Sentence 11 names what the two blocks have just described.  
**Transferable rule:** Explain parallel methods with the same sequence of moves, and name them only after the reader knows what they do.  
**Reusable pattern:** `The most useful tools for X include A and B. A measures P ... The measured curve can be decomposed to obtain Q, which is related to R, and thus S can be estimated. B measures T ... For simplicity, in this study we use 'C' and 'D' to refer to these uses.`  
**Risk when misused:** Forcing two unequal methods into identical sentences can hide a real difference between them.  
**Skill-ready instruction:** When two methods are described in sequence, align the order of their descriptions before polishing the individual sentences.

## P08-C03

**Source pointer:** p. 1792, §1 ¶3, sentences 1-7  
**Section:** Introduction  
**Function tag:** LNK + GAP  
**Score:** 10/10  
**Use status:** positive  
**Reader mark:** note: `gap`, research significance; sentences 3-6 underlined for reuse

**Local context:** Turns the promise of the two tools into a problem: the inferred pore size rests on simplifications that may fail.  
**Sentence-by-sentence moves:**
1. Concession: the relation is complicated and work on it continues.
2. `In practice` introduces simplifications and what they make possible.
3. `For instance`: what tool 1 assumes, as a numbered list.
4. `However`: when those assumptions may be violated, with sources.
5. The same pattern for tool 2.
6. `However`: other processes that may also contribute.
7. Summary subject and consequence: these approximate relations may cause errors in the estimate.

**Why it works:** The gap is built from named assumptions and named failure conditions, so it reads as a technical need and does not criticize earlier authors.  
**Sentence link:** `some simplifications` in sentence 2 is unpacked by `For instance`. `these assumptions` in sentence 4 refers to the list just above it. The closing summary noun gathers both tools into one consequence.  
**Transferable rule:** Build a gap from what practice assumes, where the assumption fails, and what the failure does to the quantity of interest.  
**Reusable pattern:** `In practice, some simplifications are made so that X can be inferred from Y. For instance, M assumes (1) that A and (2) that B. However, these assumptions may not hold for C (sources). ... These approximate relations may cause errors in X.`  
**Risk when misused:** The final consequence needs support, because `may cause errors` is a claim about accuracy.  
**Skill-ready instruction:** Replace a vague limitation with the assumption, its failure condition, and its consequence when the author's text or citations provide them. Otherwise mark `author-confirm`.

## P08-C04

**Source pointer:** p. 1792, §1 ¶4, sentences 1-6  
**Section:** Introduction  
**Function tag:** LNK + GAP  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** note: introduces inversion, then stresses joint inversion as the new element; compares with earlier work

**Local context:** Introduces the second obstacle, inversion, and arrives at the study's idea and the closest earlier attempt.  
**Sentence-by-sentence moves:**
1. Why the operation is needed.
2. Two known problems with it, given as causes.
3. `To mitigate these problems`, the common remedy and why it helps.
4. `This has inspired us` moves from the general remedy to the present idea.
5. `One similar attempt` names the closest study and what it did.
6. `However`: the precise step that study did not take.

**Why it works:** Each sentence answers the question left by the previous one: why needed, what goes wrong, how it is handled, why here, has it been done, what is missing.  
**Sentence link:** `these problems` restates sentence 2 as the starting point of sentence 3. `This` in sentence 4 refers to the remedy. Sentence 6 reuses the method named in sentence 5, so the contrast is exact.  
**Transferable rule:** Place the closest earlier study immediately before the study's own aim, and name the single step it did not take.  
**Reusable pattern:** `X is needed to obtain Y. However, X is often limited by A and B. To reduce these problems, C has become common because D. This led us to consider E. One similar attempt is F, in which G. However, in that study H, and I has not been done.`  
**Risk when misused:** `has not been done` needs a literature basis that the author can defend.  
**Skill-ready instruction:** When a gap paragraph jumps to the aim, insert the missing logical step only if the author has given it, and keep the comparison to the closest study specific.

## P08-C05

**Source pointer:** p. 1792, §1 ¶5, sentences 1-7  
**Section:** Introduction  
**Function tag:** MAP + AIM  
**Score:** 10/10  
**Use status:** positive  
**Reader mark:** note: introduces the order in which the paper is written

**Local context:** Final Introduction paragraph. It states the idea of the study and promises the order of the sections.  
**Sentence-by-sentence moves:**
1. `In this study`: the idea and target quantity.
2. `We first`: background, with what it emphasizes.
3. `We then`: the method.
4. One sub-problem inside the method is named.
5. The answer to that sub-problem is proposed.
6. How applicability is tested on synthetic data.
7. `In the last part`: the real-sample application, results, and limitations.

**Why it works:** A reader can predict each main section, and the sub-problem in sentences 4-5 explains why a separate method step appears later.  
**Sentence link:** Sentence 5 answers sentence 4 directly. The order `first`, `then`, `last` matches the section numbers.  
**Transferable rule:** End the Introduction with the aim and an ordered list of what the paper does, and include any method problem that later needs its own section.  
**Reusable pattern:** `In this study, we explore X for Y. We first review A. We then introduce B. In B, one important aspect is C. We propose D to handle it. A test with E is designed to show F. Finally, we apply B to G and discuss the results and limitations.`  
**Risk when misused:** A road map that no longer matches the headings misleads the reader. For short letters it may take too much space.  
**Skill-ready instruction:** Check every step of a road map against the headings and repair the mismatch by asking the author which order is intended.

## P08-C06

**Source pointer:** p. 1793-1794, §2.3 ¶1-2  
**Section:** Theory  
**Function tag:** ASS + LNK  
**Score:** 10/10  
**Use status:** positive  
**Reader mark:** several assumption and validity sentences underlined for reuse

**Local context:** Closes the theory by listing every assumption behind each measurement, and prepares the reason for the method section.  
**Sentence-by-sentence moves:**
1. The subsection states its job.
2. Assumption 1 for tool 1. 3. Where the effect comes from. 4. When the assumption is usually valid.
5. `Another assumption` for tool 1. 6. Materials for which it is approximately valid. 7. `However`: materials for which it might break down.
8. `In addition`: assumption 3. 9. When it may not be appropriate.
10. Tool 2 follows in the same pattern, with `The most important assumption`, `Second`, and `Lastly` as the order markers.

**Why it works:** The same four questions recur: what is assumed, why, when it is valid, and when it fails. The reader always knows the state of each assumption.  
**Sentence link:** `This assumption` opens the validity sentence, which keeps the topic fixed. `However` then moves from the valid case to the invalid case with the same subject.  
**Transferable rule:** Give each assumption its own short unit: statement, origin if needed, valid case, failing case.  
**Reusable pattern:** `In this subsection, we summarize the assumptions of X. In X, it is assumed that A. This assumption is usually valid if B. Another assumption is C. For D, this is approximately valid. However, for E, it might break down.`  
**Risk when misused:** A catalogue of limits is wasted if the next section does not use it.  
**Skill-ready instruction:** When assumptions are scattered, group them by method and give each a validity condition. Do not supply a validity condition the author did not state.

## P08-C07

**Source pointer:** p. 1794, §3 opening paragraph, sentences 1-4  
**Section:** Methods  
**Function tag:** LNK + MET  
**Score:** 10/10  
**Use status:** positive

**Local context:** Very short bridge from the listed assumptions to the proposed method.  
**Sentence-by-sentence moves:**
1. `As discussed` restates the previous section in one clause.
2. `Since` gives the difficulty and its result for separate use.
3. `To reduce` gives the purpose, then the proposal.
4. Points to the figure and promises step-by-step detail.

**Why it works:** Four sentences carry the argument from problem to method with no new background.  
**Sentence link:** The result in sentence 2 (the separate estimate may be inaccurate) is the problem removed by the purpose phrase in sentence 3.  
**Transferable rule:** Open a method section by taking the previous section's result as the reason for the method.  
**Reusable pattern:** `As discussed, X involves several assumptions. Since these are difficult to justify for M, Y obtained separately may not be accurate. To reduce this uncertainty, we suggest doing Z. The scheme is shown in Figure N, and each step is described below.`  
**Risk when misused:** The opening fails if the earlier section did not establish the difficulty.  
**Skill-ready instruction:** Add a one-sentence bridge at the start of Methods only when the preceding text already supports it.

## P08-C08

**Source pointer:** p. 1794-1795, §3.1 ¶1-2  
**Section:** Methods  
**Function tag:** MET + LNK  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** definition and choice sentences underlined for reuse

**Local context:** Explains the two available approaches, chooses one, and checks its central relation against published data.  
**Sentence-by-sentence moves:**
1. `In practice, there are two types`, naming both.
2. Approach A: what it assumes. 3. `Thus`: what this allows. 4. `For instance`: one example.
5. `Alternatively`, approach B: what it assumes. 6. `That is`: plain restatement. 7. `Mathematically`: how it is applied.
8. New paragraph: `In this study, we apply` approach A.
9. The assumption of this choice. 10. `This implies` a testable relation.
11. `We verify` the relation with published data. 12-13. What the data show, with one outlier acknowledged.

**Why it works:** The choice is prepared before it is made, and the implied relation is tested before the method depends on it.  
**Sentence link:** `This implies` makes the assumption's consequence the subject of the next step, and `We verify` picks up that same relation.  
**Transferable rule:** To justify a method choice, list the options, describe each by its assumption, choose one, state what it implies, and test that implication.  
**Reusable pattern:** `There are two types of approach to X: A and B. A assumes C. Thus, D. Alternatively, B assumes E. That is, F. In this study, we apply A. We assume G. This implies that H. We verify this relation using I.`  
**Risk when misused:** Describing many options at equal length can distract from the one used.  
**Skill-ready instruction:** When a method is named without a reason, ask for the alternative and the reason. Do not invent either one.

## P08-C09

**Source pointer:** p. 1796, §3.5 ¶2, sentences 1-11  
**Section:** Methods  
**Function tag:** MET + LNK  
**Score:** 9/10  
**Use status:** positive

**Local context:** Describes a two-step procedure for choosing two control parameters.  
**Sentence-by-sentence moves:**
1. The proposal, in one sentence. 2. Where it is illustrated.
3. Step 1 starts: one parameter is held fixed, with `first`. 4. `Then`: the other is varied over a stated range. 5. How a value is read from the plot. 6. `For instance`: the criterion in the figure.
7. `The second step` names the remaining task. 8. `Similarly`: same procedure with the optimum from step 1. 9-10. How the value is chosen.
11. Other methods can also be used.

**Why it works:** Each step gives its input and its output, and the output of step 1 is the input of step 2.  
**Sentence link:** `Similarly` tells the reader that the logic is unchanged, so only the changed variable needs attention.  
**Transferable rule:** Describe dependent method steps with their inputs and outputs, and mark the point at which the next step begins.  
**Reusable pattern:** `We suggest a two-step method for determining A and B. First, A is fixed. Then, X is carried out with B varying over C. By plotting D against B, a suitable value can be chosen. The second step is to determine A. Similarly, X is conducted with the chosen B and a varying A.`  
**Risk when misused:** Step markers on simple actions make prose feel mechanical.  
**Skill-ready instruction:** Number steps only when a later step depends on an earlier result.

## P08-C10

**Source pointer:** p. 1798, §4.1 ¶3, sentences 1-6  
**Section:** Results  
**Function tag:** RES + LNK  
**Score:** 9/10  
**Use status:** caution

**Local context:** Reports the joint result, gives its small deviation, compares with separate cases, and states the cause.  
**Sentence-by-sentence moves:**
1. `As shown in Fig`: the main case recovers the key feature.
2. Precise feature with a concession about the small difference.
3. `In contrast`: the reference cases as a group.
4. Each reference case separately, with what it does and does not recover.
5. Overall comparison.
6. Cause of the difference.

**Why it works:** The result comes before the comparison, and the comparison comes before the cause. Even the best case has its small deviation reported.  
**Sentence link:** `In contrast` shifts the subject from the main case to the reference cases. `this improvement` in the last sentence gathers the preceding comparison into one noun.  
**Transferable rule:** Report the main case and its deviation, then the reference cases, then the overall comparison, and only then the cause.  
**Reusable pattern:** `As shown in Figure N, A recovers X. The positions of Y are close to the true values, although Z is slightly smaller. In contrast, B gives W. Compared with B, A improves X. This improvement is due to V.`  
**Risk when misused:** The source uses `Comparing with`, `successfully`, and `Clearly`. Use `Compared with`, and keep evaluative adverbs only when the data clearly support them.  
**Skill-ready instruction:** Keep the order result, deviation, comparison, cause. Remove `clearly` and `successfully` unless the evidence is exact.

## P08-C11

**Source pointer:** p. 1800, §5.2 ¶3, sentences 1-7  
**Section:** Results  
**Function tag:** RES + IMP  
**Score:** 9/10  
**Use status:** caution

**Local context:** Evaluates a real-sample result against independent data and the fitted curves.  
**Sentence-by-sentence moves:**
1. Main agreement, with what agrees. 2. Fit to dataset 1.
3. Fit to dataset 2 is limited to two stated ranges. 4. At the middle range the simulated value is much smaller.
5. `The discrepancy may be explained by` a named process.
6. A second comparison, with `indicating` for what it shows. 7. `That implies`, limited by `for this sample`.

**Why it works:** Agreement and disagreement sit in the same paragraph, and the inference is explicitly restricted to one sample.  
**Sentence link:** Sentence 4 states the mismatch, and sentence 5 begins with a noun that names it. `That implies` carries the observation in sentence 6 to its meaning.  
**Transferable rule:** After agreement, name where agreement ends, then offer the cause cautiously and keep the inference within the sample tested.  
**Reusable pattern:** `As shown in Figure N, X is consistent with Y. Z agrees with the measurements only at A and B. At C, Z is much smaller than measured. This difference may be explained by D. This implies that, for this sample, E.`  
**Risk when misused:** The source's `perfectly` should not be copied unless the fit is exact.  
**Skill-ready instruction:** Do not let a statement of general agreement hide a range where agreement fails.

## P08-C12

**Source pointer:** p. 1800, §5.3 ¶1, sentences 1-5  
**Section:** Discussion  
**Function tag:** ASS + LNK  
**Score:** 10/10  
**Use status:** positive

**Local context:** Announces the job of the subsection, then gives limits together with the materials they affect.  
**Sentence-by-sentence moves:**
1. The subsection states its job.
2. `First`: the model may only be valid for a stated size range, and the assumption is the reason.
3. `Therefore`: the materials for which it may fail.
4. `In that case`: what this means for the proposed method.
5. `In addition`: a second limit, with its reason and affected materials.

**Why it works:** Each limit answers why, where, and so what. The limits stay concrete without weakening the rest of the paper.  
**Sentence link:** `In that case` refers to the conditional situation described just before and moves it to the method's usefulness.  
**Transferable rule:** Give each limitation its cause, the materials or conditions affected, and its consequence for the method.  
**Reusable pattern:** `In this subsection, we discuss the limitations of X. First, Y may only be valid for A because it assumes B. Therefore, for C, Y may not describe D. In that case, X may not improve E. In addition, since F, X may not work for G.`  
**Risk when misused:** Listing limits without conditions can sound apologetic or vague.  
**Skill-ready instruction:** Pair each limitation with its condition and consequence, and preserve the author's modal verbs.

## P08-C13

**Source pointer:** p. 1800-1802, §5.3 ¶2-3  
**Section:** Discussion  
**Function tag:** IMP + LNK  
**Score:** 8/10  
**Use status:** positive

**Local context:** Moves from an open question about a model to a modest statement of what the work contributes.  
**Sentence-by-sentence moves:**
1. Concession and open question about a widely used model.
2. `Thus`: assessment is needed, and the approach can do it.
3. `Indeed`: a result from this paper supports that use.
4. New paragraph: a further process used in the literature.
5. How it differs. 6. Earlier support.
7. `Considering that`: why it could explain the observed anomaly.
8. `In this perspective`: what including it would add.
9. `Therefore`: the present work as a possible first step.

**Why it works:** The paper widens only as far as its own result and cited work allow. The final claim uses `might`.  
**Sentence link:** `Thus` converts an open question into a need; `Indeed` ties that need to the paper's own figure.  
**Transferable rule:** Widen a discussion through an unresolved question that the study can actually address, and close on a modest next step.  
**Reusable pattern:** `Although X is widely used, it is still unclear whether it alone can explain Y. Thus, it is necessary to assess X for a given Z, and this approach is suited to that purpose. ... Therefore, this work might be a first step towards W.`  
**Risk when misused:** A chain of possibilities can drift away from the data. Each extension needs a source or a result.  
**Skill-ready instruction:** Keep future work connected to a limit or result already reported.

## P08-C14

**Source pointer:** p. 1802, §6 ¶1-2  
**Section:** Conclusions  
**Function tag:** CLO + LNK  
**Score:** 9/10  
**Use status:** caution

**Local context:** The first paragraph retraces the method in order, and the second gives the findings from synthetic and real samples.  
**Sentence-by-sentence moves:**
1. What the paper proposes. 2. What physical fact it rests on. 3-6. How it works, step by step, in the order of the methods section.
7. What the synthetic tests show, including inaccurate models. 8-9. Two further outcomes.
10. Application to the real sample, with `fairly consistent` as the strength of agreement.

**Why it works:** The Conclusions follow the paper's own order, and no new claim appears.  
**Sentence link:** Method sentences begin with the method's parts; results sentences begin with the test used. The change of subject marks the shift.  
**Transferable rule:** Retrace method steps in order, then give findings in the order of the tests.  
**Reusable pattern:** `In this study, we propose X for Y. X is based on the fact that Z. In X, A are linked through B. C is determined using D. Tests with E show that F. Applied to G, X gives H, which is fairly consistent with I.`  
**Risk when misused:** The original has `Comparing to` and ends on `applicability and usefulness`. Correct the grammar, and state what was tested rather than a general usefulness.  
**Skill-ready instruction:** Keep the Conclusions in the paper's order, and keep agreement words such as `fairly consistent` unchanged.

## P08-C15

**Source pointer:** p. 1791, Summary, sentences 1-11  
**Section:** Abstract  
**Function tag:** LNK + AIM  
**Score:** 8/10  
**Use status:** caution

**Local context:** The whole abstract in eleven plain sentences.  
**Sentence-by-sentence moves:**
1. Broad interest. 2. Usual practice and its limit. 3. `Therefore`: a possible improvement.
4. `In this study, we propose`. 5. Method core. 6. Test samples.
7. Main result. 8. Result when knowledge is incomplete. 9. Extra result with its condition.
10. Comparison. 11. Modest closing.

**Why it works:** Each sentence has one job, and problem, method, test, findings, and limit appear in the same order as in the paper.  
**Sentence link:** `In these applications` ties sentence 2 to sentence 1, and `Therefore` converts the limit into the reason for the study.  
**Transferable rule:** Build an abstract as one short sentence for each stage of the paper.  
**Reusable pattern:** `There is interest in X because of A. In these applications, B is usually done separately, which may be inadequate. Therefore, C could improve D. In this study, we propose E. We apply E to F. The results are G. Even when H, E can still I. This might be a first step towards J.`  
**Risk when misused:** Do not copy `growing interests` or `Comparing to`, and do not end on a result the study did not test.  
**Skill-ready instruction:** When an abstract is overloaded, split it into stage-by-stage sentences and preserve every condition.

## Sentence records

## P08-S01

**Source pointer:** p. 1791, Summary, sentences 2-3  
**Section:** Abstract  
**Function tag:** GAP  
**Score:** 8/10  
**Use status:** positive

**Local context:** Gives the common practice and a short reason it may be insufficient.  
**Why it works:** A non-restrictive `which may` adds the limitation without a separate complaint.  
**Sentence link:** `Therefore` takes the limitation as the reason for the next sentence's possible improvement.  
**Transferable rule:** In an abstract, compress the gap into usual practice, limit, and possible improvement.  
**Reusable pattern:** `In these applications, X is usually done separately, which may be inadequate to Y. Therefore, Z could potentially improve W.`  
**Risk when misused:** Two hedges in one sentence become weak. Use only what the evidence requires.  
**Skill-ready instruction:** Keep a compact abstract gap tied to one named practice and one named limit.

## P08-S02

**Source pointer:** p. 1791, Summary, sentences 4-5  
**Section:** Abstract  
**Function tag:** AIM  
**Score:** 9/10  
**Use status:** positive

**Local context:** States the proposal and then the core of the method.  
**Why it works:** The first sentence says what is estimated and from which data. The second says what links the data and how the problem is solved.  
**Sentence link:** The named data types at the end of the first sentence reappear as the subject of the second through the relation that joins them.  
**Transferable rule:** After the aim sentence, name the single relation that makes the method possible.  
**Reusable pattern:** `In this study, we propose X to estimate Y from A and B. The relation between A and B is included in C, which is solved using D.`  
**Risk when misused:** A chain of technical names may need a short plain explanation for a general journal.  
**Skill-ready instruction:** Write the aim sentence as method plus quantity plus data, then give the method's central link.

## P08-S03

**Source pointer:** p. 1791, Summary, sentence 8  
**Section:** Abstract  
**Function tag:** RES  
**Score:** 9/10  
**Use status:** positive

**Local context:** Gives the result under a less favorable condition.  
**Why it works:** `Even when` states the hard condition first, and the sentence then lists the features recovered.  
**Transferable rule:** State robustness by naming the difficult condition and what is still recovered.  
**Reusable pattern:** `Even when X is incomplete, Y can still capture Z, including A and B.`  
**Risk when misused:** Without the named features, `can still capture` sounds stronger than the result.  
**Skill-ready instruction:** When a robustness claim is general, ask which feature remains valid and name it.

## P08-S04

**Source pointer:** p. 1791, Summary, sentence 11; p. 1802, §5.3 ¶3, final sentence  
**Section:** Abstract / Discussion  
**Function tag:** IMP  
**Score:** 8/10  
**Use status:** positive

**Local context:** Gives the paper's broader value at the end of the abstract and Discussion.  
**Why it works:** `might` and `first step` limit the claim, and the larger aim is stated as future work.  
**Transferable rule:** Present a broad goal as a next step. Do not present it as an achievement.  
**Reusable pattern:** `This work might be a first step towards X that can do Y.`  
**Risk when misused:** `comprehensive` should stay only when the future scope is truly complete.  
**Skill-ready instruction:** Replace promotional closing claims with a bounded next step that follows from the study.

## P08-S05

**Source pointer:** p. 1791, §1 ¶1, sentence 1  
**Section:** Introduction  
**Function tag:** BKG  
**Score:** 9/10  
**Use status:** positive

**Local context:** First sentence of the paper.  
**Why it works:** One subject, one verb phrase, one process, and one general source.  
**Sentence link:** Sets up the object that the next sentence narrows to a class of materials.  
**Transferable rule:** Begin with one general claim about the study's actual object.  
**Reusable pattern:** `X plays an important role in controlling Y in Z (general source).`  
**Risk when misused:** Strong words such as `fundamental` need a textbook-level fact behind them.  
**Skill-ready instruction:** Start a broad Introduction with the study's object, and do not open with a statement about the field's growth or importance alone.

## P08-S06

**Source pointer:** p. 1791, §1 ¶1, sentence 3  
**Section:** Introduction  
**Function tag:** LNK  
**Score:** 8/10  
**Use status:** positive

**Local context:** Short pivot from a list of quantities to their use.  
**Why it works:** The summary noun lets the sentence be short and removes the need to repeat the list.  
**Sentence link:** `These` + noun collects the previous sentence's final list as the new subject.  
**Transferable rule:** When a sentence ends in a list, begin the next with `These` and a noun that names the list.  
**Reusable pattern:** `These parameters have often been used to estimate X.`  
**Risk when misused:** `This` or `These` without a noun can leave the reference unclear.  
**Skill-ready instruction:** Add a naming noun after `This` or `These` when the referent is not obvious.

## P08-S07

**Source pointer:** p. 1791, §1 ¶2, sentences 1-2  
**Section:** Introduction  
**Function tag:** BKG  
**Score:** 8/10  
**Use status:** positive  
**Reader mark:** important

**Local context:** Explains why a family of methods is attractive.  
**Why it works:** Two reasons sit in a closing phrase, and a third gets a separate short sentence.  
**Sentence link:** `Another advantage` adds without repeating the subject's full description.  
**Transferable rule:** Split a reason list when the last reason has its own importance.  
**Reusable pattern:** `X is increasingly used for Y, mainly because of A and B. Another advantage of X is C.`  
**Risk when misused:** `increasingly` needs recent citations.  
**Skill-ready instruction:** Keep reasons concrete and remove vague value words.

## P08-S08

**Source pointer:** p. 1792, §1 ¶2, sentence 10  
**Section:** Introduction  
**Function tag:** LNK  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** important

**Local context:** Carries a measured time to the pore-size estimate.  
**Why it works:** `Since` gives the known relation, and the main clause gives what follows from it.  
**Sentence link:** The distribution obtained in the preceding sentence becomes the subject of this main clause.  
**Transferable rule:** Use `Since A is related to B` when the relation is known and the sentence's purpose is the consequence.  
**Reusable pattern:** `Since A is related to B (source), C can give an estimate of D.`  
**Risk when misused:** Do not use `Since` for a relation that is the paper's new finding.  
**Skill-ready instruction:** Use a fronted reason only when the reason is established background.

## P08-S09

**Source pointer:** p. 1792, §1 ¶2, sentence 11  
**Section:** Introduction  
**Function tag:** DEF  
**Score:** 9/10  
**Use status:** positive

**Local context:** Introduces one local name after the reader understands the method.  
**Why it works:** The name follows the explanation, and `For simplicity` tells the reader why it exists.  
**Transferable rule:** Coin a local name only after the concept is clear, then use it without variation.  
**Reusable pattern:** `For simplicity, in this study we use 'A' to refer to the method of doing B.`  
**Risk when misused:** Too many local names force the reader to memorize a vocabulary.  
**Skill-ready instruction:** Permit a local label only if it shortens repeated text and is defined once.

## P08-S10

**Source pointer:** p. 1792, §1 ¶3, sentence 1  
**Section:** Introduction  
**Function tag:** GAP  
**Score:** 8/10  
**Use status:** positive

**Local context:** Paragraph opener that acknowledges complexity and current work.  
**Why it works:** It recognizes active work before introducing practical simplifications.  
**Sentence link:** Leads to `In practice`, which contrasts the ongoing theory with what is actually done.  
**Transferable rule:** Open a limitation paragraph with a fair concession about the state of knowledge.  
**Reusable pattern:** `The control of X on Y is quite complicated, and work on Z continues (recent sources).`  
**Risk when misused:** `quite complicated` is empty unless later sentences show the complexity.  
**Skill-ready instruction:** Follow a statement of complexity with the specific simplification or difficulty.

## P08-S11

**Source pointer:** p. 1792, §1 ¶3, sentence 2  
**Section:** Introduction  
**Function tag:** ASS  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** important

**Local context:** Introduces the simplifications before the examples.  
**Why it works:** `In practice` signals the move from ideal to actual, and the clause says what the simplifications are for.  
**Transferable rule:** Explain why a simplification is made by naming what it allows.  
**Reusable pattern:** `In practice, some simplifications are usually made so that X can be inferred from Y.`  
**Risk when misused:** The reader expects examples immediately after it.  
**Skill-ready instruction:** Keep `so that` clauses that explain the purpose of a simplification.

## P08-S12

**Source pointer:** p. 1792, §1 ¶3, sentences 3-6  
**Section:** Introduction  
**Function tag:** GAP  
**Score:** 10/10  
**Use status:** caution  
**Reader mark:** blue underline, marked for reuse

**Local context:** Two parallel assumption-then-failure pairs.  
**Why it works:** The assumption is given in numbered form, and `However` introduces conditions supported by sources.  
**Sentence link:** `these assumptions` directly refers to the numbered pair, so the second sentence needs no repeated description.  
**Transferable rule:** Present an assumption and its failure as adjacent sentences.  
**Reusable pattern:** `For instance, M assumes (1) that A and (2) that B. However, these assumptions may not hold for C (sources).`  
**Risk when misused:** The source's use of `solely` in the second pair is exact for an assumption. Do not use it for the author's own conclusion.  
**Skill-ready instruction:** Keep assumptions and failure conditions adjacent, and retain numbering when more than one assumption is listed.

## P08-S13

**Source pointer:** p. 1792, §1 ¶3, sentence 7  
**Section:** Introduction  
**Function tag:** GAP  
**Score:** 8/10  
**Use status:** positive

**Local context:** Final sentence of the limitation paragraph.  
**Why it works:** It reduces two parallel examples to one consequence and ends on the target quantity.  
**Sentence link:** A summary noun looks back; the target quantity at the end prepares the next paragraph.  
**Transferable rule:** Close a limitation paragraph with what the limitations do to the quantity of interest.  
**Reusable pattern:** `These approximate relations may cause errors in the estimated X.`  
**Risk when misused:** Use `errors in`, not `errors to`, and keep `may` unless the errors are measured.  
**Skill-ready instruction:** End a limitation paragraph on its consequence for the study's target.

## P08-S14

**Source pointer:** p. 1792, §1 ¶4, sentence 3  
**Section:** Introduction  
**Function tag:** BKG  
**Score:** 8/10  
**Use status:** positive

**Local context:** Introduces the general remedy to the stated problems.  
**Why it works:** The purpose phrase repeats the earlier problem, the main clause names the remedy, and `because` gives its working reason.  
**Transferable rule:** Explain a method's recent popularity by naming how it reduces the stated problem.  
**Reusable pattern:** `To reduce these problems, X has become a common approach because Y can reduce Z.`  
**Risk when misused:** `common` needs citations.  
**Skill-ready instruction:** Pair statements of common practice with a concrete reason.

## P08-S15

**Source pointer:** p. 1792, §1 ¶4, sentence 4  
**Section:** Introduction  
**Function tag:** AIM + LNK  
**Score:** 8/10  
**Use status:** positive

**Local context:** Turns the general remedy into the present study's idea.  
**Why it works:** The authors enter through a short active sentence after several literature sentences.  
**Sentence link:** `This` refers to the remedy just described. Without this sentence, the closest-study comparison would seem abrupt.  
**Transferable rule:** Add a short transition when moving from general practice to the study's own idea.  
**Reusable pattern:** `This led us to consider the joint use of A and B for X.`  
**Risk when misused:** `inspired` can sound personal in some journals; `led us` is more neutral.  
**Skill-ready instruction:** Keep the transition short and do not turn it into a contribution claim.

## P08-S16

**Source pointer:** p. 1792, §1 ¶4, sentences 5-6  
**Section:** Introduction  
**Function tag:** GAP  
**Score:** 9/10  
**Use status:** caution  
**Reader mark:** important; note asks what this work adds compared with earlier work

**Local context:** Compares the present idea with the closest earlier study.  
**Why it works:** The first sentence credits the work, and the second states exactly what was left separate.  
**Sentence link:** `However, in their study` keeps the same study as topic and moves to the missing step.  
**Transferable rule:** Name one close study and one missing step, without making the study sound deficient.  
**Reusable pattern:** `One similar attempt is the work of A, in which B and C were used to estimate D. However, in that study, B and C were processed separately, and E has not been done.`  
**Risk when misused:** The source's `still not realized yet` is redundant. Use either `not yet` or `still not`.  
**Skill-ready instruction:** Keep credit and limitation in separate sentences, and remove redundant `still` or `yet`.

## P08-S17

**Source pointer:** p. 1792, §1 ¶5, sentences 4-5  
**Section:** Introduction  
**Function tag:** MAP  
**Score:** 8/10  
**Use status:** caution

**Local context:** A problem-solution pair inside the road map.  
**Why it works:** The road map says why a later subsection exists, and the two sentences are short.  
**Sentence link:** The sub-problem at the end of the first sentence is answered by the proposal in the second.  
**Transferable rule:** Add a problem-solution pair to the road map when one method step needs a reason.  
**Reusable pattern:** `In X, one important aspect is Y. We propose Z to do W.`  
**Risk when misused:** `significant importance` is heavier than needed.  
**Skill-ready instruction:** Do not expand a road map beyond the one sub-problem that later needs a section.

## P08-S18

**Source pointer:** p. 1792, §2.1 ¶2, sentence 2  
**Section:** Theory  
**Function tag:** ASS  
**Score:** 8/10  
**Use status:** positive

**Local context:** Justifies removing a term from an equation.  
**Why it works:** The comparison gives the condition, and `such that` links it to the mathematical simplification.  
**Transferable rule:** Before dropping a term, say which effect dominates.  
**Reusable pattern:** `Compared with A, B could dominate C in M, such that term D in Equation N could be dropped.`  
**Risk when misused:** `could` must not become `does` without a value or source.  
**Skill-ready instruction:** Preserve the dominance condition whenever an equation term is omitted.

## P08-S19

**Source pointer:** p. 1793, §2.1 ¶3, sentences 2-3  
**Section:** Theory  
**Function tag:** ASS  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** blue wavy underline

**Local context:** Limits an equation right after it is introduced.  
**Why it works:** `It should be noted` introduces the condition, and `In that case` immediately says what changes.  
**Sentence link:** `In that case` keeps the condition in view and moves to the consequence.  
**Transferable rule:** State an equation's limit near the equation, with the condition and required correction.  
**Reusable pattern:** `It should be noted that X could be important if Y. In that case, Equation N might be insufficient for Z, and X should also be included.`  
**Risk when misused:** `It should be noted` loses force when used for unimportant details.  
**Skill-ready instruction:** Keep validity statements next to the equation they limit.

## P08-S20

**Source pointer:** p. 1793, §2.2 ¶1, sentence 2  
**Section:** Theory  
**Function tag:** DEF  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** blue underline, marked for reuse

**Local context:** Defines the real and imaginary parts.  
**Why it works:** `While` holds two definitions in one balanced sentence, and the verbs are plain.  
**Transferable rule:** Use one balanced sentence for two parts of the same quantity.  
**Reusable pattern:** `While the real part of X quantifies a material's ability to do A, the imaginary part reflects B.`  
**Risk when misused:** Do not use `While` for two unrelated definitions.  
**Skill-ready instruction:** Keep paired definitions parallel in grammar and level of detail.

## P08-S21

**Source pointer:** p. 1793, §2.2 ¶2, sentences 2-3  
**Section:** Theory  
**Function tag:** DEF  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** blue underline, marked for reuse

**Local context:** Explains how a double layer forms.  
**Why it works:** Cause, condition, process, purpose, and resulting name occur in that order.  
**Sentence link:** The charged surface from the first sentence is what the ions balance in the second. The new term arrives at the end.  
**Transferable rule:** Explain the formation of a structure through a short causal order and put its name last.  
**Reusable pattern:** `X is usually charged because of A and/or B. When X is placed in C, some D will gather at E to balance the charge, forming F.`  
**Risk when misused:** Participial endings can lose their subject if the sentence is long.  
**Skill-ready instruction:** Put a newly named result at the end of its explanation.

## P08-S22

**Source pointer:** p. 1793, §2.2 ¶2, the sentences that open with a spherical case  
**Section:** Theory  
**Function tag:** DEF  
**Score:** 8/10  
**Use status:** positive

**Local context:** A short thought experiment introduces the equation.  
**Why it works:** The imperative sets a simple case, and the next sentence applies a change.  
**Sentence link:** The simple case is the assumed setting for the equation that follows.  
**Transferable rule:** Use a simple case to introduce a mechanism before writing the general equation.  
**Reusable pattern:** `Consider X filled with Y. After applying Z, W will happen.`  
**Risk when misused:** A thought experiment must be simpler than the real system and clearly limited.  
**Skill-ready instruction:** Do not add an illustrative case unless the author's model already supports it.

## P08-S23

**Source pointer:** p. 1793, §2.2 ¶2, sentences on colloids and a spherical pore  
**Section:** Theory  
**Function tag:** CON  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** blue underline, marked for reuse

**Local context:** Applies the same relation to two geometries.  
**Why it works:** Both sentences use the same order: case, geometric fact, result.  
**Sentence link:** Parallel openings tell the reader that the comparison is the sentence's purpose.  
**Transferable rule:** Compare geometric or physical cases by keeping sentence order identical.  
**Reusable pattern:** `For A, X is B, and therefore Y is equal to C. For D, X is E, and therefore Y is equal to F.`  
**Risk when misused:** Parallelism should not imply that the two cases are equally supported.  
**Skill-ready instruction:** Align case comparisons around one repeated structure.

## P08-S24

**Source pointer:** p. 1793, §2.2 ¶4-5, sentence on what will not be addressed  
**Section:** Theory  
**Function tag:** ASS  
**Score:** 9/10  
**Use status:** positive

**Local context:** Limits the scope of the theory.  
**Why it works:** The semicolon and `instead` place the omitted task and the chosen approach side by side.  
**Transferable rule:** Say directly what the study does not address and what it does in its place.  
**Reusable pattern:** `In this study, we will not address X; instead, we simplify Y by using Z.`  
**Risk when misused:** It must not be used to avoid a question essential to the conclusion.  
**Skill-ready instruction:** Preserve explicit out-of-scope statements and do not make them sound like results.

## P08-S25

**Source pointer:** p. 1793, §2.2 ¶5, final sentence  
**Section:** Theory  
**Function tag:** ASS  
**Score:** 8/10  
**Use status:** positive

**Local context:** Claims only a partial representation of several effects.  
**Why it works:** `to a certain extent` matches the limited claim.  
**Transferable rule:** When a lumped parameter absorbs effects, say that the effects are only partly considered.  
**Reusable pattern:** `Since X and Y are both optimized, to a certain extent, the effects of Z are also considered.`  
**Risk when misused:** Removing the hedge would imply a full physical treatment.  
**Skill-ready instruction:** Keep partial-treatment phrases in methods that use lumped parameters.

## P08-S26

**Source pointer:** p. 1794, §2.3 ¶2, sentences 2-4  
**Section:** Theory  
**Function tag:** ASS  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** important

**Local context:** Ranks assumptions and separates simple from uncertain cases.  
**Why it works:** The strongest assumption comes first, then a clear case, then an unresolved case.  
**Sentence link:** Case openings repeat the structure and shift only the material class.  
**Transferable rule:** Order assumptions by importance and show where each is clear or uncertain.  
**Reusable pattern:** `The most important assumption is that A. For B, this assumption is valid. For C, although D has been observed, it remains unclear whether E.`  
**Risk when misused:** Use `clearly` only for an analytically true case.  
**Skill-ready instruction:** Keep the distinction between valid, approximately valid, and unresolved assumptions.

## P08-S27

**Source pointer:** p. 1794, §2.3 ¶2, sentences 9-10  
**Section:** Theory  
**Function tag:** ASS  
**Score:** 9/10  
**Use status:** positive

**Local context:** Makes an implicit model assumption visible.  
**Why it works:** The concession acknowledges that the assumption is rarely stated, and `That is` gives the concrete meaning.  
**Sentence link:** `That is` restates the technical assumption in observable terms.  
**Transferable rule:** State hidden assumptions and restate them in physical terms.  
**Reusable pattern:** `Lastly, although not stated explicitly, X uses Y, which assumes Z. That is, W does not occur during V.`  
**Risk when misused:** Do not claim a hidden assumption unless the model structure shows it.  
**Skill-ready instruction:** Mark inferred assumptions `author-confirm` when the source text does not establish them.

## P08-S28

**Source pointer:** p. 1794, §3.1 ¶1, sentence 1  
**Section:** Methods  
**Function tag:** MET  
**Score:** 8/10  
**Use status:** positive  
**Reader mark:** important

**Local context:** Announces the available types of approach.  
**Why it works:** The colon tells the reader exactly what the next sentences will cover.  
**Transferable rule:** Open an option comparison by stating how many options there are.  
**Reusable pattern:** `In practice, there are two types of approach to X: A and B.`  
**Risk when misused:** Check that the count is accurate; `two main types` is safer.  
**Skill-ready instruction:** Keep option counts only when the listed options are complete.

## P08-S29

**Source pointer:** p. 1795, §3.1 ¶2, final sentence  
**Section:** Methods  
**Function tag:** IMP  
**Score:** 8/10  
**Use status:** positive

**Local context:** Evaluates a cross-plot with published data.  
**Why it works:** `lends additional support` is the right strength for one dataset.  
**Transferable rule:** Use support language when a dataset agrees with a relation but does not prove it.  
**Reusable pattern:** `The experimental data lend additional support to the relation between X and Y.`  
**Risk when misused:** Do not upgrade it to `confirms`.  
**Skill-ready instruction:** Preserve the strength of `support` language.

## P08-S30

**Source pointer:** p. 1795, §3.2 ¶1 sentence 3 and ¶2 sentences 1-2  
**Section:** Methods  
**Function tag:** MET  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** important

**Local context:** Explains which parameters can be recovered.  
**Why it works:** It gives the non-uniqueness first, then what the linking relation changes.  
**Sentence link:** `This implies` turns the relation into a statement about what can be recovered.  
**Transferable rule:** State why a parameter cannot be obtained, then what makes it recoverable.  
**Reusable pattern:** `A and B cannot be recovered separately because of C. As shown in D, X and Y are related through Z. This implies that A and B are not independent, and it is possible to recover one once the other is known.`  
**Risk when misused:** `possible` must not imply accuracy.  
**Skill-ready instruction:** Keep identifiability limits and their cause together.

## P08-S31

**Source pointer:** p. 1795, §3.2 ¶2, final two sentences  
**Section:** Methods  
**Function tag:** MET  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** highlighted

**Local context:** Explains why variables are transformed.  
**Why it works:** The purpose comes directly after the operation, and `Moreover` gives a second reason.  
**Transferable rule:** Explain the reason for each transformation that affects the result.  
**Reusable pattern:** `The use of X is to ensure Y. Moreover, since A, X ensures that B.`  
**Risk when misused:** Reasons need a source or a mathematical basis.  
**Skill-ready instruction:** Keep reason clauses attached to their operation.

## P08-S32

**Source pointer:** p. 1795, §3.3, sentences on regularization and the choice made  
**Section:** Methods  
**Function tag:** MET  
**Score:** 8/10  
**Use status:** positive

**Local context:** Moves from why a term is needed to common practice and the present choice.  
**Why it works:** Need, common use, and study choice are three short steps.  
**Sentence link:** `also` in the last sentence ties the choice to the common practice just stated.  
**Transferable rule:** Before naming the choice, give the need and common practice.  
**Reusable pattern:** `X is needed to stabilize Y. In Z studies, A is commonly used. In this study, we also use A.`  
**Risk when misused:** Common practice alone does not justify every setting.  
**Skill-ready instruction:** Add a reason when the choice is not standard.

## P08-S33

**Source pointer:** p. 1796, §3.4, sentences on analytical calculation and known parameters  
**Section:** Methods  
**Function tag:** MET  
**Score:** 8/10  
**Use status:** positive

**Local context:** States an implementation choice and a case-specific adjustment.  
**Why it works:** A purpose phrase gives the reason, and a conditional covers a special case.  
**Transferable rule:** Tie implementation details to purpose and state what changes in special cases.  
**Reusable pattern:** `To ensure X, Y is calculated at each Z. If A is known, we can set B to zero so that A is not updated.`  
**Risk when misused:** Too many implementation details can hide the main method.  
**Skill-ready instruction:** Keep only implementation details needed to interpret or reproduce the result.

## P08-S34

**Source pointer:** p. 1796, §3.5 ¶1, sentences 5-6  
**Section:** Methods  
**Function tag:** CON  
**Score:** 9/10  
**Use status:** caution

**Local context:** Contrasts the ideal search with what is practical.  
**Why it works:** The method's cost explains why a simpler approach is needed.  
**Sentence link:** `However` and `this method` keep the same object while changing evaluation.  
**Transferable rule:** Justify a simplified procedure by contrasting the ideal one with its practical cost.  
**Reusable pattern:** `It would be better to do X using Y (source). However, Y is computationally costly, and in practice Z is mainly based on W.`  
**Risk when misused:** The source's `always better` is strong. Prefer `would be better` unless proved.  
**Skill-ready instruction:** Use cost-based justification only when the cost is real for the study.

## P08-S35

**Source pointer:** p. 1796, §4 opening paragraph, sentences 1 and 6-9  
**Section:** Results  
**Function tag:** MAP + MET  
**Score:** 9/10  
**Use status:** positive

**Local context:** Introduces a test and its two cases.  
**Why it works:** The section's job and the difference between cases appear before the details.  
**Sentence link:** The case labels are defined once and later reused as subsection names.  
**Transferable rule:** Define test cases by the one condition that differs.  
**Reusable pattern:** `In this section, X is used to demonstrate the applicability of Y. Two cases were tested. In Case 1, A. In Case 2, B.`  
**Risk when misused:** `demonstrate the applicability` must match what the test covers.  
**Skill-ready instruction:** State the difference between test cases before giving parameter values.

## P08-S36

**Source pointer:** p. 1798, §4.1 ¶4, sentences 1-6  
**Section:** Results  
**Function tag:** RES  
**Score:** 8/10  
**Use status:** positive

**Local context:** A secondary test of parameter recovery.  
**Why it works:** The test is phrased as a question, and the final number is compared with the true value.  
**Transferable rule:** Introduce a side test by its question, then report the numeric outcome.  
**Reusable pattern:** `We also tested whether X can estimate Y by allowing Y to change during Z. The final value of Y is A, which is close to the true value B.`  
**Risk when misused:** `very close` should be used with the two numbers present.  
**Skill-ready instruction:** Keep numeric baselines next to closeness claims.

## P08-S37

**Source pointer:** p. 1799, §4.2 ¶1, sentences 6-8  
**Section:** Results  
**Function tag:** CON  
**Score:** 8/10  
**Use status:** positive

**Local context:** Compares two model types through their responses.  
**Why it works:** It gives the difference, then uses `The former` to give its cause and effect.  
**Sentence link:** `The former` refers directly to the first compared item.  
**Transferable rule:** Use a short comparison sentence and then explain each side.  
**Reusable pattern:** `For comparison, X is also shown. As shown in Figure N, A and B give different C. The former does D, and thus E.`  
**Risk when misused:** `the former` is unclear if the antecedent is far away.  
**Skill-ready instruction:** Repeat the noun when `former` or `latter` requires a search.

## P08-S38

**Source pointer:** p. 1799, §4.2 ¶2, sentences 7-8  
**Section:** Results  
**Function tag:** IMP  
**Score:** 8/10  
**Use status:** positive

**Local context:** Attributes the poorer result to the known test condition.  
**Why it works:** The cause is the one deliberately changed variable, so `attributed` is justified.  
**Sentence link:** `This` names the observed difference.  
**Transferable rule:** Use direct attribution only when the study design isolates the cause.  
**Reusable pattern:** `Compared with Figure A, the results in Figure B differ notably from X. This is attributed to the use of Y.`  
**Risk when misused:** For uncontrolled observations, use `might be due to`.  
**Skill-ready instruction:** Choose attribution strength from the study design.

## P08-S39

**Source pointer:** p. 1799, §5.1, sentence 1; p. 1800, §5.2 ¶2, sentences 2-3  
**Section:** Methods  
**Function tag:** MET  
**Score:** 8/10  
**Use status:** positive

**Local context:** Explains why a sample and an external comparison are appropriate.  
**Why it works:** `because` gives the practical reason, and matching porosity justifies the comparison.  
**Transferable rule:** Justify a sample and a borrowed comparison by their relevant shared properties.  
**Reusable pattern:** `X is chosen because A and B are available. Here, we use the sample in C as an example. It has D, which is close to that of our sample (E).`  
**Risk when misused:** Similarity in one property does not make samples equivalent.  
**Skill-ready instruction:** State which property makes an external comparison reasonable.

## P08-S40

**Source pointer:** p. 1799, §5.2 ¶1, sentences 3-6  
**Section:** Results  
**Function tag:** ASS + RES  
**Score:** 9/10  
**Use status:** positive

**Local context:** Gives a parameter's source, its limit, and an unexpected inversion behavior.  
**Why it works:** The value is traced to a source and condition, and the unexpected outcome is reported with a tentative reason.  
**Sentence link:** `However, we find` reports what contradicted the expected behavior. `The reason could be` keeps the explanation tentative.  
**Transferable rule:** Report parameter origin and unexpected behavior plainly.  
**Reusable pattern:** `X was taken as A as suggested by B, considering that C. ... However, we find that Y does not change during Z. The reason could be that W.`  
**Risk when misused:** A tentative reason should still be testable or plausible.  
**Skill-ready instruction:** Keep unexpected outcomes and do not rewrite them as confirmations.

## P08-S41

**Source pointer:** p. 1799, §5.2 ¶1, sentence 10  
**Section:** Methods  
**Function tag:** ASS  
**Score:** 8/10  
**Use status:** positive

**Local context:** Warns that comparison settings differ.  
**Why it works:** The reader learns that a difference may come from settings.  
**Transferable rule:** State differences in settings that could affect a comparison.  
**Reusable pattern:** `The parameters used in A are determined separately using B, so they may differ from those used in C.`  
**Risk when misused:** Disclosure does not remove the bias.  
**Skill-ready instruction:** Keep comparison caveats next to the comparison method.

## P08-S42

**Source pointer:** p. 1800, §5.3 ¶3, the sentence that contrasts two polarization views  
**Section:** Discussion  
**Function tag:** CON  
**Score:** 8/10  
**Use status:** positive

**Local context:** Introduces a different mechanism through its contrast with the one used.  
**Why it works:** The first half states the known relation; the second gives the new control.  
**Transferable rule:** Present an alternative by the difference that matters.  
**Reusable pattern:** `Different from A, which relates B to C, D suggests that B may also be controlled by E.`  
**Risk when misused:** `suggests` should not become `shows`.  
**Skill-ready instruction:** Name the single differing relation in a model comparison.

## P08-S43

**Source pointer:** p. 1804, Appendix A, sentence after the coefficient comparison; p. 1805, final paragraph  
**Section:** Appendix  
**Function tag:** LNK + ASS  
**Score:** 8/10  
**Use status:** positive

**Local context:** A derivation signals future use of a result and states the range of its validity.  
**Why it works:** The forward pointer gives the purpose of an intermediate result, and the closing sentence names both covered cases.  
**Sentence link:** The final statement returns to the derivation's unspecified domains and turns that into applicability.  
**Transferable rule:** In derivations, say why an intermediate result matters and what cases the result covers.  
**Reusable pattern:** `This result is used later to determine X. In the derivation, Y was not specified, and therefore Equation N holds for two cases: (1) A; and (2) B.`  
**Risk when misused:** Do not say an equation holds generally when derivation assumptions restrict it.  
**Skill-ready instruction:** Preserve assumptions when summarizing a derivation.

## P08-S44

**Source pointer:** p. 1791 Summary sentence 10; p. 1798 §4.1 ¶3 sentence 5; p. 1800 §5.2 ¶2 sentences 5 and 7; p. 1795 §3.1 ¶2 sentence 6; p. 1799 §4.2 ¶2 sentence 11  
**Section:** Across sections  
**Function tag:** STY  
**Score:** 7/10  
**Use status:** caution

**Local context:** Places where the function is useful but the surface form should not be copied.  
**Why it works:** The comparison or emphasis is useful, but the wording contains non-native or inflated forms.  
**Transferable rule:** Learn the sentence function, and correct the surface form.  
**Reusable pattern:** `Compared with X, Y ...` for `Comparing to`; `One notable feature` or `The main feature` for `profound feature`; `outlier` for `outliner`; `even though` or `although` for `despite that`.  
**Risk when misused:** Copying the exemplar's slips would make a revision less correct.  
**Skill-ready instruction:** Do not transfer these errors from the exemplar. Use the corrected forms above.

---

# P05 (continued): Broadband Electrical Properties Framework (E2)

## Paper-Level Notes

**Source:** Niu, Zhang, and Prasad (2020), *JGR: Solid Earth* 125, e2020JB020515, doi:10.1029/2020JB020515. Page numbers below are the article's own (1-18).  
**Relation to existing records:** P05-S01 to P05-S10 are in `source_sentence_corpus.md` and are not repeated. Sentence records here start at P05-S11. Chains may pass through a sentence that an earlier record covers; the chain records the order and the links, which the earlier record does not.  
**Strength of writing:** The Introduction teaches the reader the two central concepts before it reviews the literature, and the gap is a four-step causal argument. Every method step says why it is needed.

## Paragraph chains

## P05-C01

**Source pointer:** p. 1, §1 ¶1, sentences 1-4  
**Section:** Introduction  
**Function tag:** LNK + BKG  
**Score:** 10/10  
**Use status:** positive  
**Reader mark:** note: broad background; an interpretation of the mechanism is needed

**Local context:** Opening paragraph, four sentences, from the use of a family of methods to the knowledge needed to interpret them.  
**Sentence-by-sentence moves:**
1. General statement: the methods are often used in a field to study a class of targets, with several citations.
2. `Relevant techniques include`: five members, each with one citation.
3. `Such` + noun: what all these tests provide, namely the distribution of two properties.
4. `To correctly interpret` the measurements, what one needs to understand, and what controls it.

**Why it works:** The paragraph goes from use, to members, to output, to requirement. The last sentence names the two concepts that the next two paragraphs explain.  
**Sentence link:** `Such` + noun gathers the list in sentence 2. The two properties at the end of sentence 3 are what sentence 4 says must be understood. The final sentence ends on the terms that open paragraphs 2 and 3.  
**Transferable rule:** In a first paragraph, say what the method family is used for, what it delivers, and what must be known to interpret it.  
**Reusable pattern:** `X methods are frequently used in F to study Y (sources). Relevant techniques include A, B, and C. Such tests provide the distribution of P and Q. To correctly interpret these measurements, one needs to understand R and its controlling factors such as S.`  
**Risk when misused:** A technique list longer than about five items turns into a citation dump.  
**Skill-ready instruction:** If the first paragraph does not end on the concept the paper studies, move or add a final requirement sentence built from the author's own content.

## P05-C02

**Source pointer:** p. 1, §1 ¶2, sentences 1-4  
**Section:** Introduction  
**Function tag:** LNK + DEF  
**Score:** 10/10  
**Use status:** positive  
**Reader mark:** note: the two main sources of conduction in porous media; basic knowledge

**Local context:** Teaches the first central property in four sentences.  
**Sentence-by-sentence moves:**
1. One-line definition of the property as an ability of a material.
2. Phase 1 (solid): typical value, and `thus` how it is usually treated.
3. Phase 2 (pore water): why it conducts, and its role as the main path.
4. `In addition to` phase 2: a third contributor at the interface, and where it matters most.

**Why it works:** The definition is followed by one sentence per component, ordered from the one that contributes nothing to the ones that contribute. No sentence carries two components.  
**Sentence link:** Sentence 4 opens by repeating the subject of sentence 3 inside `In addition to`, so the new contributor is attached to a known one.  
**Transferable rule:** Explain a bulk property by defining it and then taking the material's components one at a time.  
**Reusable pattern:** `X quantifies a material's ability to do Y. For A, X is of the order of V, and thus A is usually considered W. B is ... because of C, and it is the main pathway for Y. In addition to B, D also contributes, especially in E.`  
**Risk when misused:** Tutorial detail that specialists do not need should be cut for a specialist journal.  
**Skill-ready instruction:** When a concept paragraph mixes components in one sentence, give each component its own sentence in order of contribution.

## P05-C03

**Source pointer:** p. 1-2, §1 ¶3, sentences 1-5  
**Section:** Introduction  
**Function tag:** LNK + DEF  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** note: polarization ability and its frequency response

**Local context:** Teaches the second central property, in the same shape as the paragraph before it.  
**Sentence-by-sentence moves:**
1. One-line definition, with a short `i.e.` gloss.
2. The property of the separate phases is usually constant below a stated frequency.
3. The property of the whole material, `however`, depends on frequency and can differ from the phase average.
4. `As the frequency decreases`: direction of change and its general cause.
5. Mechanisms proposed, with a pointer to the section that reviews them.

**Why it works:** The contrast between parts and whole creates the question that the paper answers. Paragraphs 2 and 3 have the same opening form, so the reader sees them as a pair.  
**Sentence link:** `however` sits after the subject in sentence 3, so the sentence still opens on the known term. The cause named at the end of sentence 4 is expanded in sentence 5.  
**Transferable rule:** Give paired concepts paired paragraphs, and use the difference between the parts and the whole to raise the question.  
**Reusable pattern:** `X is associated with a material's ability to do Y. The X of A and B is usually constant at C. The effective X of M, however, depends on D and may differ from E. As D decreases, the effective X generally increases due to F. Several mechanisms have been proposed to explain this, including G and H, which are reviewed in Section N.`  
**Risk when misused:** A forward pointer needs a section that really delivers the review.  
**Skill-ready instruction:** Keep parallel concept paragraphs parallel in their first sentences.

## P05-C04

**Source pointer:** p. 2, §1 ¶4, sentences 1-7  
**Section:** Introduction  
**Function tag:** LNK + IMP  
**Score:** 9/10  
**Use status:** caution  
**Reader mark:** note: the relation between conduction and polarization

**Local context:** Explains why the two properties are linked, through a short thought experiment.  
**Sentence-by-sentence moves:**
1. `In principle`: the two variations are linked, and by what principle.
2. `Consider a material` with a stated feature.
3. `As` the driving variable decreases, what additionally happens.
4. `This means`: the consequence for property 1, with the direction restated in parentheses.
5. `Since` the induced field opposes the applied one, the consequence for property 2.
6. What the link means in practice: one spectrum determines the other.
7. `Mathematically`: the named relations that express it.

**Why it works:** The physical picture comes before the named mathematical relation, so the name arrives as a summary of something already understood.  
**Sentence link:** Each sentence begins with the result of the one before (`This means`, `Since`, the link itself as subject). The ladder `In principle` -> `Consider` -> `This means` -> `Mathematically` moves from idea to picture to formal statement.  
**Transferable rule:** Explain a coupling between two quantities by a simple case first, and name the formal relation last.  
**Reusable pattern:** `In principle, the variations in X and Y are linked by Z. Consider a material with A. As B decreases, C occurs and also contributes to D. This means X increases as B decreases. Since E, Y decreases. Mathematically, X and Y can be linked through the R relations (sources).`  
**Risk when misused:** The source has `if compared to` and one missing article. Use `compared with`. A thought experiment that is longer than the result it explains should be shortened.  
**Skill-ready instruction:** Offer the simple-case explanation only from physics the author has stated; never invent the mechanism.

## P05-C05

**Source pointer:** p. 2, §1 ¶5, sentences 1-5  
**Section:** Introduction  
**Function tag:** LNK + BKG  
**Score:** 8/10  
**Use status:** caution  
**Reader mark:** note: mainstream results so far; empirical and theoretical formulas

**Local context:** Reviews the two established approaches and their products.  
**Sentence-by-sentence moves:**
1. Purpose phrase, then the two most common approaches.
2. What these approaches have been used for over several decades.
3. The best-known model and what it relates to what.
4. `Other examples include` two further model families.
5. `Recently`: progress on the topic nearest to the paper.

**Why it works:** The review is organized by what each model relates, so the reader learns the content of the literature and does not just see names.  
**Sentence link:** `these two approaches` restates sentence 1. `Recently` moves the paragraph to the present and toward the paper's own topic.  
**Transferable rule:** Review established work by saying what each model connects, and end on the recent work nearest the study.  
**Reusable pattern:** `To study X, the most commonly used approaches are A and B. These two approaches have been used to develop models that translate X to Y. The best-known model is M (source), which relates P to Q through R. Other examples include S and T. Recently, progress has been made in modeling U (sources).`  
**Risk when misused:** The source's `robust models` and `significant progress` are evaluative. Keep such words only with support.  
**Skill-ready instruction:** In review sentences, state what a cited model relates or predicts; delete praise that carries no information.

## P05-C06

**Source pointer:** p. 2, §1 ¶6, sentences 1-6  
**Section:** Introduction  
**Function tag:** LNK + GAP  
**Score:** 9/10  
**Use status:** caution  
**Reader mark:** note: current research methods and their emphasis; one aspect is studied much less

**Local context:** Introduces the controlling factor, the under-studied part of it, and the tool that can address it.  
**Sentence-by-sentence moves:**
1. The properties are influenced by a factor, glossed with `i.e.` into two components.
2. `While` component 1 is well studied, component 2 is less explored, `due to` a stated difficulty.
3. `Recently`: a tool has emerged.
4. `In a` + tool: what it calculates and from what.
5. `Such` + tool plural: what it allows.
6. `In addition to` one data source: another way to produce the input, and what that opens.

**Why it works:** The under-studied component comes with its practical reason, and the tool is introduced right after the difficulty it removes.  
**Sentence link:** The two components named in sentence 1 are the two halves of sentence 2. The tool at the end of sentence 3 is the opening phrase of sentence 4 and, in plural with `Such`, of sentence 5.  
**Transferable rule:** Split a controlling factor into parts, say which part is under-studied and why, then introduce the tool that makes it accessible.  
**Reusable pattern:** `X is influenced by Y (i.e., A and B). While the effect of A has been extensively studied (sources), the influence of B is less explored because C is difficult. Recently, T has emerged as a tool for studying D. In T, E can be calculated from F. Such simulations allow us to explore G.`  
**Risk when misused:** The source calls the tool `powerful`. Say what the tool does. `less explored` needs a literature basis.  
**Skill-ready instruction:** Keep a `While A ..., B ...` gap sentence only if the reason for the imbalance is stated.

## P05-C07

**Source pointer:** p. 2, §1 ¶7, sentences 1-5  
**Section:** Introduction  
**Function tag:** LNK + GAP  
**Score:** 10/10  
**Use status:** positive  
**Reader mark:** note: research significance (marked three times); the physical reason underlined

**Local context:** The gap paragraph. P05-S01 records its first sentence; this chain records how the gap is argued.  
**Sentence-by-sentence moves:**
1. `Although` the tool has been used for two simpler cases, it is still hard to apply to the target case.
2. `This is because` the target process happens in a very thin layer, with its size.
3. A direct treatment therefore requires fine discretization near the interface.
4. `Considering that` the sample volume is large, with its size, the cost is very high.
5. `It is therefore desirable to` develop methods that include the process effectively.

**Why it works:** The gap is a physical argument with two numbers in it (layer thickness, sample volume). The need in the last sentence follows from the argument and does not rest on the claim that nobody has done it.  
**Sentence link:** Each sentence picks up the last noun phrase of the one before: target process -> thin layer -> fine discretization -> cost -> need for new methods.  
**Transferable rule:** Argue a gap as: what works, what remains hard, the physical reason, the practical consequence, the need.  
**Reusable pattern:** `Although X has been used to study A (sources) and B (sources), applying it to C is still challenging. This is because C is associated with D occurring at scale E. A direct simulation of D requires F. Considering that G is relatively large, the cost is very high. It is therefore desirable to develop methods that can include C in X.`  
**Risk when misused:** Every step needs a fact from the author. A missing step must be asked for; it must not be filled in.  
**Skill-ready instruction:** When a gap sentence says only that something is challenging, ask the author for the reason and the consequence, then write them as separate short sentences.

## P05-C08

**Source pointer:** p. 2-3, §1 ¶8, sentences 1-5  
**Section:** Introduction  
**Function tag:** MAP + AIM  
**Score:** 10/10  
**Use status:** positive

**Local context:** Objective, scope, and road map. P05-S02 covers the framework sentence of the abstract; this chain covers the closing paragraph of the Introduction.  
**Sentence-by-sentence moves:**
1. `The objective of this study is to develop such a ...`: answers the need in the previous paragraph.
2. `For simplicity, in this study, we only consider`: the scope.
3. `In the following, we first` review the background.
4. `We then` develop the method, with the processes it includes.
5. `Finally, we` demonstrate it on a named sample.

**Why it works:** `such a` ties the objective to the need just stated, so the aim needs no further justification. The three steps equal the three main sections.  
**Sentence link:** The previous paragraph ends on the kind of method needed, and this one opens by promising it. Scope comes before the map, so the reader knows the limits before the plan.  
**Transferable rule:** State the objective as the answer to the stated need, limit the scope in one sentence, then give the order of the paper.  
**Reusable pattern:** `The objective of this study is to develop such an X for Y. For simplicity, in this study, we only consider Y. In the following, we first review A. We then develop B, including C and D. Finally, we demonstrate B by applying it to E.`  
**Risk when misused:** `such a` fails if the preceding sentence did not name the kind of thing needed.  
**Skill-ready instruction:** Place the scope sentence between the objective and the road map.

## P05-C09

**Source pointer:** p. 3, §2.1 ¶1, sentences 1-6  
**Section:** Theory  
**Function tag:** DEF + LNK  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** definition sentences underlined

**Local context:** Fixes the paper's terms before any equation. P05-S03 and P05-S04 record two of the sentences; this chain records the order.  
**Sentence-by-sentence moves:**
1. `In this paper, we use` two terms for a stated purpose.
2. `Note that` the object they apply to can be of two kinds.
3. Other terms are also found in the literature.
4. `To avoid confusion`, the terms are defined through stated equations.
5. For composite materials, the measured values are averages.
6. `To distinguish` the average from the phase values, a modifier is added to the terms.

**Why it works:** Each definition is preceded by the confusion it prevents. The reader accepts the terminology because the reason is visible.  
**Sentence link:** Sentence 3 raises the problem (several competing terms) and sentence 4 opens with the purpose that solves it. Sentence 5 raises a second problem and sentence 6 solves it the same way.  
**Transferable rule:** Before defining terms, state the ambiguity. Use the form problem, then purpose phrase, then definition.  
**Reusable pattern:** `In this paper, we use A and B to describe X. Other terms such as C and D are also used in the literature. To avoid confusion, we define A and B through E. For M, the measured values are averages of F. To distinguish these from G, we use 'effective A' to indicate H.`  
**Risk when misused:** A terminology paragraph is unnecessary when the field has one settled usage.  
**Skill-ready instruction:** Add a terminology paragraph only where competing usages could change how a result is read.

## P05-C10

**Source pointer:** p. 3-4, §2.1 ¶2 to the end of the subsection  
**Section:** Theory  
**Function tag:** DEF + LNK  
**Score:** 8/10  
**Use status:** positive

**Local context:** A short derivation that ends by fixing which symbol each term means.  
**Sentence-by-sentence moves:**
1. `Assume that` a field is applied. 2. The total quantity `is then the sum of` two parts.
3. Part 1 is related to the field by a named law. 4. Part 2 `is defined as` a derivative.
5. `Note that` an auxiliary relation holds. 6. `Inserting` one equation into another and considering a form of the field `yield` the next.
7. `Combining` equations `results in` the total. 8. `If we define` quantity A by an equation, `we then have` its parts. 9. `Similarly, if we define` quantity B, the parallel result.
10. `In this study`, term 1 `refers to` one symbol and term 2 `represents` another.

**Why it works:** Every equation has a short lead-in that says what operation produced it, and the derivation ends by returning to the two words the paper will use.  
**Sentence link:** The lead-in verbs name the operation (`Inserting`, `Combining`, `If we define`), so the reader knows how each equation follows from the earlier ones.  
**Transferable rule:** Introduce each equation by the operation that produces it, and close a derivation by tying symbols back to the paper's terms.  
**Reusable pattern:** `Assume that X is applied to M. The total A is then the sum of B and C. B is related to X by L's law. C is defined as D. Inserting Equation i into Equation j yields ... Combining Equations i-k results in ... In this study, T1 refers to S1 in Equation m, and T2 refers to S2 in Equation n.`  
**Risk when misused:** Repeating `yields` for every step is monotonous; vary among `gives`, `results in`, and `we then have`.  
**Skill-ready instruction:** Do not edit equations. Edit only the lead-ins, and keep every `where` definition.

## P05-C11

**Source pointer:** p. 4, §2.2, sentences 1-8  
**Section:** Theory  
**Function tag:** LNK + ASS  
**Score:** 9/10  
**Use status:** caution  
**Reader mark:** mechanism sentences underlined; a reader question is written beside the last sentence

**Local context:** Explains one polarization mechanism and ends by saying why the study needs no model for it.  
**Sentence-by-sentence moves:**
1. Where the mechanism occurs, with its alternative name in parentheses.
2. `Under an external` field, a continuity condition.
3. `Because of the mismatch`, what differs and what accumulates.
4. The induced effect, named, and what it does to the bulk property.
5. In the material class of interest, what controls its frequency and size.
6. Existing models, in one sentence.
7. `In a` + this paper's method, `however`, the feature is represented directly because real geometry is used.
8. `Thus`, no model of this mechanism is required here.

**Why it works:** Mechanism, effect, controls, and models take one sentence each, and the paragraph ends with what all this means for the present method.  
**Sentence link:** Sentence 3 turns the condition of sentence 2 into a cause. Sentence 4 names the accumulated result and makes it the subject.  
**Transferable rule:** End a background subsection by saying what it implies for the study's own method.  
**Reusable pattern:** `In M, X occurs where A separates two phases with different B. Under an external field, C must be equal. Because B is mismatched, D differs, resulting in E. The induced F gives rise to an increase in G. ... In a pore-scale simulation, however, H is represented directly because I. Thus, no X models are required in this study.`  
**Risk when misused:** The reader's margin question shows that the final sentence can be misread as "the mechanism is ignored". Say that the mechanism is included through the geometry and that only a separate model is unnecessary. The source also has `There has been a number of` and `if compared to`.  
**Skill-ready instruction:** When a sentence says something is `not required`, state what replaces it, so the reader does not infer omission.

## P05-C12

**Source pointer:** p. 4, §2.3 ¶1-2  
**Section:** Theory  
**Function tag:** DEF + LNK  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** note: why the surface is charged and how the double layer forms

**Local context:** Builds the interface structure, then lists its two effects, names the second, and classifies the models.  
**Sentence-by-sentence moves:**
1. The surface is charged, with two causes.
2. `If immersed in` a solution, ions accumulate to balance it, `forming` a cloud that is then named.
3. The standard model describes the structure as two layers.
4. `In the inner layer`: what the ions do. 5. `In the outer` layer: how they are treated and which equation describes them.
6. New paragraph: the structure can affect `both` of two things.
7. `First, because` of higher concentration, effect 1. 8. `known as` + its name, with where it has been observed.
9. `Second, when` a field is applied, the local process and the resulting imbalance.
10. The gradient forms a dipole, `and thus` the material is polarized.
11. `This polarization ... is termed` + name `in this paper`.
12. Many models exist. 13. `Based on` their assumptions, they `can be classified into three groups`, with a colon list.

**Why it works:** The reader is given structure, then consequences, then a name, then a classification that becomes the next three subsections.  
**Sentence link:** `both` in sentence 6 promises two items, and `First` and `Second` deliver them. The colon list in the last sentence is the order of the following subsections.  
**Transferable rule:** Describe a structure before its effects, announce the number of effects, and end with the classification that organizes what follows.  
**Reusable pattern:** `The presence of X can affect both A and B. First, because C, A is enhanced. This increase, known as D, has been observed in E. Second, when F is applied, X can influence G, resulting in H. ... This process is termed I in this paper. Based on J, these models can be classified into three groups: K, L, and M.`  
**Risk when misused:** `both ... First ... Second` becomes heavy for small points.  
**Skill-ready instruction:** If a paragraph promises a number of items, check that the same number is delivered in the same order.

## P05-C13

**Source pointer:** p. 4-6, §2.3.1 ¶1, §2.3.2 sentence 1, and §2.3.3 ¶1  
**Section:** Theory  
**Function tag:** LNK + DEF  
**Score:** 9/10  
**Use status:** positive

**Local context:** Three sibling subsections describe three mechanisms with the same sequence of moves.  
**Sentence-by-sentence moves (each subsection):**
1. What the model assumes about the geometry.
2. The state at rest, or the role of the key geometric element.
3. `After applying` / `Under an external` field: where ions gather and where they are depleted.
4. The resulting gradient imposes a dipole across the element, `and thus` polarization occurs.

**Why it works:** The same four moves and the same closing clause recur, so the reader compares the three mechanisms by geometry alone.  
**Sentence link:** Across subsections, the repeated closing clause works as a refrain. Within each, the gradient at the end of move 3 is the subject of move 4.  
**Transferable rule:** Describe sibling mechanisms, cases, or models with the same order of moves and the same key terms.  
**Reusable pattern:** `The X model assumes that A. At equilibrium, B. After applying an external field, C will accumulate on one side of D and be depleted on the other. The induced gradient imposes E across D, and thus F occurs.`  
**Risk when misused:** Identical wording over more than three or four siblings becomes tedious. Keep the order and vary minor words.  
**Skill-ready instruction:** When sibling descriptions differ in order, reorder them to match before polishing.

## P05-C14

**Source pointer:** p. 5, §2.3.1 ¶2-3  
**Section:** Theory  
**Function tag:** DEF + LNK  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** note: how the grain model developed; the basic assumptions of the first model

**Local context:** A short history of one model family, then a clarification of two names that are often confused.  
**Sentence-by-sentence moves:**
1. `Using this concept`, many models have been developed.
2. `Assuming that` two conditions hold, an author developed an equation for the simplest case.
3. Other shapes were `also` considered. 4. `Note that` the validity condition (covered by P05-S07). 5. A general model exists for other sizes. 6. `In addition to` one type of movement, a second type has been treated.
7. New paragraph: `It is worth` noting that these models did not separate two layers.
8. `In practice, however`, models with only the first movement are usually given one name.
9. `This is because` of a similarity to one layer in the standard model.
10. `Similarly`, models with both movements are given the other name, `since` they resemble the other layer.
11. `Recently`, work has combined the two.

**Why it works:** The history is ordered by what each model added. The naming paragraph says where two names come from, which clears a confusion that the literature leaves open.  
**Sentence link:** The assumptions in sentence 2 are the ones relaxed in sentences 3, 5, and 6. `Similarly` shows that the second name follows the same logic as the first.  
**Transferable rule:** Order a model history by the assumption each model relaxes, and explain the origin of names that readers confuse.  
**Reusable pattern:** `Assuming that A and B, Author (year) developed X for the simplest case. Other cases were also considered (sources). In addition to A, C has also been treated (source). ... In practice, models considering only A are usually termed N1. This is because D. Similarly, models considering both A and C are usually termed N2 since E.`  
**Risk when misused:** `It is worth addressing` in the source is unidiomatic; use `It is worth noting that` or start with the point.  
**Skill-ready instruction:** Keep the reason for a conventional name when the name could mislead.

## P05-C15

**Source pointer:** p. 6, §2.3.2, sentences 1-5  
**Section:** Theory  
**Function tag:** GAP + LNK  
**Score:** 9/10  
**Use status:** caution  
**Reader mark:** note: `gap`, weakness of earlier work on this model

**Local context:** A second, local gap inside the theory section.  
**Sentence-by-sentence moves:**
1. What the model assumes.
2. For the material of interest, `it seems more natural` to use this model than the alternative.
3. `This is because` experiments indicate what controls the measured time.
4. `Few` theoretical works treat the single-element case.
5. Equations for the other geometry have been used by swapping one variable, `but` without physical justification.

**Why it works:** The preference is hedged and supported by experiments. The gap is exact: what has been done instead, and what that practice lacks.  
**Sentence link:** `This is because` gives the evidence for the hedged preference. Sentence 5 explains what researchers do in the absence stated by sentence 4.  
**Transferable rule:** A local gap can be stated as: preferred model, evidence, little theory, the workaround in use, and what the workaround lacks.  
**Reusable pattern:** `For M, it seems more natural to use X rather than Y. This is because experiments have indicated that A is controlled by B rather than C (sources). Few theoretical studies have modeled D. Equations developed for Y have been used for X by replacing E with F (source), but no physical justification is provided.`  
**Risk when misused:** The source writes `Few theoretical works have been done`; prefer `Few theoretical studies have`. If the paper then uses the same workaround, as this one does, it must say so openly (see P05-S29).  
**Skill-ready instruction:** Do not strengthen `few` to `no`, and keep the stated weakness of a workaround even when the author adopts it.

## P05-C16

**Source pointer:** p. 6, §2.3.3 final paragraph, sentences 1-6  
**Section:** Theory  
**Function tag:** CON + LNK  
**Score:** 10/10  
**Use status:** positive

**Local context:** Closes the background by matching models to materials. It prepares the choice made in the method.  
**Sentence-by-sentence moves:**
1. The models above have been used to explain a property of many materials.
2. `For` material class 1, `it is intuitive to` apply model A, `because`.
3. `For` class 2, `it seems still reasonable`, `although` one feature is treated incorrectly.
4. `For` class 3, `it is however questionable`.
5. `Instead`, models B and C `seem more appealing because` they fit a more realistic geometry.
6. `In addition`, recent interest in one of them for a practical estimate.

**Why it works:** The fit is graded in three steps (`intuitive`, `still reasonable`, `questionable`), each with its reason. The reader reaches the paper's choice without being told that the other model is wrong.  
**Sentence link:** Three sentences open with `For` + material, so the grading is easy to follow. `Instead` moves from the rejected fit to the preferred one.  
**Transferable rule:** When choosing among models, grade their suitability for each case, and give a reason for each grade.  
**Reusable pattern:** `For A, it is intuitive to apply X because B. For C, it still seems reasonable to apply X, although D. For E, however, it is questionable to F. Instead, Y and Z seem more appealing because G.`  
**Risk when misused:** Graded words are judgments. Each needs its reason in the same sentence.  
**Skill-ready instruction:** Keep the graded wording of suitability; do not flatten it to `suitable` and `unsuitable`.

## P05-C17

**Source pointer:** p. 6-7, §3 opening paragraph  
**Section:** Methods  
**Function tag:** MAP + MET  
**Score:** 10/10  
**Use status:** positive

**Local context:** A one-paragraph overview of the whole method before the steps. P05-S06 records the last sentence.  
**Sentence-by-sentence moves:**
1. `In this section, we propose` the method, with its figure.
2. `In particular`: what it includes.
3. `To reduce` the cost, one process is `not` simulated from first principles.
4. `Instead`, its effect is calculated with two simpler models on a simplified geometry.
5. The result is `then` transferred to one phase, and the governing equation is solved in a representative volume.
6. The volume holds the real geometry `so that` the other process is represented reliably.
7. Pointer to the figure and the details.

**Why it works:** The design decision and its reason are given before any detail, in the form purpose, what is avoided, what is done in its place.  
**Sentence link:** `Instead` answers the negative statement before it. `then` orders the remaining steps. The `so that` clause explains why real geometry is kept.  
**Transferable rule:** Open a method section with its design in miniature: what it includes, the main simplification and why, and the order of operations.  
**Reusable pattern:** `In this section, we propose X for Y (Figure N). In particular, both A and B are considered. To reduce C, A is not modeled from first principles. Instead, D is calculated using E with F simplified as G. D is then H, and I is solved in J. J contains K so that B can be accounted for.`  
**Risk when misused:** An overview that repeats the Introduction's road map word for word wastes space.  
**Skill-ready instruction:** If a method starts with details, write one overview paragraph from the author's own steps and place it first.

## P05-C18

**Source pointer:** p. 7, §3.1 ¶1-2  
**Section:** Methods  
**Function tag:** MET + LNK  
**Score:** 10/10  
**Use status:** positive  
**Reader mark:** note: learn how to express "calculating a parameter": cite the established method, compare methods, say why the parameter matters, say what steps are needed

**Local context:** First method step. Explains which geometric properties are needed, why, and how they are obtained.  
**Sentence-by-sentence moves:**
1. `The first step ... is to determine` the properties, `by` the general operation.
2. `The properties of interest include` a list.
3. `One of the purposes ... is to` validate an earlier processing stage by comparison with experiment.
4. `In addition`, some properties are needed by a later calculation, `and thus` must be determined.
5. New paragraph: `While` some properties are easy to calculate, others `are not straightforward`.
6. `In this study, we use` an established family of algorithms, with citations (P05-S05).
7. Experimental data `can also be used`, `but` they involve assumptions that may not hold for some materials.

**Why it works:** The reader learns what is needed, the two reasons, which part is hard, what is used, and why the alternative is weaker. The algorithm itself is left to the citations.  
**Sentence link:** `this step` and `these properties` keep the topic fixed. The hard item in sentence 5 is what the algorithms in sentence 6 determine. Sentence 7 gives the alternative only after the choice is made.  
**Transferable rule:** To describe obtaining a parameter, give what, why (two reasons at most), where the difficulty is, the established method with citations, and the alternative with its drawback.  
**Reusable pattern:** `The first step is to determine X by analyzing Y. The properties of interest include A, B, and C. One purpose of this step is to validate D. In addition, A and B are needed in E, and thus they have to be determined. While F is relatively easy to calculate, the determination of A is not straightforward. In this study, we use G (sources) to determine these properties. H can also be used, but additional assumptions are involved, which may not be valid for I.`  
**Risk when misused:** Citing an algorithm without any settings can be too little for reproduction; add settings when the result depends on them.  
**Skill-ready instruction:** For a parameter paragraph, check that it answers what, why, how, and why not the alternative. Ask the author for any missing part.

## P05-C19

**Source pointer:** p. 7-8, §3.2  
**Section:** Methods  
**Function tag:** DEF + MET  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** note: important; do not confuse the real part with surface conduction

**Local context:** Defines the output of the models, prevents a likely confusion, then builds the total response.  
**Sentence-by-sentence moves:**
1. The output of most models is a named complex quantity, with unit, and it is `only a perturbation` that the process causes.
2. `If no` process occurs, both parts are zero.
3. The imaginary part measures one thing. 4. The real part is related to another and vanishes at the zero-frequency limit.
5. `Thus`, the real part `should not be confused with` a similar-looking quantity that exists even at that limit.
6. New paragraph: `As discussed`, the geometry is assumed to be a network.
7. Model 1 `can be applied to determine` the response of individual elements.
8. The individual contributions `can then be convolved with` the size distribution.
9. `Similarly`, model 2 for the other element, with its own distribution.
10. The superposition of the two gives the total.

**Why it works:** The limiting case (nothing happens, so the quantity is zero) makes the meaning of the quantity plain. The warning sentence prevents a specific error.  
**Sentence link:** The limiting case supports the warning. In the second paragraph, `individual contributions` restates the previous output, and `Similarly` reuses the same two steps for the second model.  
**Transferable rule:** Define a derived quantity through its limiting case, and warn the reader against the nearest confusable quantity.  
**Reusable pattern:** `The output of X is Q (in unit), which is only a perturbation that P causes. If no P occurs, both parts of Q are zero. ... Thus, Q' should not be confused with R, which exists even at S. ... The individual contributions can then be convolved with the distribution f to obtain the overall response. Similarly, ...`  
**Risk when misused:** Warning sentences should be rare, and each should name the confusable quantity.  
**Skill-ready instruction:** Keep limiting-case sentences and `should not be confused with` sentences; they carry meaning that concision edits often delete.

## P05-C20

**Source pointer:** p. 8, §3.3 ¶1-3  
**Section:** Methods  
**Function tag:** MET + LNK  
**Score:** 10/10  
**Use status:** caution  
**Reader mark:** note: the end restates how the upscaling is done and why this type is used here

**Local context:** The key step of the method: converting an interface quantity to a volume quantity, and choosing between two ways of doing it.  
**Sentence-by-sentence moves:**
1. Where the induced effect is located in the models.
2. `To include them in` the simulation, `we suggest` converting quantity A (unit) to quantity B (unit), which is added to one phase.
3. `That is`, a plain restatement: the phase gains an extra value.
4. The conversion equation, with the characteristic length defined after it.
5. `For` simple geometries, the length is analytical. 6. `For example`, one case. 7. `For complex` geometries, `however`, it must be computed from its definition.
8. `To calculate` it, what must be solved.
9. New paragraph: such a conversion is common in the field.
10. `In general, there are two ways`: named.
11. Way 1 has long been used for one material, `for which` it is safe, `because` of where the dipole lies.
12. `However, for` the present material, the dipole lies elsewhere, `and hence it is logical to use` way 2, with a pointer back to the equation.

**Why it works:** The step is stated, restated in plain words, quantified, and then justified against the alternative. The justification returns to the physical location named in sentence 1.  
**Sentence link:** `That is` introduces the plain restatement. The last sentence repeats the location from sentence 1 and the equation number from sentence 4, so the paragraph closes on its own start.  
**Transferable rule:** For the central step of a method, give the operation, a plain restatement, the equation, how its parameter is obtained, and why this variant is used.  
**Reusable pattern:** `To include X in Y, we suggest converting A (in unit 1) to B (in unit 2), which is added to C. That is, C gains an extra B in addition to its own value. ... For simple geometries, L can be determined analytically. For complex geometries, however, L needs to be determined numerically from its definition. ... In general, there are two ways to do this: W1 and W2. W1 has long been used for M1 because D. However, for M2, E, and hence it is logical to use W2, that is, Equation N.`  
**Risk when misused:** `we suggest to upscale` in the source is not standard; write `we suggest upscaling` or `we propose to upscale`.  
**Skill-ready instruction:** End the paragraph on the reason for the chosen variant, and tie it back to the equation by number.

## P05-C21

**Source pointer:** p. 9, §3.4  
**Section:** Methods  
**Function tag:** MET + LNK  
**Score:** 8/10  
**Use status:** positive

**Local context:** Assigns properties to each phase and states how the effective value is computed.  
**Sentence-by-sentence moves:**
1. Phase 1 is usually nonconductive, `and thus` its complex property has only one component, defined with `where`.
2. Phase 2 has both components. 3. `While` one component is X, the other is Y, defined with `where`.
4. `After` the previous step, phase 2 `now has` an apparent value.
5. The simulation `can be conducted by solving` a named equation in the volume.
6. After the equation: the symbol's meaning, and its value in each phase.
7. `In the simulation`, a gradient is applied and two fields are determined. 8. A third field follows. 9. `Then`, the effective property is determined, with the averaged quantities defined.

**Why it works:** One phase per sentence, then the change produced by the previous step, then the equation, then the order of computation.  
**Sentence link:** `After` + the previous step and the word `now` connect this subsection to the one before. `Then` marks the final output.  
**Transferable rule:** Assign inputs phase by phase, and connect each method subsection to the previous one with a short phrase about what has changed.  
**Reusable pattern:** `A is usually P, and thus its X has only Q, that is, R, where S is ... B has both Q and T. After step N, B now has an apparent X. The simulation can be conducted by solving the L equation in V. ... In the simulation, G is applied across V, and the distributions of H and I are determined. Then, the effective X can be determined as ...`  
**Risk when misused:** None beyond keeping every symbol definition.  
**Skill-ready instruction:** Keep the phrase that connects a method step to the result of the previous step.

## P05-C22

**Source pointer:** p. 9-10, §4 opening and §4.1 ¶1-3  
**Section:** Methods  
**Function tag:** MET  
**Score:** 9/10  
**Use status:** caution

**Local context:** Introduces the test sample, how its geometry was extracted, and how it was measured.  
**Sentence-by-sentence moves:**
1. The sample is selected `to demonstrate the use of` the method. 2. Experiments were `also` conducted over a stated range. 3. The section's content is announced.
4. Basic properties with values, each with `as determined by` its method.
5. Composition from earlier studies. 6. The image and its resolution. 7. One further parameter with its method and source.
8. New paragraph: `To determine` the statistical properties, the pore space `is assumed as` a simple structure.
9. `Here, we use the algorithm developed by` named authors. 10. `The results include` two distributions with figure parts.
11. `These ... will be used later to` calculate a named quantity.
12. New paragraph: the sample state and the two instruments.
13. `For frequencies lower than` a value: instrument, method, electrodes. 14. `For the frequency` range above: probe and analyzer. 15. Results are in a figure.

**Why it works:** Every value has its method attached in the same clause. The measurement description is organized by frequency range, the same variable that organizes the results.  
**Sentence link:** `These` + noun in sentence 11 says what the extracted data are for, connecting this section to the method step that needs them.  
**Transferable rule:** Attach to each reported property the way it was determined, and organize measurement descriptions by the variable that organizes the results.  
**Reusable pattern:** `The porosity of the sample is A, and the surface area is B as determined by C. ... To determine D, the pore space is assumed to be E. Here, we use the algorithm developed by F to extract G. These properties will be used later to calculate H. For frequencies lower than I, X was measured by J with K. For frequencies between L and M, X was measured with N.`  
**Risk when misused:** The source has agreement slips in this passage and uses `assumed as`; write `assumed to be`.  
**Skill-ready instruction:** Do not separate a value from the method that produced it.

## P05-C23

**Source pointer:** p. 10-12, §4.2  
**Section:** Methods  
**Function tag:** MET + ASS  
**Score:** 9/10  
**Use status:** caution  
**Reader mark:** several parameter-source sentences underlined; a reader question beside the modified model

**Local context:** Gives the settings of the simulation, with the source or check for each value.  
**Sentence-by-sentence moves:**
1. The effective property was `also` calculated by solving two numbered equations. 2. The image used and the frequency range.
3. Values for each phase, one clause per phase, joined by a semicolon.
4. Both mechanisms are considered. 5. `For` mechanism 1, a named model `is used to calculate` the quantity.
6. `Note that` the equations `are modified from` the original `by replacing` one variable with another.
7. `In our simulation`, a value, `which corresponds to` a typical physical quantity.
8. `For` mechanism 2, `we use` a named model. 9. Its output is a different quantity.
10. `Note that` this quantity `also contains` a component not affected by the mechanism.
11. `To determine` the wanted quantity, that component `needs to be subtracted`.
12. A value, `which is close to the value reported in` a source.
13. Another value, `which is consistent with` a related quantity under a named relation.
14. The code and its origin, the numerical method, and the grid size.
15. A table summarizes the values.
16. `We emphasize that` the models are used for demonstration only. 17. Other models may also be used.

**Why it works:** No value stands alone: each is tied to a typical quantity, a published value, or a consistency relation. The modification to a published model is stated openly, and the last two sentences keep the method independent of the particular models.  
**Sentence link:** `For` + mechanism opens each block, so the two blocks are parallel. `Note that` introduces what the reader must know before using each model's output.  
**Transferable rule:** Give every parameter value a justification clause, state modifications to borrowed models openly, and separate the method from the particular models used to demonstrate it.  
**Reusable pattern:** `For A, the model of B is used to calculate C. Note that Equations i and j are modified from B by replacing D with E. In our simulation, F is V1, which corresponds to G. H is V2, which is close to the value reported in I. J is V3, which is consistent with K under the L equation. We emphasize that the models used here are for demonstration only. Other models may also be used.`  
**Risk when misused:** The source has a wrong equation cross-reference in this passage and the phrase `if consider`. Check every equation number against the equation it should cite, and write `according to`. A reader also asked why a model for one geometry is used for another; the borrowed-model sentence should give its reason or point to where the weakness is acknowledged.  
**Skill-ready instruction:** Flag any parameter value that has no source, typical range, or consistency check as `author-confirm`. Verify cross-references.

## P05-C24

**Source pointer:** p. 12-13, §5.1 ¶1-2  
**Section:** Results  
**Function tag:** RES + LNK  
**Score:** 10/10  
**Use status:** caution  
**Reader mark:** note: the simulated value is smaller because nanometer-scale features are not resolved

**Local context:** First results subsection. P05-S09 records the cautious explanation sentence; this chain records the full order.  
**Sentence-by-sentence moves:**
1. What is shown in the figure.
2. `For` the low range, where the measured data come from. 3. `In` the high range, how the plotted data were calculated. 4. A correction added, with its reason and value.
5. New paragraph: `A comparison of` the two `shows that` the simulation follows the general trend, `especially for` a stated range.
6. `When` the frequency is above a value, both increase, due to a named process, with a forward reference.
7. `However`, the size of the increase in one is a stated value, much smaller than the other's stated value.
8. `This discrepancy might be due to` a resolution limit.
9. `Since` the process is associated with a feature, ignoring that feature underestimates the quantity.

**Why it works:** The data's origin comes first. Then the paragraph gives agreement with its range, the common feature, the difference with both numbers, a tentative cause, and the mechanism that makes the cause plausible.  
**Sentence link:** `However` keeps the same frequency range and turns from the shared trend to the difference. `This discrepancy` names the difference. The final `Since` sentence links the proposed cause to the direction of the error.  
**Transferable rule:** Compare model and data as: agreement and its range, shared feature, difference with numbers, tentative cause, and why that cause gives an error in this direction.  
**Reusable pattern:** `A comparison of A and B shows that A follows the general trend of X, especially for C. When D, both A and B increase due to E (discussed in Section N). However, the increase in A is only about V1, much smaller than that in B (about V2). This discrepancy might be due to F. Since E is associated with G, ignoring G underestimates H.`  
**Risk when misused:** The source writes `due to fact that` and `(will be discussed in ...)`. Use `due to the fact that` or `because`, and `(discussed in Section N)`.  
**Skill-ready instruction:** Never report a discrepancy without its size when the numbers are available. Keep the cause tentative and add the direction-of-error sentence only if the author supplied the mechanism.

## P05-C25

**Source pointer:** p. 13, §5.2 ¶1-2  
**Section:** Results  
**Function tag:** RES + LNK  
**Score:** 10/10  
**Use status:** caution

**Local context:** Reads one spectrum from high to low frequency, reporting agreement and disagreement range by range.  
**Sentence-by-sentence moves:**
1. What is shown. 2. `It is observed that` the quantity varies over several orders of magnitude.
3. `At` the highest range: nearly constant, with one value for experiment and one for simulation.
4. `These` values are close to a reference value, `implying that` no polarization occurs there.
5. `When the frequency is decreased to` a value: the experiment shows an increase, with a value and a cause.
6. `However`, this increase was not observed in the simulation.
7. `As the frequency is further decreased`: the two agree well and both rise, with a cause.
8. `When the frequency is lower than` a value: large differences.
9. New paragraph: a second plot of the same data. 10. `Note that` the two plotted quantities are related, with the relation. 11. How to read the plot. 12. The statements above `also hold for` the second plot.

**Why it works:** The frequency axis is the organizing principle: every sentence starts with a range and moves in one direction. Agreement and disagreement alternate honestly, range by range.  
**Sentence link:** Sentence openers are the ranges, in order (`At`, `When ... decreased to`, `As ... further decreased`, `When ... lower than`). The last sentence saves a paragraph by transferring the discussion to the equivalent plot.  
**Transferable rule:** Describe a curve by walking along its axis in one direction, opening each sentence with the range.  
**Reusable pattern:** `At A, X is nearly constant, about V1 for the experiment and V2 for the simulation. These values are close to R, implying that S. When the frequency is decreased to B, the experimental spectrum shows an increase in X due to C. However, the increase was not observed in the simulation. As the frequency is further decreased, the two spectra agree well. When the frequency is lower than D, large discrepancies are observed. ... Our discussion of X in Figure Na also holds for Y in Figure Nb.`  
**Risk when misused:** The source has `varies over several orders`, `increase sharply`, and three repeated forward-reference parentheses. Write `orders of magnitude`, keep `sharply` only if the plot shows it, and use one forward reference.  
**Skill-ready instruction:** When a results paragraph jumps around a plot, reorder its sentences along the axis and keep every range and number.

## P05-C26

**Source pointer:** p. 13-15, §5.3 ¶1-4  
**Section:** Results  
**Function tag:** RES + IMP  
**Score:** 10/10  
**Use status:** caution  
**Reader mark:** note: the key finding (a process omitted in earlier studies explains their underestimate); extended discussion and comparison with the literature; an important mechanism

**Local context:** Separates the contribution of each process and explains each remaining mismatch. P05-S08 records one comparison sentence.  
**Sentence-by-sentence moves:**
1. `To identify` each contribution, simulations with one process at a time were `also` conducted.
2-3. `In simulating` process A / B: what is assigned to each phase. 4. Other settings are as in the table. 5. Where the results are shown.
6. New paragraph, process A: similar to experiment in two plateaus (P05-S08).
7. The characteristic frequency `is, however, different`, with both values.
8. `One possible explanation ... is that` the images are smoother than the sample, `and thus` a fine-scale contribution could be missed.
9. `Thus`, the direction of the shift.
10. New paragraph, process B: it `seems to` affect a broad range, dominating around a value.
11. `If` it `is not accounted for`, the other two together underestimate the property in a stated range.
12. This underestimate has been reported in earlier studies that did not include B.
13. With all processes, the simulation agrees at that range.
14. `This implies that` B `could be a significant contributor`.
15. New paragraph, process C: at low frequency `it appears that` C dominates.
16. The affected range is narrower than in the experiment. 17. Below a value, the simulation is low.
18. `This could be because` the image covers a small volume, and larger elements may be missed.

**Why it works:** One paragraph per process, in frequency order. Each paragraph has result, mismatch, and tentative cause. The key finding in the middle paragraph is built from a counterfactual, a link to earlier studies, the full result, and a hedged implication.  
**Sentence link:** Each paragraph opens with the process name and its place in the figure. `If not accounted for` leads to the underestimate, the underestimate leads to the earlier studies, and `This implies` draws the conclusion.  
**Transferable rule:** To show that a component matters, report what happens without it, connect that to earlier work that lacked it, show the full result, and state the implication with a modal.  
**Reusable pattern:** `To identify the contribution of each X, we also conducted simulations that consider one X at a time. ... If B is not accounted for, the combination of A and C underestimates Y at D. This underestimate has been reported in earlier studies that did not consider B (source). With all X included, the simulated Y agrees with the experiment at D. This implies that B could be a significant contributor to Y.`  
**Risk when misused:** The source has `Comparing to` and `considerably low`; write `Compared with` and `considerably lower`. The implication is the paper's main finding and still uses `could`; do not strengthen it.  
**Skill-ready instruction:** Keep the counterfactual sentence and the link to earlier studies; they are the evidence for the claim. Keep every hedge.

## P05-C27

**Source pointer:** p. 15, §5.4 ¶1-2  
**Section:** Discussion  
**Function tag:** IMP + LNK  
**Score:** 8/10  
**Use status:** caution

**Local context:** Two paragraphs on what the method can be used for.  
**Sentence-by-sentence moves:**
1. The method `can be used to` improve understanding and modeling of the property, tied to the need stated in the Introduction.
2. `In particular`, what it is `well suited for`.
3. `Also, because` models can be exchanged easily, it can be used to evaluate them. 4. `One example is` a specific comparison.
5. New paragraph: `Another application` is a second topic.
6. `Recently`, a related capability has become available. 7. `Thus`, realistic inputs can be generated.
8. `Coupled with` the method, signatures can be quantified and linked to changes.
9. `In this regard`, a closing statement of the method's value.

**Why it works:** Each use is specific and ends in an example or a named capability. The first sentence echoes the first paragraph of the paper.  
**Sentence link:** `In particular` narrows, `One example is` narrows again, `Another application` opens the second item.  
**Transferable rule:** State applications as specific uses with one example each, and tie the first one back to the need stated in the Introduction.  
**Reusable pattern:** `The proposed X can be used to improve the modeling of Y, which is essential in Z. In particular, X is well suited for studying A. Also, because B, X can be used to evaluate C. One example is D. Another application of X is to study E. ... Coupled with X, F can be quantified and linked to G.`  
**Risk when misused:** The source ends with `becomes an attractive way` and has `resulted from` for `resulting from`. Replace self-praise with the specific use.  
**Skill-ready instruction:** Limit application statements to uses that the method's demonstrated capabilities support.

## P05-C28

**Source pointer:** p. 15, §6 ¶1-3  
**Section:** Conclusions  
**Function tag:** CLO + LNK  
**Score:** 10/10  
**Use status:** caution  
**Reader mark:** note: the wording of the overall agreement is skilful; discrepancy sentences underlined

**Local context:** Three paragraphs: the method, the high-frequency comparison, and the intermediate and low-frequency findings. P05-S10 records one limitation sentence.  
**Sentence-by-sentence moves:**
1. `In this study, we developed` the method for the property over a range. 2. What it considers.
3. `To account for` one process, the geometric assumption. 4. `Then`, the models applied to each element, `so that` the effect can be quantified.
5. The quantity is `then` transferred to one phase. 6. The simulation `can then be conducted`. 7. `By doing so`, both processes can be considered.
8. New paragraph: the sample used. 9. `A comparison ... shows that` the spectra `in general agree very well` over the range.
10. `At` high frequencies: both show the same trend. 11. `However`, the characteristic frequency is much lower in the simulation.
12. `This discrepancy can be explained by` the smoother images. 13. `Thus`, what could be missed.
14. New paragraph: `At intermediate frequencies`: one process contributes significantly. 15. `If overlooked`, the result is much smaller.
16. `For frequencies lower than` a value: another process dominates. 17. `It seems that` the range is narrower than measured. 18. `In particular`, the lowest range is low. 19. `This may be due to` the small volume.

**Why it works:** The first paragraph retraces the method in its own order, and the other two retrace the results from high to low frequency. `in general` lets the paper claim agreement and still list three specific mismatches. No sentence adds a claim that the body does not contain.  
**Sentence link:** `Then` and `By doing so` carry the method paragraph. Range openers carry the results paragraphs in the same order as the body.  
**Transferable rule:** Write Conclusions as a compressed replay: method steps in order, overall agreement with a qualifier, then each main finding and each mismatch with its likely cause.  
**Reusable pattern:** `In this study, we developed X for Y. Both A and B are considered. To account for A, C is assumed. Then, D is applied so that E can be quantified. ... By doing so, both A and B can be considered. A comparison of F and G shows that the spectra in general agree very well between H and I. At J, ... However, K is much lower in the simulation. This discrepancy can be explained by L. ... This may be due to M.`  
**Risk when misused:** The source has `utilized`, `resulted from`, and `systemically low`; write `used`, `resulting from`, and `systematically low`. Do not let `in general agree very well` stand without the mismatches that follow it.  
**Skill-ready instruction:** If Conclusions claim general agreement, check that the specific mismatches reported in Results are still present.

## P05-C29

**Source pointer:** p. 1, Abstract, sentences 1-9  
**Section:** Abstract  
**Function tag:** LNK + AIM  
**Score:** 8/10  
**Use status:** caution  
**Reader mark:** the gap phrase and the two processes underlined

**Local context:** The abstract compresses the Introduction's eight paragraphs to four sentences before the aim.  
**Sentence-by-sentence moves:**
1. The methods are widely used. 2. `To correctly interpret` field data, what must be understood.
3. `Recently`, a tool has become available. 4. `However`, one thing is still difficult (P05-S01).
5. `In this study, we develop` the method, and what it enables (P05-S02).
6. The sample used. 7. The experiments used for comparison.
8. The agreement and what it supports. 9. `This work thus provides` a tool for a stated purpose.

**Why it works:** Sentences 1-4 are the first sentences of the Introduction's main moves. The abstract has the same order as the paper.  
**Sentence link:** `However` and `In this study` mark the turn to the gap and to the aim; `these` + noun in sentence 5 picks up the difficulty named in sentence 4.  
**Transferable rule:** Draft the abstract's opening from the Introduction's own topic sentences: need, requirement, tool, difficulty, aim.  
**Reusable pattern:** `X methods are widely used in F. To correctly interpret X data, it is essential to understand Y. Recently, T has become a tool for studying Y. However, it is still difficult to include Z in T. In this study, we develop a framework to consider Z in T, which enables the calculation of W. A sample of S is used to demonstrate the framework. The agreement between A and B supports C.`  
**Risk when misused:** Do not copy `for various purposes`, `powerful tool`, `utilized`, `valuable`, or `useful tool`. The source also has an agreement slip after `simulations, which`. The last two sentences state validation twice; one is enough.  
**Skill-ready instruction:** Build the abstract from the paper's topic sentences, then delete evaluative adjectives and duplicate claims.

## Sentence records

## P05-S11

**Source pointer:** p. 1, §1 ¶1, sentence 1  
**Section:** Introduction  
**Function tag:** BKG  
**Score:** 9/10  
**Use status:** positive

**Local context:** First sentence of the paper.  
**Why it works:** It names the method family, the field, and what is studied, and gives varied citations. It makes no claim of importance.  
**Sentence link:** The next sentence lists members of the family named here.  
**Transferable rule:** An opening sentence can simply say what is used, where, and for what.  
**Reusable pattern:** `X methods are frequently used in F to study A and B of C (sources).`  
**Risk when misused:** It needs citations that show the breadth claimed.  
**Skill-ready instruction:** Replace openings such as `X has attracted increasing attention` with a statement of use.

## P05-S12

**Source pointer:** p. 1, §1 ¶1, sentence 4  
**Section:** Introduction  
**Function tag:** BKG  
**Score:** 10/10  
**Use status:** positive  
**Reader mark:** underlined; noted as the broad background

**Local context:** Last sentence of the first paragraph; states the need behind the whole paper.  
**Why it works:** A purpose phrase gives the goal, the impersonal `one needs` gives the requirement, and `such as` names the controlling factors.  
**Sentence link:** Its object contains the two concepts that open the next two paragraphs.  
**Transferable rule:** State the motivation as what must be understood in order to do something practical.  
**Reusable pattern:** `To correctly interpret X, one needs a mechanistic understanding of Y and its controlling factors such as A and B (source).`  
**Risk when misused:** `mechanistic` should be kept only if the paper works with mechanisms.  
**Skill-ready instruction:** Prefer a purpose-plus-requirement sentence to a sentence that only says a topic is important.

## P05-S13

**Source pointer:** p. 1, §1 ¶2 sentence 1; ¶3 sentence 1  
**Section:** Introduction  
**Function tag:** DEF  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** underlined

**Local context:** Two paragraph openers that define the two central properties.  
**Why it works:** Each defines a property by what the material can do, in under fifteen words, and the two have the same form.  
**Transferable rule:** Define a property functionally, by the ability it measures.  
**Reusable pattern:** `X quantifies a material's ability to do A. ... Y is associated with a material's ability to do B (i.e., C).`  
**Risk when misused:** A functional definition is not a formal one; give the formal definition where the equations start.  
**Skill-ready instruction:** Use functional definitions in the Introduction and formal ones in Theory or Methods.

## P05-S14

**Source pointer:** p. 1, §1 ¶2, sentence 2  
**Section:** Introduction  
**Function tag:** BKG  
**Score:** 8/10  
**Use status:** positive  
**Reader mark:** underlined; noted as basic knowledge

**Local context:** Gives a typical value and the simplification that follows from it.  
**Why it works:** The number justifies the simplification in the same sentence.  
**Transferable rule:** Justify a standard simplification with an order-of-magnitude value.  
**Reusable pattern:** `For A (e.g., B), X is of the order of V (source), and thus A is usually considered C.`  
**Risk when misused:** Write `of the order of`, not `in the order of`.  
**Skill-ready instruction:** Keep typical values that support a simplification.

## P05-S15

**Source pointer:** p. 1, §1 ¶3, sentences 2-3  
**Section:** Introduction  
**Function tag:** CON  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** underlined

**Local context:** Contrasts the phases with the whole material.  
**Why it works:** The two sentences share a structure, and `however` comes after the subject, so the contrast falls on the predicate.  
**Sentence link:** The second sentence's subject adds one modifier to the first's, which shows exactly what has changed.  
**Transferable rule:** In a contrast pair, keep the subjects parallel and place `however` after the second subject.  
**Reusable pattern:** `The X of A and B is usually constant at C. The effective X of M, however, depends on D and may differ significantly from E.`  
**Risk when misused:** Mid-sentence `however` needs commas on both sides.  
**Skill-ready instruction:** When several sentences begin with `However`, move some to the position after the subject.

## P05-S16

**Source pointer:** p. 2, §1 ¶3, sentence 5  
**Section:** Introduction  
**Function tag:** MAP  
**Score:** 8/10  
**Use status:** positive

**Local context:** Names mechanisms and defers their explanation.  
**Why it works:** A short relative clause tells the reader where the detail is, so the Introduction stays short.  
**Transferable rule:** Name a topic in the Introduction and point to the section that explains it.  
**Reusable pattern:** `Several mechanisms have been proposed to explain X, including A (source) and B (source), both of which are reviewed in Section N.`  
**Risk when misused:** More than one or two such pointers make the Introduction read like a table of contents.  
**Skill-ready instruction:** Move mechanism detail out of the Introduction and leave a single pointer.

## P05-S17

**Source pointer:** p. 2, §1 ¶5, sentence 3  
**Section:** Introduction  
**Function tag:** BKG  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** underlined

**Local context:** Describes the best-known model.  
**Why it works:** `probably` hedges the ranking, and the relative clause says exactly what the model relates, with the condition for each variant in parentheses.  
**Transferable rule:** Describe a cited model by the variables it connects and the form of the connection.  
**Reusable pattern:** `The most widely used model is probably M (source), which relates X to Y through a power function of A (condition 1) or B (condition 2).`  
**Risk when misused:** Superlatives without a hedge invite challenge.  
**Skill-ready instruction:** Replace `X proposed a model` with what the model relates.

## P05-S18

**Source pointer:** p. 2, §1 ¶6, sentence 2  
**Section:** Introduction  
**Function tag:** GAP  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** underlined and highlighted

**Local context:** States which part of a factor is under-studied.  
**Why it works:** Both parts are glossed in parentheses with concrete examples, and the reason for the imbalance closes the sentence.  
**Transferable rule:** State an imbalance in the literature with examples of each side and the reason.  
**Reusable pattern:** `While the effect of A (e.g., a1 and a2) has been extensively studied (source), the influence of B (e.g., b1 and b2) is less explored because C is difficult.`  
**Risk when misused:** Without the reason, the sentence is a bare novelty claim.  
**Skill-ready instruction:** Ask for the reason behind `less explored` and attach it.

## P05-S19

**Source pointer:** p. 2, §1 ¶6, sentences 4-5  
**Section:** Introduction  
**Function tag:** DEF  
**Score:** 8/10  
**Use status:** positive

**Local context:** Explains what the tool does and what that allows.  
**Why it works:** One sentence gives inputs and outputs; the next gives the benefit, with `allow us to explore`, which does not overclaim.  
**Sentence link:** The tool is repeated in plural with `Such`, so the second sentence opens on known ground.  
**Transferable rule:** Introduce a tool by its input and output, then by what it lets the researcher do.  
**Reusable pattern:** `In a T, both A and B can be calculated from C. Such simulations allow us to explore possible relationships between D and E.`  
**Risk when misused:** `allow us to` should not become `reveal`.  
**Skill-ready instruction:** Describe tools by input, output, and use.

## P05-S20

**Source pointer:** p. 2, §1 ¶7, sentence 2  
**Section:** Introduction  
**Function tag:** GAP  
**Score:** 10/10  
**Use status:** positive  
**Reader mark:** underlined

**Local context:** The physical reason behind the gap.  
**Why it works:** `This is because` announces the reason, and the parenthetical gives the scale as a number.  
**Sentence link:** `This` refers to the difficulty just stated. The thin layer at the end is the reason for the next sentence's fine discretization.  
**Transferable rule:** Follow a statement of difficulty with its physical reason, including the scale.  
**Reusable pattern:** `This is because X is associated with A occurring in a very thin B (typically V) near C.`  
**Risk when misused:** `This is because` three times in one section becomes a tic.  
**Skill-ready instruction:** Where a difficulty has a scale, state the scale.

## P05-S21

**Source pointer:** p. 2, §1 ¶7, sentences 4-5  
**Section:** Introduction  
**Function tag:** GAP  
**Score:** 10/10  
**Use status:** positive  
**Reader mark:** highlighted; noted as research significance

**Local context:** The consequence and the need.  
**Why it works:** The fronted `Considering that` gives the second number, and the need is impersonal and specific about what the new method must do.  
**Sentence link:** `therefore` makes the need a conclusion of the two preceding sentences.  
**Transferable rule:** State the need as a consequence and say what a solution must be able to do.  
**Reusable pattern:** `Considering that A is relatively large (V), the cost of B is very high. It is therefore desirable to develop methods that can effectively include C in D.`  
**Risk when misused:** `extremely` needs the numbers that precede it.  
**Skill-ready instruction:** Write the need sentence after the reason, and never before it.

## P05-S22

**Source pointer:** p. 2-3, §1 ¶8, sentences 1-2  
**Section:** Introduction  
**Function tag:** AIM + ASS  
**Score:** 9/10  
**Use status:** positive

**Local context:** Objective and scope.  
**Why it works:** The objective is one clause. The scope sentence uses `only` and names two restrictions.  
**Transferable rule:** Follow the objective immediately with the scope.  
**Reusable pattern:** `The objective of this study is to develop such an X for Y. For simplicity, in this study, we only consider A made of B.`  
**Risk when misused:** Leaving the scope to the Methods makes the aim look broader than it is.  
**Skill-ready instruction:** Keep `only` in scope sentences.

## P05-S23

**Source pointer:** p. 3, §2.1 ¶1, sentence 2; and the `Note that` sentences on p. 5, p. 10, and p. 11  
**Section:** Theory / Methods  
**Function tag:** ASS  
**Score:** 8/10  
**Use status:** positive

**Local context:** Short notes that prevent a misreading.  
**Why it works:** Each `Note that` sentence carries one fact the reader needs at that point: a scope, a validity limit, a modification, or a hidden component.  
**Transferable rule:** Use `Note that` for one necessary clarification at the point of need.  
**Reusable pattern:** `Note that X here can be either A or B.` / `Note that Q also contains C, which is not affected by D.`  
**Risk when misused:** Frequent `Note that` weakens its signal; use it at most once per paragraph.  
**Skill-ready instruction:** Keep `Note that` sentences that state validity, scope, or modification.

## P05-S24

**Source pointer:** p. 4, end of §2.1  
**Section:** Theory  
**Function tag:** DEF  
**Score:** 9/10  
**Use status:** positive

**Local context:** Final sentences of the terminology subsection.  
**Why it works:** After the derivation, the two everyday terms are tied to exact symbols and equation numbers.  
**Transferable rule:** Close a definitions section by fixing which symbol each term means.  
**Reusable pattern:** `In this study, T1 refers to S1 in Equation i, and T2 refers to S2 in Equation j. For M, the effective T1 and T2 are denoted by S3 and S4, respectively.`  
**Risk when misused:** The terms must then be used with this meaning everywhere.  
**Skill-ready instruction:** After such a sentence, check the whole manuscript for consistent use of the terms.

## P05-S25

**Source pointer:** p. 4, §2.2, sentences 3-4  
**Section:** Theory  
**Function tag:** IMP  
**Score:** 9/10  
**Use status:** caution  
**Reader mark:** underlined; noted as the basic mechanism

**Local context:** Cause and effect of one mechanism.  
**Why it works:** A fronted `Because of` gives the cause, and the next sentence names the result and says what it does to the bulk property.  
**Sentence link:** The accumulated charge at the end of the first sentence is renamed as the subject of the second, with `that is` supplying the standard term.  
**Transferable rule:** Explain a mechanism as cause, local effect, named result, bulk consequence.  
**Reusable pattern:** `Because of the mismatch of A, B in the two phases is different, resulting in C at D. The induced E, that is, F, gives rise to an increase in G compared with H.`  
**Risk when misused:** Write `compared with`, not `if compared to`.  
**Skill-ready instruction:** Keep mechanism sentences in causal order.

## P05-S26

**Source pointer:** p. 4, §2.3 ¶1, sentences 3-5  
**Section:** Theory  
**Function tag:** DEF  
**Score:** 8/10  
**Use status:** caution

**Local context:** Describes a two-part structure.  
**Why it works:** One sentence announces two parts, and the next two each open with the location of one part.  
**Transferable rule:** Describe a layered or multi-part structure by announcing the number of parts, then one sentence per part opening with its location.  
**Reusable pattern:** `The standard X model (source) describes the structure of Y as two layers. In the inner layer (A), B. In the outer layer, C, and the D equation can be used to describe E.`  
**Risk when misused:** The source has `immobile in relative to`; write `immobile relative to`.  
**Skill-ready instruction:** Open each part's sentence with the part's name or location.

## P05-S27

**Source pointer:** p. 4, §2.3 ¶2, sentences 2-3  
**Section:** Theory  
**Function tag:** DEF  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** the named term highlighted

**Local context:** Explains an effect and then gives it its standard name.  
**Why it works:** The effect is explained first. The name follows in an appositive, with the materials in which it has been observed.  
**Sentence link:** The increase stated at the end of the first sentence is the subject of the second.  
**Transferable rule:** Explain first, name second.  
**Reusable pattern:** `Because A is considerably higher than B, X is enhanced. The increase, known as N, has been observed in many materials, including C (sources) and even D (source).`  
**Risk when misused:** Naming before explaining forces the reader to hold an undefined term.  
**Skill-ready instruction:** Where a term appears before its explanation, reverse the order if the paragraph allows it.

## P05-S28

**Source pointer:** p. 4, §2.3 ¶2, sentence 6  
**Section:** Theory  
**Function tag:** DEF  
**Score:** 8/10  
**Use status:** positive  
**Reader mark:** the term highlighted

**Local context:** Introduces the paper's own collective term.  
**Why it works:** The sentence says what the process is related to and limits the term to `in this paper`.  
**Transferable rule:** When the paper uses a collective term of its own, say so and give its basis.  
**Reusable pattern:** `This process is related to A occurring near B and thus is termed N in this paper.`  
**Risk when misused:** Write `termed N`, not `termed as N`.  
**Skill-ready instruction:** Mark paper-specific terms with `in this paper` at first use.

## P05-S29

**Source pointer:** p. 10, §4.2, the sentence after the relaxation-time equation  
**Section:** Methods  
**Function tag:** ASS  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** highlighted; a reader question beside it

**Local context:** Discloses that a published model is used in modified form.  
**Why it works:** One sentence states that the equations are modified and exactly how.  
**Sentence link:** It answers the local gap in P05-C15: the paper uses the workaround it has just described as unjustified, and it says so.  
**Transferable rule:** State every modification to a borrowed model, and name the variable changed.  
**Reusable pattern:** `Note that Equations i and j are modified from Author (year) by replacing A with B.`  
**Risk when misused:** Disclosure is not justification. Where the modification affects the results, add the reason or acknowledge the weakness.  
**Skill-ready instruction:** If a manuscript uses a model outside its original setting, check that it says so.

## P05-S30

**Source pointer:** p. 10, §4.2, the sentence giving the surface conductance value; p. 12, the sentences giving the polarizability and the diffusion coefficient  
**Section:** Methods  
**Function tag:** MET  
**Score:** 10/10  
**Use status:** caution  
**Reader mark:** underlined

**Local context:** Three parameter values, each with a justification clause.  
**Why it works:** Three different justifications are used: correspondence to a typical physical quantity, closeness to a published value, and consistency with another parameter under a named relation.  
**Transferable rule:** Give each chosen value one of three supports: typical, published, or consistent.  
**Reusable pattern:** `X is V1, which corresponds to a typical A of B.` / `X used in the calculation is V2, which is close to the value (V3) reported in C.` / `X was V4, which is consistent with D according to the E equation.`  
**Risk when misused:** The source writes `if consider`; use `according to` or `based on`.  
**Skill-ready instruction:** When a value has no support clause, ask the author which of the three applies.

## P05-S31

**Source pointer:** p. 11, §4.2, sentences after the pore-throat relaxation-time equation  
**Section:** Methods  
**Function tag:** MET  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** underlined

**Local context:** Removes a component before using a model's output.  
**Why it works:** The fact comes first, then the purpose, then the operation and its equation.  
**Sentence link:** The component named at the end of the first sentence is the thing subtracted in the second.  
**Transferable rule:** Before a correction, state what the raw output contains and why that part must be removed.  
**Reusable pattern:** `Note that Q also contains A, which is not influenced by B. To determine the B-induced C, A needs to be subtracted, which gives ...`  
**Risk when misused:** None, if the equation follows.  
**Skill-ready instruction:** Keep the reason for each correction next to it.

## P05-S32

**Source pointer:** p. 12, §4.2, final two sentences  
**Section:** Methods  
**Function tag:** ASS  
**Score:** 9/10  
**Use status:** positive

**Local context:** Separates the method from the models chosen to demonstrate it.  
**Why it works:** Two short sentences. The second is five words long and states the generality without praise.  
**Transferable rule:** Say which parts of a demonstration are replaceable.  
**Reusable pattern:** `We emphasize that the X models used here are for demonstration only. Other models may also be used.`  
**Risk when misused:** `We emphasize` should be used once in a paper.  
**Skill-ready instruction:** Keep such statements short; do not expand them into claims of flexibility.

## P05-S33

**Source pointer:** p. 12, §4.2, the sentences on the code and grid  
**Section:** Methods  
**Function tag:** MET  
**Score:** 8/10  
**Use status:** positive  
**Reader mark:** underlined; noted as the source of the method

**Local context:** States the software used.  
**Why it works:** It gives the code's origin, that it was modified, the numerical method, and the grid.  
**Transferable rule:** For software, state origin, modification, numerical method, and discretization.  
**Reusable pattern:** `In this study, a standard code (name) developed at A was modified for the simulation. It uses the B method to solve Equation N, and a total of C cells was used to approximate D.`  
**Risk when misused:** `modified` should be followed somewhere by what was changed.  
**Skill-ready instruction:** Keep all four elements in software sentences.

## P05-S34

**Source pointer:** p. 13, §5.1 ¶1, last two sentences  
**Section:** Results  
**Function tag:** MET  
**Score:** 8/10  
**Use status:** positive

**Local context:** Explains a correction applied before plotting.  
**Why it works:** The reason comes first, then the correction, the resulting expression, and how the constant was chosen.  
**Transferable rule:** Explain any processing of measured data before the comparison that uses it.  
**Reusable pattern:** `Because A only accounts for B, C is also added, and thus X is equal to D (see Equation N). In this study, C is V, determined as the lowest measured E.`  
**Risk when misused:** Processing steps hidden in captions are easy to miss.  
**Skill-ready instruction:** Keep data-processing statements in the text next to the comparison.

## P05-S35

**Source pointer:** p. 13, §5.1 ¶2, sentence 3  
**Section:** Results  
**Function tag:** RES  
**Score:** 10/10  
**Use status:** positive

**Local context:** Reports the size of a mismatch.  
**Why it works:** Both magnitudes are in the sentence, so `much smaller` is supported.  
**Transferable rule:** Give both numbers when comparing magnitudes.  
**Reusable pattern:** `However, the magnitude of the increase in A is only about V1, which is much smaller than that in B (about V2).`  
**Risk when misused:** `only` is evaluative; keep it only when the ratio is large.  
**Skill-ready instruction:** Add the two values to any `much larger` or `much smaller`. If the values are missing, mark `author-confirm`.

## P05-S36

**Source pointer:** p. 13, §5.1 ¶2, final sentence  
**Section:** Results  
**Function tag:** IMP  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** underlined

**Local context:** Explains why the proposed cause gives an underestimate.  
**Why it works:** `Since` gives the established link, and the main clause gives the direction of the error.  
**Sentence link:** It follows the tentative cause recorded in P05-S09 and shows that the cause predicts the sign of the mismatch.  
**Transferable rule:** After a tentative cause, show that it predicts the direction of the mismatch.  
**Reusable pattern:** `Since A is associated with B, ignoring B in the simulation underestimates C and thus D.`  
**Risk when misused:** If the cause does not predict the direction, do not write this sentence.  
**Skill-ready instruction:** Check that a proposed cause is consistent with the sign of the discrepancy.

## P05-S37

**Source pointer:** p. 13, §5.2 ¶1, sentences 3-4  
**Section:** Results  
**Function tag:** RES + IMP  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** underlined

**Local context:** Reports a plateau and infers what it means.  
**Why it works:** Two values, a reference, and an inference with `implying that`.  
**Sentence link:** `These` + noun picks up the two values.  
**Transferable rule:** Interpret a value by comparing it with a known reference.  
**Reusable pattern:** `At A, X is nearly constant, about V1 for the experiment and V2 for the simulation. These values are close to R, implying that S in this range.`  
**Risk when misused:** `very close` with unequal values such as these needs the reference value shown.  
**Skill-ready instruction:** Keep the reference value in comparisons that support an inference.

## P05-S38

**Source pointer:** p. 13, §5.2 ¶2, final sentence  
**Section:** Results  
**Function tag:** LNK  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** underlined

**Local context:** Transfers a discussion to an equivalent plot.  
**Why it works:** One sentence replaces a repeated paragraph, and the sentences before it give the relation that makes the transfer valid.  
**Transferable rule:** When two plots show equivalent quantities, discuss one and state that the discussion holds for the other.  
**Reusable pattern:** `Our discussion of X in Figure Na also holds for Y in Figure Nb.`  
**Risk when misused:** Only valid when the two quantities are mathematically related.  
**Skill-ready instruction:** Remove duplicated descriptions of equivalent plots and add one transfer sentence.

## P05-S39

**Source pointer:** p. 13, §5.3 ¶1, sentence 1  
**Section:** Results  
**Function tag:** MET  
**Score:** 9/10  
**Use status:** positive

**Local context:** Introduces a further analysis.  
**Why it works:** The purpose phrase says why, and `one ... at a time` says exactly how.  
**Transferable rule:** Introduce an additional analysis by its purpose and its single change.  
**Reusable pattern:** `To identify the relative contribution of each X, we also conducted simulations that consider only one X at a time.`  
**Risk when misused:** None.  
**Skill-ready instruction:** Begin sentences about added analyses with their purpose.

## P05-S40

**Source pointer:** p. 13, §5.3 ¶2, sentences 2-4  
**Section:** Results  
**Function tag:** IMP  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** underlined

**Local context:** A difference in one feature, with a tentative explanation.  
**Why it works:** Both values are given. `One possible explanation` admits that there may be others, and `could be overlooked` keeps the mechanism tentative.  
**Sentence link:** `this discrepancy` names the difference. The last sentence ties the cause to the direction of the shift.  
**Transferable rule:** Offer an explanation as one of several possible ones when the study cannot test it.  
**Reusable pattern:** `The X where Y changes is, however, different: about V1 for A and V2 for B. One possible explanation for this difference is that C, and thus D could be overlooked in A. Thus, X of A shifts to E.`  
**Risk when misused:** Do not shorten `One possible explanation is` to `This is because`.  
**Skill-ready instruction:** Preserve `one possible explanation` when the cause is untested.

## P05-S41

**Source pointer:** p. 14, §5.3 ¶3, sentences 2-3  
**Section:** Results  
**Function tag:** CON  
**Score:** 10/10  
**Use status:** positive  
**Reader mark:** highlighted; noted as the key finding

**Local context:** A counterfactual and its link to earlier studies.  
**Why it works:** The counterfactual states what omitting the process does, in a stated range. The next sentence shows that this is what earlier studies without the process found.  
**Sentence link:** `The underestimation` turns the predicate of the first sentence into the subject of the second.  
**Transferable rule:** Compare with earlier work through the specific element those studies lacked and the specific result that follows.  
**Reusable pattern:** `If A is not accounted for, the combination of B and C will underestimate X at D (e.g., from V1 to V2). This underestimate has been reported in earlier studies that did not consider A (source).`  
**Risk when misused:** The earlier studies must really show that underestimate.  
**Skill-ready instruction:** State literature comparisons as specific, checkable differences.

## P05-S42

**Source pointer:** p. 14, §5.3 ¶3, final sentence  
**Section:** Results  
**Function tag:** IMP  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** underlined

**Local context:** The implication of the key result.  
**Why it works:** `implies` and `could be` together give the right strength for a result from one sample, and a citation shows agreement with earlier theory.  
**Transferable rule:** State the main implication with a modal when it rests on one sample.  
**Reusable pattern:** `This implies that A could be a significant contributor to X of M (source).`  
**Risk when misused:** Do not change `could be` to `is`.  
**Skill-ready instruction:** Keep the modal in implications drawn from a single case.

## P05-S43

**Source pointer:** p. 14-15, §5.3 ¶4, sentences 1-4  
**Section:** Results  
**Function tag:** RES + ASS  
**Score:** 8/10  
**Use status:** caution  
**Reader mark:** underlined; noted as an important mechanism

**Local context:** The low-frequency result and its limitation. P05-S10 records the matching sentence in the Conclusions.  
**Why it works:** Observation words (`it appears that`) are used for a visual reading of the plot, and the cause names the limited volume with its size.  
**Transferable rule:** Use `appears` or `seems` for readings of a plot, and state the size of what limits the model.  
**Reusable pattern:** `At A, it appears that B dominates over other C. Compared with the experimental data, the range affected by B is much narrower in the simulation. This could be because D only covers a small fraction of E (about V), and F may not be accounted for.`  
**Risk when misused:** The source has `Comparing to` and `considerably low`.  
**Skill-ready instruction:** Keep `appears` and `seems` where the statement is a reading of a figure.

## P05-S44

**Source pointer:** p. 15, §5.4 ¶1, sentences 3-4  
**Section:** Discussion  
**Function tag:** IMP  
**Score:** 8/10  
**Use status:** positive  
**Reader mark:** underlined

**Local context:** A use of the method, with an example.  
**Why it works:** The use follows from a property of the method, and the example is specific and cited.  
**Transferable rule:** Derive a stated application from a property of the method and give one example.  
**Reusable pattern:** `Also, because A can be easily included in X, it can be used to evaluate B. One example is to compare C and D (source) in E.`  
**Risk when misused:** `easily` should be true of the implementation.  
**Skill-ready instruction:** Attach one concrete example to each claimed application.

## P05-S45

**Source pointer:** p. 15, §6 ¶1, sentence 7  
**Section:** Conclusions  
**Function tag:** CLO  
**Score:** 9/10  
**Use status:** caution

**Local context:** Last sentence of the method summary.  
**Why it works:** `By doing so` gathers all the steps, and the two parentheticals give the origin of each process in a few words.  
**Transferable rule:** End a method summary with what the steps together achieve.  
**Reusable pattern:** `By doing so, both A (resulting from B) and C (due to D) can be considered in X.`  
**Risk when misused:** The source writes `resulted from`.  
**Skill-ready instruction:** Close a method summary on capability, and keep it to what the steps deliver.

## P05-S46

**Source pointer:** p. 15, §6 ¶2, sentence 2  
**Section:** Conclusions  
**Function tag:** RES  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** underlined; noted as skilful wording

**Local context:** The overall verdict of the comparison.  
**Why it works:** `in general` makes room for the mismatches reported in the following sentences, and the range of the comparison is stated.  
**Sentence link:** The next sentences open with the frequency ranges where agreement holds or fails.  
**Transferable rule:** Give an overall verdict with a qualifier and the range, and follow it with the exceptions.  
**Reusable pattern:** `A comparison of A and B shows that X and Y in general agree very well in the range between V1 and V2.`  
**Risk when misused:** Without the exceptions that follow, `in general` hides the mismatches.  
**Skill-ready instruction:** Keep `in general` only when the exceptions are stated nearby.

## P05-S47

**Source pointer:** p. 15, §6 ¶3, sentences 1-2  
**Section:** Conclusions  
**Function tag:** CLO  
**Score:** 9/10  
**Use status:** positive  
**Reader mark:** underlined

**Local context:** The main finding in the Conclusions.  
**Why it works:** Range, process, and effect appear in one sentence, and the consequence of omission follows in a short conditional.  
**Transferable rule:** In Conclusions, state a finding with its range and the consequence of ignoring it.  
**Reusable pattern:** `At A (e.g., from V1 to V2), B has a significant contribution to X. If overlooked, the simulated X is much smaller than the measured values.`  
**Risk when misused:** `significant` here means large; avoid it where a reader could take it as statistical.  
**Skill-ready instruction:** Use `large` or `substantial` when `significant` could be read as a statistical term.

## P05-S48

**Source pointer:** Abstract; p. 2 ¶4 and ¶6; p. 4 §2.2; p. 6 §2.3.2; p. 8 §3.3; p. 12 §4.2; p. 13-15 §5; p. 15 §5.4 and §6  
**Section:** Across sections  
**Function tag:** STY  
**Score:** 7/10  
**Use status:** caution

**Local context:** Surface forms in this paper that should not be copied.  
**Why it works:** The sentences around them are well organized, which is why the slips are easy to absorb unnoticed.  
**Transferable rule:** Learn the function of the sentence and correct the form.  
**Reusable pattern:** `Compared with` for `Comparing to` and `if compared to`; `used` for `utilized`; `resulting from` for `resulted from`; `we suggest upscaling` for `we suggest to upscale`; `Few studies have` for `Few works have been done`; `A number of models have been` for `There has been a number of models`; `of the order of` for `in the order of`; `orders of magnitude` for `orders`; `systematically` for `systemically`; `considerably lower` for `considerably low`; `according to` for `if consider`; `(discussed in Section N)` for `(will be discussed in ...)`.  
**Risk when misused:** Evaluative words in the same paper (`powerful tool`, `valuable`, `useful tool`, `attractive way`, `extremely`) should also not be copied without support.  
**Skill-ready instruction:** Apply these corrections whenever a draft imitates the exemplar's wording.
