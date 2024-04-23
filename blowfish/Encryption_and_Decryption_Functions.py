def feistel_network(xl, xr, P, S):
    # Blowfish Feistel network
    for i in range(16):
        xl = xl ^ P[i]
        xr = F(xl, S) ^ xr
        xl, xr = xr, xl

    xl, xr = xr, xl  # Swap the halves back at the end
    xr = xr ^ P[16]
    xl = xl ^ P[17]

    return xl, xr

def F(x, S):
    # Blowfish F function
    a, b, c, d = (x >> 24) & 0xFF, (x >> 16) & 0xFF, (x >> 8) & 0xFF, x & 0xFF

    y = (S[0][a] + S[1][b]) % 2**32
    y = y ^ S[2][c]
    y = (y + S[3][d]) % 2**32

    return y

def int_to_bytes(i):
    # Convert integer to bytes (little-endian)
    return bytes([(i >> (8 * j)) & 0xFF for j in range(4)])

def bytes_to_int(b):
    # Convert bytes to integer (little-endian)
    return sum((b[i] << (8 * i) for i in range(len(b))))

def encrypt_block(block, P, S):
    # Blowfish block encryption
    xl, xr = bytes_to_int(block[:4]), bytes_to_int(block[4:])
    xl, xr = feistel_network(xl, xr, P, S)
    return int_to_bytes(xl) + int_to_bytes(xr)

def decrypt_block(block, P, S):
    # Blowfish block decryption
    xl, xr = bytes_to_int(block[:4]), bytes_to_int(block[4:])
    xl, xr = feistel_network(xl, xr, P, S)
    return int_to_bytes(xl) + int_to_bytes(xr)

# Example usage:
key = b'Gilian' 
plaintext_block = b'12345678' 

# Initialize and calibrate Blowfish 
P = [0] * 18
S = [[0] * 256 for _ in range(4)]

ciphertext_block = encrypt_block(plaintext_block, P, S)
decrypted_block = decrypt_block(ciphertext_block, P, S)

print("Plaintext block:", plaintext_block)
print("Ciphertext block:", ciphertext_block)
print("Decrypted block:", decrypted_block)
