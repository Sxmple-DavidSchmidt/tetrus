from enum import Enum


class Block(Enum):
    LIGHT_BLUE = 1
    BLUE = 2
    ORANGE = 3
    PURPLE = 4
    GREEN = 5
    RED = 6


def getBlock(block_string):
    # Could be solved using map, but it doesn't really matter with this few objects
    if block_string == "11110000":
        return Block.LIGHT_BLUE
    if block_string == "10001110":
        return Block.BLUE
    if block_string == "00101110":
        return Block.ORANGE
    if block_string == "01001110":
        return Block.PURPLE
    if block_string == "01101100":
        return Block.GREEN
    if block_string == "11000110":
        return Block.RED
    return None
