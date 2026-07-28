import secrets

_active_session_token: str | None = None


def create_session() -> str:
    global _active_session_token

    _active_session_token = secrets.token_urlsafe(32)

    return _active_session_token


def validate_session(token: str) -> bool:
    if _active_session_token is None:
        return False

    return secrets.compare_digest(
        token,
        _active_session_token,
    )


def clear_session() -> None:
    global _active_session_token

    _active_session_token = None
