from __future__ import annotations

from typing import TYPE_CHECKING

import pykraken as kn

from core.player_data import MovementBinding, PlayerStates

if TYPE_CHECKING:
    from typing import TypedDict

    from pykraken import AnimationController, Scancode, Texture, Vec2

    from core.animator import Animator

    class ControllerData(TypedDict):
        controller: AnimationController
        texture: Texture


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
        self.animator: Animator = animator
        self.current_state: PlayerStates = current_state
        self.position: Vec2 = position or kn.Vec2()

        self.flip: bool = False
        self.walking_speed: int = 200
        self.running_speed: int = 350

    def movement(self, dt: float) -> None:
        speed = 0
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
            if kn.input.is_pressed(MovementBinding.RUN.name):
                self.animator.change_animation(PlayerStates.RUNNING)
                speed = self.running_speed
            else:
                self.animator.change_animation(PlayerStates.WALKING)
                speed = self.walking_speed
            direction_vec.normalize()
        else:
            self.animator.change_animation(PlayerStates.IDLE)

        x_magnitude = direction_vec.x * speed * dt
        y_magnitude = direction_vec.y * speed * dt
        self.position += kn.Vec2(x_magnitude, y_magnitude)

    def process_update(self, dt: float) -> None:
        self.movement(dt)
