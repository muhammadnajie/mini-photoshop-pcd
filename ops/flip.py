import utils.utils as util

def vertical_flip(pixels, image_size):
    pixels_2d = util.convert_1d_to_2d(pixels, image_size)
    flipped_image = []
    for i in range(image_size[1]):
        flipped_image.append([0] * image_size[0])
    K = image_size[1] - 1
    for i in range(image_size[1]):
        for j in range(image_size[0]):
            flipped_image[K][j] = pixels_2d[i][j]
        K -= 1
    return flipped_image

def horizontal_flip(pixels, image_size):
    """
    :param pixels:
    :param image_size (tuple, w*h):
    :return:
    """
    pixels_2d = util.convert_1d_to_2d(pixels, image_size)
    flipped_image = []
    W = image_size[0]
    for i in range(image_size[1]):
        row = []
        for j in range(image_size[0]):
            row.append(pixels_2d[i][W-j-1])
        flipped_image.append(row)
    return flipped_image
