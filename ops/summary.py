def summary(pixels1, pixels2):
    new_pixels = []
    for i in range(len(pixels1)):
        pixel  = 0
        if type(pixels2) == int:
            pixel = min(pixels1[i] + pixels2, 255)
        if type(pixels2) == list:    
            pixel = min(pixels1[i] + pixels2[i], 255)
        new_pixels.append(pixel)
    return new_pixels
