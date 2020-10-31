from PIL import Image
import numpy as np

class ImageProcess:
    def gray_scale(self, src):
        Width, Height = src.size

        ArrayImage = np.array(src)
        ArrayImage.flags.writeable = True
        for y in range(Height):
            for x in range(Width):
                ArrayImage[y, x][0] = 255 - ArrayImage[y, x][0]
                ArrayImage[y, x][1] = 255 - ArrayImage[y, x][1]
                ArrayImage[y, x][2] = 255 - ArrayImage[y, x][2]

        return Image.fromarray(np.uint8(ArrayImage))