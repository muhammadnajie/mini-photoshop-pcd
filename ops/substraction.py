def substraction(pixels1, pixels2):
    new_pixels = []
    for i in range(len(pixels1)):
        if type(pixels2) == int:
            pixel = pixels1[i] - pixels2
            if (pixel != 0):
                pixel = 255
        elif type(pixels2) == list:
            pixel = pixels1[i] - pixels2[i]
            if (pixel != 0):
                pixel = 255
        new_pixels.append(pixel)
    return new_pixels
