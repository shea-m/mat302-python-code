import numpy as np
import random as rand
SEED_100 = 5113736189842830779456493914130649529424217430403290429652251102390965369569659408838301037615573824 
SEED_150 = 162393509060232147910630780279628898760487714968995550562710528035511985764690527861312982060608533223600227976189762439238319450678007857869631362747 
SEED_200 = 93805862905091456503661333338161980394572880044377929312084677659240083085578548708780754762611931101238327641910425518571066357476148645734658981670472140665228616080403252058128605364490965311995267 


def pow_2_factor(n: int):
    """Factors even integer n into form 2^k * n"""
    k = 0
    while (n % 2 == 0):
        k += 1
        n //= 2
    return k, n


# TODO: Change print to file output?
def test(n: int, wit_num=128, pBool=False):
    """Miller-Rabin probablistic primality test to determine if n is 
    probably prime using <wit_num> number of witnesses
    <wit_num>: Number of witnesses to check, default=128
    <pBool>: Whether to print info to console, default=False"""
    for i in range (1, wit_num+1):
        a_i = rand.randint(2, n-1)
        if pBool: print(f"Checking {a_i} (num {i})...")
        if np.gcd(n, a_i) != 1:
            if pBool: print(f"Failed gcd test with {a_i} as witness")
            return False
        elif pow(a_i, n-1, n) != 1:
            if pBool: print(f"Failed Fermat test with {a_i} as witness")
            return False
        if pBool: print(f"Passed fermat test, checking MR...")
        k, q = pow_2_factor(n-1)
        if pow(a_i, q, n) == 1:
            if pBool: print(f"Passed MR on pow = q. Checking next a_i\n")
            continue
        else:
            found = False
            for l in range(0, k):
                exp = ((2**l)*q)
                power = pow(a_i, exp, n)
                if power == (n-1):
                    if pBool: print(f"Passed MR on l = {l}: pow = {power}. Checking next a_i.\n")
                    found = True
                    break
            if found:
                continue
            else:
                if pBool: print(f"Failed MR critera with {a_i} as witness")
                return False
    return True

def generate(n: int):
    """Generates a probabalistic prime using Miller-Rabin with size bounded
    by n, 2n"""
    k = rand.randint(2, n-1)
    if k % 2 == 0:
        k += 1
    while not test(k):
        k = rand.randint(2, n-1)
    return k



set = [2340479967655351190021083, 2340479967655351240021083, 3252485846352620806586381, 3252485846352620806786381, 2408442571612536557073539, 2408442571664836557073539, 3511744070107906197282793, 3511744070107392097282793, 7266695084672381508723951]
for n in set:
    print (test(n))


