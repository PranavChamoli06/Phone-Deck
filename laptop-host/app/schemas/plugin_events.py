from datetime import datetime

from pydantic import BaseModel


class PluginEventResponse(BaseModel):
    """
    Event sent to clients for plugin activity.
    """

    plugin_id: str
    event_type: str
    payload: dict
    timestamp: datetime
