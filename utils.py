import os.path
from cryptography.fernet import Fernet

PATH = "~/Documents/keys/"
KEY_PATH = os.path.expanduser(PATH)

# intervals so altered pixel values are not next to one another
# intervals were chosen first digits of pi
ROWINTV = 3
COLUMNINTV = 1
CHANNELINTV = 4

def get_fernet_obj(key=None):
    if key == None:
        with open(os.path.join(KEY_PATH, "steg_key"), "rb") as key_file:
            key = key_file.read()
    return Fernet(key)

def pad_encrypt_message(message, key=None):
    # If no key is specified, looks in PATH location for steg_key file
    fernet_obj = get_fernet_obj(key)
    encrypted_message = fernet_obj.encrypt(message.encode('utf-8'))
    #add to indicate end of message
    encrypted_message = bytearray(encrypted_message) + b'\0\0\0'
    return bytes(encrypted_message)

def decrypt_and_trim(message, key=None):
    #remove trailing end indicators
    message = message[:-3]
    fernet_obj = get_fernet_obj(key)
    decrypted_message = fernet_obj.decrypt(bytes(message))
    return decrypted_message.decode('utf-8')

def calc_location(index, shape):
    #calculates the location associated with a specific index on a image of a specific shape

    # helper variables for ease of understanding
    # and reuse of same calculations
    vert_idx = (index) * ROWINTV
    horz_idx = (vert_idx // shape[0]) * COLUMNINTV
    depth_idx = (horz_idx // shape[1]) * CHANNELINTV
    return (vert_idx % shape[0], horz_idx % shape[1], depth_idx % shape[2])
