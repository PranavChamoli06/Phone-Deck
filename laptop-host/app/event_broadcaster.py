from __future__ import annotations

from pydantic import BaseModel

from app.connection_manager import connection_manager


class EventBroadcaster:
    async def broadcast(
        self,
        event: BaseModel,
    ):
        await connection_manager.broadcast(event.model_dump())


event_broadcaster = EventBroadcaster()
