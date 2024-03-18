import sys
sys.path.append(".")
import Utility_Files.primality as prime
import random as rand
import math

# Public Keys
n = 10249631804059
e = 4483382918951

# Private Keys
p = 32118727
q = 319117
d = 9851282373407
phi_n = 10249599366216

# Check keys are valid
print(f"p and q are prime? {prime.primality_test(p) and prime.primality_test(q)}")
print(f"p*q=n? {p*q == n}")
print(f"Correct phi(n)? {phi_n == (p-1)*(q-1)}")
print(f"gcd(e, phi(n)) = 1? {math.gcd(phi_n, e) == 1}")
print(f"d correctly generated? {pow(e, -1, phi_n) == d}")