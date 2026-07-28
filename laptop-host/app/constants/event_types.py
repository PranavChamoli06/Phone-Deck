from enum import StrEnum


class EventType(StrEnum):
    CONNECTED = "connected"
    BUTTON_EXECUTED = "button_executed"
    BUTTON_STATE_CHANGED = "button_state_changed"
    RUNTIME_STATE = "runtime_state"
    PROFILE_CHANGED = "profile_changed"
