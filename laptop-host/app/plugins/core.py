from __future__ import annotations

from app.plugins.base import Plugin
from app.register_actions import register_all_actions


class CorePlugin(Plugin):
    """
    Built-in Phone Deck functionality.
    """

    @property
    def id(self) -> str:
        return "core"

    @property
    def name(self) -> str:
        return "Core"

    @property
    def version(self) -> str:
        return "1.0.0"

    def register(self) -> None:
        """
        Register all built-in actions.
        """
        register_all_actions()

    @property
    def author(self) -> str:
        return "Phone Deck"

    @property
    def description(self) -> str:
        return "Built-in Phone Deck functionality."
