from PIL import Image
import numpy as np
import time

from numpy.lib.utils import source

DEFAULT_EXTENSION = ".png"


def get_pixels(source_file):
    """ Convert image from the source file into array
    representing each pixel for its element

    Args:
        source_file (str): The first parameter
            the location of the image

    Returns:
        obj: 1d array of unsigned int

    Raises:
        FileNotFoundError:
    """
    try:
        im = Image.open(source_file)
        pixels = list(im.getdata())
        im.close()
        return pixels
    except FileNotFoundError:
        msg = "can't open the source file. Make sure source file is correct."
        raise FileNotFoundError(msg)


def is_grayscale(pixels):
    """ Check if the image is a grayscale"""
    return pixels[0] == int


# save image from pixels with name 'destFile', height 'height', and width 'width'
def save_image(pixels, height, width, dest_file):
    try:
        ar = np.array(pixels, dtype=np.uint8)
        ar = np.reshape(ar, (height, width))
        im = Image.fromarray(ar)
        dest_file = dest_file or str(round(time.time() * 1000)) + DEFAULT_EXTENSION
        im.save(dest_file)
        return dest_file
    except:
        print("Fail to save the image.")


# get all source file from command
def get_all_source_files(command):
    op_index = 0
    for arg in command:
        if arg == "--op":
            break
        op_index = op_index + 1
    source_file = []
    if len(command) - 1 > op_index:
        for i in range(op_index + 1, len(command)):
            if (command[i][0] == '-'):
                break
            source_file.append(command[i])
    return source_file


# get image size from file name
# return data type is tuple (width, height)
def get_image_size(image):
    im = Image.open(image)
    size = im.size
    im.close()
    return size


# return max width and max height
# ex. data = (150, 300) and (220, 110)
# returned data (220, 110)
def get_max_size(images):
    max_width = 0
    max_height = 0
    for image in images:
        size = get_image_size(image)
        max_width = max(max_width, size[0])
        max_height = max(max_height, size[1])
    return tuple([max_width, max_height])


# get destiny file name from command
def get_dest_file(command):
    d_index = 0
    for arg in command:
        if arg == "-d":
            break
        d_index = d_index + 1
    return command[d_index + 1] if len(command) - 1 > d_index else ""


def convert_1d_to_2d(pixels, image_size):
    new_pixels = []
    for i in range(image_size[1]):
        start = i * image_size[0]
        end = start + image_size[0]
        new_line = pixels[start:end]
        new_pixels.append(new_line)
    return new_pixels

def get_overlap(source_file1, source_file2):
    image_size1 = get_image_size(source_file1)
    image_size2 = get_image_size(source_file2)
    return (min(image_size1[0], image_size2[0]), min(image_size1[1], image_size2[1]))

def crop(pixels, old_image_size, new_image_size):
    new_pixels = convert_1d_to_2d(pixels, old_image_size)
    return crop(new_pixels, new_image_size)

def crop(pixels, new_image_size):
    width, height = new_image_size
    new_pixels = []
    for row in height:
        new_pixels.append(row[:width])
    return new_pixels

def flatten(array):
    return list(np.array(array).flatten())
