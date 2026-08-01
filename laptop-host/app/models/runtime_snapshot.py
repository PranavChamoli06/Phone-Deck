"""
Runtime snapshot models.

These models represent the current runtime state
that is synchronized with connected mobile devices.
"""

from pydantic import BaseModel

from app.models.profile import Button


class RuntimeSnapshot(BaseModel):
    """
    Complete runtime state sent to a mobile client.
    """

    profile: str
    page: str
    buttons: list[Button]


class RuntimeRequest(BaseModel):
    """
    Request for the current runtime snapshot.
    """

    pass