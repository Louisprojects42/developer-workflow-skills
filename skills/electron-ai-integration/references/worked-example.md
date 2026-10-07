# Example message boundary

Renderer request: `{requestId, task: "summarize", noteId, provider}`. The handler resolves a note only within the current workspace and enforces a payload bound; it does not accept an arbitrary path or provider URL from the renderer.

Stream events include the same request ID and a kind such as `chunk`, `done`, or `error`. Cancellation records that ID; later chunks for it are discarded. A second request has its own lifecycle, even if it targets the same note.

Failure checks:

- Renderer attempts `../../outside.md`: handler rejects it before reading.
- A foreign frame invokes the same IPC: sender validation rejects it.
- Mind-map response lacks required node fields: show a retryable parsing error and retain the original note.
- Request A is cancelled before request B starts: delayed A chunks never appear in B.

These examples define behavior, not a prescribed SDK or model version.
