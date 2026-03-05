# test_security.py - Tests for core/security.py and path traversal hardening
import pytest
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.security import is_safe_skill_name, validate_skill_path, validate_file_path


class TestIsSafeSkillName:
    """Tests for is_safe_skill_name validation."""

    def test_valid_names(self):
        assert is_safe_skill_name("my-skill") is True
        assert is_safe_skill_name("skill123") is True
        assert is_safe_skill_name("my_skill") is True
        assert is_safe_skill_name("A-Z") is True

    def test_rejects_empty(self):
        assert is_safe_skill_name("") is False
        assert is_safe_skill_name(None) is False

    def test_rejects_path_traversal(self):
        assert is_safe_skill_name("../etc/passwd") is False
        assert is_safe_skill_name("..") is False
        assert is_safe_skill_name("foo/../bar") is False

    def test_rejects_absolute_paths(self):
        assert is_safe_skill_name("/etc/passwd") is False
        assert is_safe_skill_name("/tmp/evil") is False

    def test_rejects_null_bytes(self):
        assert is_safe_skill_name("skill\x00evil") is False

    def test_rejects_special_chars(self):
        assert is_safe_skill_name("skill name") is False
        assert is_safe_skill_name("skill.name") is False
        assert is_safe_skill_name("skill/name") is False
        assert is_safe_skill_name("skill\\name") is False

    def test_rejects_non_string(self):
        assert is_safe_skill_name(123) is False
        assert is_safe_skill_name([]) is False


class TestValidateSkillPath:
    """Tests for validate_skill_path validation."""

    def test_valid_path(self, temp_skills_dir):
        import core.config as config
        original = config._skills_dir
        config._skills_dir = temp_skills_dir
        try:
            path = temp_skills_dir / "my-skill"
            assert validate_skill_path(path) is True
        finally:
            config._skills_dir = original

    def test_rejects_traversal(self, temp_skills_dir):
        import core.config as config
        original = config._skills_dir
        config._skills_dir = temp_skills_dir
        try:
            path = temp_skills_dir / ".." / "etc" / "passwd"
            assert validate_skill_path(path) is False
        finally:
            config._skills_dir = original

    def test_rejects_absolute_escape(self, temp_skills_dir):
        import core.config as config
        original = config._skills_dir
        config._skills_dir = temp_skills_dir
        try:
            path = Path("/tmp/evil")
            assert validate_skill_path(path) is False
        finally:
            config._skills_dir = original


class TestValidateFilePath:
    """Tests for validate_file_path validation."""

    def test_valid_paths(self):
        assert validate_file_path("SKILL.md") is True
        assert validate_file_path("references/advanced.md") is True
        assert validate_file_path("scripts/helper.py") is True

    def test_rejects_empty(self):
        assert validate_file_path("") is False
        assert validate_file_path(None) is False

    def test_rejects_traversal(self):
        assert validate_file_path("../../../etc/passwd") is False
        assert validate_file_path("foo/../bar") is False

    def test_rejects_absolute(self):
        assert validate_file_path("/etc/passwd") is False
        assert validate_file_path("\\server\\share") is False

    def test_rejects_null_bytes(self):
        assert validate_file_path("file\x00.md") is False


class TestCoreSkillsPathTraversal:
    """Tests for path traversal prevention in core/skills.py CRUD operations."""

    def test_get_skill_rejects_dotdot_encoded(self, flask_test_client):
        """core/skills.py get_skill_by_name rejects traversal names."""
        from core.skills import get_skill_by_name
        result, error = get_skill_by_name("../../../etc/passwd")
        assert error is not None
        assert "Invalid" in error

    def test_get_skill_rejects_absolute_path(self, flask_test_client):
        """core/skills.py get_skill_by_name rejects absolute paths."""
        from core.skills import get_skill_by_name
        result, error = get_skill_by_name("/etc/passwd")
        assert error is not None
        assert "Invalid" in error

    def test_update_skill_rejects_traversal(self, flask_test_client):
        """core/skills.py update_skill rejects traversal names."""
        from core.skills import update_skill
        result, error = update_skill("../../../etc/passwd", "evil", "evil")
        assert error is not None
        assert "Invalid" in error

    def test_delete_skill_rejects_traversal(self, flask_test_client):
        """core/skills.py delete_skill rejects traversal names."""
        from core.skills import delete_skill
        result, error = delete_skill("../../../etc/passwd")
        assert error is not None
        assert "Invalid" in error

    def test_delete_skill_rejects_absolute(self, flask_test_client):
        """core/skills.py delete_skill rejects absolute paths."""
        from core.skills import delete_skill
        result, error = delete_skill("/tmp/evil")
        assert error is not None
        assert "Invalid" in error

    def test_create_skill_sanitizes_traversal_name(self, flask_test_client, temp_skills_dir):
        """create_skill sanitizes traversal names into safe names."""
        response = flask_test_client.post('/api/skills',
            json={"name": "../../../etc/evil", "description": "test", "content": "test"})
        assert response.status_code == 200
        data = response.get_json()
        # Sanitized to "etc-evil", NOT written to /etc/evil
        assert data["name"] == "etc-evil"
        assert (temp_skills_dir / "etc-evil" / "SKILL.md").exists()
        assert not Path("/etc/evil").exists()

    def test_import_folder_sanitizes_traversal_name(self, flask_test_client, temp_skills_dir):
        """import_folder sanitizes traversal names."""
        # Create a source directory
        src = temp_skills_dir.parent / "src-skill"
        src.mkdir()
        (src / "SKILL.md").write_text("# Test")
        response = flask_test_client.post('/api/import/folder',
            json={"path": str(src), "name": "../../../evil"})
        assert response.status_code == 200
        data = response.get_json()
        assert data["name"] == "evil"  # sanitized, not a traversal

    def test_import_json_rejects_absolute_file_path(self, flask_test_client, temp_skills_dir):
        response = flask_test_client.post('/api/import/json',
            json={
                "skill_name": "safe-skill",
                "files": [
                    {"path": "/etc/cron.d/backdoor", "content": "evil"}
                ]
            })
        assert response.status_code == 200
        data = response.get_json()
        assert len(data["files_imported"]) == 0

    def test_import_json_rejects_null_bytes(self, flask_test_client, temp_skills_dir):
        response = flask_test_client.post('/api/import/json',
            json={
                "skill_name": "safe-skill",
                "files": [
                    {"path": "file\x00.md", "content": "evil"}
                ]
            })
        assert response.status_code == 200
        data = response.get_json()
        assert len(data["files_imported"]) == 0

    def test_browse_rejects_traversal(self, flask_test_client):
        response = flask_test_client.get('/api/browse?path=../../etc')
        assert response.status_code in (403, 404)
        data = response.get_json()
        assert "error" in data


class TestCoreSkillsPathTraversalApp:
    """Mirror path traversal tests for the standalone app."""

    def test_create_skill_sanitizes_traversal_name(self, flask_app_test_client, temp_skills_dir):
        """create_skill sanitizes traversal names into safe names."""
        response = flask_app_test_client.post('/api/skills',
            json={"name": "../../../etc/evil", "description": "test", "content": "test"})
        assert response.status_code == 200
        data = response.get_json()
        assert data["name"] == "etc-evil"

    def test_browse_rejects_traversal(self, flask_app_test_client):
        response = flask_app_test_client.get('/api/browse?path=../../etc')
        assert response.status_code in (403, 404)
        data = response.get_json()
        assert "error" in data

    def test_import_json_rejects_traversal(self, flask_app_test_client, temp_skills_dir):
        response = flask_app_test_client.post('/api/import/json',
            json={
                "skill_name": "safe-skill",
                "files": [
                    {"path": "../../../etc/passwd", "content": "evil"}
                ]
            })
        assert response.status_code == 200
        data = response.get_json()
        assert len(data["files_imported"]) == 0


class TestServerPathTraversal:
    """Tests for path traversal in server.py MCP functions."""

    def test_get_skill_rejects_traversal(self, server_module):
        result = server_module._get_skill("../../../etc/passwd")
        assert "error" in result
        assert "Invalid" in result["error"]

    def test_get_skill_rejects_absolute(self, server_module):
        result = server_module._get_skill("/etc/passwd")
        assert "error" in result

    def test_get_sub_skill_rejects_traversal(self, server_module):
        result = server_module._get_sub_skill("../evil", "sub")
        assert "error" in result
        assert "Invalid" in result["error"]


# ============ Tier 1 Tests ============


class TestSanitizeDescription:
    """Tests for sanitize_description (Fix 1.2)."""

    def test_normal_description(self):
        from core.security import sanitize_description
        assert sanitize_description("A normal description") == "A normal description"

    def test_strips_null_bytes(self):
        from core.security import sanitize_description
        assert sanitize_description("hello\x00world") == "helloworld"

    def test_strips_control_chars(self):
        from core.security import sanitize_description
        result = sanitize_description("hello\x01\x02\x03world")
        assert result == "helloworld"

    def test_preserves_newlines_and_tabs(self):
        from core.security import sanitize_description
        result = sanitize_description("hello\nworld\there")
        assert result == "hello\nworld\there"

    def test_handles_yaml_special_chars(self):
        from core.security import sanitize_description
        result = sanitize_description("---\nkey: value\n---")
        assert result == "---\nkey: value\n---"

    def test_handles_html_tags(self):
        from core.security import sanitize_description
        result = sanitize_description("<script>alert('xss')</script>")
        assert result == "<script>alert('xss')</script>"

    def test_empty_and_none(self):
        from core.security import sanitize_description
        assert sanitize_description("") == ""
        assert sanitize_description(None) == ""

    def test_multiline_with_code_blocks(self):
        from core.security import sanitize_description
        desc = "A skill\n```python\nprint('hello')\n```"
        assert sanitize_description(desc) == desc


class TestValidateUploadFile:
    """Tests for validate_upload_file (Fix 1.4)."""

    def test_valid_files(self):
        from core.security import validate_upload_file
        assert validate_upload_file("SKILL.md", 100) is None
        assert validate_upload_file("script.py", 1000) is None
        assert validate_upload_file("data.json", 500) is None
        assert validate_upload_file("image.png", 1000) is None

    def test_rejects_oversized(self):
        from core.security import validate_upload_file, MAX_FILE_SIZE
        result = validate_upload_file("big.md", MAX_FILE_SIZE + 1)
        assert result is not None
        assert "too large" in result

    def test_rejects_disallowed_extension(self):
        from core.security import validate_upload_file
        result = validate_upload_file("evil.exe", 100)
        assert result is not None
        assert "Disallowed" in result

    def test_rejects_dangerous_extensions(self):
        from core.security import validate_upload_file
        for ext in ['.exe', '.dll', '.so', '.bat', '.cmd', '.ps1']:
            result = validate_upload_file(f"file{ext}", 100)
            assert result is not None, f"Should reject {ext}"

    def test_allows_no_extension(self):
        from core.security import validate_upload_file
        assert validate_upload_file("Makefile", 100) is None


class TestImportUploadValidation:
    """Tests for file upload validation in import_files_json (Fix 1.4)."""

    def test_rejects_oversized_upload(self, flask_test_client, temp_skills_dir):
        huge_content = "x" * (6 * 1024 * 1024)  # 6MB
        response = flask_test_client.post('/api/import/json',
            json={
                "skill_name": "upload-test",
                "files": [
                    {"path": "huge.md", "content": huge_content}
                ]
            })
        assert response.status_code == 200
        data = response.get_json()
        assert len(data["files_imported"]) == 0

    def test_rejects_disallowed_extension(self, flask_test_client, temp_skills_dir):
        response = flask_test_client.post('/api/import/json',
            json={
                "skill_name": "upload-test",
                "files": [
                    {"path": "evil.exe", "content": "MZ..."}
                ]
            })
        assert response.status_code == 200
        data = response.get_json()
        assert len(data["files_imported"]) == 0

    def test_rejects_null_bytes_in_content(self, flask_test_client, temp_skills_dir):
        import base64
        content_with_nulls = base64.b64encode(b"hello\x00world").decode()
        response = flask_test_client.post('/api/import/json',
            json={
                "skill_name": "upload-test",
                "files": [
                    {"path": "data.bin", "content": content_with_nulls, "base64": True}
                ]
            })
        assert response.status_code == 200
        data = response.get_json()
        assert len(data["files_imported"]) == 0


class TestSkillsDirValidation:
    """Tests for SKILLS_DIR startup validation (Fix 1.3)."""

    def test_api_fails_with_missing_skills_dir(self):
        import core.config as config
        original = config._skills_dir
        try:
            config._skills_dir = Path("/nonexistent/skills/dir")
            # Importing/using the app should handle this gracefully
            from core.skills import list_all_skills
            skills = list_all_skills()
            assert skills == []
        finally:
            config._skills_dir = original


# ============ Tier 2 Tests ============


class TestStructuredErrorResponses:
    """Tests for standardized error response format (Fix 2.1)."""

    def test_api_error_has_structured_format(self, flask_test_client):
        response = flask_test_client.get('/api/skills/nonexistent-skill-xyz')
        assert response.status_code == 404
        data = response.get_json()
        assert "error" in data
        assert isinstance(data["error"], dict)
        assert "code" in data["error"]
        assert "message" in data["error"]

    def test_app_error_has_structured_format(self, flask_app_test_client):
        response = flask_app_test_client.get('/api/skills/nonexistent-skill-xyz')
        assert response.status_code == 404
        data = response.get_json()
        assert "error" in data
        assert isinstance(data["error"], dict)
        assert "code" in data["error"]
        assert "message" in data["error"]

    def test_error_code_not_found(self, flask_test_client):
        response = flask_test_client.get('/api/skills/nonexistent-skill-xyz')
        data = response.get_json()
        assert data["error"]["code"] == "NOT_FOUND"

    def test_error_code_conflict(self, flask_test_client, sample_skill):
        response = flask_test_client.post('/api/skills',
            json={"name": "test-skill", "description": "dup", "content": "dup"})
        assert response.status_code == 409
        data = response.get_json()
        assert data["error"]["code"] == "CONFLICT"


class TestReloadEndpoint:
    """Tests for reload endpoint actually working (Fix 2.2)."""

    def test_api_reload_returns_skill_count(self, flask_test_client, sample_skill):
        response = flask_test_client.post('/api/reload')
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert "skill_count" in data
        assert data["skill_count"] >= 1

    def test_app_reload_returns_skill_count(self, flask_app_test_client, sample_skill):
        response = flask_app_test_client.post('/api/reload')
        assert response.status_code == 200
        data = response.get_json()
        assert data["success"] is True
        assert "skill_count" in data
        assert data["skill_count"] >= 1


class TestServerShutdown:
    """Tests for server shutdown function (Fix 2.3)."""

    def test_shutdown_without_watcher(self, server_module):
        """shutdown() is safe to call when watcher not started."""
        server_module.shutdown()

    def test_shutdown_stops_watcher(self, server_module):
        """shutdown() sets stop flag."""
        server_module.start_watcher()
        server_module.shutdown()
        assert server_module._watcher_stop is True
