def F(x, S):
    return ((S[0][x >> 24] + S[1][(x >> 16) & 0xFF]) ^ S[2][(x >> 8) & 0xFF]) + S[3][x & 0xFF]

def int_to_bytes(i):
    # Convert integer to bytes (big-endian)
    return bytes([(i >> (8 * j)) & 0xFF for j in range(3, -1, -1)])

def bytes_to_int(b):
    # Convert bytes to integer (big-endian)
    return sum((b[i] << (8 * i) for i in range(len(b))))

def encrypt_block(block, P, S):
    left, right = bytes_to_int(block[:4]), bytes_to_int(block[4:])

    for i in range(16):
        left ^= P[i]
        right ^= F(left, S)
        left, right = right, left

    left, right = right, left
    right ^= P[16]
    left ^= P[17]

    return int_to_bytes(left) + int_to_bytes(right)

def initialize_blowfish(key):
    # Blowfish key initialization

    # P-array (18 32-bit subkeys)
    P = [0] * 18
    for i in range(18):
        key_part = key[i % len(key):i % len(key) + 4].ljust(4, b'\x00')  # Pad key if needed
        P[i] ^= bytes_to_int(key_part)

    # S-boxes (4 S-boxes with 256 32-bit entries each)
    S = [[0] * 256 for _ in range(4)]
    for i in range(4):
        for j in range(256):
            key_part = key[i % len(key):i % len(key) + 4].ljust(4, b'\x00')  # Pad key if needed
            S[i][j] ^= bytes_to_int(key_part)

    return P, S

# usage:
key = b'SecretKey'
P, S = initialize_blowfish(key)

print(f'P-array: {P}')
print(f'S-boxes: {S}')
