# MCP Skills Server — Deduplicated Remediation Plan

Generated from: REVIEW_SUMMARY.md, METADATA_AUDIT.md, SKILL_CLASSIFICATION.md,
COMPOSITION_MAP.md, TEST_BASELINE.md, SCHEMA_V1.md, and both original security review documents.

**Scope:** Every remaining issue from both reviews, deduplicated, organized into execution tiers.

**Format:** Small Plan — remediation within an existing architecture, not greenfield.

---

## Tier 0: Critical Security (Do First — Blocks Everything)

### Fix 0.1 — Path Traversal in API Files
- **Files:** `skills_manager_api.py`, `skills_manager_app.py`, `core/skills.py`
- **Problem:** Core skills functions accept unsanitized skill names from user input
- **Status:** DONE — Created `core/security.py` with shared validators; added `is_safe_skill_name()` + `validate_skill_path()` checks to all CRUD functions in `core/skills.py`; 31 new tests in `tests/test_security.py`

### Fix 0.2 — Arbitrary File Write via Absolute Paths (core/skills.py)
- **Files:** `core/skills.py`
- **Problem:** Absolute path injection bypasses skills directory (`Path("skills") / "/etc/passwd"` → `/etc/passwd`)
- **Status:** DONE — `validate_skill_path()` resolves and checks containment; `validate_file_path()` rejects absolute paths and null bytes; applied to all write paths in `core/skills.py`

### Fix 0.3 — Zip Slip in migrate.py
- **Files:** `migrate.py`
- **Problem:** Malicious ZIP entries could write outside extraction directory
- **Status:** DONE (lines 166-172 have `relative_to()` check)

### Fix 0.4 — Unauthenticated Vercel API Endpoint with Wildcard CORS
- **Files:** `api/index.py`
- **Problem:** CORS and auth concerns
- **Status:** DONE (ALLOWED_ORIGIN env var + Bearer token auth)

---

## Tier 1: High Priority (Security Hardening + Correctness)

### Fix 1.1 — Bare Except Clauses (Silent Failures)
- **Files:** `core/skills.py`, `api/index.py`
- **Status:** DONE — All silent `pass` catches in `core/skills.py` and `api/index.py` now log warnings with `logger.warning()`; added `import logging` and module logger to both files

### Fix 1.2 — YAML/Metadata Escaping
- **Files:** `core/security.py`, `core/skills.py`
- **Status:** DONE — Added `sanitize_description()` to `core/security.py`; applied in `create_skill()` and `update_skill()` before writing descriptions; strips null bytes and control characters

### Fix 1.3 — SKILLS_DIR Existence Validation in API
- **Files:** `skills_manager_api.py`, `skills_manager_app.py`
- **Status:** DONE — Both Flask apps now raise `RuntimeError` at import time if `SKILLS_DIR` doesn't exist or isn't a directory

### Fix 1.4 — File Upload Validation
- **Files:** `core/security.py`, `core/skills.py`
- **Status:** DONE — Added `validate_upload_file()` with extension allowlist and 5MB size limit; applied in `import_files_json()`; null byte content rejection for both text and base64 uploads; 17 new tests

---

## Tier 2: Medium Priority (Reliability + Maintainability)

### Fix 2.1 — Standardize Error Responses
- **Status:** DONE — Added `error_response(code, message, status)` helper to both Flask apps; all error returns now use `{"error": {"code": "...", "message": "..."}}` format with proper HTTP status codes

### Fix 2.2 — Reload Endpoint Is a No-Op
- **Status:** DONE — Both `/api/reload` endpoints now call `list_all_skills()` and return `skill_count` in response

### Fix 2.3 — Fix Pytest Deadlock
- **Status:** DONE — Added `shutdown()` function to `server.py` that stops file watcher thread cleanly; watcher loop checks `_watcher_stop` flag; conftest calls `shutdown()` in teardown; tests run in ~2s without hanging

### Fix 2.4 — Rate Limiting
- **Status:** DONE — Added `flask-limiter` to both Flask apps; default 60/minute, write endpoints 10/minute; limits configurable via `RATE_LIMIT_DEFAULT` and `RATE_LIMIT_WRITE` env vars

---

## Tier 3: Low Priority (Quality + Hygiene)

### Fix 3.1 — Consolidate Shared Validation into core/
- **Status:** DONE — Created `core/flask_helpers.py` with shared `error_response()` and `require_json()`; both Flask apps import from core instead of defining their own; removed `functools` import from both apps

### Fix 3.2 — Add Type Hints
- **Status:** DONE — All public functions in `core/` already had type hints; added missing return types to `core/flask_helpers.py`

### Fix 3.3 — Strengthen Weak Test Assertions
- **Status:** DONE — `test_extracts_description_from_frontmatter` now asserts exact description value; `test_finds_partial_words` now asserts `len > 0`

### Fix 3.4 — Harden Fragile call_args Tests
- **Status:** DONE — `test_includes_skill_context` and `test_includes_context` now join full command list and search for context string, instead of indexing `call_args[0][0][2]`

### Fix 3.5 — Normalize Schema to v1.1
- **Status:** DONE — Schema requires all 5 fields (`name`, `description`, `tags`, `sub_skills`, `source`); migrated 4 skills missing `source` field; updated all test fixtures to include all required fields

### Fix 3.6 — Clean Up Stub/Test Skills
- **Status:** DONE — Removed 14 test artifact/stub skill directories (`binary-import`, `binary-skill`, `safe`, `traversal-test`, `json-import`, `json-skill`, `import-me`, `renamed-skill`, `new-skill`, `my-new-skill`, `integration-test`, `no-skill-md`, `imported-skill`, `source-skill`)

---

## What This Plan Does NOT Cover
- New skill creation (feature request)
- Tag taxonomy normalization (design decisions needed)
- Router architecture refactoring (architectural debt)
- Performance monitoring / observability
- HTTPS termination (infrastructure)
