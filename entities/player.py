from __future__ import annotations

from enum import StrEnum, auto
from typing import TYPE_CHECKING

import pykraken as kn
from pykraken import Vec2

if TYPE_CHECKING:
    from pykraken import AnimationController, Event, Scancode


class PlayerStates(StrEnum):
    IDLE = auto()


class Player:
    UP: tuple[Scancode, Scancode] = (kn.S_w, kn.S_UP)
    DOWN: tuple[Scancode, Scancode] = (kn.S_s, kn.S_DOWN)
    RIGHT: tuple[Scancode, Scancode] = (kn.S_d, kn.S_RIGHT)
    LEFT: tuple[Scancode, Scancode] = (kn.S_a, kn.S_LEFT)

    def __init__(
        self,
        animation: AnimationController,
        current_state: PlayerStates,
        position: None | Vec2 = None,
    ) -> None:
        super().__init__()

        self.animation: AnimationController = animation
        self.current_state: PlayerStates = current_state
        self.position: Vec2 = position or Vec2()

        self.speed: int = 200
        self.direction: Vec2 = Vec2()

    def process_event(self, event: Event) -> None:
        if event.type == kn.KEY_DOWN:
            if event.scan in self.UP:
                self.direction.y = -1
            elif event.scan in self.DOWN:
                self.direction.y = 1

            if event.scan in self.LEFT:
                self.direction.x = -1
            elif event.scan in self.RIGHT:
                self.direction.x = 1

        elif event.type == kn.KEY_UP:
            if event.scan in self.UP or event.scan in self.DOWN:
                self.direction.y = 0

            if event.scan in self.LEFT or event.scan in self.RIGHT:
                self.direction.x = 0

        if self.direction.length != 0:
            self.direction.normalize()

    def process_update(self, dt: float) -> None:
        x_magnitude = self.direction.x * self.speed * dt
        y_magnitude = self.direction.y * self.speed * dt
        self.position += kn.Vec2(x_magnitude, y_magnitude)
