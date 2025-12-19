from __future__ import annotations

from typing import TYPE_CHECKING

from pykraken import Sprite

if TYPE_CHECKING:
    from pykraken import AnimationController


class Player(Sprite):
    def __init__(self, animation: AnimationController) -> None:
        super().__init__()
