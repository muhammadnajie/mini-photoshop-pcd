def negative(pixels):
    for i in range(len(pixels)):
        pixels[i] = 255 - pixels[i]
    return pixels