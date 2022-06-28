import os.path
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def append_to_filename(filename):
  return "{0}_message{1}".format(*os.path.splitext(filename))

def key_from_file(path):
    if not os.path.isabs(path):
        dir = os.path.dirname(__file__)
        path = os.path.join(dir, path)
    with open(path, "rb") as key_file:
        key = key_file.read()
    return key

def key_from_password(password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'1234567890123456',
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))


def pad_encrypt_message(message, key):
    # If no key is specified, looks in PATH location for steg_key file
    fernet_obj = Fernet(key)
    encrypted_message = fernet_obj.encrypt(message.encode('utf-8'))
    #add to indicate end of message
    encrypted_message = b'\2' + bytearray(encrypted_message) + b'\3\3\3'
    return bytes(encrypted_message)

def decrypt_and_trim(message, key):
    #remove trailing end indicators
    message = message[1:-3]
    fernet_obj = Fernet(key)
    decrypted_message = fernet_obj.decrypt(bytes(message))
    return decrypted_message.decode('utf-8')

def calc_location(index, shape):
    #calculates the location associated with a specific index on a image of a specific shape

    # intervals so altered pixel values are not next to one another
    # intervals were chosen first digits of pi
    ROWINTV = 3
    COLUMNINTV = 1
    CHANNELINTV = 4

    # helper variables for ease of understanding
    # and reuse of same calculations
    vert_idx = (index) * ROWINTV
    horz_idx = (vert_idx // shape[0]) * COLUMNINTV
    depth_idx = (horz_idx // shape[1]) * CHANNELINTV
    return (vert_idx % shape[0], horz_idx % shape[1], depth_idx % shape[2])
