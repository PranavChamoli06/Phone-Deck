from app.action_registry import registry

# ---------------- Applications ----------------
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

# ---------------- Keyboard ----------------
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

# ---------------- Mouse ----------------
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


def register_all_actions() -> None:
    # ==========================================================
    # Keyboard
    # ==========================================================

    registry.register(
        "keyboard.enter",
        press_enter,
        description="Press the Enter key",
        category="keyboard",
    )

    registry.register(
        "keyboard.escape",
        press_escape,
        description="Press the Escape key",
        category="keyboard",
    )

    registry.register(
        "keyboard.space",
        press_space,
        description="Press the Space key",
        category="keyboard",
    )

    registry.register(
        "keyboard.tab",
        press_tab,
        description="Press the Tab key",
        category="keyboard",
    )

    registry.register(
        "keyboard.copy",
        copy,
        description="Copy the selected content",
        category="keyboard",
    )

    registry.register(
        "keyboard.paste",
        paste,
        description="Paste clipboard content",
        category="keyboard",
    )

    registry.register(
        "keyboard.cut",
        cut,
        description="Cut the selected content",
        category="keyboard",
    )

    registry.register(
        "keyboard.undo",
        undo,
        description="Undo the previous action",
        category="keyboard",
    )

    registry.register(
        "keyboard.redo",
        redo,
        description="Redo the previous action",
        category="keyboard",
    )

    registry.register(
        "keyboard.select_all",
        select_all,
        description="Select all content",
        category="keyboard",
    )

    registry.register(
        "keyboard.save",
        save,
        description="Save the current document",
        category="keyboard",
    )

    registry.register(
        "keyboard.find",
        find,
        description="Open the Find dialog",
        category="keyboard",
    )

    # ==========================================================
    # Mouse
    # ==========================================================

    registry.register(
        "mouse.left_click",
        left_click,
        description="Perform a left mouse click",
        category="mouse",
    )

    registry.register(
        "mouse.right_click",
        right_click,
        description="Perform a right mouse click",
        category="mouse",
    )

    registry.register(
        "mouse.double_click",
        double_click,
        description="Perform a double left mouse click",
        category="mouse",
    )

    registry.register(
        "mouse.move_up",
        move_up,
        description="Move the mouse cursor upward",
        category="mouse",
    )

    registry.register(
        "mouse.move_down",
        move_down,
        description="Move the mouse cursor downward",
        category="mouse",
    )

    registry.register(
        "mouse.move_left",
        move_left,
        description="Move the mouse cursor left",
        category="mouse",
    )

    registry.register(
        "mouse.move_right",
        move_right,
        description="Move the mouse cursor right",
        category="mouse",
    )

    registry.register(
        "mouse.scroll_up",
        scroll_up,
        description="Scroll upward",
        category="mouse",
    )

    registry.register(
        "mouse.scroll_down",
        scroll_down,
        description="Scroll downward",
        category="mouse",
    )

    registry.register(
        "mouse.left_button_down",
        left_button_down,
        description="Press and hold the left mouse button",
        category="mouse",
    )

    registry.register(
        "mouse.left_button_up",
        left_button_up,
        description="Release the left mouse button",
        category="mouse",
    )

    # ==========================================================
    # Applications
    # ==========================================================

    registry.register(
        "application.notepad",
        open_notepad,
        description="Open Notepad",
        category="applications",
    )

    registry.register(
        "application.calculator",
        open_calculator,
        description="Open Calculator",
        category="applications",
    )

    registry.register(
        "application.paint",
        open_paint,
        description="Open Microsoft Paint",
        category="applications",
    )

    registry.register(
        "application.cmd",
        open_cmd,
        description="Open Command Prompt",
        category="applications",
    )

    registry.register(
        "application.desktop",
        open_desktop,
        description="Show the desktop",
        category="applications",
    )

    registry.register(
        "application.downloads",
        open_downloads,
        description="Open the Downloads folder",
        category="applications",
    )

    registry.register(
        "application.google",
        open_google,
        description="Open Google in the default browser",
        category="applications",
    )

    registry.register(
        "application.github",
        open_github,
        description="Open GitHub in the default browser",
        category="applications",
    )

    registry.register(
        "application.open",
        open_target,
        description="Open a specified application or file",
        category="applications",
    )
