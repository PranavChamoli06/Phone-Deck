from time import sleep
from typing import Any

from app.action_registry import registry


class MacroEngine:
    def execute(self, actions: list[dict[str, Any]]) -> None:
        for step in actions:
            # Delay step
            if "delay_ms" in step:
                sleep(step["delay_ms"] / 1000)
                continue

        action_name = step["action"]
        args = step.get("args", {})

        registry.execute(action_name, **args)


macro_engine = MacroEngine()
