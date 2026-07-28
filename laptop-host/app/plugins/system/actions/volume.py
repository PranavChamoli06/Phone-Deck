from __future__ import annotations

from app.plugins.system.audio import audio_controller


async def volume_up(parameters: dict | None = None):
    step = parameters.get("step", 5) if parameters else 5

    volume = audio_controller.volume_up(step)

    return {
        "status": "success",
        "volume": volume,
    }


async def volume_down(parameters: dict | None = None):
    step = parameters.get("step", 5) if parameters else 5

    volume = audio_controller.volume_down(step)

    return {
        "status": "success",
        "volume": volume,
    }


async def mute(parameters: dict | None = None):
    audio_controller.mute()

    return {
        "status": "success",
        "muted": True,
    }


async def unmute(parameters: dict | None = None):
    audio_controller.unmute()

    return {
        "status": "success",
        "muted": False,
    }


async def toggle_mute(parameters: dict | None = None):
    audio_controller.toggle_mute()

    return {
        "status": "success",
        "muted": audio_controller.is_muted(),
    }


from app.action_registry import registry


def register_volume_actions() -> None:
    """
    Register volume actions.
    """

    registry.register(
        name="system.volume_up",
        action=volume_up,
        description="Increase system volume.",
        category="system",
    )

    registry.register(
        name="system.volume_down",
        action=volume_down,
        description="Decrease system volume.",
        category="system",
    )

    registry.register(
        name="system.mute",
        action=mute,
        description="Mute system volume.",
        category="system",
    )

    registry.register(
        name="system.unmute",
        action=unmute,
        description="Unmute system volume.",
        category="system",
    )

    registry.register(
        name="system.toggle_mute",
        action=toggle_mute,
        description="Toggle mute state.",
        category="system",
    )
