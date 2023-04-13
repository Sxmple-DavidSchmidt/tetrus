import matplotlib.pyplot
import numpy as np
from PIL import Image

import Config


def get_sub_windows(image: Image):
    return [
        image.crop(Config.PRIMARY_BBOX),
        image.crop(Config.SECONDARY_BBOX)
    ]


def parse_primary_window(cropped_image: Image, flatten: bool = True) -> np.array:
    # Possible improvement: Not making a 2D array and flattening it later but making a 1D array from the start.
    ret_data = np.zeros((Config.PRIMARY_ROWS, Config.PRIMARY_COLS))

    for i in range(Config.PRIMARY_COLS):
        for j in range(Config.PRIMARY_ROWS):
            ret_data[j][i] = 1 if cropped_image.getpixel(
                (
                    i * Config.PRIMARY_BOX_DIFFERENCE + Config.PRIMARY_BOX_SIZE / 2,
                    j * Config.PRIMARY_BOX_DIFFERENCE + Config.PRIMARY_BOX_SIZE / 2
                )
            ) != 0 else 0

    if flatten:
        return ret_data.flatten()
    return ret_data


def parse_secondary_window(cropped_image: Image, flatten: bool = True) -> np.array:
    ret_data = np.zeros
    return ret_data


if __name__ == "__main__":
    image = Image.open("Screenshot 2023-04-13 115934.png").convert("L")
    wins = get_sub_windows(image)
    wins[1].show()
    image.crop(Config.SECONDARY_SUBBBOX[0]).show()
    print(wins)

    data = parse_primary_window(wins[0], flatten=False)
    matplotlib.pyplot.imshow(data, interpolation="nearest")
    matplotlib.pyplot.show()
