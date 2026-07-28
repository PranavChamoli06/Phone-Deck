from __future__ import annotations

import inspect
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from fastapi import HTTPException

Action = Callable[..., Any]


@dataclass(slots=True)
class ActionDefinition:
    name: str
    handler: Action
    description: str = ""
    category: str = "general"
    enabled: bool = True


class ActionRegistry:
    def __init__(self) -> None:
        self._actions: dict[str, ActionDefinition] = {}

    def register(
        self,
        name: str,
        action: Action,
        *,
        description: str = "",
        category: str = "general",
    ) -> None:
        if name in self._actions:
            raise ValueError(f"Action '{name}' is already registered.")

        self._actions[name] = ActionDefinition(
            name=name,
            handler=action,
            description=description,
            category=category,
        )

    def get(
        self,
        name: str,
    ) -> ActionDefinition:
        if name not in self._actions:
            raise KeyError(f"Unknown action: {name}")

        return self._actions[name]

    async def execute(
        self,
        name: str,
        **kwargs,
    ) -> Any:
        if not self.exists(name):
            raise HTTPException(
                status_code=404,
                detail=f"Unknown action: {name}",
            )

        action = self.get(name)

        if not action.enabled:
            raise HTTPException(
                status_code=400,
                detail=f"Action '{name}' is disabled.",
            )

        try:
            result = action.handler(**kwargs)

            if inspect.isawaitable(result):
                result = await result

                return result

        except TypeError as exc:
            raise HTTPException(
                status_code=400,
                detail=str(exc),
            ) from exc

        except Exception as exc:
            raise HTTPException(
                status_code=500,
                detail=f"Action '{name}' failed: {exc}",
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        return name in self._actions

    def list_actions(self) -> list[str]:
        return sorted(self._actions.keys())

    def get_definition(
        self,
        name: str,
    ) -> ActionDefinition | None:
        return self._actions.get(name)

    def list_definitions(self) -> list[ActionDefinition]:
        return sorted(
            self._actions.values(),
            key=lambda action: action.name,
        )

    def list_categories(self) -> list[str]:
        """
        Returns all unique action categories in alphabetical order.
        """
        return sorted({action.category for action in self._actions.values()})


registry = ActionRegistry()
