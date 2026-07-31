"""
Action execution handler.
"""

import json
import logging

from fastapi import HTTPException

from app.action_registry import registry
from app.communication.protocol import (
    MessageType,
    create_message,
)

logger = logging.getLogger(__name__)


class ActionHandler:
    """
    Executes registered Phone Deck actions.
    """

    async def execute_action(
        self,
        websocket,
        session,
        message: dict,
    ):
        """
        Execute an action from the action registry.
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

        data = message.get("data", {})

        action = data.get("action")
        args = data.get("args", {})

        if not action:
            await websocket.send_text(
                json.dumps(
                    create_message(
                        MessageType.ACTION_FAILED,
                        {
                            "message": "Missing action name",
                        },
                    )
                )
            )
            return

        try:
            result = await registry.execute(
                action,
                **args,
            )

            await websocket.send_text(
                json.dumps(
                    create_message(
                        MessageType.ACTION_RESULT,
                        {
                            "action": action,
                            "success": True,
                            "result": result,
                        },
                    )
                )
            )

        except HTTPException as exc:
            logger.warning(
                "Action '%s' failed: %s",
                action,
                exc.detail,
            )

            await websocket.send_text(
                json.dumps(
                    create_message(
                        MessageType.ACTION_FAILED,
                        {
                            "action": action,
                            "error": exc.detail,
                        },
                    )
                )
            )