import Utility_Files.discretelog as dlp

# %-%-%-%-%-%-%-%-% IMPORTANT %-%-%-%-%-%-%-%-%-%
# THIS SCRIPT IS PURELY FOR EDUCATIONAL PURPOSES. DO NOT USE FOR ANYTHING THAT
# REQUIRES ACTUAL SECURITY, THE PRIME NUMBER USED HERE IS TOO SMALL AND CAN BE
# EASILY CRACKED WITH THE GIVEN ALGORITHMS ON A LAPTOP.

# CONSTANTS GIVEN BY JACKY
PRIME = 16977708269389697
GENERATOR = 3


# NOTE: Elgamal encryption can use any large prime and generator in Z*p.
# In this case I was given <PRIME> and <GENERATOR>, however if you want
# to use different ones, you can modify either the static ints at the 
# start or alter the functions to enable you to chose your prime and gen.
# Remember: you must use the same prime and gen for encryption and decryption
# or that is to say, when chosing keys they must be the same
def encrypt_elgamal(m: int, A: int, b: int) -> tuple[int, int]:
    """Encrypts plaintext to cypher text using an Elgamal Scheme given:
    plaintext message <m>, public key <A>, private key <b>"""
    c1 = pow(GENERATOR, b, PRIME)
    c2 = (m * pow(A, b, PRIME)) % PRIME
    return (c1, c2)


def decrypt_elgamal(c1: int, c2: int, a: int) -> int:
    """Decrypt cyphertext encrypted with an Elgamal Scheme given:
    cyphertext1 <c1>, cyphertext2 <c2>, private key <a>"""
    return (pow(c1, -a, PRIME)*c2 % PRIME)

# TODO Add brute force using DLP
    

# BRAINSTORMING DONE FOR THIS #TODO: Move to txt file
# Starts similar to DHKE
# Trusted 3rd party picks p and g
# Alice will pick some 1 <= a <= p-1, publish A = g^a mod p
# Encryption: 
# - Bob picks k in Z and plaintext m. He then computes: 
#   (c1 = g^k mod p, c2 = mA^k mod p)
# - Bob sends (c1, c2) to Alice
# Decryption:
# - Alice computes [(c1^a)^(-1)]*c2 mod p

# As Charlie, how do you go about cracking it?
# We know A, p, g, c1, c2; We want to find a, k
# If |g| is small, we can brute force
# Solution: Shank's Baby-Step Giant-Step Algorithm
#   - Use to crack a then apply to decrypt like Alice