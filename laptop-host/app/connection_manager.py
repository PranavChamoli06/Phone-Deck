from __future__ import annotations

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.connections: list[WebSocket] = []

    async def connect(
        self,
        websocket: WebSocket,
    ):
        print("Incoming websocket...")
        await websocket.accept()
        self.connections.append(websocket)
        print("Connected")

    def disconnect(
        self,
        websocket: WebSocket,
    ):
        if websocket in self.connections:
            self.connections.remove(websocket)

    async def broadcast(
        self,
        message: dict,
    ):
        disconnected: list[WebSocket] = []

        for websocket in self.connections:
            try:
                await websocket.send_json(message)
            except Exception:
                disconnected.append(websocket)

        for websocket in disconnected:
            self.disconnect(websocket)

    def connection_count(self) -> int:
        return len(self.connections)


connection_manager = ConnectionManager()
