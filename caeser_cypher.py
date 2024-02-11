import numpy as np
# TODO: Potentially allow encryption of all ascii characters?

def encryptCaeser(p: str, b: int):
    c = ""
    for char in p:
        ascii = ord(char) - 65
        if ascii == -33:
            c += ""
        else:
            c += chr(np.mod(ascii + b, 26) + 65)
    return c


def decryptCaser(c: str, b: int):
    return encryptCaeser(c, -b)


def decryptCaserBrute(c: str):
    possibilities = {}
    for b in range(0, 26):
        ptext = decryptCaser(c, b)
        possibilities[b] = ptext
        print(f"Decryption Possibility: {ptext} with key {b}")
    return possibilities

ptext = "TEST"
ctext = encryptCaeser(ptext, 15)
print(decryptCaser(ctext, 15))
decryptCaserBrute(ctext)