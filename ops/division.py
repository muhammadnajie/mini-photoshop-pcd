def division(pixels, scalar):
    new_pixels = []
    for i in range(len(pixels)):
        new_pixels.append(int(pixels[i]/scalar))
    return new_pixels