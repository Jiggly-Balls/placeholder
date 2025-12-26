from __future__ import annotations

import itertools
from typing import TYPE_CHECKING

import pykraken as kn

from core.constants import PLAYER_TARGET_RES
from core.player_data import MovementBinding, PlayerHair, PlayerStates

if TYPE_CHECKING:
    from pykraken import Scancode, Vec2

    from core.animator import Animator, PlayerCosmeticAnimator


class Player:
    UP: tuple[Scancode, Scancode] = (kn.S_w, kn.S_UP)
    DOWN: tuple[Scancode, Scancode] = (kn.S_s, kn.S_DOWN)
    RIGHT: tuple[Scancode, Scancode] = (kn.S_d, kn.S_RIGHT)
    LEFT: tuple[Scancode, Scancode] = (kn.S_a, kn.S_LEFT)

    def __init__(
        self,
        animator: Animator,
        cosmetic_animator: PlayerCosmeticAnimator,
        current_state: PlayerStates,
        position: None | Vec2 = None,
    ) -> None:
        self.animator: Animator = animator
        self.cosmetic_animator: PlayerCosmeticAnimator = cosmetic_animator
        self.current_state: PlayerStates = current_state
        self.position: Vec2 = position or kn.Vec2()

        self.flip: bool = False
        self.walking_speed: int = 200
        self.running_speed: int = 350
        self.hair_cycle: itertools.cycle[PlayerHair] = itertools.cycle(
            PlayerHair
        )

    def _switch_animation(self, state: PlayerStates) -> None:
        self.animator.change_animation(state)
        self.cosmetic_animator.change_animation(state)

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

        if direction_vec:
            if kn.input.is_pressed(MovementBinding.RUN.name):
                self._switch_animation(PlayerStates.RUN)
                speed = self.running_speed
            else:
                self._switch_animation(PlayerStates.WALK)
                speed = self.walking_speed
            direction_vec.normalize()
        else:
            self._switch_animation(PlayerStates.IDLE)

        x_magnitude = direction_vec.x * speed * dt
        y_magnitude = direction_vec.y * speed * dt
        self.position += kn.Vec2(x_magnitude, y_magnitude)

    def change_hair(self) -> None:
        if kn.key.is_just_pressed(kn.S_e):
            hair = next(self.hair_cycle)
            self.cosmetic_animator.current_hair = hair

    def process_update(self, dt: float) -> None:
        self.movement(dt)
        self.change_hair()

    def process_render(self) -> None:
        player_texture, player_clip = self.animator.get_base_frame(self.flip)

        player_tool_texture, player_tool_clip = self.animator.get_tool_frame(
            self.flip
        )

        player_hair_texture, player_hair_clip = (
            self.cosmetic_animator.get_frame(self.flip)
        )

        kn.renderer.draw(
            player_texture,
            kn.Transform(self.position, size=PLAYER_TARGET_RES),
            src=player_clip,
        )
        kn.renderer.draw(
            player_tool_texture,
            kn.Transform(self.position, size=PLAYER_TARGET_RES),
            src=player_tool_clip,
        )
        kn.renderer.draw(
            player_hair_texture,
            kn.Transform(self.position, size=PLAYER_TARGET_RES),
            src=player_hair_clip,
        )
