from __future__ import annotations

import ctypes

from app.action_registry import registry

user32 = ctypes.windll.user32

KEYEVENTF_KEYUP = 0x0002

VK_MEDIA_PLAY_PAUSE = 0xB3
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1


def _press_key(vk: int) -> None:
    user32.keybd_event(vk, 0, 0, 0)
    user32.keybd_event(vk, 0, KEYEVENTF_KEYUP, 0)


async def play_pause(parameters: dict | None = None):
    _press_key(VK_MEDIA_PLAY_PAUSE)

    return {
        "status": "success",
    }


async def next_track(parameters: dict | None = None):
    _press_key(VK_MEDIA_NEXT_TRACK)

    return {
        "status": "success",
    }


async def previous_track(parameters: dict | None = None):
    _press_key(VK_MEDIA_PREV_TRACK)

    return {
        "status": "success",
    }


def register_media_actions() -> None:
    registry.register(
        name="media.play_pause",
        action=play_pause,
        description="Toggle media play/pause.",
        category="media",
    )

    registry.register(
        name="media.next",
        action=next_track,
        description="Play the next media track.",
        category="media",
    )

    registry.register(
        name="media.previous",
        action=previous_track,
        description="Play the previous media track.",
        category="media",
    )
