from fastapi import APIRouter, Depends

from app.actions.media import next_track, play_pause, previous_track
from app.auth import require_session

router = APIRouter(
    prefix="/actions/media",
    tags=["Media"],
)


@router.post("/play-pause")
def media_play_pause(
    token: str = Depends(require_session),
):
    play_pause()

    return {
        "status": "success",
        "action": "media_play_pause",
    }


@router.post("/next")
def media_next(
    token: str = Depends(require_session),
):
    next_track()

    return {
        "status": "success",
        "action": "media_next",
    }


@router.post("/previous")
def media_previous(
    token: str = Depends(require_session),
):
    previous_track()

    return {
        "status": "success",
        "action": "media_previous",
    }
