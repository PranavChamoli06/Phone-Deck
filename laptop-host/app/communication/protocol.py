"""
Communication protocol definitions for Phone Deck.

This file contains:
- Protocol version
- Message type constants
- Helper methods
"""

import time
from enum import Enum
from typing import Any, Dict

PROTOCOL_VERSION = "1.0"

# Heartbeat configuration
HEARTBEAT_INTERVAL = 30  # seconds
HEARTBEAT_TIMEOUT = 10   # seconds


class MessageType(str, Enum):
    # Connection
    CONNECT = "CONNECT"
    DISCONNECT = "DISCONNECT"
    PING = "PING"
    PONG = "PONG"

    # Authentication
    OTP_REQUEST = "OTP_REQUEST"
    OTP_VERIFY = "OTP_VERIFY"
    AUTH_SUCCESS = "AUTH_SUCCESS"
    AUTH_FAILED = "AUTH_FAILED"

    # Actions
    ACTION_EXECUTE = "ACTION_EXECUTE"
    ACTION_RESULT = "ACTION_RESULT"
    ACTION_FAILED = "ACTION_FAILED"

    # Device
    DEVICE_INFO = "DEVICE_INFO"
    DEVICE_STATUS = "DEVICE_STATUS"

    # Controls
    BUTTON_PRESS = "BUTTON_PRESS"
    BUTTON_RELEASE = "BUTTON_RELEASE"
    SLIDER_CHANGE = "SLIDER_CHANGE"
    KNOB_ROTATE = "KNOB_ROTATE"

    # General
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"

    # Future Features
    SCREENSHOT = "SCREENSHOT"
    FILE_TRANSFER = "FILE_TRANSFER"
    MEDIA_CONTROL = "MEDIA_CONTROL"
    SYSTEM_STATUS = "SYSTEM_STATUS"
    MACRO_EXECUTE = "MACRO_EXECUTE"


def create_message(message_type: MessageType, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a standardized protocol message.
    """
    return {
        "version": PROTOCOL_VERSION,
        "type": message_type.value,
        "timestamp": int(time.time()),
        "data": data,
    }


def validate_message(message: Dict[str, Any]) -> tuple[bool, str]:
    """
    Validate that a received message follows the Phone Deck protocol.
    """

    required_fields = {
        "version",
        "type",
        "timestamp",
        "data",
    }

    missing = required_fields - message.keys()

    if missing:
        return (
            False,
            f"Missing required field(s): {', '.join(sorted(missing))}",
        )

    if message["version"] != PROTOCOL_VERSION:
        return (
            False,
            "Unsupported protocol version",
        )

    try:
        MessageType(message["type"])
    except ValueError:
        return (
            False,
            f"Unknown message type: {message['type']}",
        )

    if not isinstance(message["data"], dict):
        return (
            False,
            "'data' must be a JSON object",
        )

    return True, ""