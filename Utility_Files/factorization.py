# See algorithm in rho_algorithm.txt (math behind it can
# found online, might add it to that txt file)

# |------ Rho Factorization -------|
# Uses Pollard's Rho Method of factorization for finding
# one factor of a composite number
# NOTE: If you want to drop the assumption of compositeness,
# you can add a primality test by importing primality_test.py
import sys
sys.path.append(".")
import math
import Utility_Files.primality as prime
import time


def func(x: int, n: int) -> int:
    return (pow(x, 2) + x + 1) % n

# I think this works?
def rho_factorization(x_naught: int, n: int) -> int:
    """Factor a number of at least 2 factors using Pollard's Rho method"""
    start = time.time()
    dict = {0: x_naught}
    for i in range(1, n):
        dict[i] = func(dict[i-1], n)
        for k in range(i):
            d = math.gcd(dict[i] - dict[k], n)
            if d > 1:
                end = time.time()
                print(f"Rho factored d={d} in {end-start} seconds.")
                return d


# Need to find a way to check if something is an int or perfect square
def fermat_facorization(n: int) -> tuple[int,int]:
    """Factor a number made of at least 2 factors using fermats method.
    #TODO: Insert link to fermat algorithm info
    >>> fermat_factorization(200819)
    >>> (491, 409)"""
    start = time.time()
    rt_n = math.floor(math.sqrt(n))
    for i in range(1, n): # Placeholder until i can find how to check better
        t = rt_n + i
        if math.sqrt(t**2 - n) % 1 == 0:
            s = int(math.sqrt(t**2 - n))
            print(f"Factors found: i = {i}, (t, s) = ({t}, {s}), (a, b) = ({t + s}, {t-s})")
            end = time.time()
            print(f"Fermat factored in {end-start} seconds")
            return t + s, t - s 
            


a = prime.generate_prime(45293788759)
b = prime.generate_prime(45223979852)

fermat_facorization(228223876469)
# rho_factorization(124, 228223876469)

# rho_factorization(124, a*b)
# fermat_facorization(a*b)
