from __future__ import annotations

from fastapi import HTTPException

from app.action_registry import registry
from app.models.profile import Profile
from app.profile_repository import profile_repository
from app.settings_service import settings_service


class ProfileService:
    def load_profiles(self) -> list[Profile]:
        return profile_repository.load()

    def save_profiles(self, profiles: list[Profile]) -> None:
        self.validate_profiles(profiles)
        profile_repository.save(profiles)

    def validate_profiles(
        self,
        profiles: list[Profile],
    ) -> None:
        profile_ids: set[str] = set()

        for profile in profiles:
            if profile.id in profile_ids:
                raise HTTPException(
                    status_code=400,
                    detail=f"Duplicate profile ID: {profile.id}",
                )

            profile_ids.add(profile.id)

            button_ids: set[str] = set()

            for button in profile.buttons:
                if button.id in button_ids:
                    raise HTTPException(
                        status_code=400,
                        detail=(
                            f"Duplicate button ID '{button.id}' "
                            f"in profile '{profile.id}'"
                        ),
                    )

                button_ids.add(button.id)

                if not registry.exists(button.action.action):
                    raise HTTPException(
                        status_code=400,
                        detail=(
                            f"Unknown action '{button.action.action}' "
                            f"in profile '{profile.id}'"
                        ),
                    )

    def get_profile(self, profile_id: str) -> Profile:
        for profile in self.load_profiles():
            if profile.id == profile_id:
                return profile

        raise HTTPException(
            status_code=404,
            detail=f"Profile '{profile_id}' not found.",
        )

    def create_profile(self, profile: Profile) -> Profile:
        profiles = self.load_profiles()

        if any(existing.id == profile.id for existing in profiles):
            raise HTTPException(
                status_code=409,
                detail=f"Profile '{profile.id}' already exists.",
            )

        profiles.append(profile)
        self.save_profiles(profiles)

        return profile

    def update_profile(
        self,
        profile_id: str,
        profile: Profile,
    ) -> Profile:
        profiles = self.load_profiles()

        for index, existing in enumerate(profiles):
            if existing.id == profile_id:
                if profile.id != profile_id:
                    raise HTTPException(
                        status_code=400,
                        detail="Profile ID cannot be changed.",
                    )

                profiles[index] = profile
                self.save_profiles(profiles)

                return profile

        raise HTTPException(
            status_code=404,
            detail=f"Profile '{profile_id}' not found.",
        )

    def delete_profile(self, profile_id: str) -> None:
        profiles = self.load_profiles()

        for index, profile in enumerate(profiles):
            if profile.id == profile_id:
                del profiles[index]
                self.save_profiles(profiles)
                return

        raise HTTPException(
            status_code=404,
            detail=f"Profile '{profile_id}' not found.",
        )

    def get_active_profile(self) -> Profile:
        active_profile_id = settings_service.get_active_profile()
        return self.get_profile(active_profile_id)


profile_service = ProfileService()
