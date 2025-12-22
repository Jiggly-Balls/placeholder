from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

import pykraken as kn
from pykraken import (
    InputAction,
    Texture,
    TextureScaleMode,
    Vec2,
)

from core.animator import Animator
from core.bindings import MovementBinding
from core.constants import (
    ASSET_HUMAN_IDLE,
    ASSET_HUMAN_RUNNING,
    ASSET_HUMAN_WALKING,
    PLAYER_ANIMATION_FPS,
)
from entities.player import Player, PlayerStates
from states.meta.base_state import BaseState
from states.meta.state_enums import StateEnum

if TYPE_CHECKING:
    from core.types import AnimationData


class LoaderState(BaseState, state_name=StateEnum.LOADER):
    def _fetch_asset(self, path: str) -> Texture:
        return Texture(path, TextureScaleMode.PIXEL_ART)

    def _load_player(self) -> None:
        animation_data: dict[StrEnum, AnimationData] = {
            PlayerStates.IDLE: {
                "texture": self._fetch_asset(ASSET_HUMAN_IDLE),
                "frames": 9,
            },
            PlayerStates.WALKING: {
                "texture": self._fetch_asset(ASSET_HUMAN_WALKING),
                "frames": 8,
            },
            PlayerStates.RUNNING: {
                "texture": self._fetch_asset(ASSET_HUMAN_RUNNING),
                "frames": 8,
            },
        }

        animator = Animator(
            animation_data,
            PlayerStates.IDLE,
            Vec2(96, 64),
            PLAYER_ANIMATION_FPS,
        )

        BaseState.player = Player(animator, PlayerStates.IDLE)

    def _load_keybinds(self) -> None:
        for player_bindings in MovementBinding:
            actions: list[InputAction] = [
                InputAction(binding) for binding in player_bindings.value
            ]
            kn.input.bind(player_bindings.name, actions)

    def on_enter(self, previous_state: None | BaseState) -> None:
        self._load_player()
        self._load_keybinds()

        self.manager.change_state(self.manager.post_init_state)
