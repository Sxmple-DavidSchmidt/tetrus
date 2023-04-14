from pathlib import Path

import matplotlib.pyplot
import numpy as np
from PIL import Image, ImageMode

import Config
import Block


def get_sub_windows(image: Image):
    return [
        image.crop(Config.PRIMARY_BBOX),
        image.crop(Config.SECONDARY_BBOX)
    ]

def translate_bw_color(bw_num, image_mode):
    # Kind of an ugly solution...
    # This is supposed to make the default background color adjust based on the image mode.
    # There is probably a better solution I am not aware of
    return Image.fromarray(
        np.uint8(
            [[bw_num]]
        )
    ).convert(image_mode).getpixel((0, 0))

def parse_primary_window(cropped_image: Image, flatten: bool = True) -> np.array:
    # Possible improvement: Not making a 2D array and flattening it later but making a 1D array from the start.
    ret_data = np.zeros((Config.PRIMARY_ROWS, Config.PRIMARY_COLS))
    default_color = translate_bw_color(Config.PRIMARY_DEFAULT_BG, image.mode)

    for i in range(Config.PRIMARY_COLS):
        for j in range(Config.PRIMARY_ROWS):
            ret_data[j][i] = 1 if cropped_image.getpixel((
                i * Config.PRIMARY_BOX_DIFFERENCE + Config.PRIMARY_BOX_SIZE / 2,
                j * Config.PRIMARY_BOX_DIFFERENCE + Config.PRIMARY_BOX_SIZE / 2
            )) != default_color else 0

    if flatten:
        return ret_data.flatten()
    return ret_data


def parse_secondary_window(cropped_image: Image, flatten: bool = True) -> np.array:
    default_color = translate_bw_color(Config.SECONDARY_DEFAULT_BG, image.mode)
    blocks = []

    for bbox in Config.SECONDARY_SUBBBOX_RELATIVE:
        subimage = cropped_image.crop(box=bbox)

        if subimage.getpixel((0, 26)) != default_color:
            blocks.append(Block.Block.LIGHT_BLUE)
        else:
            block = ""
            for y in range(2):
                for x in range(3):
                    px = (26 + x * 26, 13 + y * 26)
                    block += "1" if subimage.getpixel(px) != default_color else "0"
                block += "0"
            blocks.append(Block.get(block))
        subimage.save(f"{bbox[1]}.png")
    return blocks


if __name__ == "__main__":
    image_path = Path("assets", "testimages", "ingame_002.png")
    image = Image.open(image_path)
    image = image.convert("L")

    wins = get_sub_windows(image)

    print(Image.MODES)

    data_1 = parse_primary_window(wins[0], flatten=False)
    data_2 = parse_secondary_window(wins[1], flatten=False)
    print(data_2)

    matplotlib.pyplot.imshow(data_1, interpolation="nearest")
    matplotlib.pyplot.show()

