from fastapi import APIRouter, Depends

from app.actions.mouse import (
    double_click,
    left_button_down,
    left_button_up,
    left_click,
    move_down,
    move_left,
    move_right,
    move_up,
    right_click,
    scroll_down,
    scroll_up,
)
from app.auth import require_session

router = APIRouter(
    prefix="/actions/mouse",
    tags=["Mouse"],
)


@router.post("/left-click")
def mouse_left_click(
    token: str = Depends(require_session),
):
    left_click()

    return {
        "status": "success",
        "action": "mouse_left_click",
    }


@router.post("/right-click")
def mouse_right_click(
    token: str = Depends(require_session),
):
    right_click()

    return {
        "status": "success",
        "action": "mouse_right_click",
    }


@router.post("/double-click")
def mouse_double_click(
    token: str = Depends(require_session),
):
    double_click()

    return {
        "status": "success",
        "action": "mouse_double_click",
    }


@router.post("/move/up")
def mouse_move_up(
    token: str = Depends(require_session),
):
    move_up()

    return {
        "status": "success",
        "action": "mouse_move_up",
    }


@router.post("/move/down")
def mouse_move_down(
    token: str = Depends(require_session),
):
    move_down()

    return {
        "status": "success",
        "action": "mouse_move_down",
    }


@router.post("/move/left")
def mouse_move_left(
    token: str = Depends(require_session),
):
    move_left()

    return {
        "status": "success",
        "action": "mouse_move_left",
    }


@router.post("/move/right")
def mouse_move_right(
    token: str = Depends(require_session),
):
    move_right()

    return {
        "status": "success",
        "action": "mouse_move_right",
    }


@router.post("/scroll/up")
def mouse_scroll_up(
    token: str = Depends(require_session),
):
    scroll_up()

    return {
        "status": "success",
        "action": "mouse_scroll_up",
    }


@router.post("/scroll/down")
def mouse_scroll_down(
    token: str = Depends(require_session),
):
    scroll_down()

    return {
        "status": "success",
        "action": "mouse_scroll_down",
    }


@router.post("/left-button/down")
def mouse_left_button_down(
    token: str = Depends(require_session),
):
    left_button_down()

    return {
        "status": "success",
        "action": "mouse_left_button_down",
    }


@router.post("/left-button/up")
def mouse_left_button_up(
    token: str = Depends(require_session),
):
    left_button_up()

    return {
        "status": "success",
        "action": "mouse_left_button_up",
    }
