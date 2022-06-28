# steganography
Steganography using python

This program encrypts a message an stores it in the last pixel values of an image.

The message is encrypted using Fernet from the cryptography library. It can use either stored key or a key derived from a password.

An example key is found in the keys folder, this is also the default key used encryption and decryption. If you would like to make another key, the keygen.py script can be used.

The encryption is used for obfuscation and not

## usage
usage: python steganography.py [-h] [-r] [-m MESSAGE] [-i IMAGE_LOCATION]
                        [-p PASSWORD] [-k KEY_LOCATION]

## improvements
Right now the system uses a hard coded salt for the key derivation function. If an attacker gets access to the decrypted message and the image, they could use a then use a brute force or rainbow table attack to figure out the password. A better option would be to use a nonce as the salt and store it in the image as well.
