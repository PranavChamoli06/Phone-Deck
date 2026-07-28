from typing import Any

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from app.action_registry import registry
from app.auth import require_session

router = APIRouter(
    prefix="/actions",
    tags=["Action Executor"],
)


class ExecuteActionRequest(BaseModel):
    action: str
    args: dict[str, Any] = Field(default_factory=dict)


@router.post("/execute")
def execute_action(
    request: ExecuteActionRequest,
    token: str = Depends(require_session),
):
    registry.execute(
        request.action,
        **request.args,
    )

    return {
        "status": "success",
        "action": request.action,
    }
