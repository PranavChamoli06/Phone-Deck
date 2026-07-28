import ctypes
import subprocess


def lock_workstation() -> None:
    ctypes.windll.user32.LockWorkStation()


def sleep_system() -> None:
    subprocess.run(
        [
            "rundll32.exe",
            "powrprof.dll,SetSuspendState",
            "0,1,0",
        ],
        check=False,
    )
