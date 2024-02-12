# Problem: Want to send a key over an unsecured channel for
# a symmetric cypher. How do we accomplish this?
# Solution:
# - (1) Pick large prime, (2) g in Fp*, |g| a large prime: both public
#    - Note: could find generator of Zp*, but that can be
#      computationally difficult
# - (3) Alice picks a, Bob picks b, both in Fp*
# - (4) Alice computes A = g^a mod p, Bob computes B = g^b mod p
# - (5) Alice sends A to Bob, and Bob B to Alice (both public)
# - (6) Secret key becomes A^b = B^a = g^ab mod p
# Secure because the discrete log problem is hard to solve

# To find g, find largest prime diving p-1, then find generator
# - Good guesses: 3, 5, 7, 11, 2
# Write p-1 as qk, then g = generator**k
