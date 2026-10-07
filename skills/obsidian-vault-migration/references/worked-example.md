# Synthetic migration fixture

Source contains `Projects/Plan.md`, `Archive/Plan.md`, `Projects/Index.md`, and `Media/diagram.png`. The index links to `[[Plan]]`, `[[../Archive/Plan|old plan]]`, and `![[../Media/diagram.png]]`.

Resolve `[[Plan]]` using the source app's configured resolution rules if known; otherwise record it as ambiguous because two matching basenames exist. The explicit archive path stays distinct, and the image reference points to the copied attachment.

Import identity is the source-relative path plus a stable source-root identifier, not the display title. A manifest row can contain `source_path`, `content_sha256`, `destination_id`, `action`, `link_findings`, and `status`.

First import: create three notes and one attachment. Unchanged second import: skip all four. If the destination Plan and the source Plan both changed since the last successful import, preserve both and report a conflict. If a directory cannot be read, list its failure and mark the overall import incomplete.
