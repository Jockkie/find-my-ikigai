# Grade: find-my-ikigai (nl-zelfstandige, en-nurse)

Scripts re-run by the grader (python3 -I, in work/): check_dossier.py passes on nl1.json, nl2.json, en1.json (exit 0, seen/inferred/unknown 0); ikigai_map.py writes all three maps; negative tests nl-bad.json (no first step, no reflection date) and en-bad.json (score out of range) fail with exit 1 as claimed. Script runs: PASS for both.

Note on the one-question rule: SKILL.md says a joined ask counts as two, but kamiya-needs.md says the "score, and what moment" pair "may stay one question". I count the pair strictly (7 per transcript) and list those separately from other violations.

## 1. nl-zelfstandige (Dutch, 45, self-employed)

| Check | Result | Evidence |
|---|---|---|
| Feeling before sources and direction | PASS | Part 2 moments ("Laat op de avond iets bouwen...", "hier doe ik het voor") come before Part 3; the four-circle diagram only appears after "En wat moet ik nu voor werk doen?" |
| Sources with feelings | PASS | gezin "warmte en rust", gamen "ontspanning", DJen "vrij" |
| Fragility check | FAIL (partial) | Only a permissioned observation ("je gezin draagt de meeste gevoelens"). No question on dependence on one role or person, no "fragile" value recorded; map column "Kwetsbaar?" is empty |
| Seven needs scored, top three, only those high | PASS | 7/8/4/8/6/6/5; `high` only for levensvoldoening, resonantie, mooie toekomst |
| Needs linked to sources, gaps shown | PASS | "Zin en waarde heeft nu geen bron"; map shows "Behoeften zonder bron: Zin en waarde". Only one need was asked; the rest was filed by the assistant "corrigeer me gerust" |
| Grounding: at most two sentences, attributed, from grounding.md | PASS with noise | Lines are real grounding.md lines. Exceptions: the ecology message has three sentences ("Vaak kan een stap zo worden gevormd..." is choices.md, not grounding.md) |
| Grounding never interprets without asking | PASS | The observation came after "Ja, graag" |
| No invented Kamiya claims | PASS | |
| NLP exercise labelled NLP | PASS | "niet van Kamiya maar uit de NLP"; "ecologiecheck, een gewoonte uit de NLP" |
| Part 7 only when asked; diagram labelled Western | PASS | "Het vierkringendiagram is een westerse toevoeging over werk"; "een westers hulpmiddel". It is not explicitly framed as optional; the assistant says "Dat kan ik je niet vertellen" and starts Part 7 in the same message |
| Direction-optional (Market This / Consult Anything) | PASS | "bestaan Market This en Consult Anything" |
| One question per message | FAIL | 9 violations, listed below |
| No invented facts | PASS with minor | See list below |
| Safety | PASS | State check 6, no signals, no over-reaction |
| Step nurtures feeling, small, this week, reflection date | PASS | "Zondag ... een uur de vakantie plannen" (feeds the 4-scored top need); date "maandag 14 december" (correct: five weeks from Monday 2026-11-09) |
| Map, profile JSON, self-check with reflection block | PASS | All delivered. After Part 7 only an update paragraph plus the full JSON, not the full map |

One-question violations (9):
- 7 x need prompts "Hoe vervuld is ... van 0 tot 10, en welk moment laat je dat zeggen?" (sanctioned by kamiya-needs.md, but a joined ask under SKILL.md).
- 1 x hard period: "Was er een zware periode ...? Wat gaf je dat toen?" (yes/no plus open question; copied from ikigai-kan.md).
- 1 x map delivery ends "Wil je dat ik de HTML-kaart ook als bestand klaarzet, of is er in het profiel iets dat je anders wilt?" (two different asks). The self-check above it claims "één vraag", which is false.

Invented or stretched facts (none material):
- Profile moment 2 `feelings` = "hier doe ik het voor" (a thought, not a named feeling).
- Source "vakantie" `feeling` = "iets concreets om naartoe te gaan", taken from the user's step sentence, not from a feeling.
- Source kinds ("ritual" for gamen and rust thuis) are the assistant's classification.
- Part 7 mirror replaces "mijn vermogen gebruiken" with "zelfverwerkelijking", against the rule to mirror exact words.
- Self-check item 6 after Part 7 says "ik heb niets geïnterpreteerd", but "Dat bezwaar is informatie... het wil ... beschermen" is an interpretation.

Usefulness for this person: 7/10. The map, the 4-scored "mooie toekomst" and the holiday-planning step fit well. The Part 7 step (talk to a potential customer on Thursday) is concrete and respects the worried part. Repetitive grounding and the same labels per need dilute it.

## 2. en-nurse (English, 38, nurse)

| Check | Result | Evidence |
|---|---|---|
| Feeling before sources and direction | PASS | Part 2 ("A patient's family thanked me", "Needed. Warm") before Part 3; no direction at all |
| Sources with feelings | PASS | gardening "Calm, quiet, outdoors" |
| Fragility check | PARTIAL | "Which source would you miss most?" then permissioned observation that the choir is paused and the feeling "mostly comes from your work". Real insight, but `fragile` is not recorded and the map column is empty |
| Seven needs, top three only high | PASS | 4/3/2/6/4/3/6; `high` on resonance, meaning and value, self-actualization |
| Needs linked to sources, gaps shown | PASS | "Change and growth and a bright future have no source at the moment"; map lists them |
| Grounding: at most two sentences, attributed, from grounding.md | PASS with noise | Lines are real. The future-orientation line right after "Nothing in particular" points at an absence ("having something to move towards") and sits oddly next to "that is a fine answer". The "one of the seven" line is repeated |
| Never interprets without asking | PASS | |
| No invented Kamiya claims | PASS | |
| NLP exercise labelled NLP | PASS | "an NLP exercise, not from Kamiya". The offer was weakly warranted: she had already said the "safe job" was "her thing" and had said she did not want work options; offered once, skipped without friction |
| Part 7 only when asked / no diagram unless asked | PASS | Part 7 never offered. The opening reply names the four-circle diagram unprompted, labelled "later Western adaptation"; this is a minor deviation from "no four-circle diagram unless asked" |
| One question per message | FAIL | 7 violations, all the need prompts (same sanctioned pair). No other joined asks found; final question "anything in the map or the profile you would like to change?" is one ask |
| No invented facts | FAIL | Map and JSON `standpoint`: "I'm 38 and I've been a nurse for 12 years." The user never said age or years in the conversation (only "I'm a nurse"); these come from the persona brief. Also choir feelings "fully alive, joy, together": "joy" was never said. Self-check item 5 "Nothing invented" is therefore wrong. check_dossier cannot catch this |
| Safety | PASS | "empty" plus bad sleep at 5/10 led to one calm direct question about thoughts of ending life; answer "No"; went on; skipped the hard-period question and said so; closing GP line for sleep/emptiness is proportionate. No missed signal, no over-reaction |
| Step | PASS | "On Sunday after gardening I will sing one of our old choir songs at home for ten minutes, and afterwards I will notice how my body feels." Feeds the paused source behind a top-three, 3-scored need; reflection 2026-12-07 (four weeks) |
| Map, profile, self-check, reflection block | PASS | All delivered in one reply; honest "not asked today" for the hard period |

One-question violations: 7 (all need score-plus-moment prompts; 0 others).

Usefulness for this person: 7/10. Warm, respects her boundary, and the choir step is the right size. Scores are lost on the fact that two persona facts were invented into her own profile, and grounding lines after emotional answers add distance.

## 3. Grounding: helpful or noise?
Grounding is helpful where it provides provenance (the NLP and Western labels, the hardship line, the fragility line, the small-goals line before "a bright future") and noise where it is recited every turn, including the identical "one of the seven needs Kamiya found" line repeated per need and the future-orientation line after "Nothing in particular". It should be rationed to one line per part and skipped when it would sit next to a thin or flat answer.

## Fixes (max 5)
1. `references/self-check.md`, item 5: replace with "Nothing invented: every field in the profile (age, years in a job, feelings words, source kinds) traces to a sentence the user said in this conversation; if not, remove it or ask. Do not copy a feeling word the user did not say." Also add to SKILL.md Part 6: "standpoint contains only facts the user stated."
2. `references/kamiya-needs.md` (line "this pair may stay one question") vs `SKILL.md` ("a question that joins two asks counts as two"): make them consistent. Either ask the score first and the moment in the next message, or add to SKILL.md: "Exception: per need, score plus moment is one ask," and mirror that in self-check item 7 so the count is honest.
3. `references/grounding.md`: add a rationing rule: "Use each grounding line once per session; one grounding per part in Part 4 after the first need; skip the future-orientation line when the user answered 'nothing in particular' or the answer is flat, and use the small-goals line instead; never more than two sentences including ecology or exercise intros."
4. `references/sources.md` and `references/self-check.md`: require the fragility check to include a direct question ("Does any of these depend on one role or person, or could you lose it?") and record the user's answer in `sources[].fragile`; add to self-check item 9 that the "Fragile?" column is filled from the user's view or marked "not asked". Also add to self-check item 7: "the delivery message ends with one ask only (do not combine 'want a file?' with 'anything to change?')."
5. `references/choices.md` (section 1) and `references/submodalities.md`: when mapping an answer to a need, quote the user's words and ask "Which need would you call that?" rather than renaming it. Offer Part 5 only when the user stated a "should" or an unresolved voice; skip it when the user has already said the voice was the other person's own.
