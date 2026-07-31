from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class ClientSession:
    """
    Stores information about a connected client.
    """

    websocket: object

    authenticated: bool = False

    device_name: Optional[str] = None

    device_id: Optional[str] = None

    session_id: Optional[str] = None

    connected_at: datetime = field(default_factory=datetime.utcnow)

    last_heartbeat: datetime = field(default_factory=datetime.utcnow)