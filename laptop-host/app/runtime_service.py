from __future__ import annotations

from fastapi import HTTPException

from app.action_registry import registry
from app.event_broadcaster import event_broadcaster
from app.models.events import ButtonExecutedData, ButtonExecutedEvent
from app.models.profile import Button
from app.models.runtime import ExecutionResponse
from app.profile_service import profile_service
from app.runtime_state_manager import runtime_state_manager


class RuntimeService:
    def get_active_profile(self):
        return profile_service.get_active_profile()

    def get_button(
        self,
        button_id: str,
    ) -> Button:
        runtime_button = runtime_state_manager.get_button(button_id)

        if runtime_button is not None:
            return runtime_button

        profile = self.get_active_profile()

        for button in profile.buttons:
            if button.id == button_id:
                runtime_state_manager.set_button(button)
                return button

        raise HTTPException(
            status_code=404,
            detail=f"Button '{button_id}' not found in active profile.",
        )

    async def execute_button(
        self,
        button_id: str,
    ) -> ExecutionResponse:
        button = self.get_button(button_id)

        # Execute the action
        result = await registry.execute(
            button.action.action,
            **button.action.args,
        )

        # Broadcast the event to all connected WebSocket clients
        await event_broadcaster.broadcast(
            ButtonExecutedEvent(
                data=ButtonExecutedData(
                    button=button.id,
                    action=button.action.action,
                )
            )
        )

        return ExecutionResponse(
            success=True,
            button=button.id,
            action=button.action.action,
            result=result,
        )


runtime_service = RuntimeService()
