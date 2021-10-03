def multipication(pixels, pixels2):
    for i in range(len(pixels)):
        if pixels2 == int:
            pixels[i] *= pixels2
        elif pixels2 == list:
            pixels[i] *= pixels2[i]

        if pixels2[i] > 255:
            pixels2[i] = 255
    return pixels