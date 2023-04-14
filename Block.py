from enum import Enum


class Block(Enum):
    LIGHT_BLUE = "00001111"
    BLUE = "10001110"
    ORANGE = "00101110"
    PURPLE = "01001110"
    GREEN = "01101100"
    RED = "11000110"


_map = {
    "10001110": Block.BLUE,
    "00001111": Block.LIGHT_BLUE,
    "00101110": Block.ORANGE,
    "01001110": Block.PURPLE,
    "01101100": Block.GREEN,
    "11000110": Block.RED
}


def get(string):
    return _map[string]
