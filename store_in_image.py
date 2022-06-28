import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# local imports
from utils import pad_encrypt_message, calc_location, append_to_filename


def addNoise(image):
    noise = np.random.randint(3, size=image.shape, dtype=np.uint8) - 1 # array of image size with -1's,0's and 1's
    image = image + noise
    image = image.clip(0,255)
    return image

def store_in_image(img_path, key, message):
    # prepare message
    encrypted_message = pad_encrypt_message(message, key)

    img = cv.imread(img_path, cv.IMREAD_UNCHANGED)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    img = addNoise(img)

    # flip image to start from other side
    img = cv.flip(img, -1)

    for byte_idx, byte in enumerate(encrypted_message):

        for bit_idx in range(8):
            bit = byte // 128 # only want first bit

            pixel_loc = calc_location(byte_idx * 8 + bit_idx, img.shape)

            img.itemset(pixel_loc, (((img.item(pixel_loc) >> 1) << 1) + bit))
            byte = byte % 128 << 1 # to put next bit in first position

    img = cv.flip(img, -1)
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    cv.imwrite(append_to_filename(img_path), img)
