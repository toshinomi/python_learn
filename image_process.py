from PIL import Image
import numpy as np
from enum import IntEnum

class ImageProcess:
    def gray_scale(self, src):
        Width, Height = src.size

        ArrayImage = np.array(src)
        ArrayImage.flags.writeable = True
        for y in range(Height):
            for x in range(Width):
                ArrayImage[y, x][Color.RED] = Rgb.MAX - ArrayImage[y, x][Color.RED]
                ArrayImage[y, x][Color.GREEN] = Rgb.MAX - ArrayImage[y, x][Color.GREEN]
                ArrayImage[y, x][Color.BLUE] = Rgb.MAX - ArrayImage[y, x][Color.BLUE]

        return Image.fromarray(np.uint8(ArrayImage))

class Color(IntEnum):
    RED = 0
    GREEN = 1
    BLUE = 2
    ALPHA  = 3

class Rgb(IntEnum):
    MIN = 0
    MAX = 255