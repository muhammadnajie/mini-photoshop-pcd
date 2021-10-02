def or_ops(pixels1, pixels2):
    new_pixels = []
    for i in range(len(pixels1)):
        pixel = int(pixels1[i] | pixels2[i])
        new_pixels.append(pixel)
    return new_pixels
