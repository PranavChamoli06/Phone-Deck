from __future__ import annotations

import pyperclip

from app.action_registry import registry


async def get_text(**kwargs):
    return {
        "status": "success",
        "text": pyperclip.paste(),
    }


async def set_text(text: str = "", **kwargs):
    pyperclip.copy(text)

    return {
        "status": "success",
    }


async def clear(**kwargs):
    pyperclip.copy("")

    return {
        "status": "success",
    }


def register_clipboard_actions() -> None:
    registry.register(
        name="clipboard.get_text",
        action=get_text,
        description="Read text from the system clipboard.",
        category="clipboard",
    )

    registry.register(
        name="clipboard.set_text",
        action=set_text,
        description="Write text to the system clipboard.",
        category="clipboard",
    )

    registry.register(
        name="clipboard.clear",
        action=clear,
        description="Clear the system clipboard.",
        category="clipboard",
    )
