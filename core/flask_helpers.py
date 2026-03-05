# core/flask_helpers.py
# Shared Flask helpers to avoid duplication between API server and standalone app

import functools
from typing import Any, Callable
from flask import Response, jsonify, request


def error_response(code: str, message: str, status: int) -> tuple[Response, int]:
    """Return a standardized error response.

    Format: {"error": {"code": "NOT_FOUND", "message": "Skill 'foo' not found"}}
    """
    return jsonify({"error": {"code": code, "message": message}}), status


def require_json(f: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to ensure request body is valid JSON."""
    @functools.wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if not request.is_json or request.json is None:
            return error_response("INVALID_JSON", "Request body must be valid JSON", 400)
        return f(*args, **kwargs)
    return wrapper
