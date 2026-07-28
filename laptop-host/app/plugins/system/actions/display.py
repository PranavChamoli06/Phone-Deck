from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pyautogui
import screen_brightness_control as sbc

from app.action_registry import registry

SCREENSHOT_DIR = Path("screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)


async def get_brightness(**kwargs):
    brightness = sbc.get_brightness()

    if isinstance(brightness, list):
        brightness = brightness[0]

    return {
        "status": "success",
        "brightness": brightness,
    }


async def set_brightness(level: int = 50, **kwargs):
    level = max(0, min(100, int(level)))

    sbc.set_brightness(level)

    return {
        "status": "success",
        "brightness": level,
    }


async def brightness_up(step: int = 10, **kwargs):
    current = sbc.get_brightness()

    if isinstance(current, list):
        current = current[0]

    new_level = min(100, current + step)

    sbc.set_brightness(new_level)

    return {
        "status": "success",
        "brightness": new_level,
    }


async def brightness_down(step: int = 10, **kwargs):
    current = sbc.get_brightness()

    if isinstance(current, list):
        current = current[0]

    new_level = max(0, current - step)

    sbc.set_brightness(new_level)

    return {
        "status": "success",
        "brightness": new_level,
    }


async def screenshot(**kwargs):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = SCREENSHOT_DIR / f"screenshot_{timestamp}.png"

    image = pyautogui.screenshot()
    image.save(filepath)

    return {
        "status": "success",
        "path": str(filepath),
    }


async def screenshot_region(
    left: int,
    top: int,
    width: int,
    height: int,
    **kwargs,
):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = SCREENSHOT_DIR / f"region_{timestamp}.png"

    image = pyautogui.screenshot(region=(left, top, width, height))

    image.save(filepath)

    return {
        "status": "success",
        "path": str(filepath),
    }


def register_display_actions() -> None:
    registry.register(
        name="display.get_brightness",
        action=get_brightness,
        description="Get the current display brightness.",
        category="display",
    )

    registry.register(
        name="display.set_brightness",
        action=set_brightness,
        description="Set the display brightness.",
        category="display",
    )

    registry.register(
        name="display.brightness_up",
        action=brightness_up,
        description="Increase display brightness.",
        category="display",
    )

    registry.register(
        name="display.brightness_down",
        action=brightness_down,
        description="Decrease display brightness.",
        category="display",
    )

    registry.register(
        name="display.screenshot",
        action=screenshot,
        description="Capture the entire screen.",
        category="display",
    )

    registry.register(
        name="display.screenshot_region",
        action=screenshot_region,
        description="Capture a region of the screen.",
        category="display",
    )
