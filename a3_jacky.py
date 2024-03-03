import random
import math
# For the Jacky part of HW3. Elgamal Encryption stuff.

# Given in Assignment
P = 16977708269389697
G = 3

# Defining Alice and Bob's Keys
# Note: Bob's are placeholders for testing
alice_priv = 7777777
alice_pub = pow(G, alice_priv, P)
bob_priv = 22334455
bob_priv = pow(G, bob_priv, P)

# Creating Elgamal Encryption Scheme
# NOTE: Assignment has a help tool to convert our message to a number,
# so im assuming that we encrypt the whole number as one thing and as
# such im treating this as enrypting one number as the message

def encrypt_elgamal(m: int, A: int, b: int) -> tuple[int, int]:
    """Encrypt message <m> with with public key <A> and private key
    <b> using the Elgamal scheme into cypher text <c1> and <c2>"""
    c1 = pow(G, b, P)
    c2 = (m * pow(A, b, P)) % P
    return (c1, c2)


def decrypt_elgamal(c1: int, c2: int, a: int) -> int:
    """Decrypt cypher text <c1> and <c2> into plaintext using key <a>"""
    return (pow(c1, -a, P)*c2 % P)
    

def shanks_collision() -> int:
    """Given discrete log problem g^x = y log p, with g, y, and p known,
    solves for x with O(2^(k/2)k^2) bit complexity"""
    return


# This one I probably wont get to tbh, I think its beyond
# my skillset at the moment. However, I might return to
# it at a later time :)
def sph_method():
    return

message = 123456789
cypher1, cypher2 = encrypt_elgamal(message, alice_pub, bob_priv)
plain = decrypt_elgamal(cypher1, cypher2, alice_priv)
print(f"Message: {message} has been encrypted into Cyphertext ({cypher1}, {cypher2}). \n\
This has been decrypted into plaintext {plain}.")