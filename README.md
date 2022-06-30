# steganography
Steganography using python

This program encrypts a message an stores it in the last pixel values of an image.

The message is encrypted using Fernet from the cryptography library. It can use either stored key or a key derived from a password.

An example key is found in the keys folder, this is also the default key used encryption and decryption. If you would like to make another key, the keygen.py script can be used.

The encryption is mostly used for obfuscation of the message. The implementation still properly uses Fernet encryption but this was mostly done for me to get some experience with the library. In any case putting your keys on github usually isn't the best security practice (don't worry this is key generated specifically to be made public for this project).

## usage
usage: python steganography.py [-h] [-r] [-m MESSAGE] [-i IMAGE_LOCATION]
                        [-p PASSWORD] [-k KEY_LOCATION]

## improvements
Right now the system uses a hard coded salt for the key derivation function. This is not much of a problem since the hashes are not stored. They are used to encrypt the messages. Since Fernet uses AES, which is resistant to known plain text attacks, recovering a key from a image and message will be difficult. Therefore the output of the key derivation function should be reasonably safe. But to increase safety even more, a specific salt could be generated for each image, which would also be stored in the image. This ensures that even with the hashes, a brute force or rainbow table attack becomes more difficult. Implementing this is for the future
