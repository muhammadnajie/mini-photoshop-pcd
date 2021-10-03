from PIL import Image
import numpy as np
import time
from ops.and_ops import and_ops

from ops.brightening import image_brightening
from ops.division import division
from ops.flip import horizontal_flip, vertical_flip
from ops.multiplication import multipication
from ops.negative import negative
from ops.or_ops import or_ops
from ops.rgb2grayscale import rgb2grayscale
from ops.substraction import substraction
from ops.summary import summary
from ops.translation import translation
from ops.xor import xor_ops
from ops.zooming import zoomout

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
    # try:
        ar = np.array(pixels, dtype=np.uint8)
        ar = np.reshape(ar, (height, width))
        im = Image.fromarray(ar)
        dest_file = dest_file or str(round(time.time() * 1000)) + DEFAULT_EXTENSION
        im.save(dest_file)
        return dest_file
    # except:
    #     print("Fail to save the image.")


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

def get_overlap(image_size1, image_size2):
    return (min(image_size1[0], image_size2[0]), min(image_size1[1], image_size2[1]))

def crop_1d(pixels, old_image_size, new_image_size):
    new_pixels = convert_1d_to_2d(pixels, old_image_size)
    return flatten(crop_2d(new_pixels, new_image_size))

def crop_2d(pixels, new_image_size):
    width, height = new_image_size
    new_pixels = []
    for row in pixels:
        new_pixels.append(row[:width])
    return new_pixels

def flatten(array):
    return list(np.array(array).flatten())

def is_rgb(pixels):
    return isinstance(pixels[0], tuple)

def mapping_parameter(command):
    user_input = {"x": "", "y": "", "c": "", "o": "", "r": ""}
    op_and_sourcefile = {"op":"", "source_file": [], "image_size": []}
    param = ""
    i = 0
    while i < len(command):
        if command[i][0] == "-":
            param = command[i][1:]
            if param in user_input:
                i += 1
                user_input[param] = eval(command[i])
            else:
                raise ValueError("can't reconignize the '"+param+"' parameter.")
        else:
            op = command[i]
            op_and_sourcefile["op"] = op
            j = i+1
            while j < len(command):
                if command[j][0] == "-":
                    break 
                file = command[j]
                pixels = get_pixels(file)
                image_size = get_image_size(file)
                op_and_sourcefile["source_file"].append(pixels)
                # op_and_sourcefile["source_file"].append(file)
                op_and_sourcefile["image_size"].append(image_size)
                j += 1
            i = j-1
        i += 1
    user_input.update(op_and_sourcefile)
    if len(user_input["source_file"]) == 2:
        sizes = user_input["image_size"]
        overlap_size = get_overlap(*sizes)
        user_input["source_file"][0] = crop_1d(user_input["source_file"][0], sizes[0], overlap_size)
        user_input["source_file"][1] = crop_1d(user_input["source_file"][1], sizes[1], overlap_size)
        user_input["result_size"] = overlap_size
    return user_input

def prepare_data(conf):
    args = []
    temp = {}
    with open("rules.txt") as rules_file:
        rules = eval(rules_file.read())
        op = conf["op"]
        if op not in rules:
            raise ValueError("can't reconignize the '"+conf["op"]+"' command.")
        rules_op = rules[op]
        print("rules_op",rules_op )
        for rule in rules_op:
            detail = rule.split(".")
            data = conf[detail[0]]
            if data == "":
                raise ValueError("command "+op+" need "+detail[0]+" data")
            if isinstance(data, list):
                temp.setdefault(detail[0], [])
                if data:
                    data = data.pop(0)
                    temp[detail[0]].append(data)
                else:
                    raise ValueError("command "+op+" need more "+detail[0])
            if len(detail) == 2:
                if detail[1] == "rgb" and not is_rgb(data):
                    raise TypeError("Image must be rgb for "+op+" command")
            elif isinstance(data, list):
                if not is_grayscale(data):
                    raise TypeError("Image must be greyscale for "+op+" command")
            elif detail[0] == "image_size":
                pass
            elif not isinstance(data, int):
                raise TypeError("Image must be int for "+detail[0]+" parameter")
            args.append(data)
    conf.update(temp)
    return args

def do_ops(conf, data):
    op_functions = {
        "and" : and_ops,
        "bright": image_brightening,
        "div": division,
        "vflip": vertical_flip,
        "hflip": horizontal_flip,
        "or": or_ops,
        "rgb2grayscale": rgb2grayscale,
        "subc": substraction,
        "sub": substraction,
        "sumc": summary,
        "sum": summary,
        "translation": translation,
        "xor": xor_ops,
        "zoomout": zoomout,
        "negative": negative,
        "multi": multipication,
        "multic": multipication
    }
    op = conf["op"]
    result = op_functions[op](*data)
    if conf["source_file"] == 2:
        size = conf["result_size"][0]
    else:
        size = conf["image_size"][0]
    size = list(size)
    if op == "zoomout":
        size[0] *= conf["x"]
        size[1] *= conf["y"]
    elif op == "zoomin":
        size[0] /= conf["x"]
        size[1] /= conf["y"]
    o = save_image(result, size[1], size[0], conf["o"])
    print("Image successfully saved in "+o)