from Block_Encryption import feistel_network
from Initialization import initialize_blowfish

def calibrate_blowfish(P, S):
    # Blowfish calibration function
    zero_block = b'\x00\x00\x00\x00\x00\x00\x00\x00'

    for i in range(0, len(P), 2):
        xl, xr = int.from_bytes(zero_block[:4], 'big'), int.from_bytes(zero_block[4:], 'big')
        xl, xr = feistel_network(xl, xr, P, S)
        P[i], P[i + 1] = xl, xr

    for i in range(4):
        for j in range(0, 256, 2):
            xl, xr = int.from_bytes(zero_block[:4], 'big'), int.from_bytes(zero_block[4:], 'big')
            xl, xr = feistel_network(xl, xr, P, S)
            S[i][j], S[i][j + 1] = xl, xr

# usage:
key = b'Gilian'  
P, S = initialize_blowfish(key)

calibrate_blowfish(P, S)

print("Calibrated P-array:", P)
print("Calibrated S-boxes:", S)
