def and_ops(pixels1, pixels2):
    new_pixels = []
    for i in range(len(pixels1)):
        new_pixels.append(pixels1[i]&pixels2[i])
    return new_pixels