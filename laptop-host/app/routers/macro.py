from typing import Any

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.auth import require_session
from app.macro_engine import macro_engine

router = APIRouter(
    prefix="/actions",
    tags=["Macros"],
)


class MacroStep(BaseModel):
    action: str | None = None
    args: dict[str, Any] = {}
    delay_ms: int | None = None


class MacroRequest(BaseModel):
    actions: list[MacroStep]


@router.post("/macro")
def execute_macro(
    request: MacroRequest,
    token: str = Depends(require_session),
):
    macro_engine.execute(
        [step.model_dump(exclude_none=True) for step in request.actions]
    )

    return {
        "status": "success",
        "steps": len(request.actions),
    }
