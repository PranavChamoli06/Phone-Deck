from __future__ import annotations

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.connection_manager import connection_manager
from app.models.events import RuntimeStateData, RuntimeStateEvent
from app.runtime_state_manager import runtime_state_manager

router = APIRouter(
    tags=["WebSocket"],
)


@router.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
):
    await connection_manager.connect(websocket)

    await websocket.send_json(
        {
            "type": "connected",
            "message": "Connected to Phone Deck Host",
        }
    )

    await websocket.send_json(
        RuntimeStateEvent(
            data=RuntimeStateData(
                buttons=runtime_state_manager.snapshot(),
            )
        ).model_dump()
    )

    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        connection_manager.disconnect(websocket)
