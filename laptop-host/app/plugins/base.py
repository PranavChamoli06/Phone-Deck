from __future__ import annotations

from abc import ABC, abstractmethod

from app.plugins.events import PluginEvent, plugin_event_bus


class Plugin(ABC):
    """
    Base class for every Phone Deck plugin.
    """

    @property
    @abstractmethod
    def id(self) -> str: ...

    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def version(self) -> str: ...

    @property
    @abstractmethod
    def author(self) -> str:
        """
        Plugin author.
        """
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Short plugin description.
        """
        ...

    @abstractmethod
    def register(self) -> None:
        """
        Register actions.
        """
        ...

    def initialize(self) -> None:
        """
        Called after registration.
        Override if needed.
        """

    def shutdown(self) -> None:
        """
        Called before application shutdown.
        Override if needed.
        """

    async def emit(self, event_type: str, payload: dict) -> None:
        """
        Publish a plugin event.
        """
        await plugin_event_bus.publish(
            PluginEvent(
                plugin_id=self.id,
                event_type=event_type,
                payload=payload,
            )
        )

    def subscribe(
        self,
        event_type: str,
        handler,
    ) -> None:
        """
        Subscribe to a plugin event.
        """
        plugin_event_bus.subscribe(
            event_type,
            handler,
        )
