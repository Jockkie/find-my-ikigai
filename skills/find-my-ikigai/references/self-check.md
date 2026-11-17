# Self-check (visible to the user)

Run this before every gate summary and every delivery, and show the result to the user as a short block titled "Self-check". If an item fails, fix it first and say what you fixed. Never claim a check passed that you did not do.

## Checklist
1. **Feeling first:** the session explored the feeling (ikigai-kan) and its sources before any direction or work choice; Part 7 only happened because the user asked or confirmed.
2. **Grounding attributed:** every grounding line said whose idea it was (Kamiya, NLP, Western diagram) and came from `grounding.md`; nothing was presented as Kamiya's that is not.
3. **Importance as given:** only the three needs the user chose are `high`; the rest are `not in top three`, not a level you filled in.
4. **Their words:** the map, the candidates and the verdicts use the user's own words. Every verdict (owned, borrowed, mixed, unsure) was given by the user, not by you.
5. **Nothing invented:** every profile and map field (age, years in a job, feeling words) traces to the user's own words in this conversation; you did not fill in earlier answers, a profile or a reference memory the user did not give.
6. **Asked before interpreting:** every pattern you shared was preceded by asking permission.
7. **Safety:** you checked the state when starting; no exercise continued after a crisis signal.
8. **One ask:** every message ended with exactly one question; the only exception is the Part 4 need prompt.
9. **Fragility asked:** the fragility check was asked directly, or `sources[].fragile` says "not asked".
10. **Profile:** printed in the same reply as the map. If you can run code: `python3 scripts/check_dossier.py profile.json --gate deliver` must pass (first step and reflection date present).

## Reflection block (in the map delivery)
Show "What you said and what I reflected": the user's key sentences, and each reflection you offered with whether they recognised it.
