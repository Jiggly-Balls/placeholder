from __future__ import annotations

from typing import TYPE_CHECKING

from pykraken import Sprite

if TYPE_CHECKING:
    from pykraken import Texture


class Player(Sprite):
    def __init__(self, texture: Texture) -> None:
        super().__init__(texture)
