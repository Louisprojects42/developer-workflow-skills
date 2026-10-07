---
name: electron-ai-integration
description: "Implement or review AI features in Electron across renderer, preload, main process, and backend boundaries. Use for model calls, streaming, and filesystem-backed AI features."
---

# Electron AI Integration

Establish where credentials live and which content is trusted. Renderer bundles, including build-time variables, are visible to users. Keep application-owned provider secrets behind a backend. For bring-your-own-key desktop tools, obtain an explicit storage/consent model and prefer appropriate OS credential storage; explain that desktop packaging does not protect a shared secret.

Trace renderer -> named preload method -> validated IPC handler -> provider or backend. Expose narrow operations rather than raw `ipcRenderer`, arbitrary URLs, shell commands, or unrestricted filesystem paths. Validate the sending frame, argument shape, operation scope, and selected-root containment. Treat imported notes and model output as untrusted content.

Preserve context isolation, disabled renderer Node integration, and appropriate sandboxing. Check navigation, new-window, and external-link handling when those paths are involved. Read the [Electron security guide](https://www.electronjs.org/docs/latest/tutorial/security) for version-specific implementation details instead of assuming defaults.

Model each request with an ID, explicit task/model selection, cancellation, bounded timeout, and observable states. Guard against late chunks from a cancelled request being appended to a later conversation. Preserve the user's provider choice unless a documented feature requires another provider and the user accepts that behavior. Verify current SDK and model details only when implementing that adapter.

Validate structured model output against the actual schema. A malformed response is a recoverable error, not fabricated successful content. Avoid logging prompts, notes, keys, or full provider errors by default. Determine what leaves the device before adding an automatic AI action.

Deliver a focused implementation or findings tied to source, plus checks for success, cancellation, malformed output, and unauthorized IPC. Read [the worked example](references/worked-example.md) when designing the message contract.
