from PIL import Image
import sys
from image_process import ImageProcess

if __name__ == '__main__':
    Param = sys.argv
    if (len(Param) != 2):
        print ("Usage: $ python3 " + Param[0] + " sample.jpg")
        quit()

    FileName = Param[1]
    try:
        InputImage = Image.open(FileName)
    except:
        print ('faild to load %s' % FileName)
        quit()

    if InputImage is None:
        print ('faild to load %s' % FileName)
        quit()

    ImageProcess = ImageProcess()
    OutputImage = ImageProcess.gray_scale(InputImage)
    OutputImage.save("filtered_" + FileName)
    OutputImage.show()