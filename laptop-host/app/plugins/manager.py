from __future__ import annotations

from app.plugins.base import Plugin


class PluginManager:
    """
    Manages all registered plugins.
    """

    def __init__(self) -> None:
        self._plugins: dict[str, Plugin] = {}
        self._initialized: set[str] = set()
        self._disabled: set[str] = set()

    def register(self, plugin: Plugin) -> None:
        """
        Register a plugin.
        """
        if plugin.id in self._plugins:
            raise ValueError(f"Plugin '{plugin.id}' is already registered.")

        self._plugins[plugin.id] = plugin

    def get(self, plugin_id: str) -> Plugin:
        """
        Retrieve a registered plugin.
        """
        if plugin_id not in self._plugins:
            raise KeyError(f"Unknown plugin '{plugin_id}'.")

        return self._plugins[plugin_id]

    def exists(self, plugin_id: str) -> bool:
        """
        Returns whether a plugin exists.
        """
        return plugin_id in self._plugins

    def list_plugins(self) -> list[Plugin]:
        """
        Returns all registered plugins.
        """
        return list(self._plugins.values())

    def initialize(self) -> None:
        """
        Initialize every enabled plugin.
        """
        for plugin in self._plugins.values():
            if not self.is_enabled(plugin.id):
                continue

            plugin.register()
            plugin.initialize()
            self._initialized.add(plugin.id)

    def shutdown(self) -> None:
        """
        Shutdown all plugins.
        """
        for plugin in self._plugins.values():
            plugin.shutdown()

    def is_loaded(self, plugin_id: str) -> bool:
        """
        Returns whether the plugin is registered.
        """
        return plugin_id in self._plugins

    def is_initialized(self, plugin_id: str) -> bool:
        """
        Returns whether the plugin has been initialized.
        """
        return plugin_id in self._initialized

    def is_healthy(self, plugin_id: str) -> bool:
        """
        Returns the health of a plugin.
        """
        return self.is_enabled(plugin_id) and self.is_initialized(plugin_id)

    def enable(self, plugin_id: str) -> None:
        """
        Enable a plugin.
        """
        if plugin_id not in self._plugins:
            raise KeyError(f"Unknown plugin '{plugin_id}'.")

        self._disabled.discard(plugin_id)

    def disable(self, plugin_id: str) -> None:
        """
        Disable a plugin.
        """
        if plugin_id not in self._plugins:
            raise KeyError(f"Unknown plugin '{plugin_id}'.")

        self._disabled.add(plugin_id)

    def is_enabled(self, plugin_id: str) -> bool:
        """
        Returns whether the plugin is enabled.
        """
        return plugin_id not in self._disabled


plugin_manager = PluginManager()
