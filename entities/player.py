from __future__ import annotations

from enum import StrEnum, auto
from typing import TYPE_CHECKING

import pykraken as kn

if TYPE_CHECKING:
    from typing import TypedDict

    from pykraken import AnimationController, Scancode, Texture, Vec2

    from core.animator import Animator

    class ControllerData(TypedDict):
        controller: AnimationController
        texture: Texture


class PlayerStates(StrEnum):
    IDLE = auto()
    WALKING = auto()
    RUNNING = auto()


class Player:
    UP: tuple[Scancode, Scancode] = (kn.S_w, kn.S_UP)
    DOWN: tuple[Scancode, Scancode] = (kn.S_s, kn.S_DOWN)
    RIGHT: tuple[Scancode, Scancode] = (kn.S_d, kn.S_RIGHT)
    LEFT: tuple[Scancode, Scancode] = (kn.S_a, kn.S_LEFT)

    def __init__(
        self,
        animator: Animator,
        current_state: PlayerStates,
        position: None | Vec2 = None,
    ) -> None:
        super().__init__()

        self.animator: Animator = animator
        self.current_state: PlayerStates = current_state
        self.position: Vec2 = position or kn.Vec2()

        self.flip: bool = False
        self.speed: int = 200
        self.direction: Vec2 = kn.Vec2()

    def movement(self, dt: float) -> None:
        if any(kn.key.is_pressed(key) for key in self.UP):
            self.direction.y = -1
        elif any(kn.key.is_pressed(key) for key in self.DOWN):
            self.direction.y = 1
        else:
            self.direction.y = 0

        if any(kn.key.is_pressed(key) for key in self.LEFT):
            self.direction.x = -1
            self.flip = True
        elif any(kn.key.is_pressed(key) for key in self.RIGHT):
            self.direction.x = 1
            self.flip = False
        else:
            self.direction.x = 0

        if self.direction.length != 0:
            self.animator.change_animation(PlayerStates.RUNNING)
            self.direction.normalize()
        else:
            self.animator.change_animation(PlayerStates.IDLE)

        x_magnitude = self.direction.x * self.speed * dt
        y_magnitude = self.direction.y * self.speed * dt
        self.position += kn.Vec2(x_magnitude, y_magnitude)

    def process_update(self, dt: float) -> None:
        self.movement(dt)
