import os.path
from cryptography.fernet import Fernet

dir = os.path.dirname(__file__)

key = Fernet.generate_key()
f = Fernet(key)
print(key)

key_name = input("What should the filename of the key be\n")

with open(os.path.join(dir, "keys", key_name), "wb") as key_file:
    key_file.write(key)

with open(os.path.join(dir, "keys", key_name), "rb") as key_file:
    key = key_file.read()

print(key)

fernet_obj = Fernet(key)
encrypted_message = fernet_obj.encrypt(b'message')
print(encrypted_message)
print(fernet_obj.decrypt(encrypted_message))
