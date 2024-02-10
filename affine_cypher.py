import numpy as np

AFFINE_ORDERS = [1, 2, 3, 4, 6, 12]


def encrypt2decrypt(a: int, b: int):
    for i in AFFINE_ORDERS:
        if pow(a, i, 26) == 1:
            return pow(a, i-1, 26), b


def encryptAffine(p: str, a: int, b: int):
    c = ""
    for char in p:
        numval = ord(char) - 65
        if numval == -33:
            c += " "
            continue
        new_pos = np.mod(a*numval + b, 26)
        c += chr(new_pos + 65)
    return c


def decryptAffine(c: str, a: int, b: int):
    p = ""
    a, b = encrypt2decrypt(a, b)
    for char in c:
        numval = ord(char) - 65
        if numval == -33:
            p += " "
            continue
        new_pos = np.mod((numval - b)*a, 26)
        p += chr(new_pos + 65)
    return p


def decryptAffineBrute(c: str):
    p = ""
    potentials = []
    U26 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    for b in range(0, 25):
        for a in U26:
            aprime, bprime = encrypt2decrypt(a, b)
            for char in c:
                numval = ord(char) - 65
                if numval == -33:
                    p += " "
                    continue
                new_pos = np.mod((numval - bprime)*aprime, 26)
                p += chr(new_pos + 65)
            potentials.append(p)
            p = ""
    return potentials
