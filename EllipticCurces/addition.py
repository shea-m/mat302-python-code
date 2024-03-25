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
    if p == q:
        return ((3*pow(p[0], 2, m)+a)*pow(2*p[1], -1, m))%m
    else:
        return ((p[1]-q[1])/pow(p[0]-q[0], -1, m))%m

def add_points(p: tuple[int, int], q: tuple[int,int], curve: tuple[int,int], m: int)->tuple[int,int]:
    """Adds points <p> and <q> on an elliptic curve <curve> over a field of order <m>"""
    # Add case for on vertical line
    if not check_singular(curve):
        raise er.NonSingular
    if not (exist_on_curve(curve, p) and exist_on_curve(curve,q)):
        raise er.OffCurve
    s = compute_s(p, q, curve[0], m)
    x_r = (s - p[0] - q[0]) % m
    y_r = (-p[1] + s*(p[0]-x_r)) % m
    return (x_r, y_r)
    