from __future__ import annotations

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.connection_manager import connection_manager
from app.models.events import RuntimeStateData, RuntimeStateEvent
from app.runtime_state_manager import runtime_state_manager

import json
import logging

from app.communication.client_session import ClientSession
from app.communication.message_handler import MessageHandler
from app.communication.protocol import validate_message

router = APIRouter(
    tags=["WebSocket"],
)

logger = logging.getLogger(__name__)


@router.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
):
    await connection_manager.connect(websocket)

    session = ClientSession(websocket)
    handler = MessageHandler()

    logger.info("Client Connected")

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
            raw_message = await websocket.receive_text()

            try:
                message = json.loads(raw_message)
            except json.JSONDecodeError:
                logger.warning("Received invalid JSON")

                await websocket.send_json(
                    {
                        "type": "error",
                        "message": "Invalid JSON",
                    }
                )

                continue
            if not validate_message(message):
                logger.warning("Protocol Validation Failed")

                await websocket.send_json(
                    {
                        "type": "error",
                        "message": "Invalid Protocol Message",
                    }
                )
                continue

            await handler.handle_message(
                websocket = websocket,
                session = session,
                message = message
            )

    except WebSocketDisconnect:
        logger.info("Client Disconnected")

        connection_manager.disconnect(websocket)
