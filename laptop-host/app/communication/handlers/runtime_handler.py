"""
Runtime synchronization handler.
"""

import json
import logging

from app.communication.protocol import (
    MessageType,
    create_message,
)
from app.runtime_state_manager import runtime_state_manager

logger = logging.getLogger(__name__)


class RuntimeHandler:
    """
    Handles runtime synchronization requests.
    """

    async def send_runtime(
        self,
        websocket,
        session,
        message: dict,
    ):
        """
        Send the current runtime snapshot to the client.
        """

        if not session.authenticated:
            await websocket.send_text(
                json.dumps(
                    create_message(
                        MessageType.AUTH_FAILED,
                        {
                            "message": "Authentication required",
                        },
                    )
                )
            )
            return

        snapshot = runtime_state_manager.snapshot()

        await websocket.send_text(
            json.dumps(
                create_message(
                    MessageType.RUNTIME_STATE,
                    snapshot.model_dump(),
                )
            )
        )

        logger.info("Runtime snapshot sent")