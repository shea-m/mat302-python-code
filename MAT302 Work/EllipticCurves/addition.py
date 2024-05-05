# TODO: Update so that O is not (0,0)
# TODO: Make scalar_mult that is recursively defined (Dev will post code)
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
    

def double_point(p: tuple, curve: int, ord: int):
    return add_points(p, p, curve, ord)

    
def iterative_scalar_mult(a: int, P: tuple, curve: int, ord: int) -> tuple:
    p = P
    for i in range(2, a+1):
        p = add_points(p, P, curve, ord)
    return p


def recursive_scalar_mult(a: int, P: tuple, curve: int, ord: int) -> tuple:
    if a == 0:
        return (0,0)
    elif a == 1:
        return P
    else:
        pNew = double_point(P, curve, ord)
        pNew = recursive_scalar_mult(a//2, pNew, curve, ord)
        if a % 2 == 1:
            pNew = add_points(P, pNew, curve, ord)
        return pNew

def compute_order(P: tuple, curve: int, ord: int):
    p = P
    i = 2
    if P == (0,0):
     return 1
    while True:
        p = add_points(p, P, curve, ord)
        if p == (0,0):
            return i
        i += 1

# print(iterative_scalar_mult(6789, (5, 4296), 3, 12589))
# print(recursive_scalar_mult(6789, (5, 4296), 3, 12589))
    