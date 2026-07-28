from __future__ import annotations

from app.config_manager import config_manager
from app.models.profile import Profile


class ProfileRepository:
    def load(self) -> list[Profile]:
        data = config_manager.load_profiles()
        return [Profile.model_validate(profile) for profile in data]

    def save(self, profiles: list[Profile]) -> None:
        config_manager.save_profiles([profile.model_dump() for profile in profiles])


profile_repository = ProfileRepository()
