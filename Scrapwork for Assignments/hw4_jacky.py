import sys
sys.path.append(".")
import CryptographyUtilities.primality as prime
import CryptographyUtilities.factorization as factor
import Encryption.rsa as rsa
import random as rand
import math

# # Public Keys
# n = 10249631804059
# e = 4483382918951

# # Private Keys
# p = 32118727
# q = 319117
# d = 9851282373407
# phi_n = 10249599366216

# Check keys are valid
# print(f"p and q are prime? {prime.primality_test(p) and prime.primality_test(q)}")
# print(f"p*q=n? {p*q == n}")
# print(f"Correct phi(n)? {phi_n == (p-1)*(q-1)}")
# print(f"gcd(e, phi(n)) = 1? {math.gcd(phi_n, e) == 1}")
# print(f"d correctly generated? {pow(e, -1, phi_n) == d}")


# ALICE
# Public Keys
n = 10249631804059
e = 4483382918951
# Private Keys
p = 32118727
q = 319117
d = 9851282373407
phi_n = 10249599366216
# -- Received --
alice_ctext = 9100835821474
alice_ptext = rsa.decrypt(alice_ctext, d, n)
print(f"Alice: Received message {alice_ctext}. Decrypted as {alice_ptext}")

# BOB
# -- Received --
bob_n = 2454168055369
bob_e = 31909
# -- Sent -- 
ptext = "NVDA"
ptextnum = 23311310
ctext = rsa.encrypt(ptextnum, bob_e, bob_n)
print(f"Bob: Message {ptext} as numeric {ptextnum} encrypted to {ctext}")

# CHARLIE
# -- Intercepted --
charlie_n = 228223876469
charlie_e = 922627
charlie_ctext = 58905270707
# -- Cracked --
a = 745993
b = 305933

charlie_phin = (a-1)*(b-1)
charlie_d = pow(charlie_e, -1, charlie_phin)
charlie_ptext = rsa.decrypt(charlie_ctext, charlie_d, charlie_n)
print(f"Charlie: Message intercepted: {charlie_ctext}. Cracked public key... \
Message decrypted: {charlie_ptext}")

