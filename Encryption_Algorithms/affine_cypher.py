import numpy as np

# TODO: Allow for encryption of all asci characters?
# TODO: Write output to a text file?

AFFINE_ORDERS = [1, 2, 3, 4, 6, 12]
ZSTAR26 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

def key_swap(a: int, b: int) -> int:
    """Swaps encryption keys to decryption keys for an Affine Cypher given:
    key1 <a>, key2 <b>"""
    for i in AFFINE_ORDERS:
        if pow(a, i, 26) == 1:
            a_inv = pow(a, i-1, 26)
            return a_inv, -b*a_inv % 26


def encrypt_affine(p: str, a: int, b: int) -> int:
    """Encrypts plaintext into cyphertext using an Affine Cypher given:
    plaintext <p>, key1 <a>, key2 <b>"""
    c = ""
    for char in p:
        ascii = ord(char) - 65
        if ascii == -33:
            c += " "
            continue
        new_pos = np.mod(a*ascii + b, 26)
        c += chr(new_pos + 65)
    return c

def decrypt_affine(c: str, a: int, b:int) -> int:
    """Decrypts cyphertext encrypted with an Affine Cypher to plaintext given:
    cyphertext <c>, encryption key1 <a>, encryption key2 <b>"""
    a_d, b_d = key_swap(a,b)
    return encrypt_affine(c, a_d, b_d)


def decrypt_affine_brute(c: str) -> {int, int}:
    """Decrypts cyphertext encrypted with an Affine Cypher using brute force
    given: cyphertext <c>"""
    possibilities = {}
    for b in range(0, 25):
        for a in ZSTAR26:
            ptext = decrypt_affine(c, a, b)
            possibilities[(a,b)] = ptext
            # print(f"Decryption Possibility: {ptext} with key pair ({a}, {b})")
    return possibilities

ctext = encrypt_affine("TEST", 11, 23)
print(decrypt_affine_brute(ctext))