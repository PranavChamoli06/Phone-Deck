from pydantic import BaseModel


class PluginResponse(BaseModel):
    id: str
    name: str
    version: str
    author: str
    description: str
    loaded: bool
    initialized: bool
    healthy: bool
    enabled: bool


class PluginStateRequest(BaseModel):
    enabled: bool
