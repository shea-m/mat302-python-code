import numpy as np
# TODO: Potentially allow encryption of all ascii characters?

def encrypt_caeser(p: str, b: int):
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


def decrypt_caeser(c: str, b: int):
    """Decrypts cyphertext to plaintext using a Caeser Cypher given:
    cyphertext <c>, key <b>"""
    return encrypt_caeser(c, -b)


def decrypt_caeser_brute(c: str):
    """Decrypts cyphertext encrypted with a Caser Cypher by brute force given:
    cyphertext <c>"""
    possibilities = {}
    for b in range(0, 26):
        ptext = decrypt_caeser(c, b)
        possibilities[b] = ptext
        print(f"Decryption Possibility: {ptext} with key {b}")
    return possibilities

ptext = "TEST"
ctext = encrypt_caeser(ptext, 15)
print(decrypt_caeser(ctext, 15))
decrypt_caeser_brute(ctext)