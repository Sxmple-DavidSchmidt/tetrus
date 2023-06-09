"""Module to store constants used throughout the program"""
# Should likely be replaced with something better down the road

import numpy as np

LIGHT_BLUE = np.array([[0, 0, 0, 0], [1, 1, 1, 1]])
ORANGE = np.array([[0, 0, 1, 0], [1, 1, 1, 0]])
BLUE = np.array([[0, 0, 1, 0], [1, 1, 1, 0]])
PURPLE = np.array([[0, 1, 0, 0], [1, 1, 1, 0]])


PRIMARY_DEFAULT_BG = 0
PRIMARY_BBOX = (271, 40, 533, 559)
PRIMARY_ROWS = 20
PRIMARY_COLS = 10
PRIMARY_BOX_SIZE = 25
PRIMARY_BOX_SEPARATION = 1
PRIMARY_BOX_DIFFERENCE = PRIMARY_BOX_SIZE + PRIMARY_BOX_SEPARATION

SECONDARY_DEFAULT_BG = 36
SECONDARY_BBOX = (607, 111, 710, 299)
SECONDARY_SUBBBOX = [(607, 111, 710, 163), (607, 179, 710, 231), (607, 247, 710, 299)]
SECONDARY_SUBBBOX_SIZE = (103, 52)
SECONDARY_SUBBBOX_SIZE_LONG = (0, 13, 103, 39)
SECONDARY_SUBBBOX_SIZE_MIN = (13, 0, 90, 52)

SECONDARY_SUBBBOX_RELATIVE = [
    (
        0,
        0,
        SECONDARY_SUBBBOX_SIZE[0],
        0 + SECONDARY_SUBBBOX_SIZE[1]
    ), (
        0,
        68,
        SECONDARY_SUBBBOX_SIZE[0],
        68 + SECONDARY_SUBBBOX_SIZE[1]
    ), (
        0,
        136,
        SECONDARY_SUBBBOX_SIZE[0],
        136 + SECONDARY_SUBBBOX_SIZE[1]
    )
]
