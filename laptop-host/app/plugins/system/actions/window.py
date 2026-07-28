from __future__ import annotations

from typing import Any

import keyboard
import win32api
import win32con
import win32gui
import win32process

from app.action_registry import registry


def enumerate_windows() -> list[dict[str, Any]]:
    windows: list[dict[str, Any]] = []

    def callback(hwnd, _):
        if not win32gui.IsWindowVisible(hwnd):
            return

        title = win32gui.GetWindowText(hwnd).strip()

        if not title:
            return

        left, top, right, bottom = win32gui.GetWindowRect(hwnd)

        windows.append(
            {
                "hwnd": hwnd,
                "title": title,
                "left": left,
                "top": top,
                "width": right - left,
                "height": bottom - top,
            }
        )

    win32gui.EnumWindows(callback, None)

    return windows


def find_window(title: str):
    matches = [window for window in enumerate_windows() if window["title"] == title]

    if not matches:
        return None

    # Prefer the largest window (usually the main application window)
    return max(
        matches,
        key=lambda w: w["width"] * w["height"],
    )


def ordered_windows() -> list[dict[str, Any]]:
    """
    Return only normal user windows.

    This filters out desktop windows, invisible windows,
    tiny helper windows, and untitled windows.
    """

    windows = []

    for window in enumerate_windows():
        title = window["title"].strip()

        if not title:
            continue

        if title == "Program Manager":
            continue

        hwnd = window["hwnd"]

        # Skip tool windows
        ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)

        if ex_style & win32con.WS_EX_TOOLWINDOW:
            continue

        if window["width"] < 80 or window["height"] < 80:
            continue

        windows.append(window)

    return windows


async def switch_next_window(**kwargs):
    try:
        keyboard.press_and_release("alt+tab")

        return {
            "status": "success",
            "message": "Switched to the next window.",
        }

    except Exception as exc:
        return {
            "status": "error",
            "message": str(exc),
        }


async def switch_previous_window(**kwargs):
    try:
        keyboard.press_and_release("alt+shift+tab")

        return {
            "status": "success",
            "message": "Switched to the previous window.",
        }

    except Exception as exc:
        return {
            "status": "error",
            "message": str(exc),
        }


def get_foreground_hwnd() -> int:
    return win32gui.GetForegroundWindow()


def activate_window(hwnd: int) -> bool:
    """
    Reliably brings a window to the foreground using the Win32 API.
    """

    try:
        foreground = win32gui.GetForegroundWindow()

        if foreground == hwnd:
            return True

        current_thread = win32api.GetCurrentThreadId()

        foreground_thread = win32process.GetWindowThreadProcessId(foreground)[0]

        target_thread = win32process.GetWindowThreadProcessId(hwnd)[0]

        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

        win32process.AttachThreadInput(
            foreground_thread,
            target_thread,
            True,
        )

        win32gui.BringWindowToTop(hwnd)

        win32gui.SetForegroundWindow(hwnd)

        win32gui.SetActiveWindow(hwnd)

        win32process.AttachThreadInput(
            foreground_thread,
            target_thread,
            False,
        )

        return True

    except Exception:
        return False


def control_window(title: str, command: int):
    window = find_window(title)

    if window is None:
        return {
            "status": "error",
            "message": f"Window '{title}' not found.",
        }

    try:
        win32gui.ShowWindow(window["hwnd"], command)

        return {
            "status": "success",
            "title": title,
        }

    except Exception as exc:
        return {
            "status": "error",
            "message": str(exc),
        }


async def minimize_window(title: str, **kwargs):
    return control_window(title, win32con.SW_MINIMIZE)


async def maximize_window(title: str, **kwargs):
    return control_window(title, win32con.SW_MAXIMIZE)


async def restore_window(title: str, **kwargs):
    return control_window(title, win32con.SW_RESTORE)


async def close_window(title: str, **kwargs):
    window = find_window(title)

    if window is None:
        return {
            "status": "error",
            "message": f"Window '{title}' not found.",
        }

    try:
        win32gui.PostMessage(
            window["hwnd"],
            win32con.WM_CLOSE,
            0,
            0,
        )

        return {
            "status": "success",
            "title": title,
        }

    except Exception as exc:
        return {
            "status": "error",
            "message": str(exc),
        }


async def focus_window(title: str, **kwargs):
    window = find_window(title)

    if window is None:
        return {
            "status": "error",
            "message": f"Window '{title}' not found.",
        }

    success = activate_window(window["hwnd"])

    if success:
        return {
            "status": "success",
            "title": title,
        }

    return {
        "status": "error",
        "message": "Unable to activate window.",
    }


async def list_windows(**kwargs):
    foreground = get_foreground_hwnd()

    windows = []

    for window in enumerate_windows():
        windows.append(
            {
                "title": window["title"],
                "left": window["left"],
                "top": window["top"],
                "width": window["width"],
                "height": window["height"],
                "active": window["hwnd"] == foreground,
            }
        )

    return {
        "status": "success",
        "count": len(windows),
        "windows": windows,
    }


def register_window_actions() -> None:
    registry.register(
        name="window.list",
        action=list_windows,
        description="List all open windows.",
        category="window",
    )

    registry.register(
        name="window.focus",
        action=focus_window,
        description="Focus a window.",
        category="window",
    )

    registry.register(
        name="window.minimize",
        action=minimize_window,
        description="Minimize a window.",
        category="window",
    )

    registry.register(
        name="window.maximize",
        action=maximize_window,
        description="Maximize a window.",
        category="window",
    )

    registry.register(
        name="window.restore",
        action=restore_window,
        description="Restore a window.",
        category="window",
    )

    registry.register(
        name="window.close",
        action=close_window,
        description="Close a window.",
        category="window",
    )

    registry.register(
        name="window.switch_next",
        action=switch_next_window,
        description="Switch to the next window.",
        category="window",
    )

    registry.register(
        name="window.switch_previous",
        action=switch_previous_window,
        description="Switch to the previous window.",
        category="window",
    )
