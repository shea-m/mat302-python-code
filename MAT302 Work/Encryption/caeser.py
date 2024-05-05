import numpy as np
# TODO: Potentially allow encryption of all ascii characters?

def encrypt(p: str, b: int):
    """Encrypts plaintext into cyphertext using a Caeser Cypher given:
    plaintext <p>, key <b>"""
    c = ""
    for char in p:
        ascii = ord(char) - 65
        if ascii == -33:
            c += ""
        else:
            c += chr(np.mod(ascii + b, 26) + 65)
    return c


def decrypt(c: str, b: int):
    """Decrypts cyphertext to plaintext using a Caeser Cypher given:
    cyphertext <c>, key <b>"""
    return encrypt(c, -b)


def decrypt_brute(c: str):
    """Decrypts cyphertext encrypted with a Caser Cypher by brute force given:
    cyphertext <c>"""
    possibilities = {}
    for b in range(0, 26):
        ptext = decrypt(c, b)
        possibilities[b] = ptext
        print(f"Decryption Possibility: {ptext} with key {b}")
    return possibilities
