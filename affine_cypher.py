import numpy as np

# TODO: Allow for encryption of all asci characters?
# TODO: Write output to a text file?

AFFINE_ORDERS = [1, 2, 3, 4, 6, 12]
ZSTAR26 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

def key_swap(a: int, b: int):
    for i in AFFINE_ORDERS:
        if pow(a, i, 26) == 1:
            a_inv = pow(a, i-1, 26)
            return a_inv, -b*a_inv % 26


def encryptAffine(p: str, a: int, b: int):
    c = ""
    for char in p:
        ascii = ord(char) - 65
        if ascii == -33:
            c += " "
            continue
        new_pos = np.mod(a*ascii + b, 26)
        c += chr(new_pos + 65)
    return c

def decryptAffine(c: str, a: int, b:int):
    a_d, b_d = key_swap(a,b)
    return encryptAffine(c, a_d, b_d)


def decryptAffineBrute(c: str):
    possibilities = {}
    for b in range(0, 25):
        for a in ZSTAR26:
            ptext = decryptAffine(c, a, b)
            possibilities[(a,b)] = ptext
            # print(f"Decryption Possibility: {ptext} with key pair ({a}, {b})")
    return possibilities

ctext = encryptAffine("TEST", 11, 23)
print(decryptAffineBrute(ctext))