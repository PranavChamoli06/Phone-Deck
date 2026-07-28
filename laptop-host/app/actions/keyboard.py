import pyautogui


def press_enter() -> None:
    pyautogui.press("enter")


def press_escape() -> None:
    pyautogui.press("esc")


def press_tab() -> None:
    pyautogui.press("tab")


def press_space() -> None:
    pyautogui.press("space")


def copy() -> None:
    pyautogui.hotkey("ctrl", "c")


def paste() -> None:
    pyautogui.hotkey("ctrl", "v")


def cut() -> None:
    pyautogui.hotkey("ctrl", "x")


def undo() -> None:
    pyautogui.hotkey("ctrl", "z")


def select_all() -> None:
    pyautogui.hotkey("ctrl", "a")


def save() -> None:
    pyautogui.hotkey("ctrl", "s")


def find() -> None:
    pyautogui.hotkey("ctrl", "f")


def redo() -> None:
    pyautogui.hotkey("ctrl", "y")
