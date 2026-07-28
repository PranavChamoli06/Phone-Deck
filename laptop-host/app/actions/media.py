import pyautogui


def play_pause() -> None:
    pyautogui.press("playpause")


def next_track() -> None:
    pyautogui.press("nexttrack")


def previous_track() -> None:
    pyautogui.press("prevtrack")
