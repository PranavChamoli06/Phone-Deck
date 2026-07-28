from __future__ import annotations

import inspect
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass(slots=True)
class PluginEvent:
    """
    Base event emitted by plugins.
    """

    plugin_id: str
    event_type: str
    payload: dict[str, Any]
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))


from collections.abc import Callable

EventHandler = Callable[[PluginEvent], None]


class PluginEventBus:
    """
    Simple in-process event bus for plugins.
    """

    def __init__(self) -> None:
        self._handlers: dict[str, list[EventHandler]] = {}

    def subscribe(
        self,
        event_type: str,
        handler: EventHandler,
    ) -> None:
        """
        Subscribe to a specific event type.
        """
        self._handlers.setdefault(event_type, []).append(handler)

    async def publish(self, event: PluginEvent) -> None:
        for handler in self._handlers.get(event.event_type, []):
            if inspect.iscoroutinefunction(handler):
                await handler(event)
            else:
                handler(event)

        for handler in self._handlers.get("*", []):
            if inspect.iscoroutinefunction(handler):
                await handler(event)
            else:
                handler(event)


plugin_event_bus = PluginEventBus()
