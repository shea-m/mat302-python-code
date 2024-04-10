import sys
sys.path.append(".")
import EllipticCurves.addition as ec
import CryptographyUtilities.primality as prime
import random as rand

# -- Given --
curve = (3, 2)
ord = 12589
P = (5,4296)
V = (4016, 6558) # Qun Ver Key
s1 = 4016 # Qun ver x
s2 = 6558 # Qun ver y

# -- My Stuff --
D = 229
a = 1337
V = ec.recursive_scalar_mult(a, P, curve[0], ord)
Vcheck = ec.iterative_scalar_mult(a, P, curve[0], ord)
print(f"Recursive and Iterative are the same: {V == Vcheck}")
print(V)


# TODO: Shift to EC Cryptography
def compute_signature(a: int, D: int, P: tuple, r: int, curve: int):
    """ placehold
    <a> - Alice private key
    <D> - document
    <r> - order of field F_r
    <curve> - coefficient a of the curve"""
    k = rand.randint(1, r)
    s1 = ec.recursive_scalar_mult(k, P, curve, r)[0]
    s2 = (D + a*s1)*pow(k, -1, r)%r 
    return (s1, s2)


def verify_signature(D: int, s: tuple[int,int]) -> bool:
    pass
    """<D> = document
       <s> = (s1, s2) = verification key
       pi(x,y) --> x"""
    # v1 = Ds2^{-1} mod r
    # v2 = s1s2^{-1} mod r

print(compute_signature(a, D, P, ord, curve[0]))