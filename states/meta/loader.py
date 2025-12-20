from pykraken import AnimationController, SheetStrip, Vec2

from core.constants import ASSET_SOLDIER, PLAYER_ANIMATION_FPS
from entities.player import Player, PlayerStates
from states.meta.base_state import BaseState
from states.meta.state_enums import StateEnum


class LoaderState(BaseState, state_name=StateEnum.LOADER):
    def _load_player(self) -> None:
        sprite_sheet: list[SheetStrip] = [
            SheetStrip(PlayerStates.IDLE, 6, PLAYER_ANIMATION_FPS),
            SheetStrip(PlayerStates.RUNNING, 8, PLAYER_ANIMATION_FPS),
        ]

        player_animation = AnimationController()
        player_animation.load_sprite_sheet(
            ASSET_SOLDIER, Vec2(100, 100), sprite_sheet
        )

        BaseState.player = Player(player_animation, PlayerStates.IDLE)

    def _load_keybinds(self) -> None: ...

    def on_enter(self, previous_state: None | BaseState) -> None:
        self._load_player()
        self._load_keybinds()

        self.manager.change_state(self.manager.post_init_state)
