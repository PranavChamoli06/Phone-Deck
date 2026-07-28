from __future__ import annotations

from fastapi import HTTPException

from app.event_broadcaster import event_broadcaster
from app.models.events import ProfileChangedData, ProfileChangedEvent
from app.profile_repository import profile_repository
from app.runtime_state_manager import runtime_state_manager
from app.settings_repository import settings_repository


class SettingsService:
    def load_settings(self) -> dict:
        return settings_repository.load()

    def save_settings(self, settings: dict) -> None:
        settings_repository.save(settings)

    def get_active_profile(self) -> str:
        settings = self.load_settings()
        return settings["active_profile"]

    async def set_active_profile(self, profile_id: str) -> str:
        profiles = profile_repository.load()

        profile = next(
            (p for p in profiles if p.id == profile_id),
            None,
        )

        if profile is None:
            raise HTTPException(
                status_code=404,
                detail=f"Profile '{profile_id}' not found.",
            )

        settings = self.load_settings()
        settings["active_profile"] = profile_id
        self.save_settings(settings)

        # Initialize runtime state with the newly active profile
        runtime_state_manager.initialize_profile(profile.buttons)

        # Notify all connected clients
        await event_broadcaster.broadcast(
            ProfileChangedEvent(
                data=ProfileChangedData(
                    profile=profile,
                )
            )
        )

        return profile_id


settings_service = SettingsService()
