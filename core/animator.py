from __future__ import annotations

from typing import TYPE_CHECKING

import pykraken as kn

if TYPE_CHECKING:
    from enum import StrEnum
    from typing import TypedDict

    from pykraken import AnimationController, Rect, Texture, Vec2

    from core.player_data import PlayerHair, PlayerStates
    from core.types import AnimationData

    class ControllerData(TypedDict, closed=True):
        controller: AnimationController
        base_texture: Texture
        tool_texture: Texture


__all__ = ("Animator",)


class Animator:
    """An advance animation controller for handling multiple sprite sheets for a single entity."""

    def __init__(
        self,
        texture_map: dict[StrEnum, AnimationData],
        current_state: StrEnum,
        frame_size: Vec2,
        speed: int,
    ) -> None:
        self._controllers: dict[StrEnum, ControllerData] = {}
        self.current_state: StrEnum = current_state

        for state, state_data in texture_map.items():
            self._controllers[state] = {}  # pyright: ignore[reportArgumentType]
            self._controllers[state]["controller"] = kn.AnimationController()
            self._controllers[state]["base_texture"] = state_data[
                "base_texture"
            ]
            self._controllers[state]["tool_texture"] = state_data[
                "tool_texture"
            ]

            self._controllers[state]["controller"].load_sprite_sheet(
                frame_size,
                kn.SheetStripList(
                    (kn.SheetStrip(state, state_data["frames"], speed),)
                ),
            )

    def change_animation(self, state: StrEnum) -> None:
        self.current_state = state
        self._controllers[state]["controller"].set(state)

    def get_base_frame(
        self, h_flip: bool = False, v_flip: bool = False
    ) -> tuple[Texture, Rect]:
        controller = self._controllers[self.current_state]["controller"]
        texture = self._controllers[self.current_state]["base_texture"]
        texture.flip.h = h_flip
        texture.flip.v = v_flip

        return (texture, controller.clip)

    def get_tool_frame(
        self, h_flip: bool = False, v_flip: bool = False
    ) -> tuple[Texture, Rect]:
        controller = self._controllers[self.current_state]["controller"]
        texture = self._controllers[self.current_state]["tool_texture"]
        texture.flip.h = h_flip
        texture.flip.v = v_flip

        return (texture, controller.clip)


class PlayerCosmeticAnimator:
    def __init__(
        self,
        data: dict[PlayerStates, dict[PlayerHair, tuple[Texture, int]]],
        current_hair: PlayerHair,
        current_state: PlayerStates,
        size: Vec2,
        speed: int,
    ) -> None:
        self.current_hair: PlayerHair = current_hair
        self.current_state: PlayerStates = current_state

        self._animation_data: dict[
            PlayerStates, dict[PlayerHair, tuple[AnimationController, Texture]]
        ] = {}

        for state, state_data in data.items():
            self._animation_data[state] = {}
            for hair, (texture, frames) in state_data.items():
                sheet = kn.SheetStrip(state, frames, speed)
                controller = kn.AnimationController()
                controller.load_sprite_sheet(
                    size, (kn.SheetStripList((sheet,)))
                )

                self._animation_data[state][hair] = (controller, texture)

    def change_animation(self, state: PlayerStates) -> None:
        self.current_state = state
        self._animation_data[state][self.current_hair][0].set(state)

    def get_frame(
        self, h_flip: bool = False, v_flip: bool = False
    ) -> tuple[Texture, Rect]:
        # fmt: off
        controller = self._animation_data[self.current_state][self.current_hair][0]
        texture = self._animation_data[self.current_state][self.current_hair][1]
        # fmt: on

        texture.flip.h = h_flip
        texture.flip.v = v_flip

        return (texture, controller.clip)
