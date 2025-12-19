from __future__ import annotations

from typing import TYPE_CHECKING

from game_state import State

if TYPE_CHECKING:
    from pykraken import Event


__all__ = ("BaseState",)


class BaseState(State["BaseState"]):
    def process_update(self, dt: float) -> None:  # pyright: ignore[reportIncompatibleMethodOverride]
        ...

    def process_event(self, event: Event) -> None: ...
