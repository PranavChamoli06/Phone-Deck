from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from app.auth import require_session
from app.event_broadcaster import event_broadcaster
from app.models.events import ButtonStateChangedData, ButtonStateChangedEvent
from app.runtime_state_manager import runtime_state_manager

router = APIRouter(
    prefix="/runtime-state",
    tags=["Runtime State"],
)


@router.put("/buttons/{button_id}")
async def update_button(
    button_id: str,
    label: str | None = None,
    icon: str | None = None,
    token: str = Depends(require_session),
):
    button = runtime_state_manager.update_button(
        button_id,
        label=label,
        icon=icon,
    )

    if button is None:
        raise HTTPException(
            status_code=404,
            detail=f"Runtime button '{button_id}' not found.",
        )

    await event_broadcaster.broadcast(
        ButtonStateChangedEvent(
            data=ButtonStateChangedData(
                button=button.id,
                label=button.label,
                icon=button.icon,
            )
        )
    )

    return button
