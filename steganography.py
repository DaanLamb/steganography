import argparse
import os.path
from utils import key_from_file, key_from_password, append_to_filename
from extract_from_image import extract_from_image, NoMessageHidden
from store_in_image import store_in_image
from cryptography.fernet import InvalidToken

def main():
    dir = os.path.dirname(__file__)
    # store or retrieve, image location, key from password, or key location
    parser = argparse.ArgumentParser(description='Stores or retrieves an encrypted message in an image.')
    parser.add_argument('-r', '--retrieve', action='store_true')
    parser.add_argument('-m', '--message')
    parser.add_argument('-i', '--image-location', default=os.path.join(dir, 'images', 'frau_antje.png'), help='Location of the image, defaults to images/frau_antje.png')
    parser.add_argument('-p', '--password', help='password to encrypt/decrypt message. If none is given, a key will be used')
    parser.add_argument('-k', '--key-location', default=os.path.join(dir, 'keys', 'steg_key'), help='Key location to encrypt/decrypt message, defaults to key/steganography')
    args = parser.parse_args()

    #logic for handling arguments
    if args.retrieve and (args.message != None):
        parser.error("retrieve option returns a message, cannot specify a message when retrieving")

    if (not args.retrieve) and (args.message is None):
        parser.error("specify a message to store in the image")

    if not (args.image_location.endswith('.png') or args.image_location.endswith('.PNG')):
        parser.error("Image should be an .png image")

    # key handling
    if args.password is not None:
        key = key_from_password(args.password)
    else:
        key = key_from_file(args.key_location)

    if args.retrieve:
        print("extracting message from: " +  args.image_location)
        try:
            print(extract_from_image(args.image_location, key))
        except InvalidToken:
            print("Problems occurred when decrypting the message. Make sure you have the right key or password")
        except NoMessageHidden:
            print("No message seems to be hidden in this image")
    else:
        print("storing message: \n" + args.message + "\nIn image: " + append_to_filename(args.image_location))
        store_in_image(args.image_location, key, args.message)





if __name__ == "__main__":
    main()
