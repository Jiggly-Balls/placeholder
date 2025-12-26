from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from pykraken import Texture


__all__ = ("AnimationData",)


class AnimationData(TypedDict, closed=True):
    frames: int
    base_texture: Texture
    tool_texture: Texture
