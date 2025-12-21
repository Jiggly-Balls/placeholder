from __future__ import annotations

from typing import Any

import pykraken as kn

# from entities.player import PlayerStates
from states.meta import BaseState, StateEnum


class GameState(BaseState, state_name=StateEnum.GAME):
    # def on_enter(self, previous_state: None | BaseState) -> None:
    #     self.player.change_animation(PlayerStates.IDLE)

    def process_update(self, dt: float) -> None:
        self.player.process_update(dt)

        player_texture, player_clip = self.player.get_animation()

        x3_scale_up: dict[str, Any]

        x3_scale_up = {}
        # x3_scale_up = {"size": (288, 192)}

        kn.renderer.draw(
            player_texture,
            kn.Transform(self.player.position, **x3_scale_up),
            src=player_clip,
        )
