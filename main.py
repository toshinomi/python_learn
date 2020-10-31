from PIL import Image
import sys
import image_process

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

    ImageProcess = image_process.ImageProcess()
    OutputImage = ImageProcess.gray_scale(InputImage)
    OutputImage.save("filtered_" + FileName)
    OutputImage.show()