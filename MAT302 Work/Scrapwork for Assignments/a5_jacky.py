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
r = ec.compute_order(P, 3, ord)
print(r)

# -- My Stuff --
D = 229
a = 1337
V = ec.recursive_scalar_mult(a, P, curve[0], ord)

# TODO: Shift to EC Cryptography
# TODO: Fix this so it follows the algorithm in Qun's notes
def compute_signature(a: int, D: int, P: tuple, r: int, curve: int):
    """ placehold
    <a> - Alice private key
    <D> - document
    <r> - order of field F_r
    <curve> - coefficient a of the curve
    Returns Tuple (s1, s2) of signature"""
    k = rand.randint(1, r) # TODO: r needs to be the order of point P, so compute that order then generate the K
    s1 = ec.recursive_scalar_mult(k, P, curve, r)[0]
    s2 = (D + a*s1)*pow(k, -1, r)%r 
    return (s1, s2)


# Need to compute order of point P first

def verify_signature(D: int, P: tuple, A: tuple, s: tuple, m: int, curve: int) -> bool:
    """<D> = document
       <s> = (s1, s2) = verification key
       <r> = order of point P
       <m> F_m
       <P> public point
       <A> verification key?
       pi(x,y) --> x"""
    r = ec.compute_order(P, curve, m) -1
    s1, s2 = s[0], s[1]
    v1 = D*pow(s2, -1, m)%r
    v2 = s1*pow(s2, -1, m)%r
    v1P = ec.recursive_scalar_mult(v1, P, curve, m)
    v2A = ec.recursive_scalar_mult(v2, A, curve, m)
    ver = ec.add_points(v1P, v2A, curve, m)
    return ver[0]%r == s1
    # Inpute needed: D = Document, P = public point, A = Verification Key, s = signature tuple
    # m = order of Field (for computing r), curve = a value of curve

    # Find r = ord point A = V
    # compute v1 = Ds2^-1 mod r
    # compute v2 = s1s2^-1 mod r
    # compute x val of (v1P + v2A) mod r = s1
    # Note in this case A = V, Quns verification key
    

