from __future__ import annotations

from typing import TYPE_CHECKING

from game_state import State

if TYPE_CHECKING:
    from pykraken import Event

    from states.meta.base_manager import BaseManager


__all__ = ("BaseState",)


class BaseState(State["BaseState"]):
    manager: BaseManager  # pyright: ignore[reportIncompatibleVariableOverride]

    def process_update(self, dt: float) -> None:  # pyright: ignore[reportIncompatibleMethodOverride]
        ...

    def process_event(self, event: Event) -> None: ...
