#/usr/bin/python3


from base64 import b64encode
from base64 import b64decode

def encrypt(plain):
    key = "n0k3y"
    cipher = ""
    for c, i in enumerate(plain):
        cipher += chr(ord(i) ^ ord(key[c % 5]))

    print(b64encode(cipher.encode()))

def decrypt(encrypted):
    key = "n0k3y"
    cipher = ""
    #decrypted = ''.join([chr(ord(i) ^ ord(key[c % 5])) for c, i in enumerate(b64decode(encrypted))])
    for c, i in enumerate(b64decode(encrypted)):
         cipher += chr(i ^ ord(key[c % 5]))
         print(cipher)

if __name__ == "__main__":
    plain = input()
    decrypt(plain)
