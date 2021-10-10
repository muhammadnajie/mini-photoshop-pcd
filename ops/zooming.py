import utils.utils as util
from division import division

def zoomout(pixels, image_size, x, y):
    new_pixels = util.convert_1d_to_2d(pixels, image_size)
    new_pixels = copy_row(new_pixels, y)
    new_pixels = copy_column(new_pixels, x)
    return new_pixels

def copy_row(pixels, y):
    new_pixels = []
    for row in pixels:
        for i in range(y):
            new_pixels.append(row.copy())
    return new_pixels

def copy_column(pixels, x):
    new_pixels = []
    for row in pixels:
        new_row = []
        for column in row:
            new_row.append([column for i in range(x)])
        new_pixels.append(new_row)
    return new_pixels

def zoomin(pixels, image_size, x, y):
    new_pixels = util.convert_1d_to_2d(pixels, image_size)
    new_pixels = add_row(new_pixels, y)
    new_pixels = add_column(new_pixels, x)
    new_pixels = division(new_pixels, x*y)
    return new_pixels

def add_row(pixels, y):
    i = 0
    sum_temp = 0
    width = len(pixels[0])
    height = len(pixels)
    new_pixels = [[] for _ in range(height//y)]
    for column in range(width):
        for row in range(height):
            sum_temp += pixels[row][column]
            i += 1
            if i == y:
                new_pixels[row//y].append(sum_temp)
                sum_temp = 0
                i = 0
    return new_pixels

def add_column(pixels, x):
    i = 0
    sum_temp = 0
    row_temp = []
    new_pixels = []
    for row in pixels:
        for pixel in row:
            sum_temp += pixel
            i += 1
            if i == x:
                row_temp.append(sum_temp)
                sum_temp = 0
                i = 0
        new_pixels.append(row_temp.copy())
        row_temp.clear()
    return new_pixels
