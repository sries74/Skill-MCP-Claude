# core/security.py
# Shared security validation functions
# Used by server.py, skills_manager_api.py, skills_manager_app.py, and core/skills.py

import re
from pathlib import Path

from .config import get_skills_dir


def is_safe_skill_name(name: str) -> bool:
    """Validate that a skill name is safe for filesystem operations.

    Rejects empty strings, non-strings, path separators, dot-dot sequences,
    null bytes, and anything outside [a-zA-Z0-9_-].
    """
    if not name or not isinstance(name, str):
        return False
    if '\x00' in name:
        return False
    return bool(re.match(r'^[a-zA-Z0-9\-_]+$', name))


def validate_skill_path(skill_path: Path) -> bool:
    """Validate that a resolved path is within the skills directory.

    Handles absolute path injection, symlink escapes, and traversal.
    """
    try:
        resolved_path = skill_path.resolve()
        skills_dir_resolved = get_skills_dir().resolve()
        resolved_path.relative_to(skills_dir_resolved)
        return True
    except (OSError, ValueError):
        return False


def validate_file_path(file_path: str) -> bool:
    """Validate a relative file path component for safety.

    Rejects absolute paths, null bytes, and path traversal attempts.
    """
    if not file_path or not isinstance(file_path, str):
        return False
    if '\x00' in file_path:
        return False
    if file_path.startswith('/') or file_path.startswith('\\'):
        return False
    if '..' in file_path.split('/') or '..' in file_path.replace('\\', '/').split('/'):
        return False
    return True


def sanitize_description(description: str) -> str:
    """Sanitize a skill description for safe storage and display.

    Strips null bytes and control characters (except newline/tab).
    Descriptions may contain markdown — we preserve that but remove
    characters that could cause injection in YAML frontmatter or HTML contexts.
    """
    if not description or not isinstance(description, str):
        return ""
    # Remove null bytes
    description = description.replace('\x00', '')
    # Remove control characters except \n and \t
    description = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', description)
    return description


# Allowed file extensions for upload
ALLOWED_EXTENSIONS = {
    # Text/docs
    '.md', '.json', '.txt', '.yaml', '.yml', '.toml',
    # Code
    '.py', '.js', '.ts', '.jsx', '.tsx', '.css', '.html', '.sh',
    # Data/binary
    '.bin', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.webp', '.pdf',
}

# Max file size for uploads (5MB)
MAX_FILE_SIZE = 5 * 1024 * 1024


def validate_upload_file(file_path: str, content_size: int) -> str | None:
    """Validate an uploaded file's extension and size.

    Returns an error message string if invalid, None if valid.
    """
    if content_size > MAX_FILE_SIZE:
        return f"File too large: {content_size} bytes (max {MAX_FILE_SIZE})"

    from pathlib import PurePosixPath
    ext = PurePosixPath(file_path).suffix.lower()
    if ext and ext not in ALLOWED_EXTENSIONS:
        return f"Disallowed file extension: {ext}"

    return None
