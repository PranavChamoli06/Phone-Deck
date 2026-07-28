from __future__ import annotations

from app.models.profile import Button


class RuntimeStateManager:
    def __init__(self):
        self.button_states: dict[str, Button] = {}

    def get_button(
        self,
        button_id: str,
    ) -> Button | None:
        return self.button_states.get(button_id)

    def set_button(
        self,
        button: Button,
    ) -> None:
        self.button_states[button.id] = button

    def remove_button(
        self,
        button_id: str,
    ) -> None:
        self.button_states.pop(button_id, None)

    def clear(self) -> None:
        self.button_states.clear()

    def all_buttons(self) -> list[Button]:
        return list(self.button_states.values())

    def update_button(
        self,
        button_id: str,
        *,
        label: str | None = None,
        icon: str | None = None,
    ) -> Button | None:
        button = self.button_states.get(button_id)

        if button is None:
            return None

        if label is not None:
            button.label = label

        if icon is not None:
            button.icon = icon

        return button

    def snapshot(self) -> list[Button]:
        """
        Returns a copy of the current runtime button list.
        """
        return list(self.button_states.values())

    def initialize_profile(
        self,
        buttons: list[Button],
    ) -> None:
        """
        Replace the current runtime state with the buttons
        from the newly active profile.
        """
        self.clear()

        for button in buttons:
            self.set_button(button)


runtime_state_manager = RuntimeStateManager()
