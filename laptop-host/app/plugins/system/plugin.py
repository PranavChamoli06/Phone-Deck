from __future__ import annotations

from app.plugins.base import Plugin
from app.plugins.system.register_actions import register_system_actions


class SystemPlugin(Plugin):
    """
    Built-in operating system plugin.
    """

    @property
    def id(self) -> str:
        return "system"

    @property
    def name(self) -> str:
        return "System"

    @property
    def version(self) -> str:
        return "1.0.0"

    @property
    def author(self) -> str:
        return "Phone Deck"

    @property
    def description(self) -> str:
        return "Provides operating system controls."

    def register(self) -> None:
        """
        Register all system actions.
        """
        register_system_actions()
