from typing import Any

from pydantic import BaseModel


class ExecutionResponse(BaseModel):
    success: bool
    button: str
    action: str
    result: Any | None = None
