from Block_Encryption import feistel_network
from Initialization import initialize_blowfish

def int_to_bytes(i):
    # Convert integer to bytes (big-endian)
    return bytes([(i >> (8 * j)) & 0xFF for j in range(3, -1, -1)])

def bytes_to_int(b):
    # Convert bytes to integer (big-endian)
    return sum((b[i] << (8 * i) for i in range(len(b))))

def decrypt_block(block, P, S):
    # Blowfish block decryption
    xl, xr = bytes_to_int(block[:4]), bytes_to_int(block[4:])

    for i in range(15, 0, -1):
        xl, xr = feistel_network(xl, xr, P, S)
        xl, xr = xl ^ P[i], xr

    xl, xr = xr, xl  # Swap the final two words

    xr = xr ^ P[0]
    xl = xl ^ P[1]

    return int_to_bytes(xl) + int_to_bytes(xr)

# usage:
key = b'Gilian'
P, S = initialize_blowfish(key)

# 'cipher_block' is the block you want to decrypt
cipher_block = b'\x1a\x2b\x3c\x4d\x5e\x6f\x70\x81'

decrypted_block = decrypt_block(cipher_block, P, S)
print("Decrypted Block:", decrypted_block.hex())