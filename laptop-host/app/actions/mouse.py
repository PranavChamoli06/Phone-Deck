import pyautogui

MOVE_DISTANCE = 50


def left_click() -> None:
    pyautogui.click(button="left")


def right_click() -> None:
    pyautogui.click(button="right")


def double_click() -> None:
    pyautogui.doubleClick()


def move_up() -> None:
    pyautogui.moveRel(0, -MOVE_DISTANCE)


def move_down() -> None:
    pyautogui.moveRel(0, MOVE_DISTANCE)


def move_left() -> None:
    pyautogui.moveRel(-MOVE_DISTANCE, 0)


def move_right() -> None:
    pyautogui.moveRel(MOVE_DISTANCE, 0)


SCROLL_AMOUNT = 500


def scroll_up() -> None:
    pyautogui.scroll(SCROLL_AMOUNT)


def scroll_down() -> None:
    pyautogui.scroll(-SCROLL_AMOUNT)


def left_button_down() -> None:
    pyautogui.mouseDown(button="left")


def left_button_up() -> None:
    pyautogui.mouseUp(button="left")
