import utils.utils as util


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