# Example: a desktop notes application

Observed files: `electron/main.js`, `electron/preload.js`, `src/App.jsx`, `src/lib/store.js`, `schema.sql`, and a package manifest with `dev` and `build` commands.

Trace: note editor -> renderer store -> authenticated database request -> database policy -> returned note. Folder selection follows renderer -> named preload method -> main-process dialog. These are distinct trust boundaries.

Useful output:

| Component | Evidence | Confidence |
| --- | --- | --- |
| Desktop startup | Main entrypoint and package manifest | Implemented; launch not executed |
| Per-user cloud notes | Store queries and ownership policies | Source inspected; integration unverified |
| AI summaries | Documentation only; no adapter found | Planned or missing |

A sensible first change is a note-save error state, verified through the store's existing tests and a local UI check if available. Do not report that the whole application was run after only reading the manifest.
