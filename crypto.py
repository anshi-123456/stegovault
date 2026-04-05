from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def generate_key(password):
    return hashlib.sha256(password.encode()).digest()

def encrypt_data(data, password):
    key = generate_key(password)
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))
    return cipher.iv + encrypted

def decrypt_data(cipher_data, password):
    key = generate_key(password)
    iv = cipher_data[:16]
    encrypted = cipher_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(encrypted), AES.block_size).decode()