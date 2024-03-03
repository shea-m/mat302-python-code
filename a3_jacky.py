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
    """Encrypts plaintext to cypher text using an Elgamal Scheme given:
    plaintext message <m>, public key <A>, private key <b>"""
    c1 = pow(G, b, P)
    c2 = (m * pow(A, b, P)) % P
    return (c1, c2)


def decrypt_elgamal(c1: int, c2: int, a: int) -> int:
    """Decrypt cyphertext encrypted with an Elgamal Scheme given:
    cyphertext1 <c1>, cyphertext2 <c2>, private key <a>"""
    return (pow(c1, -a, P)*c2 % P)
    

def shanks_collision() -> int:
    """Given discrete log problem g^x = y log p with known: 
    prime <p>, generator <g>, integer <y>,
    Solves for x with bit complexity O(2^(k/2)k^2)"""
    return


# This one I probably wont get to tbh, I think its beyond my skillset at the 
# moment. However, I might return to it at a later time :)
def sph_method():
    return

message = 123456789
cypher1, cypher2 = encrypt_elgamal(message, alice_pub, bob_priv)
plain = decrypt_elgamal(cypher1, cypher2, alice_priv)
print(f"Message: {message} has been encrypted into Cyphertext ({cypher1},\
{cypher2}). \n This has been decrypted into plaintext {plain}.")