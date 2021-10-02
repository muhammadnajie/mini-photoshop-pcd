from PIL import Image
import numpy as np
import time

from numpy.lib.utils import source

#get data pixels from source file
#return data type is list
def getPixels(sourceFile):
    try:
        im = Image.open(sourceFile)
        pixels = list(im.getdata())
        im.close()
        return pixels
    except:
        print("can't open the source file. Make sure source file is correct.")

#check if pixels (data type is list) is a grayscale or not
def isGrayscale(pixels):
    return pixels[0] == int

#save image from pixels with name 'destFile', height 'height', and width 'width'
def saveImage(pixels, height, width, destFile):
    try:
        ar = np.array(pixels, dtype=np.uint8)
        ar = np.reshape(ar, (height, width))
        im = Image.fromarray(ar)
        destFile = destFile or str(round(time.time()*1000))+".png"
        im.save(destFile)
        return destFile
    except:
        print("Fail to save the image.")

#get all source file from command
def getAllSourceFile(command):
    opIndex= 0
    for arg in command:
        if(arg == "--op"):
            break
        opIndex = opIndex + 1
    sourceFile = []
    if len(command)-1 > opIndex:
        for i in range(opIndex+1, len(command)):
            if(command[i][0] == '-'):
                break
            sourceFile.append(command[i])
    return sourceFile
    
#get image size from file name
#return data type is tuple (width, height)
def getImageSize(image):
    im = Image.open(image)
    size = im.size
    im.close()
    return size

# return max width and max height
# ex. data = (150, 300) and (220, 110)
# returned data (220, 110)
def getMaxSize(images): 
    maxWidth = 0
    maxHeight = 0
    for image in images:
        size = getImageSize(image)
        maxWidth = max(maxWidth, size[0])
        maxHeight = max(maxHeight, size[1])
    return (maxWidth, maxHeight)

#get destiny file name from command
def getDestFile(command):
    dIndex= 0
    for arg in command:
        if(arg == "-d"):
            break
        dIndex = dIndex + 1
    return command[dIndex + 1] if len(command) - 1 > dIndex else ""


def convert_1d_to_2d(pixels, image_size):
    new_pixels = []
    for i in range(image_size[1]):
        start = i * image_size[0]
        end = start + image_size[0]
        new_line = pixels[start:end]
        new_pixels.append(new_line)
    return new_pixels