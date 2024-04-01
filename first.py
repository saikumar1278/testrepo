from Crypto.Cipher import AES
from secrets import token_bytes
key = token_bytes(16)


def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ct = cipher.encrypt(msg.encode('ascii'))
    print(f'Cipher Text = {ct}')
    decrypt(ct, nonce)


def decrypt(ct, nonce):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    pt = cipher.decrypt(ct).decode('ascii')
    print("Plain Text = "+pt)


msg = input("Enter text msg :")
encrypt(msg)
