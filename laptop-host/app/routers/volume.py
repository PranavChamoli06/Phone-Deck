from fastapi import APIRouter, Depends

from app.actions.volume import toggle_mute, volume_down, volume_up
from app.auth import require_session

router = APIRouter(
    prefix="/actions/volume",
    tags=["Volume"],
)


@router.post("/up")
def system_volume_up(
    token: str = Depends(require_session),
):
    volume_up()

    return {
        "status": "success",
        "action": "volume_up",
    }


@router.post("/down")
def system_volume_down(
    token: str = Depends(require_session),
):
    volume_down()

    return {
        "status": "success",
        "action": "volume_down",
    }


@router.post("/mute")
def system_volume_mute(
    token: str = Depends(require_session),
):
    toggle_mute()

    return {
        "status": "success",
        "action": "volume_mute_toggle",
    }
