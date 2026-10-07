# Developer Workflow Skills

Understand repositories, preserve project evidence, migrate Markdown vaults, and integrate AI in Electron.

Four portable Agent Skills for Claude and ChatGPT/Codex. They contain original workflow guidance and synthetic examples, with no application source, credentials, live data, or project-specific infrastructure.

## Skills

| Skill | Use it for |
| --- | --- |
| [Repository Onboarding Map](skills/repo-onboarding-map/SKILL.md) | Map an unfamiliar codebase into verified entrypoints, runtime boundaries, setup steps, and a practical first-change path. Use for onboarding or architecture handovers. |
| [Evidence Backed Project Log](skills/evidence-backed-project-log/SKILL.md) | Create or update a project log and claim ledger tied to actual changes, commands, and artifacts. Use for engineering portfolios, research notebooks, and auditable handovers. |
| [Obsidian Vault Migration](skills/obsidian-vault-migration/SKILL.md) | Plan or implement a repeatable Markdown/Obsidian vault import while preserving paths, wikilinks, attachments, metadata, and source files. Use for notes-app migrations. |
| [Electron AI Integration](skills/electron-ai-integration/SKILL.md) | Implement or review AI features in Electron across renderer, preload, main process, and backend boundaries. Use for model calls, streaming, and filesystem-backed AI features. |

## Try a workflow

- `repo-onboarding-map`: Map this repository and identify the safest first feature change.
- `evidence-backed-project-log`: Record this change set with evidence and honest verification limits.
- `obsidian-vault-migration`: Design a repeatable import of this Markdown vault into a notes application.
- `electron-ai-integration`: Add an AI feature with a clear renderer-to-provider boundary.

Each skill is self-contained under skills/. Its SKILL.md is the entrypoint; references/ provides a worked example; agents/openai.yaml supplies optional OpenAI UI metadata. The two helper-bearing skills across this collection need Python 3.11+; other workflows use the tools already available in the host.

Read [installation and compatibility](INSTALL.md). Each skill works from the same source folder across hosts; there are no separate copies to drift apart. Host permissions and available tools still determine what can execute.

## Check and package

From this folder, using Python 3.11+ with the standard library:

```text
python -B scripts/validate.py
python -B -m unittest discover -s tests -v
python -B scripts/package.py
```

The last command creates one ZIP per skill under dist/. Each archive has one top-level skill folder. Validation checks structure, links, metadata, obvious private-path/credential patterns, and Python syntax. Run the unittest command only in packs containing tests/. Tests check helper behavior where present. [Behavioral evaluation prompts](evals/README.md) are provided for manual testing; no AI-model pass rate is claimed. CI is included for Windows and Linux and has not been run remotely.

## Sharing

This folder is an independent GitHub-ready repository. Review the files, publish it to a repository you own, and share its URL. plugin.json and .claude-plugin/plugin.json provide OpenAI/portable and Claude packaging metadata. No marketplace listing, remote repository, or publication is created automatically.

The newly authored content and helpers are MIT licensed; see [LICENSE](LICENSE) and [provenance](PROVENANCE.md). Linked documentation and original project materials retain their own terms.
