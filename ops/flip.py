from utils.utils import convert_1d_to_2d, flatten
import numpy as np

def vertical_flip():
    # TODO: Vertical Flip
    pass

def horizontal_flip(pixels, image_size):
    """
    :param pixels:
    :param image_size (tuple, w*h):
    :return:
    """
    pixels_2d = convert_1d_to_2d(pixels, image_size)
    flipped_image = []
    W = image_size[0]
    for i in range(len(pixels_2d)):
        row = []
        for j in range(len(pixels_2d[i])):
            row.append(pixels_2d[i][W-j-1])
        flipped_image.append(row)
    return flipped_image
