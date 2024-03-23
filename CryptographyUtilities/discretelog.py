import math
import time
import sympy
import CustomErrors as er

# NOTE: Shank's and SPH should be tested before deleting the commented out
# single use shanks

# NOTE: By adding default arg for gord i should be able to use just one
# shanks that works for SPH or by itself
def shanks(p:int, g: int, h:int, gord=0) -> int:
    """Shanks Collision Algorithm for use by itself or with SPH. If
    <gord> is not provided, it will default to p""" 
    if gord == 0: gord = p
    n = 1 + math.floor(math.sqrt(gord))
    sbaby = {}
    sgiant = {}
    for i in range(0, n):
        sbaby[pow(g, i, p)] = i
        sgiant[h*pow(g, -i*n, p)%p] = i
    for key in sbaby:
        if key in sgiant:
            return (sbaby[key] + sgiant[key]*n)%p
    raise er.NullSolution
    

def dlp_brute_force(p, g, h, orderg=0):
    """Brute force attack on DLP by trying all posibilities. NOTE: This
    is highly inefficient for large p as it has exponential bit complexity"""
    if orderg == 0: orderg = p
    for x in range(1, orderg):
        if pow(g, x, p) == h:
            return x
    raise er.NullSolution

# Implemented with Shank's. To use brute force comment out line 96
# and uncomment line 97
def sph_method(p: int, g: int, h: int):
    time_start = time.time()
    """Solves DLP (g^x = h mod p) using SPH given:
    prime <p>, generator <g>, integer <h>"""
    fta_fact = sympy.factorint(p-1)
    list_of_powers = []
    for key in fta_fact:
        list_of_powers.append(key**fta_fact[key])
    
    # Obtain mk's
    m_pows = []
    for power in list_of_powers:
        m_pows.append((p-1) // power)
    
    g_ks, h_ks = [], []
    for mpow in m_pows:
        g_ks.append(pow(g, mpow, p))      
        h_ks.append(pow(h, mpow, p))
    
    a_ks = []
    for i in range(len(m_pows)):
        print(f"Running DLP Subproblem {i}...")
        a_ks.append(shanks(p, g_ks[i], h_ks[i], list_of_powers[i]))
        # a_ks.append(dlp_brute_force(p, g_ks[i], h_ks[i], list_of_powers[i]))
    result = sympy.ntheory.modular.crt(list_of_powers, a_ks)
    time_end = time.time()
    print(f"DLP Cracked using the SPH Algorithm with Shank's Collision Algorithm\
    for DLP subproblems in {time_end - time_start} seconds.")
    return result[0]

dlp_brute_force(11, 3, 8)