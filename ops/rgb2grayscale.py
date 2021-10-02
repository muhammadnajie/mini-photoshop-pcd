def rgb2grayscale(pixels):
    print(pixels[0][0])
    for index, pixel in enumerate(pixels):
        imgGray = 0.299 * pixels[index][0] + 0.587 * \
            pixels[index][1] + 0.1440 * pixels[index][2]
        pixels[index] = round(imgGray)
    return pixels
