from __future__ import annotations

from fastapi import APIRouter, Depends

from app.auth import require_session
from app.models.runtime import ExecutionResponse
from app.runtime_service import runtime_service

router = APIRouter(
    prefix="/runtime",
    tags=["Runtime"],
)


@router.post(
    "/execute/{button_id}",
    response_model=ExecutionResponse,
)
async def execute_button(
    button_id: str,
    token: str = Depends(require_session),
):
    return await runtime_service.execute_button(button_id)
