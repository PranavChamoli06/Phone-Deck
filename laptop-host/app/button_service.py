from __future__ import annotations

from fastapi import HTTPException

from app.models.profile import Button
from app.profile_service import profile_service


class ButtonService:
    def get_profile(self, profile_id: str):
        return profile_service.get_profile(profile_id)

    def save_profile(self, profile):
        profiles = profile_service.load_profiles()

        for index, existing in enumerate(profiles):
            if existing.id == profile.id:
                profiles[index] = profile
                profile_service.save_profiles(profiles)
                return

        raise RuntimeError("Profile disappeared while saving.")

    def get_buttons(
        self,
        profile_id: str,
    ) -> list[Button]:
        profile = self.get_profile(profile_id)
        return profile.buttons

    def add_button(
        self,
        profile_id: str,
        button: Button,
    ) -> Button:
        profile = self.get_profile(profile_id)

        if any(existing.id == button.id for existing in profile.buttons):
            raise HTTPException(
                status_code=409,
                detail=f"Button '{button.id}' already exists.",
            )

        profile.buttons.append(button)
        self.save_profile(profile)

        return button

    def update_button(
        self,
        profile_id: str,
        button_id: str,
        button: Button,
    ) -> Button:
        profile = self.get_profile(profile_id)

        for index, existing in enumerate(profile.buttons):
            if existing.id == button_id:
                if button.id != button_id:
                    raise HTTPException(
                        status_code=400,
                        detail="Button ID cannot be changed.",
                    )

                profile.buttons[index] = button
                self.save_profile(profile)

                return button

        raise HTTPException(
            status_code=404,
            detail=f"Button '{button_id}' not found.",
        )

    def delete_button(
        self,
        profile_id: str,
        button_id: str,
    ) -> None:
        profile = self.get_profile(profile_id)

        for index, button in enumerate(profile.buttons):
            if button.id == button_id:
                del profile.buttons[index]
                self.save_profile(profile)
                return

        raise HTTPException(
            status_code=404,
            detail=f"Button '{button_id}' not found.",
        )


button_service = ButtonService()
