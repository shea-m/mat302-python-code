import numpy as np
import random
# This file contains functions to:
#   Check primarity of a number (to an extremely high degree of certainty)
#   Generate pseudoprime (to an extremely high degree of certainty)

# TODO: Make some improvements

def pow_2_factor(n: int):
    k = 0
    while (n % 2 == 0):
        k += 1
        n //= 2
    return k, n

def primality_test(n: int):
    for i in range (1, 64):
        a_i = random.randint(2, n-1)
        if np.gcd(n, a_i) != 1:
            return False
        elif pow(a_i, n-1, n) != 1:
            return False
        k, q = pow_2_factor(n-1)
        if pow(a_i, q, n) == 1:
            continue
        else:
            found = False
            for l in range(0, k):
                exp = ((2**l)*q)
                if pow(a_i, exp, n) == (n-1):
                    found = True
                    break
            if found:
                continue
            else:
                return False
    return True

def generate_prime(n: int):
    k = random.randint(2, n-1)
    if k % 2 == 0:
        k += 1
    while not primality_test(k):
        k = random.randint(2, n-1)
    return k
