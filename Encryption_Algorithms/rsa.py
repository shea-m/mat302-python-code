import sys
sys.path.append(".")
import Utility_Files.primality as prime
import random as rand
import math


# Maybe make a genernate key pairs:
# Takes input of size of prime factors
# Generates p,q --> finds n, phi(n)
# Find e, d
# Returns dict of keys?
def generate_coprime(n: int):
    while True:
        e = rand.randint(1, n)
        if math.gcd(e, n) == 1:
            return e

def generate_keys(p_seed: int, q_seed: int) -> tuple[dict, dict]:
    """p_seed and q_seed are seeds used for generating p and q"""
    dict_priv, dict_pub = {}, {}
    dict_priv["p"] = prime.generate_prime(p_seed)
    dict_priv["q"] = prime.generate_prime(q_seed)
    dict_priv["phi(n)"] = (dict_priv["p"]-1)*(dict_priv["q"]-1)
    dict_pub["n"] = (dict_priv["p"])*(dict_priv["q"])
    dict_pub["e"] = generate_coprime(dict_priv["phi(n)"])
    dict_pub["d"] = pow(dict_pub["e"], -1, dict_priv["phi(n)"])
    return (dict_priv, dict_pub)

def encrypt_rsa(m: int, e: int, n: int) -> int:
    return pow(m, e, n)


def decrypt_rsa(c: int, d: int, n: int):
    return pow(c, d, n)

        
print(generate_keys(98674394, 8953152))
