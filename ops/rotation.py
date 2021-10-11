import math
import utils.utils as util


def CcwRotation(pixels, image_size, degree):
    width = image_size[0]
    height = image_size[1]
    longest = math.ceil(math.sqrt(width * 2 + height * 2))
    pixels = util.convert_1d_to_2d(pixels, image_size)
    new_pixels = [[0 for __ in range(longest)] for _ in range(longest)]
    radian = math.radians(degree)
    coor_map = {}
    min_x = math.inf
    min_y = math.inf
    for x in range(width):
        for y in range(height):
            # x'= x cos(val) – y sin(val)
            # y'= x sin(val) + y cos(val)
            newX = round(x * math.cos(radian) - y * math.sin(radian))
            newY = round(x * math.sin(radian) + y * math.cos(radian))
            coor_map[(x, y)] = (newX, newY)
            min_x = min(min_x, newX)
            min_y = min(min_y, newY)
    if min_x < 0:
        coor_map = add_x(coor_map, min_x)
    if min_y < 0:
        coor_map = add_y(coor_map, min_y)
    for key in coor_map:
        new_coor = coor_map[key]
        new_pixels[new_coor[0]][new_coor[1]] = pixels[key[0]][key[1]]
    return new_pixels


def add_x(coor_map, x):
    for key in coor_map:
        coor_map[key] = (coor_map[key][0] + x, coor_map[key][1])
    return coor_map


def add_y(coor_map, y):
    for key in coor_map:
        coor_map[key] = (coor_map[key][0], coor_map[key][1] + y)
    return coor_map
