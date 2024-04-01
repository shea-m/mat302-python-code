# Given P=(x_p, y_p), Q=(x_q, y_q) and s = (x_p - x_q)/(y_p - y_q) and F_(p^k)
# P + Q = R
# x_r = s^2 - x_p - x_q mod p^k | y_r = -y_p + s(x_p - x_r) mod p^k
# P + P:
# s = (3(x_p)^2+ a)/(2y_p) mod p^k

# Need to pick a & b such that non singular
# Want eliptic curve y^2 = x^3 + ax + b represented as (a,b)
# Points as (x_i, y_i)
import sys
sys.path.append(".")
import CryptographyUtilities.CustomErrors as er

def exist_on_curve(curve: tuple[int, int], p: tuple[int, int]) -> bool:
    # Check if p[1]^2 = p[0]^3 + curve[1]*p[0] + curve[2]
    # first check if curve[1] is a perfect square
    # then check if curve[0] can be put in the curve and output
    pass

def check_singular(curve: tuple[int, int], m: int)->bool:
    """<m> = order of the field"""
    return not (4*pow(curve[0], 3) + 27*pow(curve[1], 2))%m == 0

def compute_s(p: tuple[int, int], q: tuple[int,int], a: int, m: int) -> int:
    """ Find s for addition of points one elliptic curve
    <p> = point P=(x1,y1)
    <q> = point Q=(x2,y2)
    <a> = coeffecient a in y^2=x^3+ax+b
    <m> = m from F_m
    """
    x1, y1 = p[0], p[1]
    if p == q:
        return ((3*pow(x1, 2, m) + a) * pow(2*y1, -1, m))%m
    else:
        x2, y2 = q[0], q[1]
        return ((y2 - y1) * pow((x2-x1), -1, m))%m

# Given a curve y^2 = x^3 + ax + b, point P=(x1,y1), point Q(x1,y1)
# and the curve is on some field F_m
# Denote O as (0,0)
def add_points(p: tuple[int, int], q: tuple[int,int], a: int, m: int)->tuple[int,int]:
    if p[0] == q[0] and p != q: # If x1 = x2, return O
        return (0,0)
    elif p == (0,0): # If P = O, return Q
        return q
    elif q == (0,0): # If Q = O, return P
        return p
    else: # If x1 != x2 and Q != O != P
        s = compute_s(p, q, a, m)
        x1, x2, y1, y2 = p[0], q[0], p[1], q[1]
        x3 = (pow(s, 2, m) - x1 - x2)%m
        y3 = (s*(x1-x3)-y1)%m
        return (x3,y3)



# print(add_points((2,3), (2,3), 3, 13)) # should be (12,11)
    