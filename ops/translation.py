from utils.utils import convert_1d_to_2d


def translation(pixels, imgSize, x, y):
    pixels = convert_1d_to_2d(pixels, imgSize)
    height = imgSize[1]
    width = imgSize[0]
    new_pixels = [[0 for i in range(width)] for j in range(height)]
    for i in range(height):
        for j in range(width):
            if(i+y < height and j-x < width and i+y > 0 and j-x > 0):
                new_pixels[i][j] = pixels[i+y][j-x]
    return new_pixels
