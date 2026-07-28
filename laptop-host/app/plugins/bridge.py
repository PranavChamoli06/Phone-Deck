from __future__ import annotations

from app.event_broadcaster import event_broadcaster
from app.plugins.events import PluginEvent
from app.schemas.plugin_events import PluginEventResponse


class PluginEventBridge:
    """
    Bridges plugin events into the application event system.
    """

    async def handle(self, event: PluginEvent) -> None:
        """
        Forward plugin events into the application event system.
        """

        await event_broadcaster.broadcast(
            PluginEventResponse(
                plugin_id=event.plugin_id,
                event_type=event.event_type,
                payload=event.payload,
                timestamp=event.timestamp,
            )
        )


from app.plugins.events import plugin_event_bus


def initialize_plugin_bridge() -> None:
    """
    Subscribe the bridge to all plugin events.
    """

    plugin_event_bus.subscribe(
        "*",
        plugin_event_bridge.handle,
    )


plugin_event_bridge = PluginEventBridge()
