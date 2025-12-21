from __future__ import annotations

from enum import StrEnum, auto
from typing import TYPE_CHECKING

import pykraken as kn

if TYPE_CHECKING:
    from pykraken import AnimationController, Rect, Scancode, Texture, Vec2


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
        animation: dict[PlayerStates, AnimationController],
        current_state: PlayerStates,
        position: None | Vec2 = None,
    ) -> None:
        super().__init__()

        self.animation: dict[PlayerStates, AnimationController] = animation
        self.current_state: PlayerStates = current_state
        self.position: Vec2 = position or kn.Vec2()

        self.flip: bool = False
        self.speed: int = 200
        self.direction: Vec2 = kn.Vec2()

    def get_animation(self) -> tuple[Texture, Rect]:
        self.animation[self.current_state].texture.flip.h = self.flip

        return (
            self.animation[self.current_state].texture,
            self.animation[self.current_state].clip,
        )

    def change_animation(self, state: PlayerStates) -> None:
        self.current_state = state
        self.animation[state].set(state)

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
            self.change_animation(PlayerStates.RUNNING)
            self.direction.normalize()
        else:
            self.change_animation(PlayerStates.IDLE)

        x_magnitude = self.direction.x * self.speed * dt
        y_magnitude = self.direction.y * self.speed * dt
        self.position += kn.Vec2(x_magnitude, y_magnitude)

    def process_update(self, dt: float) -> None:
        self.movement(dt)
