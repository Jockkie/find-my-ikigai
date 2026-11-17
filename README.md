# Find My Ikigai

*Part of [Jockkie Studio's open-source skills](https://github.com/Jockkie/jockkie-studio). I do the geeking. You get the easy part.*

> **Version 0.1.0, beta.** Tested in Claude; built to the specification of the other platforms but not yet tested there. See [Platform status](#platform-status), and please [report what you find](https://github.com/Jockkie/find-my-ikigai/issues/new/choose).

A reflective coaching skill based on Mieko Kamiya's ikigai psychology. It starts where Kamiya started: the feeling that life is worth living (ikigai-kan). You look at moments when you felt it, the sources that feed it, and which of Kamiya's seven needs those sources meet or leave empty. Along the way the skill briefly explains why it asks what it asks and what Kamiya found, and it always says whose idea something is.

Optional extras: an owned-or-borrowed exercise from NLP (to feel which wishes are yours and which you carry for someone else), and a work or direction check with the Western four-circle diagram, only if you ask for it.

You end with an ikigai map, one small step to nurture the feeling, and a date to look back.

Start by saying something like "help me find my ikigai" or "what makes my life worth living?".

No external tools: nothing you share leaves the conversation. This is reflective coaching, not therapy; the skill stops and points to professional help when that is needed. Kamiya's book has not been translated into English; the skill relies on secondary sources it names.

## Install

The skill folder is `skills/find-my-ikigai`.

**Claude Code (plugin)**
```
/plugin marketplace add Jockkie/find-my-ikigai
/plugin install find-my-ikigai@find-my-ikigai
```
Want all five Jockkie Studio skills in one go? Use `/plugin marketplace add Jockkie/jockkie-studio` and then `/plugin install find-my-ikigai@jockkie-studio`.

**Claude.ai**
Zip the `skills/find-my-ikigai` folder and upload it in Claude's skills settings.

**Hermes Agent (plugin)**
This repository is also a portable [Agent Plugins](https://vercel.com/kb/guide/agent-plugins) package (`plugin.json`, `skills/`, `mcp.json`), which Hermes loads natively. Copy the repository into `~/.hermes/plugins/find-my-ikigai`, then `hermes plugins enable find-my-ikigai`. Skill only: copy `skills/find-my-ikigai` into `~/.hermes/skills/`.

**ChatGPT (Business, Enterprise, Edu)**
Zip the `skills/find-my-ikigai` folder and upload it under Skills, Create, Upload.

**OpenClaw**
Copy `skills/find-my-ikigai` into `~/.openclaw/skills/` (or your workspace `skills/` folder) and start a new session.

**Grok**
Import the zipped `skills/find-my-ikigai` folder under Skills. For Grok Build, copy the folder into `~/.grok/skills/`.

**GitHub Copilot (VS Code, Visual Studio, Copilot CLI, cloud agent)**
Copy `skills/find-my-ikigai` into `~/.copilot/skills/` for all your projects, or into `.github/skills/` in one repository.

**Codex, Cursor, Gemini CLI and other Agent Skills clients**
Copy `skills/find-my-ikigai` into the client's skills directory (for example `.agents/skills/`, `.cursor/skills/`, `~/.claude/skills/`).

## Platform status

| Platform | Status | What that means |
|----------|--------|-----------------|
| Claude Code | Validated | The marketplace, manifest and hook pass `claude plugin validate`; the skill was tested in evaluation rounds with Claude models |
| Claude.ai | Skill tested | The same `SKILL.md` as in the evaluations; the zip upload itself is not yet tested |
| Hermes Agent | Untested | Built to the Agent Plugins specification |
| ChatGPT, OpenClaw, Grok, GitHub Copilot | Untested | Built to the Agent Skills format |
| Codex, Cursor, Gemini CLI and others | Untested | Built to the Agent Skills format |

The guard hook only runs in Claude Code. On other platforms, the visible self-check in the skill does that job. Tried it on an untested platform? [Tell us how it went](https://github.com/Jockkie/find-my-ikigai/issues/new/choose), whether it worked or not.

## How this skill keeps you from trusting a guess

AI tools sound sure of themselves, even when they are guessing. This skill is built to show you the difference:

1. **What you told me and what I assumed.** Every summary and every delivery separates what you said (with your own words), what the skill estimated (with its basis) and what is still unknown.
2. **A check before every step that matters.** Where the skill can run code, `check_dossier.py` or the skill's own script blocks the next step while a fact is labelled as yours without your words or a number has no label.
3. **A visible self-check** before every delivery: sources, invented numbers, one question at a time, files that really exist.
4. **In Claude Code, a guard.** A small hook sends a reply back for a fix when it asks several questions at once, contains an internal note, or claims a file was saved when none was written. It only acts in sessions where this skill is used.

A good habit with any AI advice: before you act on it, ask "Which of this did I tell you, and which did you assume?"

## Privacy

What you share stays with you. Personal data is never sent to external tools, and the files the skill makes are yours to keep.

## Quality

Every change runs the script tests and checks on GitHub (`.github/workflows/tests.yml`). The skill itself is tested with written evaluation cases (`evals/evals.json`) and full simulated conversations, graded by a separate model; results are in `evals/results`.

What changed per version is in the [changelog](CHANGELOG.md). Want to help? Read [CONTRIBUTING](CONTRIBUTING.md). Found a security problem? Report it privately through the Security tab ([how](SECURITY.md)), not in a public issue.

## Credits

Mieko Kamiya, *Ikigai ni tsuite* (1966), through secondary sources (Ikigai Tribe, The Meaning Movement); NLP submodalities for the optional owned-or-borrowed exercise.

## The other skills

| Skill | For |
|-------|-----|
| [Consult Anything](https://github.com/Jockkie/consult-anything) | Owners and managers whose business is stuck |
| [Market This](https://github.com/Jockkie/market-this) | Owners and makers who need more customers |
| [Copywrite Me](https://github.com/Jockkie/copywrite-me) | Anyone who needs a text that sells |
| [Align My Astro](https://github.com/Jockkie/align-my-astro) | Anyone who likes a daily reflection |

## Need a human?

The skill refers you to the right type of professional when a problem needs one. Jockkie Studio is one of the options: helicopter view, project management and workflows, process improvement, change and innovation, go-to-market, AI implementation.

## Contact and support

- Website: https://www.jockkie.com
- Email: info@jockkie.com
- The skill is free. If it helped you: https://buymeacoffee.com/jockkie

## License

MIT
