def tambah(pixels1, pixels2):
    new_pixels = []
    for i in range(len(pixels1)):
        if pixels2 == int:
            pixel = min(pixels1[i] + pixels2, 255)
        if pixels2 == list:    
            pixel = min(pixels1[i] + pixels2[i], 255)
        new_pixels.append(pixel)
    return new_pixels
