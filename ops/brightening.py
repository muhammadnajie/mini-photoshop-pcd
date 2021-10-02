def image_brightening(pixels, addition):
    for index, pixel in enumerate(pixels):
        if pixel + addition < 0:
            pixels[index] = 0
        elif pixel + addition > 255:
            pixels[index] = 255
        else:
            pixels[index] = pixels[index] + addition
    return pixels
