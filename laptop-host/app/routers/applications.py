from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.actions.applications import (
    open_calculator,
    open_cmd,
    open_desktop,
    open_downloads,
    open_github,
    open_google,
    open_notepad,
    open_paint,
    open_target,
)
from app.auth import require_session


class OpenTargetRequest(BaseModel):
    target: str


router = APIRouter(
    prefix="/actions/applications",
    tags=["Applications"],
)


@router.post("/notepad")
def launch_notepad(
    token: str = Depends(require_session),
):
    open_notepad()

    return {
        "status": "success",
        "action": "launch_notepad",
    }


@router.post("/calculator")
def launch_calculator(
    token: str = Depends(require_session),
):
    open_calculator()

    return {
        "status": "success",
        "action": "launch_calculator",
    }


@router.post("/paint")
def launch_paint(
    token: str = Depends(require_session),
):
    open_paint()

    return {
        "status": "success",
        "action": "launch_paint",
    }


@router.post("/cmd")
def launch_cmd(
    token: str = Depends(require_session),
):
    open_cmd()

    return {
        "status": "success",
        "action": "launch_cmd",
    }


@router.post("/desktop")
def launch_desktop(
    token: str = Depends(require_session),
):
    open_desktop()

    return {
        "status": "success",
        "action": "open_desktop",
    }


@router.post("/downloads")
def launch_downloads(
    token: str = Depends(require_session),
):
    open_downloads()

    return {
        "status": "success",
        "action": "open_downloads",
    }


@router.post("/google")
def launch_google(
    token: str = Depends(require_session),
):
    open_google()

    return {
        "status": "success",
        "action": "open_google",
    }


@router.post("/github")
def launch_github(
    token: str = Depends(require_session),
):
    open_github()

    return {
        "status": "success",
        "action": "open_github",
    }


@router.post("/open")
def launch_target(
    request: OpenTargetRequest,
    token: str = Depends(require_session),
):
    open_target(request.target)

    return {
        "status": "success",
        "action": "open_target",
        "target": request.target,
    }
