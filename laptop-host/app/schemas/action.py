from pydantic import BaseModel


class ActionResponse(BaseModel):
    name: str
    description: str
    category: str
    enabled: bool
