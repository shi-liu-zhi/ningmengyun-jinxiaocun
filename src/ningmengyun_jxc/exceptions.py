class JxcError(Exception):
    """Base exception for ningmengyun JXC SDK."""


class JxcApiError(JxcError):
    """API returned a non-1000 state code."""

    def __init__(self, state: int, msg: str, data=None):
        self.state = state
        self.msg = msg
        self.data = data
        super().__init__(f"[State={state}] {msg}")


class JxcAuthError(JxcApiError):
    """Authentication failed (token invalid, etc.)."""


class JxcNotFoundError(JxcApiError):
    """Resource not found."""


class JxcValidationError(JxcApiError):
    """Request validation failed."""
