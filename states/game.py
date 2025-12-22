from __future__ import annotations

import pykraken as kn

from entities.player import PlayerStates
from states.meta import BaseState, StateEnum


class GameState(BaseState, state_name=StateEnum.GAME):
    def on_enter(self, previous_state: None | BaseState) -> None:
        self.player.animator.change_animation(PlayerStates.RUNNING)

    def process_update(self, dt: float) -> None:
        self.player.process_update(dt)

        player_texture, player_clip = self.player.animator.get_animation(
            self.player.flip
        )

        kn.renderer.draw(
            player_texture,
            kn.Transform(self.player.position),
            src=player_clip,
        )
