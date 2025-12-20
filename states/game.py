from __future__ import annotations

import pykraken as kn

from entities.player import PlayerStates
from states.meta import BaseState, StateEnum


class GameState(BaseState, state_name=StateEnum.GAME):
    def on_enter(self, previous_state: None | BaseState) -> None:
        self.player.animation.set(PlayerStates.IDLE)
        self.player.animation.play(PlayerStates.IDLE)

    def process_update(self, dt: float) -> None:
        self.player.process_update(dt)

        kn.renderer.draw(
            self.player.animation.texture,
            kn.Transform(self.player.position),
            src=self.player.animation.clip,
        )
