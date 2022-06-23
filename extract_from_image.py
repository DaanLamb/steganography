import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# local imports
from utils import calc_location, decrypt_and_trim


def extract_from_image():
    # Extract a encrypted message from an image

    img = cv.imread("images/frau_antje_with_message.png", cv.IMREAD_UNCHANGED)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    img = cv.flip(img, -1)

    message = bytearray(b'')
    index = 0
    char = 0

    while len(message) < 3 or message[-3:] != b'\x00\x00\x00':
        pixel_loc = calc_location(index, img.shape)
        char <<= 1
        char += img.item(pixel_loc) % 2
        if index % 8 == 7:
            message.append(char)
            char = 0
            byte = 0
        index += 1
    message = decrypt_and_trim(message, None)
    print("found message: " + message)


extract_from_image()
