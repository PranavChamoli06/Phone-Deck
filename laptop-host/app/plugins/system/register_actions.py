from __future__ import annotations

from app.plugins.system.actions.clipboard import register_clipboard_actions
from app.plugins.system.actions.display import register_display_actions
from app.plugins.system.actions.explorer import register_explorer_actions
from app.plugins.system.actions.media import register_media_actions
from app.plugins.system.actions.power import register_power_actions
from app.plugins.system.actions.volume import register_volume_actions
from app.plugins.system.actions.window import register_window_actions


def register_system_actions() -> None:
    """
    Register all System Plugin actions.
    """
    register_volume_actions()
    register_media_actions()
    register_power_actions()
    register_clipboard_actions()
    register_display_actions()
    register_window_actions()
    register_explorer_actions()
