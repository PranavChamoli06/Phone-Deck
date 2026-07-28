from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class ConfigManager:
    def __init__(self) -> None:
        config_dir = Path(__file__).parent / "config"

        self.profiles_file = config_dir / "profiles.json"
        self.macros_file = config_dir / "macros.json"
        self.settings_file = config_dir / "settings.json"

    def _read_json(self, path: Path) -> Any:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def _write_json(self, path: Path, data: Any) -> None:
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_profiles(self) -> list[dict[str, Any]]:
        return self._read_json(self.profiles_file)

    def save_profiles(self, profiles: list[dict[str, Any]]) -> None:
        self._write_json(self.profiles_file, profiles)

    def load_macros(self) -> list[dict[str, Any]]:
        return self._read_json(self.macros_file)

    def save_macros(self, macros: list[dict[str, Any]]) -> None:
        self._write_json(self.macros_file, macros)

    def load_settings(self) -> dict[str, Any]:
        return self._read_json(self.settings_file)

    def save_settings(self, settings: dict[str, Any]) -> None:
        self._write_json(self.settings_file, settings)


config_manager = ConfigManager()
