"""Module to parse Tetris game window and make it easier to work with"""

from pathlib import Path
import matplotlib.pyplot
import numpy as np
from PIL import Image

from src import config
from src.block import Block


def get_sub_windows(canvas_image: Image):
    """
    Turns a 800 x 600 sized image of the Tetris gameplay window
    into a list of cropped sub-images

    :param canvas_image: Screenshot of the Tetris gameplay window
    :returns: List of cropped sub-images
    """
    return [
        canvas_image.crop(config.PRIMARY_BBOX),
        canvas_image.crop(config.SECONDARY_BBOX)
    ]


def translate_bw_color(bw_num, image_mode):
    """
    Converts a black/white color pixel to a given format

    :param bw_num: The black/white pixel-value to convert
    :param image_mode: The image mode to convert the pixel-value to
    :returns: Returns the black/white pixel-value
    """

    # Kind of an ugly solution...
    return Image.fromarray(
        np.uint8(
            [[bw_num]]
        )
    ).convert(image_mode).getpixel((0, 0))


def parse_primary_window(cropped_image: Image, flatten: bool = True) -> np.array:
    """
    Converts a cropped image of the primary window into a numpy array representing the data

    :param cropped_image: Cropped image of the primary window
    :param flatten: Bool to decide if the numpy array should be flattened. Default: True
    :returns: Numpy array representing the playing field
    """

    # Possible improvement: Not making a 2D array and flattening it later
    # but instead making a 1D array from the start.
    ret_data = np.zeros((config.PRIMARY_ROWS, config.PRIMARY_COLS))
    default_color = translate_bw_color(config.PRIMARY_DEFAULT_BG, cropped_image.mode)

    for i in range(config.PRIMARY_COLS):
        for j in range(config.PRIMARY_ROWS):
            ret_data[j][i] = 1 if cropped_image.getpixel((
                i * config.PRIMARY_BOX_DIFFERENCE + config.PRIMARY_BOX_SIZE / 2,
                j * config.PRIMARY_BOX_DIFFERENCE + config.PRIMARY_BOX_SIZE / 2
            )) != default_color else 0

    if flatten:
        return ret_data.flatten()
    return ret_data


def parse_secondary_window(cropped_image: Image):
    """
    Reads a cropped image of the secondary window
    and turns it into a list containing the upcoming Tetris pieces

    :param cropped_image: Cropped image of the secondary window
    :returns: List containing the upcoming Tetris pieces
    """

    default_color = translate_bw_color(config.SECONDARY_DEFAULT_BG, cropped_image.mode)

    blocks = []
    for bbox in config.SECONDARY_SUBBBOX_RELATIVE:
        # TODO is not actually necessary. Could be solved just by using math. Keeping for now.
        subimage = cropped_image.crop(box=bbox)

        if subimage.getpixel((0, 26)) != default_color:
            blocks.append(Block.LIGHT_BLUE)
        else:
            block_string = ""
            for row in range(2):
                for col in range(3):
                    block_string += "1" if subimage.getpixel(
                        (26 + col * 26, 13 + row * 26)
                    ) != default_color else "0"
                block_string += "0"
            blocks.append(Block.get_block(block_string))
    return blocks


if __name__ == "__main__":
    image_path = Path("../assets", "test", "images", "image_002.png")
    image = Image.open(image_path)
    image = image.convert("L")

    wins = get_sub_windows(image)

    print(Image.MODES)

    data_1 = parse_primary_window(wins[0], flatten=False)
    data_2 = parse_secondary_window(wins[1])
    print(data_2)

    matplotlib.pyplot.imshow(data_1, interpolation="nearest")
    matplotlib.pyplot.show()
