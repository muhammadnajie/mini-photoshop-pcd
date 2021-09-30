from utils.utils import *
from ops.tes import * # <---- untuk import operasi yang sedang dikerjakan, ganti tes dengan nama python file yang dibuat
import sys

pixels = getPixels("alamat file")
imageSize = getImageSize("alamat file") # <----- mendapatkan image size (width, height)
resultPixels = test(pixels) #<------- untuk manggil fungsi yang sedang dibuat
savedImage = saveImage(pixels, imageSize[1], imageSize[0], "test.png")

# if __name__ == "__main__":
#     sourceFiles = getAllSourceFile(sys.argv)
#     pixelDatas = []
#     for file in sourceFiles:
#         pixelDatas.append(getPixels(file))
#     destFile = getDestFile(sys.argv)
#     resultWidth, resultHeight = getMaxSize(sourceFiles)
#     # pixelDatas bertipe data list dan berisi data pixel dari source files (sesuai dengan urutan source file)
#     # ubah nama fungsi test sesuai dengan nama fungsi yang anda buat 
#     image = test(pixelDatas[0])
#     savedFile = saveImage(image, resultHeight, resultWidth, destFile)
#     print("File saved in "+savedFile)