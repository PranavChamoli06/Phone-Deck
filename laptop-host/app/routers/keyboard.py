from fastapi import APIRouter, Depends

from app.actions.keyboard import (
    copy,
    cut,
    find,
    paste,
    press_enter,
    press_escape,
    press_space,
    press_tab,
    redo,
    save,
    select_all,
    undo,
)
from app.auth import require_session

router = APIRouter(
    prefix="/actions/keyboard",
    tags=["Keyboard"],
)


@router.post("/enter")
def keyboard_enter(
    token: str = Depends(require_session),
):
    press_enter()

    return {
        "status": "success",
        "action": "keyboard_enter",
    }


@router.post("/escape")
def keyboard_escape(
    token: str = Depends(require_session),
):
    press_escape()

    return {
        "status": "success",
        "action": "keyboard_escape",
    }


@router.post("/tab")
def keyboard_tab(
    token: str = Depends(require_session),
):
    press_tab()

    return {
        "status": "success",
        "action": "keyboard_tab",
    }


@router.post("/space")
def keyboard_space(
    token: str = Depends(require_session),
):
    press_space()

    return {
        "status": "success",
        "action": "keyboard_space",
    }


@router.post("/copy")
def keyboard_copy(
    token: str = Depends(require_session),
):
    copy()

    return {
        "status": "success",
        "action": "keyboard_copy",
    }


@router.post("/paste")
def keyboard_paste(
    token: str = Depends(require_session),
):
    paste()

    return {
        "status": "success",
        "action": "keyboard_paste",
    }


@router.post("/cut")
def keyboard_cut(
    token: str = Depends(require_session),
):
    cut()

    return {
        "status": "success",
        "action": "keyboard_cut",
    }


@router.post("/undo")
def keyboard_undo(
    token: str = Depends(require_session),
):
    undo()

    return {
        "status": "success",
        "action": "keyboard_undo",
    }


@router.post("/select-all")
def keyboard_select_all(
    token: str = Depends(require_session),
):
    select_all()

    return {
        "status": "success",
        "action": "keyboard_select_all",
    }


@router.post("/save")
def keyboard_save(
    token: str = Depends(require_session),
):
    save()

    return {
        "status": "success",
        "action": "keyboard_save",
    }


@router.post("/find")
def keyboard_find(
    token: str = Depends(require_session),
):
    find()

    return {
        "status": "success",
        "action": "keyboard_find",
    }


@router.post("/redo")
def keyboard_redo(
    token: str = Depends(require_session),
):
    redo()

    return {
        "status": "success",
        "action": "keyboard_redo",
    }
