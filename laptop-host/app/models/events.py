from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class Event(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    data: dict[str, Any]


class ButtonExecutedData(BaseModel):
    button: str
    action: str


class ButtonExecutedEvent(Event):
    type: str = "button_executed"
    data: ButtonExecutedData


class ButtonStateChangedData(BaseModel):
    button: str
    label: str
    icon: str


class ButtonStateChangedEvent(Event):
    type: str = "button_state_changed"
    data: ButtonStateChangedData

from app.models.profile import Button


class RuntimeStateData(BaseModel):
    buttons: list[Button]

class RuntimeStateEvent(Event):
    type: str = "runtime_state"
    data: RuntimeStateData


from app.models.profile import Profile


class ProfileChangedData(BaseModel):
    profile: Profile


class ProfileChangedEvent(Event):
    type: str = "profile_changed"
    data: ProfileChangedData
