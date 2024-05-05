# %-%-%-%-%-%-%-%-% IMPORTANT %-%-%-%-%-%-%-%-%-%
# THIS SCRIPT IS PURELY FOR EDUCATIONAL PURPOSES. DO NOT USE FOR ANYTHING THAT
# REQUIRES ACTUAL SECURITY, THE PRIME NUMBER USED HERE IS TOO SMALL AND CAN BE
# EASILY CRACKED WITH THE GIVEN ALGORITHMS ON A LAPTOP.

# CONSTANTS GIVEN BY JACKY
PRIME = 16977708269389697
GENERATOR = 3

def encrypt(m: int, A: int, b: int) -> tuple[int, int]:
    """Encrypts plaintext to cypher text using an Elgamal Scheme given:
    plaintext message <m>, public key <A>, private key <b>"""
    c1 = pow(GENERATOR, b, PRIME)
    c2 = (m * pow(A, b, PRIME)) % PRIME
    return (c1, c2)


def decrypt(c1: int, c2: int, a: int) -> int:
    """Decrypt cyphertext encrypted with an Elgamal Scheme given:
    cyphertext1 <c1>, cyphertext2 <c2>, private key <a>"""
    return (pow(c1, -a, PRIME)*c2 % PRIME)

# TODO Add brute force using DLP