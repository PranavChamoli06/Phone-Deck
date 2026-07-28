from __future__ import annotations

import ctypes
import subprocess

user32 = ctypes.windll.user32
powrprof = ctypes.windll.powrprof


async def lock_workstation(parameters: dict | None = None):
    success = bool(user32.LockWorkStation())

    if not success:
        raise RuntimeError("Failed to lock workstation.")

    return {
        "status": "success",
    }


async def sleep_system(parameters: dict | None = None):
    # Hibernate=False, Force=False, DisableWakeEvent=False
    success = bool(powrprof.SetSuspendState(False, False, False))

    if not success:
        raise RuntimeError("Failed to enter sleep mode.")

    return {
        "status": "success",
    }


async def shutdown_system(parameters: dict | None = None):
    subprocess.Popen(
        ["shutdown", "/s", "/t", "0"],
        shell=False,
    )

    return {
        "status": "success",
    }


async def restart_system(parameters: dict | None = None):
    subprocess.Popen(
        ["shutdown", "/r", "/t", "0"],
        shell=False,
    )

    return {
        "status": "success",
    }


async def logoff_system(parameters: dict | None = None):
    subprocess.Popen(
        ["shutdown", "/l"],
        shell=False,
    )

    return {
        "status": "success",
    }


from app.action_registry import registry


def register_power_actions() -> None:
    registry.register(
        name="system.lock",
        action=lock_workstation,
        description="Lock the workstation.",
        category="system",
    )

    registry.register(
        name="system.sleep",
        action=sleep_system,
        description="Put the computer to sleep.",
        category="system",
    )

    registry.register(
        name="system.shutdown",
        action=shutdown_system,
        description="Shut down the computer.",
        category="system",
    )

    registry.register(
        name="system.restart",
        action=restart_system,
        description="Restart the computer.",
        category="system",
    )

    registry.register(
        name="system.logoff",
        action=logoff_system,
        description="Log off the current user.",
        category="system",
    )
