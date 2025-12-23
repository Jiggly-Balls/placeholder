from __future__ import annotations

from typing import TYPE_CHECKING

import pykraken as kn

if TYPE_CHECKING:
    from enum import StrEnum
    from typing import TypedDict

    from pykraken import AnimationController, Rect, Texture, Vec2

    from core.types import AnimationData

    class ControllerData(TypedDict):
        controller: AnimationController
        texture: Texture


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
        super().__init__()

        self.controllers: dict[StrEnum, ControllerData] = {}
        self.current_state: StrEnum = current_state

        for state, state_data in texture_map.items():
            self.controllers[state] = {}  # pyright: ignore[reportArgumentType]
            self.controllers[state]["controller"] = kn.AnimationController()
            self.controllers[state]["texture"] = state_data["texture"]

            self.controllers[state]["controller"].load_sprite_sheet(
                frame_size,
                (kn.SheetStrip(state, state_data["frames"], speed),),
            )

    def change_animation(self, state: StrEnum) -> None:
        self.current_state = state
        self.controllers[state]["controller"].set(state)

    def get_frame(
        self, h_flip: bool = False, v_flip: bool = False
    ) -> tuple[Texture, Rect]:
        controller = self.controllers[self.current_state]["controller"]
        texture = self.controllers[self.current_state]["texture"]
        texture.flip.h = h_flip
        texture.flip.v = v_flip

        return (texture, controller.clip)


class PlayerAnimator(Animator): ...
