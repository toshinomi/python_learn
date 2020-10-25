from PIL import Image
import numpy as np
import sys

def image_process(src):
    width, height = src.size

    imageArray = np.array(src)
    imageArray.flags.writeable = True
    for y in range(height):
        for x in range(width):
            imageArray[y, x][0] = 255 - imageArray[y, x][0] #R
            imageArray[y, x][1] = 255 - imageArray[y, x][1] #G
            imageArray[y, x][2] = 255 - imageArray[y, x][2] #B

    return Image.fromarray(np.uint8(imageArray))

if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 2):
        print ("Usage: $ python3 " + param[0] + " sample.jpg")
        quit()

    file_name = param[1]
    try:
        input_image = Image.open(file_name)
    except:
        print ('faild to load %s' % file_name)
        quit()

    if input_image is None:
        print ('faild to load %s' % fileName)
        quit()

    output_image = image_process(input_image)
    output_image.save("filtered_" + file_name)
    output_image.show()