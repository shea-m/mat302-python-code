import sys
sys.path.append(".")
import CryptographyUtilities.primality as prime
import random as rand
import math

def generate_signature(seed=64) -> tuple[int, int, int]:
    """Generate A Signature"""
    p, q = prime.generate(seed), prime.generate(seed)
    n, phin = p*q, (p-1)*(q-1)
    e = rand.randint(1, phin)
    while math.gcd(e, phin) != 1:
        e = rand.randint(1, phin)
    d = pow(e, -1, phin)
    return (n, e, d)


def sign(D: int, da: int, n: int) -> tuple[int, int]:
    """Precondition: Assumes the inpute keys are valid"""
    return (D, pow(D, da, n))


def verify(D: int, s: int, ea: int, n: int) -> bool:
    "Verify authenticity of a document"
    return D == pow(s, ea, n)