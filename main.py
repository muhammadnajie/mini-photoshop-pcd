from utils.utils import *
from ops import *
import sys

# pixels = getPixels("image.jpg")
# print(type(pixels))
# imageSize = getImageSize("image.jpg") # <----- mendapatkan image size (width, height)
# resultPixels = test(pixels) #<------- untuk manggil fungsi yang sedang dibuat
# savedImage = saveImage(pixels, imageSize[1], imageSize[0])

if __name__ == "__main__":
    conf = mapping_parameter(sys.argv[1:])
    data = prepare_data(conf)
    do_ops(conf, data)