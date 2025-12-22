from __future__ import annotations

from enum import StrEnum, auto
from typing import TYPE_CHECKING

import pykraken as kn

from core.bindings import MovementBinding

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
        direction_vec = kn.input.get_direction(
            up=MovementBinding.UP.name,
            right=MovementBinding.RIGHT.name,
            down=MovementBinding.DOWN.name,
            left=MovementBinding.LEFT.name,
        )
        if direction_vec.x < 0:
            self.flip = True
        elif direction_vec.x > 0:
            self.flip = False

        if direction_vec.length != 0:
            self.animator.change_animation(PlayerStates.RUNNING)
            direction_vec.normalize()
        else:
            self.animator.change_animation(PlayerStates.IDLE)

        x_magnitude = direction_vec.x * self.speed * dt
        y_magnitude = direction_vec.y * self.speed * dt
        self.position += kn.Vec2(x_magnitude, y_magnitude)

    def process_update(self, dt: float) -> None:
        self.movement(dt)
