---
name: obsidian-vault-migration
description: "Plan or implement a repeatable Markdown/Obsidian vault import while preserving paths, wikilinks, attachments, metadata, and source files. Use for notes-app migrations."
---

# Obsidian Vault Migration

First identify the source root and destination model. Decide whether the task is a one-time copy, repeatable import, or bidirectional sync; do not implement sync for a one-time import. Inventory note and attachment counts without printing private note contents.

Preserve source-relative paths as identity: `Projects/Plan.md` and `Archive/Plan.md` are different notes even when titles match. Define case and Unicode behavior for the destination platform. Resolve wikilinks, aliases, heading/block targets, embeds, and relative Markdown links against an explicit path mapping. Report ambiguous basename links instead of guessing.

Preserve frontmatter and original Markdown. Map folder schemes such as PARA only when requested; make unmatched folders visible rather than silently filing everything into an inbox. Keep hidden application configuration separate from note content. Do not follow symlinks or junctions outside the selected root. Include attachments according to the user's migration scope and preserve their relative references.

For repeatable imports, persist source identity and content hash plus destination identity. Define skip, update, and conflict behavior before applying another run. Preserve both versions when source and destination changed independently. Distinguish unchanged from failed; interrupted work must resume without duplicate notes. A partial read must never be presented as a complete import.

Prefer a preview manifest before a large write: source path, destination path/id, intended action, link changes, attachment decisions, and conflicts. Verify counts, representative links, duplicate titles, non-ASCII paths, and a second run. Keep originals intact unless removal is explicitly requested.

Return the migration manifest, outcome counts, unresolved links, and recovery instructions. Read [the worked example](references/worked-example.md) for collisions and restart behavior.
