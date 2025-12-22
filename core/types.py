from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from pykraken import Texture


__all__ = ("AnimationData",)


class AnimationData(TypedDict):
    frames: int
    texture: Texture
