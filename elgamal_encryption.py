# NOTE: This is just brainstorming. For actual encryption/decryption and 
# bruteforce solving methods, see a3_jacky.py

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

# We will assume g and p are given
import random as rand
import numpy as np
import primality_test as prime

G_GEN = 1 # PLACEHOLDER
P_PRIME = 1 # PLACEHOLDER

def elgamal_Alice(p=P_PRIME, g=G_GEN):
    a = rand.randint(1, p-1)
    return pow(g, a, p)

def elgamal_encrypt(A: int, m: str, p=P_PRIME, g=G_GEN):
    k = rand.randint(1, p-1)
    c1 = pow(g, k, p)
    # Convert m to nums first
    # for char in m multiply by A^k
    # convert back to str, return c1 c2?