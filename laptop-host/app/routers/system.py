from fastapi import APIRouter, Depends

from app.actions.system import lock_workstation, sleep_system
from app.auth import require_session

router = APIRouter(
    prefix="/actions/system",
    tags=["System"],
)


@router.post("/lock")
def system_lock(
    token: str = Depends(require_session),
):
    lock_workstation()

    return {
        "status": "success",
        "action": "system_lock",
    }


@router.post("/sleep")
def system_sleep(
    token: str = Depends(require_session),
):
    sleep_system()

    return {
        "status": "success",
        "action": "system_sleep",
    }
