"""
Authentication message handler.
"""

import json
import logging

from app.communication.protocol import (
    MessageType,
    create_message,
)
from app.pairing import verify_pairing_pin

logger = logging.getLogger(__name__)


class AuthHandler:
    """
    Handles client authentication.
    """

    async def verify_otp(
        self,
        websocket,
        session,
        message: dict,
    ):
        otp = message["data"].get("otp", "")

        result = verify_pairing_pin(otp)

        if result["success"]:
            session.authenticated = True

            logger.info("Client authenticated successfully")

            await websocket.send_text(
                json.dumps(
                    create_message(
                        MessageType.AUTH_SUCCESS,
                        {
                            "message": "Authentication successful",
                        },
                    )
                )
            )
            return

        logger.warning("Authentication failed")

        await websocket.send_text(
            json.dumps(
                create_message(
                    MessageType.AUTH_FAILED,
                    {
                        "message": "Invalid or expired OTP",
                        "reason": result["reason"],
                    },
                )
            )
        )