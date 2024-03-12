# See algorithm in rho_algorithm.txt (math behind it can
# found online, might add it to that txt file)

# |------ Rho Factorization -------|
# Uses Pollard's Rho Method of factorization for finding
# one factor of a composite number
# NOTE: If you want to drop the assumption of compositeness,
# you can add a primality test by importing primality_test.py
from math import gcd


def func(x: int, n: int) -> int:
    return (pow(x, 2) + x + 1) % n

# I think this works?
def rho_factorization(x_naught: int, n: int) -> int:
    dict = {0: x_naught}
    for i in range(1, n):
        dict[i] = func(dict[i-1], n)
        for k in range(i):
            d = gcd(dict[i] - dict[k], n)
            if d > 1:
                return d

import primality_test as prime
q = prime.generate_prime(10000)
p = prime.generate_prime(10000)    
print(f"n = {p}*{q} found: {rho_factorization(6, p*q)}")
            
