def bagi(pixels1, pixels2):
    new_pixels = []
    for i in range(len(pixels1)):
        new_pixels.append(int(pixels1[i]&pixels2[i]))
    return new_pixels