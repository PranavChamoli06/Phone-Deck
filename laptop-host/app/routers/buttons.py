from __future__ import annotations

from fastapi import APIRouter, Depends

from app.auth import require_session
from app.button_service import button_service
from app.models.profile import Button

router = APIRouter(
    prefix="/profiles/{profile_id}/buttons",
    tags=["Buttons"],
)


@router.get("", response_model=list[Button])
def get_buttons(
    profile_id: str,
    token: str = Depends(require_session),
):
    return button_service.get_buttons(profile_id)


@router.post("", response_model=Button, status_code=201)
def add_button(
    profile_id: str,
    button: Button,
    token: str = Depends(require_session),
):
    return button_service.add_button(profile_id, button)


@router.put("/{button_id}", response_model=Button)
def update_button(
    profile_id: str,
    button_id: str,
    button: Button,
    token: str = Depends(require_session),
):
    return button_service.update_button(
        profile_id,
        button_id,
        button,
    )


@router.delete("/{button_id}", status_code=204)
def delete_button(
    profile_id: str,
    button_id: str,
    token: str = Depends(require_session),
):
    button_service.delete_button(
        profile_id,
        button_id,
    )
