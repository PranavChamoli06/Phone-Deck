from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class ButtonAction(BaseModel):
    action: str
    args: dict[str, Any] = Field(default_factory=dict)


class Button(BaseModel):
    id: str
    label: str
    icon: str | None = None
    action: ButtonAction


class Profile(BaseModel):
    id: str
    name: str
    buttons: list[Button] = Field(default_factory=list)
