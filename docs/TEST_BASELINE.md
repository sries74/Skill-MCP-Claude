# Test Baseline Audit

**Date:** 2026-03-05  
**Suite:** `tests/test_api.py`, `tests/test_app.py`, `tests/test_server.py`  
**Result:** 189 passed, 0 failed (Python 3.12.3, pytest 9.0.2)

---

## Status Legend

| Status | Meaning |
|--------|---------|
| **PASS** | References correct symbols, patches correct surfaces, expected behavior matches implementation |
| **FAIL** | References missing symbol or patches wrong surface |
| **STALE** | Tests behavior that no longer exists |
| **UNTESTABLE** | Requires missing dependencies |

---

## test_api.py — Flask Skills Manager API (57 tests)

### TestSanitizeName (7 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_lowercase` | PASS | Imports `core.utils.sanitize_name` directly |
| `test_replaces_spaces` | PASS | |
| `test_replaces_special_chars` | PASS | |
| `test_strips_leading_trailing_hyphens` | PASS | |
| `test_strips_whitespace` | PASS | |
| `test_allows_numbers` | PASS | |
| `test_empty_string` | PASS | |

### TestFindClaudeCli (3 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_finds_cli_in_path` | PASS | Patches `shutil.which` (correct — `find_claude_cli` calls it directly) |
| `test_finds_cli_in_home` | PASS | Patches `pathlib.Path.home` classmethod + creates fake binary at `tmp_path/.claude/claude` |
| `test_returns_none_when_not_found` | PASS | Patches `shutil.which` → None, `os.path.exists` → False (covers final `os.path.exists` fallback) |

### TestListSkillsEndpoint (6 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_lists_skills` | PASS | Uses `flask_test_client` fixture which patches `config._skills_dir` |
| `test_includes_metadata` | PASS | Verifies `description`, `tags` keys from `list_all_skills()` |
| `test_includes_content` | PASS | `list_all_skills()` includes `content` from SKILL.md |
| `test_includes_file_info` | PASS | Checks `has_scripts`, `has_references`, `file_count` |
| `test_extracts_description_from_frontmatter` | PASS | Weak assertion (only checks `description is not None`); description sourced from `_meta.json` in fixture, not frontmatter extraction |
| `test_empty_skills_directory` | PASS | |

### TestGetSkillEndpoint (3 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_gets_skill` | PASS | |
| `test_returns_404_for_missing_skill` | PASS | |
| `test_includes_file_list` | PASS | Checks `"SKILL.md" in data["files"]` |

### TestCreateSkillEndpoint (5 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_creates_skill` | PASS | Verifies files on disk (`SKILL.md`, `_meta.json`) |
| `test_sanitizes_name` | PASS | `"My New Skill!"` → `"my-new-skill"` |
| `test_requires_name` | PASS | `create_skill(name="")` → `sanitize_name("")` → `""` → error |
| `test_prevents_duplicate_without_overwrite` | PASS | 409 from `"already exists"` in error string |
| `test_allows_overwrite` | PASS | `overwrite=True` → 200 |

### TestUpdateSkillEndpoint (3 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_updates_skill` | PASS | Verifies file content on disk |
| `test_returns_404_for_missing_skill` | PASS | |
| `test_updates_meta` | PASS | Verifies `_meta.json` fields |

### TestDeleteSkillEndpoint (2 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_deletes_skill` | PASS | Verifies directory removed |
| `test_returns_404_for_missing_skill` | PASS | |

### TestImportFolderEndpoint (7 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_imports_folder` | PASS | |
| `test_allows_rename` | PASS | `name` param overrides source dir name |
| `test_requires_path` | PASS | Empty `path` → `"Source path is required"` → 400 |
| `test_returns_404_for_missing_path` | PASS | `"not found"` in error → 404 |
| `test_requires_directory` | PASS | `"Path must be a directory"` → 400 |
| `test_prevents_duplicate` | PASS | `"already exists"` → 409 |
| `test_creates_missing_skill_md` | PASS | Verifies SKILL.md created when source lacks one |

### TestImportJsonEndpoint (4 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_imports_files` | PASS | Verifies `files_imported` count and files on disk |
| `test_imports_base64_content` | PASS | Verifies binary round-trip |
| `test_requires_skill_name` | PASS | |
| `test_prevents_path_traversal` | PASS | `"../../../etc/passwd"` → skipped, 0 files imported |

### TestBrowseFilesystemEndpoint (5 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_browses_root` | PASS | |
| `test_browses_skill_subdirectory` | PASS | Checks `parent == ""` |
| `test_identifies_skill_folders` | PASS | `is_skill` flag from SKILL.md presence |
| `test_hides_hidden_files` | PASS | `.hidden` excluded from listing |
| `test_returns_404_for_missing_path` | PASS | |

### TestClaudeStatusEndpoint (2 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_returns_available_when_found` | PASS | Patches `core.claude_cli.find_claude_cli` (correct surface — imported via `from .config import`) |
| `test_returns_unavailable_when_not_found` | PASS | |

### TestClaudeRunEndpoint (4 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_runs_claude` | PASS | `mock_subprocess` fixture patches `subprocess.run` at module level (correct — `claude_cli.py` calls `subprocess.run` via module import) |
| `test_includes_skill_context` | PASS | Accesses `call_args[0][0][2]` to get full_prompt from `[cli_path, '-p', full_prompt]`; fragile if call signature changes |
| `test_returns_404_when_cli_not_found` | PASS | Error `"Claude Code CLI not found"` contains `"not found"` → 404 |
| `test_handles_timeout` | PASS | `TimeoutExpired` → `run_claude_prompt` returns `(None, "Timeout")` → 408 |

### TestClaudeGenerateSkillEndpoint (3 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_generates_skill` | PASS | Overrides `mock_subprocess.return_value.stdout` with frontmatter; `generate_skill_with_claude` parses name from it |
| `test_requires_idea` | PASS | `data.get("idea", "")` → empty string → `"Skill idea required"` → 400 |
| `test_returns_404_when_cli_not_found` | PASS | |

### TestClaudeImproveSkillEndpoint (2 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_improves_skill` | PASS | `sample_skill` creates file on disk; `improve_skill_with_claude` reads it via `get_skills_dir()` (patched correctly) |
| `test_returns_404_for_missing_skill` | PASS | `"not found"` in error → 404 |

### TestReloadEndpoint (1 test)

| Test | Status | Notes |
|------|--------|-------|
| `test_reloads_index` | PASS | API just returns `{"success": True, "message": "Skills reloaded"}` — no actual index reload |

---

## test_app.py — Standalone Skills Manager App (44 tests)

### TestGetAppDir (2 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_returns_file_parent_when_not_frozen` | PASS | Calls `get_app_dir()` directly |
| `test_returns_executable_parent_when_frozen` | PASS | Resets `config._app_dir = None`, patches `sys.frozen` with `create=True` |

### TestSanitizeName (3 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_lowercase` | PASS | Duplicate of test_api.py tests |
| `test_replaces_special_chars` | PASS | |
| `test_strips_hyphens` | PASS | |

### TestFindClaudeCli (2 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_finds_via_which` | PASS | Subset of test_api.py tests |
| `test_returns_none_when_not_found` | PASS | |

### TestIsPortInUse (2 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_returns_false_for_free_port` | PASS | Binds/releases socket, then checks |
| `test_returns_true_for_used_port` | PASS | Keeps socket bound, checks within `with` block |

### TestListSkillsEndpoint (3 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_lists_skills` | PASS | Uses `flask_app_test_client` fixture |
| `test_includes_metadata` | PASS | Checks `name`, `has_scripts`, `has_references` |
| `test_handles_empty_directory` | PASS | |

### TestGetSkillEndpoint (3 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_gets_skill` | PASS | |
| `test_returns_404_for_missing` | PASS | |
| `test_includes_files_list` | PASS | |

### TestCreateSkillEndpoint (3 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_creates_skill` | PASS | |
| `test_requires_name` | PASS | |
| `test_prevents_duplicates` | PASS | |

### TestUpdateSkillEndpoint (2 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_updates_skill` | PASS | |
| `test_returns_404_for_missing` | PASS | |

### TestDeleteSkillEndpoint (2 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_deletes_skill` | PASS | |
| `test_returns_404_for_missing` | PASS | |

### TestImportFolderEndpoint (4 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_imports_folder` | PASS | |
| `test_requires_path` | PASS | |
| `test_returns_404_for_invalid_path` | PASS | |
| `test_creates_missing_files` | PASS | Verifies `SKILL.md` and `_meta.json` auto-created |

### TestImportJsonEndpoint (4 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_imports_files` | PASS | |
| `test_imports_base64` | PASS | |
| `test_requires_skill_name` | PASS | |
| `test_prevents_path_traversal` | PASS | |

### TestBrowseFilesystemEndpoint (4 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_browses_root` | PASS | |
| `test_browses_skill_subdirectory` | PASS | |
| `test_returns_404_for_missing` | PASS | |
| `test_identifies_skills` | PASS | |

### TestClaudeStatusEndpoint (2 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_available` | PASS | Patches both `find_claude_cli` and `subprocess.run` directly (correct surface) |
| `test_unavailable` | PASS | |

### TestClaudeRunEndpoint (4 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_runs_prompt` | PASS | Patches `find_claude_cli` and `subprocess.run` inline |
| `test_includes_context` | PASS | `call_args[0][0]` → command list, `[2]` → full_prompt; fragile if call shape changes |
| `test_returns_404_without_cli` | PASS | |
| `test_handles_timeout` | PASS | |

### TestClaudeGenerateSkillEndpoint (3 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_generates_skill` | PASS | |
| `test_requires_idea` | PASS | |
| `test_returns_404_without_cli` | PASS | |

### TestReloadEndpoint (1 test)

| Test | Status | Notes |
|------|--------|-------|
| `test_reload` | PASS | `skills_manager_app` returns `{"success": True}` — no actual reload logic |

### TestIntegrationScenarios (4 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_create_and_retrieve_skill` | PASS | End-to-end: create → list → get |
| `test_update_and_verify` | PASS | End-to-end: update → get → verify fields |
| `test_import_and_list` | PASS | End-to-end: import folder → list |
| `test_create_update_delete` | PASS | Full lifecycle |

---

## test_server.py — MCP Skills Server (88 tests)

### TestValidateMeta (10 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_valid_meta_minimal` | PASS | |
| `test_valid_meta_full` | PASS | |
| `test_missing_name` | PASS | |
| `test_missing_description` | PASS | |
| `test_missing_both_required` | PASS | |
| `test_name_mismatch` | PASS | |
| `test_tags_not_list` | PASS | |
| `test_sub_skills_not_list` | PASS | |
| `test_sub_skill_missing_name` | PASS | |
| `test_sub_skill_missing_file` | PASS | |

### TestBuildContentIndex (5 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_empty_skills_dir` | PASS | |
| `test_indexes_skill_md` | PASS | Verifies index key format `"name:SKILL.md"` |
| `test_indexes_references` | PASS | Verifies sub_skill extracted from `ref_file.stem` |
| `test_content_is_lowercased` | PASS | |
| `test_multiple_skills_indexed` | PASS | |

### TestLoadIndex (5 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_loads_skills` | PASS | |
| `test_loads_multiple_skills` | PASS | |
| `test_handles_invalid_json` | PASS | `"Invalid JSON"` in validation_errors |
| `test_skips_non_directories` | PASS | |
| `test_builds_content_index` | PASS | Checks `_CONTENT_INDEX is not None` |

### TestGetIndex (2 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_caches_index` | PASS | `index1 is index2` identity check |
| `test_loads_on_first_call` | PASS | |

### TestTrackUsage (4 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_tracks_tool_calls` | PASS | |
| `test_tracks_skill_loads` | PASS | |
| `test_tracks_searches` | PASS | |
| `test_limits_search_history` | PASS | Deque maxlen=100 enforced by production code |

### TestCheckForChanges (4 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_detects_new_file` | PASS | |
| `test_detects_modified_file` | PASS | Uses `time.sleep(0.1)` to force mtime change |
| `test_detects_deleted_file` | PASS | |
| `test_no_changes` | PASS | |

### TestExtractSnippet (6 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_extracts_around_match` | PASS | |
| `test_adds_ellipsis_before` | PASS | |
| `test_adds_ellipsis_after` | PASS | |
| `test_fallback_to_beginning` | PASS | |
| `test_finds_first_word` | PASS | |
| `test_removes_newlines` | PASS | |

### TestListSkills (4 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_lists_all_skills` | PASS | |
| `test_includes_required_fields` | PASS | Checks `name`, `description`, `sub_skills` |
| `test_lists_sub_skills` | PASS | |
| `test_tracks_usage` | PASS | |

### TestGetSkill (6 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_gets_existing_skill` | PASS | |
| `test_returns_error_for_missing_skill` | PASS | |
| `test_includes_sub_skills_list` | PASS | |
| `test_indicates_references_exist` | PASS | |
| `test_indicates_no_references` | PASS | `sample_skill_minimal` has no `references/` dir |
| `test_tracks_usage` | PASS | |

### TestGetSubSkill (4 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_gets_existing_sub_skill` | PASS | |
| `test_returns_error_for_missing_domain` | PASS | |
| `test_returns_error_for_missing_sub_skill` | PASS | |
| `test_returns_error_for_missing_file` | PASS | Creates broken-skill with sub_skill pointing to nonexistent file |

### TestGetSkillsBatch (3 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_gets_multiple_skills` | PASS | |
| `test_gets_mixed_skills_and_sub_skills` | PASS | |
| `test_handles_missing_skills_in_batch` | PASS | |

### TestSearchSkills (8 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_finds_by_name` | PASS | |
| `test_finds_by_description` | PASS | |
| `test_finds_by_tags` | PASS | |
| `test_finds_sub_skills_by_name` | PASS | |
| `test_finds_sub_skills_by_triggers` | PASS | Searches `"zod"` which is in forms/validation triggers |
| `test_respects_limit` | PASS | |
| `test_sorts_by_score` | PASS | |
| `test_tracks_usage` | PASS | |

### TestSearchContent (7 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_finds_exact_phrase` | PASS | |
| `test_finds_all_words` | PASS | |
| `test_finds_partial_words` | PASS | Weak assertion (`len(matches) >= 0`) |
| `test_includes_snippet` | PASS | |
| `test_respects_limit` | PASS | |
| `test_boosts_early_matches` | PASS | |
| `test_handles_empty_index` | PASS | |

### TestReloadIndex (3 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_reloads_index` | PASS | |
| `test_returns_counts` | PASS | Checks `skill_count` and `content_files_indexed` |
| `test_returns_validation_errors` | PASS | |

### TestGetStats (5 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_returns_uptime` | PASS | |
| `test_returns_tool_calls` | PASS | |
| `test_returns_skill_loads` | PASS | |
| `test_returns_recent_searches` | PASS | |
| `test_returns_total_skills` | PASS | |

### TestValidateSkills (8 tests)

| Test | Status | Notes |
|------|--------|-------|
| `test_valid_skills_pass` | PASS | |
| `test_detects_missing_meta` | PASS | |
| `test_detects_missing_skill_md` | PASS | |
| `test_detects_invalid_json` | PASS | |
| `test_warns_about_missing_tags` | PASS | |
| `test_warns_about_no_sub_skills` | PASS | |
| `test_detects_missing_sub_skill_files` | PASS | |
| `test_returns_skills_checked_count` | PASS | |

---

## Summary

| File | Tests | PASS | FAIL | STALE | UNTESTABLE |
|------|-------|------|------|-------|------------|
| test_api.py | 57 | 57 | 0 | 0 | 0 |
| test_app.py | 44 | 44 | 0 | 0 | 0 |
| test_server.py | 88 | 88 | 0 | 0 | 0 |
| **Total** | **189** | **189** | **0** | **0** | **0** |

---

## Fixes Needed

**None.** All 189 tests pass against the current codebase. No broken symbols, no wrong patch surfaces, no stale behavior.

---

## Observations & Maintenance Notes

These are not failures, but areas to watch for future drift:

### 1. Fragile `call_args` Inspection (2 tests)

`test_api.py::TestClaudeRunEndpoint::test_includes_skill_context` and `test_app.py::TestClaudeRunEndpoint::test_includes_context` both inspect `mock.call_args[0][0][2]` to verify the CLI prompt. This depends on `subprocess.run` being called with the command list as its first positional arg, and the prompt being at index 2 (`[cli_path, '-p', prompt]`). Any refactor to keyword args or different CLI flags would break these two tests.

### 2. Weak Assertions (2 tests)

- `test_api.py::TestListSkillsEndpoint::test_extracts_description_from_frontmatter` — only checks `description is not None`; the fixture already provides description via `_meta.json`, so the frontmatter extraction path is never actually exercised.
- `test_server.py::TestSearchContent::test_finds_partial_words` — asserts `len(matches) >= 0`, which is always true. This is effectively a no-op assertion.

### 3. Duplicate Coverage

`test_api.py` and `test_app.py` both test `sanitize_name` and `find_claude_cli` from `core`. Since both Flask apps delegate to the same `core` module, these tests are redundant (not harmful, but worth knowing).

### 4. Fixture Isolation via Global Mutation

The `flask_test_client`, `flask_app_test_client`, and `server_module` fixtures directly mutate module-level globals (`config._skills_dir`, `server.SKILLS_DIR`, `server._INDEX`, etc.) and restore them in teardown. This works because pytest runs tests sequentially within a file, but would break under parallel execution (e.g., `pytest-xdist`).

### 5. No `/api/claude/improve-skill` Route in `skills_manager_app.py`

`skills_manager_app.py` does not import `improve_skill_with_claude` or define an improve-skill route. `test_app.py` correctly does not test it. The route only exists in `skills_manager_api.py`.

### 6. Reload Endpoint Is a No-Op in Both Flask Apps

Both `skills_manager_api.py` and `skills_manager_app.py` return a static success response from `POST /api/reload` without actually reloading any index. The tests correctly verify this trivial behavior. If real reload logic is expected, the endpoints and tests need updating.
