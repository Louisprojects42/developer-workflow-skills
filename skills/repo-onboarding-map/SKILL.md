---
name: repo-onboarding-map
description: "Map an unfamiliar codebase into verified entrypoints, runtime boundaries, setup steps, and a practical first-change path. Use for onboarding or architecture handovers."
---

# Repository Onboarding Map

Produce a usable map of the repository as it exists. Treat a README's proposed features as claims to check against source, migrations, tests, and runnable entrypoints.

Start from the user's selected root and applicable repository instructions. Inventory the top level before recursively searching; exclude dependencies, generated output, caches, credentials, and linked directories outside the root. The optional `scripts/inventory.py` returns bounded directory and manifest names without reading file contents. Run `python <skill-dir>/scripts/inventory.py <repo-root> --depth 3` when a large tree makes manual inspection inefficient.

Follow one representative request or job from entrypoint through its data boundary to its output. Identify ownership of authentication, state, background work, and external calls. Distinguish a checked-in adapter from a service that actually runs elsewhere. Resolve disagreements between documentation and source explicitly, with file references.

Derive setup and verification commands from manifests, lockfiles, and CI. Separate required dependencies from optional profiles. Do not install packages or start services merely to describe the project. If asked to implement a change, use the map to choose a narrow slice and the existing verification route.

Deliver a short architecture map, key source locations, exact known setup/check commands, unverified requirements, and a first-change walkthrough. Record whether each component is implemented, documented only, or externally hosted. An empty test suite is zero observed coverage, not a successful behavioral check.

Use [the worked example](references/worked-example.md) for a mixed desktop/backend project; adapt its shape rather than imposing that stack.
