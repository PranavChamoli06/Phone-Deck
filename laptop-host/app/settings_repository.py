from __future__ import annotations

from app.config_manager import config_manager


class SettingsRepository:
    def load(self) -> dict:
        return config_manager.load_settings()

    def save(self, settings: dict) -> None:
        config_manager.save_settings(settings)


settings_repository = SettingsRepository()
