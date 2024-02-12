import numpy as np
import random as rand
TEST_COUNT = 128
# This file contains functions to:
#   Check primarity of a number (to an extremely high degree of certainty)
#   Generate probabalistic prime (to an extremely high degree of certainty)

# TODO: Make some improvements
SEED_100 = 5113736189842830779456493914130649529424217430403290429652251102390965369569659408838301037615573824 
SEED_150 = 162393509060232147910630780279628898760487714968995550562710528035511985764690527861312982060608533223600227976189762439238319450678007857869631362747 
SEED_200 = 93805862905091456503661333338161980394572880044377929312084677659240083085578548708780754762611931101238327641910425518571066357476148645734658981670472140665228616080403252058128605364490965311995267 


def pow_2_factor(n: int):
    k = 0
    while (n % 2 == 0):
        k += 1
        n //= 2
    return k, n

def primality_test(n: int):
    for i in range (1, TEST_COUNT):
        a_i = rand.randint(2, n-1)
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
    k = rand.randint(2, n-1)
    if k % 2 == 0:
        k += 1
    while not primality_test(k):
        k = rand.randint(2, n-1)
    return k

print(generate_prime(265748756348936589346583968945768934372652358295628973562389))