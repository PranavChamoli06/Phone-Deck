import pyautogui


def volume_up() -> None:
    pyautogui.press("volumeup")


def volume_down() -> None:
    pyautogui.press("volumedown")


def toggle_mute() -> None:
    pyautogui.press("volumemute")
