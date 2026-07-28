from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

from app.action_registry import registry
from app.auth import require_session
from app.pairing import generate_pairing_pin, get_pairing_pin_status, verify_pairing_pin
from app.plugins.core import CorePlugin
from app.plugins.manager import plugin_manager
from app.routers import buttons, runtime, runtime_state, settings, websocket
from app.routers.action_executor import router as action_executor_router
from app.routers.actions import router as actions_router
from app.routers.applications import router as applications_router
from app.routers.device import router as device_router
from app.routers.keyboard import router as keyboard_router
from app.routers.macro import router as macro_router
from app.routers.media import router as media_router
from app.routers.mouse import router as mouse_router
from app.routers.plugins import router as plugins_router
from app.routers.profiles import router as profiles_router
from app.routers.system import router as system_router
from app.routers.volume import router as volume_router
from app.session import create_session

app = FastAPI(
    title="Phone Deck Laptop Host",
    description="Backend service for connecting Phone Deck mobile clients to the laptop.",
    version="0.1.0",
)

plugin_manager.register(CorePlugin())

from app.plugins.system.plugin import SystemPlugin

plugin_manager.register(SystemPlugin())

plugin_manager.initialize()

from app.plugins.bridge import initialize_plugin_bridge

initialize_plugin_bridge()


class PairingVerifyRequest(BaseModel):
    pin: str


@app.get("/")
def root():
    return {
        "app": "Phone Deck",
        "component": "Laptop Host",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }


@app.post("/pairing/start")
def start_pairing():
    pin = generate_pairing_pin()

    return {
        "status": "pairing_started",
        "pin": pin,
        "expires_in": 300,
    }


@app.get("/pairing/status")
def pairing_status():
    return get_pairing_pin_status()


@app.post("/pairing/verify")
def verify_pairing(request: PairingVerifyRequest):
    result = verify_pairing_pin(request.pin)

    if result["success"]:
        token = create_session()

        return {
            "status": "pairing_successful",
            "token": token,
        }

    reason = result["reason"]

    if reason == "attempts_exceeded":
        raise HTTPException(
            status_code=429,
            detail="Maximum pairing attempts exceeded. Start a new pairing session.",
        )

    if reason in ("inactive", "expired"):
        raise HTTPException(
            status_code=401,
            detail="Pairing session is inactive or expired.",
        )

    raise HTTPException(
        status_code=401,
        detail={
            "message": "Invalid pairing PIN",
            "attempts_remaining": result["attempts_remaining"],
        },
    )


@app.get("/protected")
def protected_route(
    token: str = Depends(require_session),
):
    return {
        "status": "authorized",
        "message": "You are authenticated with the Phone Deck host.",
    }


@app.get("/debug/actions")
def debug_actions():
    return [
        {
            "name": action.name,
            "description": action.description,
            "category": action.category,
            "enabled": action.enabled,
        }
        for action in registry.list_definitions()
    ]


app.include_router(device_router)
app.include_router(media_router)
app.include_router(volume_router)
app.include_router(keyboard_router)
app.include_router(mouse_router)
app.include_router(system_router)
app.include_router(applications_router)
app.include_router(action_executor_router)
app.include_router(macro_router)
app.include_router(profiles_router)
app.include_router(settings.router)
app.include_router(buttons.router)
app.include_router(runtime.router)
app.include_router(websocket.router)
app.include_router(runtime_state.router)
app.include_router(actions_router)
app.include_router(plugins_router)
