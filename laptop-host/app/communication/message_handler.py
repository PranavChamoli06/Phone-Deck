"""
Message handler for Phone Deck communication.
"""

import json
import logging

from app.communication.handlers.auth_handler import AuthHandler
from app.communication.protocol import (
    MessageType,
    create_message,
)

from app.communication.handlers.action_handler import ActionHandler

logger = logging.getLogger(__name__)


class MessageHandler:
    """
    Routes validated protocol messages to their handlers.
    """

    def __init__(self):
        self.auth_handler = AuthHandler()
        self.action_handler = ActionHandler()

        self.routes = {
        MessageType.PING: self.handle_ping,
        MessageType.PONG: self.handle_pong,
        MessageType.OTP_VERIFY: self.auth_handler.verify_otp,
        MessageType.ACTION_EXECUTE: self.action_handler.execute_action,
    }

    async def handle_message(
        self,
        websocket,
        session,
        message: dict,
    ):
        """
        Route an incoming protocol message.
        """

        message_type = MessageType(message["type"])

        logger.info("Handling message: %s", message_type.value)

        handler = self.routes.get(message_type)

        if handler is None:
            logger.warning(
                "Unsupported message type: %s",
                message_type.value,
            )

            await websocket.send_text(
                json.dumps(
                    create_message(
                        MessageType.ERROR,
                        {
                            "message": f"Unsupported message type: {message_type.value}",
                        },
                    )
                )
            )
            return

        await handler(
            websocket,
            session,
            message,
        )

    async def handle_ping(
        self,
        websocket,
        session,
        message: dict,
    ):
        logger.debug("PING received")

        await websocket.send_text(
            json.dumps(
                create_message(
                    MessageType.PONG,
                    {},
                )
            )
        )

    async def handle_pong(
        self,
        websocket,
        session,
        message: dict,
    ):
        logger.debug("PONG received")