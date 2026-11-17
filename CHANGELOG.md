# Changelog

All notable changes to Find My Ikigai are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [0.1.0] - 2026-11-17

First public release. Beta: tested in Claude, and built to the specification of the other platforms but not yet tested there (see "Platform status" in the README).

### Added

- **Find My Ikigai.** Mieko Kamiya's ikigai psychology: the feeling (ikigai-kan), its sources and the seven needs, with short attributed grounding during the conversation. Optional NLP owned-or-borrowed exercise, an ikigai map and one small step. Scripts: `ikigai_map.py`, `check_dossier.py`.
- **Trust layer.** Every fact is labelled as seen (with the user's own words), inferred (with its basis) or unknown. Summaries and deliveries show an assumptions block, and a visible self-check runs before each delivery.
- **Claude Code guard.** A Stop hook sends a reply back for a fix when it asks more than one question, contains an internal note, or claims a file was saved when none was written.
- **Install anywhere.** A Claude Code marketplace in this repository, an Agent Plugins package for Hermes, and a plain skill folder for every Agent Skills client.
- **Quality.** Script tests, a skill checker and JSON validation run on every push. Evaluation cases and graded simulated conversations are in `evals`.
- Issue templates for reporting a mistake (with a required privacy check) and for ideas.
