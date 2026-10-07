# Example entry

**Entry:** run-017. **Time:** supplied session time with timezone. **Base:** observed revision; working tree dirty.

**Purpose:** reject invalid geometry instead of returning misleading coefficients.

**Changes:** `geometry.py` now returns structured rejection for non-finite points; `test_geometry.py` adds a malformed-input case; this log records the change.

**Evidence:** `evidence/run-017/check.txt` contains the actual command, exit code, and summary. `evidence/run-017/rejection.json` is a synthetic failing input's output.

**Result:** malformed-input regression passed. No aerodynamic benchmark or experimental comparison was run. The software behavior is supported; predictive physical accuracy is unresolved.

**Authorship:** implementation drafted with an assistant; domain assumptions were supplied in the experiment definition. No claim about the author's understanding is implied.

**Next:** compare valid cases against a named reference dataset under documented conditions.

For a retrospective entry: say which artifacts were available and which timing/author details remain unknown. Do not fill the gaps with a plausible narrative.
