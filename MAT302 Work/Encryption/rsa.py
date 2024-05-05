import sys
sys.path.append(".")
import CryptographyUtilities.primality as prime
import random as rand
import math

def generate_coprime(n: int):
    while True:
        e = rand.randint(1, n)
        if math.gcd(e, n) == 1:
            return e

def generate_keys(p_seed: int, q_seed: int) -> tuple[dict, dict]:
    """p_seed and q_seed are seeds used for generating p and q"""
    dict_priv, dict_pub = {}, {}
    dict_priv["p"] = prime.generate(p_seed)
    dict_priv["q"] = prime.generate(q_seed)
    dict_priv["phi(n)"] = (dict_priv["p"]-1)*(dict_priv["q"]-1)
    dict_pub["n"] = (dict_priv["p"])*(dict_priv["q"])
    dict_pub["e"] = generate_coprime(dict_priv["phi(n)"])
    dict_pub["d"] = pow(dict_pub["e"], -1, dict_priv["phi(n)"])
    return (dict_priv, dict_pub)

def encrypt(m: int, e: int, n: int) -> int:
    return pow(m, e, n)


def decrypt(c: int, d: int, n: int):
    return pow(c, d, n)

        