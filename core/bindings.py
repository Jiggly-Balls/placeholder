from enum import Enum

import pykraken as kn


class MovementBinding(Enum):
    UP = [kn.S_w, kn.S_UP]
    DOWN = [kn.S_s, kn.S_DOWN]
    LEFT = [kn.S_a, kn.S_LEFT]
    RIGHT = [kn.S_d, kn.S_RIGHT]
