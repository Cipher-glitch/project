from Initialization import initialize_blowfish

def feistel_network(xl, xr, P, S):
    # Feistel network function
    for i in range(16):
        xl = xl ^ P[i]
        xr = F(xl, S) ^ xr
        xl, xr = xr, xl

    xl, xr = xr, xl
    xr = xr ^ P[16]
    xl = xl ^ P[17]

    return xl, xr

def F(x, S):
    # F function used in the Feistel network
    a = x >> 24
    b = (x >> 16) & 0xFF
    c = (x >> 8) & 0xFF
    d = x & 0xFF

    y = (S[0][a] + S[1][b]) % (2**32)
    y = y ^ S[2][c]
    y = (y + S[3][d]) % (2**32)

    return y

def block_encrypt(block, P, S):
    # Blowfish block encryption
    xl, xr = block[0], block[1]

    xl, xr = feistel_network(xl, xr, P, S)

    encrypted_block = (xl, xr)
    return encrypted_block

# usage:
sample_key = b'SampleKey'
P, S = initialize_blowfish(sample_key)

plaintext_block = (0x12345678, 0)  
encrypted_block = block_encrypt(plaintext_block, P, S)

print("Plaintext Block:", plaintext_block)
print("Encrypted Block:", encrypted_block)
