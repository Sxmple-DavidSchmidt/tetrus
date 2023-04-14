"""Module to represent different kinds of Tetris blocks"""
from enum import Enum


class Block(Enum):
    """Enum class containing the possible Tetris blocks"""
    LIGHT_BLUE = 0
    BLUE = 1
    ORANGE = 2
    PURPLE = 3
    GREEN = 4
    RED = 5

    @staticmethod
    def get_block(block_string):
        """
        Method to get the corresponding Block-entity to a block_string.

        A block_string should be read as a 2 line string with 4 characters each.
        Characters set to 0 should be read as "There is no block at this position"

        This way blocks can be identified.

        Example:
            block_string: "11110000"
            returns Block.LIGHT_BLUE
        """

        # Could be solved using map, but it doesn't really matter with this few objects

        # Also this is a little inefficient.
        # Keeping for now as it is not called a lot and has little impact.
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


