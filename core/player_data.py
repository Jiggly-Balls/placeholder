from __future__ import annotations

from enum import Enum, StrEnum
from typing import TYPE_CHECKING

import pykraken as kn

if TYPE_CHECKING:
    pass


class MovementBinding(Enum):
    UP = [kn.S_w, kn.S_UP]
    DOWN = [kn.S_s, kn.S_DOWN]
    LEFT = [kn.S_a, kn.S_LEFT]
    RIGHT = [kn.S_d, kn.S_RIGHT]
    RUN = [kn.S_LSHIFT]


class PlayerStates(StrEnum):
    IDLE = "idle"
    WALK = "walk"
    RUN = "run"

    @staticmethod
    def get_frames(state: PlayerStates) -> int:
        player_state_frames: dict[PlayerStates, int] = {
            PlayerStates.IDLE: 9,
            PlayerStates.WALK: 8,
            PlayerStates.RUN: 8,
        }
        return player_state_frames[state]


class PlayerHair(StrEnum):
    BOWL_HAIR = "bowlhair"
    CURLY_HAIR = "curlyhair"
    LONG_HAIR = "longhair"
    MOP_HAIR = "mophair"
    SHORT_HAIR = "shorthair"
    SPIKEY_HAIR = "spikeyhair"
