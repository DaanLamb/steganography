import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# local imports
from utils import calc_location, decrypt_and_trim

class NoMessageHidden(Exception):
    """Exception for when a message not encoded in provided image"""
    pass

def extract_from_image(img_path, key):
    # Extract a encrypted message from an image

    img = cv.imread(img_path, cv.IMREAD_UNCHANGED)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    img = cv.flip(img, -1)

    message = bytearray(b'')
    index = 0
    char = 0

    while len(message) < 3 or message[-3:] != b'\3\3\3':
        pixel_loc = calc_location(index, img.shape)
        char <<= 1
        char += img.item(pixel_loc) % 2
        if index % 8 == 7:
            message.append(char)
            char = 0
            byte = 0
            if index == 7 and message[0:1] != b'\2':
                raise NoMessageHidden
        index += 1

    return decrypt_and_trim(message, key)
