from __future__ import annotations

from fastapi import APIRouter, Depends

from app.auth import require_session
from app.settings_service import settings_service

router = APIRouter(
    prefix="/settings",
    tags=["Settings"],
)


@router.get("/active-profile", response_model=str)
def get_active_profile(
    token: str = Depends(require_session),
):
    return settings_service.get_active_profile()


@router.put("/active-profile", response_model=str)
async def set_active_profile(
    profile_id: str,
    token: str = Depends(require_session),
):
    return await settings_service.set_active_profile(profile_id)
