#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import *
import random

#FLAG = open("flag.png", "rb").read()
encrypted = open("flag.enc", "rb").read()
STEG = b"gemasteg"


def getrandsteg():
    x = list(STEG)
    random.shuffle(x)
    return bytes(x)


#def encrypt(msg: bytes, key: bytes):
    key = SHA256.new(key).digest()
    iv = STEG * 2
    aes = AES.new(key, AES.MODE_CBC, iv)
    enc = aes.encrypt(msg)
    return enc

def decrypt(msg: bytes, key: bytes):
    key = SHA256.new(key).digest()
    iv = STEG * 2
    #aes = AES.new(key, AES.MODE_CBC, iv)
    #enc = aes.encrypt(msg)
    aes = AES.new(key, AES.MODE_ECB)
    dec1 = aes.decrypt(msg)
    return dec1


#def double(msg: bytes, keys: list[bytes]):
    msg = pad(msg, AES.block_size)
    for key in keys:
        msg = encrypt(msg, key)
    return msg


def double2(msg: bytes, keys: list[bytes]):
    msg = pad(msg, AES.block_size)
    for key in keys:
        msg = decrypt(msg, key)
    return msg


def fwrite(filename: str, data: bytes):
    f = open(filename, "wb")
    f.write(data)
    f.close()


keys = [getrandsteg() for _ in range(2)]
print(type(keys))
#fwrite("flag.png", double2(encrypted, keys))
