import random

def bytes_to_binary(data):
    return ''.join(format(byte, '08b') for byte in data)

def binary_to_bytes(binary):
    return bytes(int(binary[i:i+8], 2) for i in range(0, len(binary), 8))

def generate_positions(seed, total):
    random.seed(seed)
    positions = list(range(total))
    random.shuffle(positions)
    return positions