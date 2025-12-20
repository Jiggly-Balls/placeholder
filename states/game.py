from __future__ import annotations

import pykraken as kn

from entities.player import PlayerStates
from states.meta import BaseState, StateEnum


class GameState(BaseState, state_name=StateEnum.GAME):
    def on_enter(self, previous_state: None | BaseState) -> None:
        self.player.animation.set(PlayerStates.IDLE)

    def process_update(self, dt: float) -> None:
        self.player.process_update(dt)

        self.player.animation.texture.flip.h = self.player.flip

        kn.renderer.draw(
            self.player.animation.texture,
            kn.Transform(self.player.position, size=(200, 200)),
            src=self.player.animation.clip,
        )
