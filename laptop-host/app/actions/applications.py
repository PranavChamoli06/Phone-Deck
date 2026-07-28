import os
import subprocess
import webbrowser


def open_notepad() -> None:
    subprocess.Popen(["notepad.exe"])


def open_calculator() -> None:
    subprocess.Popen(["calc.exe"])


def open_paint() -> None:
    subprocess.Popen(["mspaint.exe"])


def open_cmd() -> None:
    subprocess.Popen(["cmd.exe"])


def open_desktop() -> None:
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    os.startfile(desktop)


def open_downloads() -> None:
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    os.startfile(downloads)


def open_google() -> None:
    webbrowser.open("https://www.google.com")


def open_github() -> None:
    webbrowser.open("https://github.com")


def open_target(target: str) -> None:
    if target.startswith(("http://", "https://")):
        webbrowser.open(target)
    else:
        os.startfile(target)
