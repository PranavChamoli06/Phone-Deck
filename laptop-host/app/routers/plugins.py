from fastapi import APIRouter, HTTPException

from app.plugins.manager import plugin_manager
from app.schemas.plugin import PluginResponse, PluginStateRequest

router = APIRouter(
    prefix="/plugins",
    tags=["Plugins"],
)


@router.get(
    "",
    response_model=list[PluginResponse],
)
def list_plugins() -> list[PluginResponse]:
    """
    List all loaded plugins.
    """
    return [
        PluginResponse(
            id=plugin.id,
            name=plugin.name,
            version=plugin.version,
            author=plugin.author,
            description=plugin.description,
            loaded=plugin_manager.is_loaded(plugin.id),
            initialized=plugin_manager.is_initialized(plugin.id),
            healthy=plugin_manager.is_healthy(plugin.id),
            enabled=plugin_manager.is_enabled(plugin.id),
        )
        for plugin in plugin_manager.list_plugins()
    ]


@router.get(
    "/{plugin_id}",
    response_model=PluginResponse,
)
def get_plugin(plugin_id: str) -> PluginResponse:
    """
    Get a specific plugin.
    """
    try:
        plugin = plugin_manager.get(plugin_id)
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail="Plugin not found.",
        )

    return PluginResponse(
        id=plugin.id,
        name=plugin.name,
        version=plugin.version,
        author=plugin.author,
        description=plugin.description,
        loaded=plugin_manager.is_loaded(plugin.id),
        initialized=plugin_manager.is_initialized(plugin.id),
        healthy=plugin_manager.is_healthy(plugin.id),
        enabled=plugin_manager.is_enabled(plugin.id),
    )


@router.put(
    "/{plugin_id}/state",
    response_model=PluginResponse,
)
def update_plugin_state(
    plugin_id: str,
    request: PluginStateRequest,
) -> PluginResponse:
    """
    Enable or disable a plugin.
    """
    try:
        plugin = plugin_manager.get(plugin_id)
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail="Plugin not found.",
        )

    if request.enabled:
        plugin_manager.enable(plugin_id)
    else:
        plugin_manager.disable(plugin_id)

    return PluginResponse(
        id=plugin.id,
        name=plugin.name,
        version=plugin.version,
        author=plugin.author,
        description=plugin.description,
        loaded=plugin_manager.is_loaded(plugin.id),
        initialized=plugin_manager.is_initialized(plugin.id),
        healthy=plugin_manager.is_healthy(plugin.id),
        enabled=plugin_manager.is_enabled(plugin.id),
    )
