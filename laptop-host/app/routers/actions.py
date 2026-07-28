from fastapi import APIRouter, HTTPException

from app.action_registry import registry
from app.schemas.action import ActionResponse

router = APIRouter(
    prefix="/actions",
    tags=["Actions"],
)


@router.get(
    "",
    response_model=list[ActionResponse],
    summary="List all registered actions",
)
def list_actions():
    """
    Returns all registered actions with their metadata.
    """
    return [
        ActionResponse(
            name=action.name,
            description=action.description,
            category=action.category,
            enabled=action.enabled,
        )
        for action in registry.list_definitions()
    ]


@router.get(
    "/categories",
    response_model=list[str],
    summary="List all action categories",
)
def list_categories():
    """
    Returns all available action categories.
    """
    return registry.list_categories()


@router.get(
    "/{name}",
    response_model=ActionResponse,
    summary="Get a registered action",
)
def get_action(name: str):
    """
    Returns metadata for a single registered action.
    """
    action = registry.get_definition(name)

    if action is None:
        raise HTTPException(
            status_code=404,
            detail=f"Action '{name}' not found.",
        )

    return ActionResponse(
        name=action.name,
        description=action.description,
        category=action.category,
        enabled=action.enabled,
    )
