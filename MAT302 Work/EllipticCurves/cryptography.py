import addition as add
import random as ran
# P = Public Point
# A = Public Verification Key
# D = Document
# s = (s1, s2) = Published Signture
# m = F_m
# c = a value of the curve


# This is all fucked lmfao

P = (5, 4296)
r = 12484
a = 1547
A = add.recursive_scalar_mult(a, P, 3, 12589)

def generate(P: tuple, D: int, a: int, r: int, c: int, m: int):
    k = ran.randint(1, r)
    s1 = add.recursive_scalar_mult(k, P, c, m)[0]%r
    s2 = (D + a*s1)*pow(k, -1, m)%r
    return (s1, s2)


def verify(P: tuple, A: tuple, D: int, s: tuple, r: int, m: int, c: int):
    s1, s2 = s[0], s[1]
    v1 = (D*pow(s2, -1, m))%r   
    v2 = (s1*pow(s2, -1, m))%r
    v1P = add.recursive_scalar_mult(v1, P, c, m)
    v2A = add.recursive_scalar_mult(v2, A, c, m)
    ver = add.add_points(v1P, v2A, c, m)
    s = ver[0]
    return s == s1%r

sigs = generate(P, 1022, a, r, 3, 12589)
print(verify(P, A, 1022, sigs, r, 12589, 3))

# print(verify((5, 4296), (4016, 6558), 1022, (11909, 2569), 12484, 12589, 3))