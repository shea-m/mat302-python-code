import numpy as np
import random
import math


# ---------- PRIMALITY ----------
# TODO: Stress test primality test


def base2factor(n: int, k=0) -> tuple[int, int]:
    """Factors integer <n> into form 2^k * q for some ints k, q
    NOTE: k should never be manually set, leave as default
    PREREQUISITE: n % 2 == 0"""
    while n % 2 == 0:
        k += 1
        n //= 2
    return k, n


def primality_test(n: int, witcount=128) -> bool:
    """Determines primality of <num> using a Miller-Rabing probabalistic
    test with  <witcount> witnesses. Default 128 witnesses"""
    for witness in range(witcount):
        currwitness = random.randint(2, n-1)
        if np.gcd(n, currwitness) != 1: # GCD Check
            return False
        elif pow(currwitness, n-1, n) != 1: # Fermat Test
            return False 
        k, q = base2factor(n-1)
        if pow(currwitness, q, n) == 1:
            continue
        else: # M-R Criteria
            flag = False
            for p in range(0, k):
                exp = (2**p)*q
                result = pow(currwitness, exp, n)
                if result == (n-1):
                    flag = True
                    break
            if flag:
                continue
            return False
    return True 


def generate_prime(n: int) -> int:
    """Generates M-R Probablistic prime bounded by [n, 2n]"""
    k = random.randint(n, 2*n)
    if k % 2 == 0:
        k += 1
    while not primality_test(k):
        k = random.randint(n, 2*n)
    return k


# ---------- FACTORIZATION ----------
# TODO: Add function class to be used as input?

def dFunc(x: int, n: int) -> int:
    return ((pow(x, 2, n) + x + 1)) % n


def rho_factorization(x0: int, n: int) -> int:
    """Factorize a known composite <n> using Pollard's Rho Method with x0
    Currently using dFunc, future will include ability to chose function
    PRECONDITION: n is composite"""
    x_set = {0: x0}
    for i in range(1, n):
        x_set[i] = dFunc(dict[i-1], n)
        for k in range(i):
            if math.gcd(dict[i] - dict[k]. n) > 1:
                return math.gcd(dict[i] - dict[k]. n)


def rho_factorization_adjusted():
    pass


def fermat_factorization():
    pass

