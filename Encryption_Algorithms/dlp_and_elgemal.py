import math
import sympy
import time

# %-%-%-%-%-%-%-%-% IMPORTANT %-%-%-%-%-%-%-%-%-%
# THIS SCRIPT IS PURELY FOR EDUCATIONAL PURPOSES. DO NOT USE FOR ANYTHING THAT
# REQUIRES ACTUAL SECURITY, THE PRIME NUMBER USED HERE IS TOO SMALL AND CAN BE
# EASILY CRACKED WITH THE GIVEN ALGORITHMS ON A LAPTOP.

# CONSTANTS GIVEN BY JACKY
PRIME = 16977708269389697
GENERATOR = 3


# NOTE: Elgamal encryption can use any large prime and generator in Z*p.
# In this case I was given <PRIME> and <GENERATOR>, however if you want
# to use different ones, you can modify either the static ints at the 
# start or alter the functions to enable you to chose your prime and gen.
# Remember: you must use the same prime and gen for encryption and decryption
# or that is to say, when chosing keys they must be the same
def encrypt_elgamal(m: int, A: int, b: int) -> tuple[int, int]:
    """Encrypts plaintext to cypher text using an Elgamal Scheme given:
    plaintext message <m>, public key <A>, private key <b>"""
    c1 = pow(GENERATOR, b, PRIME)
    c2 = (m * pow(A, b, PRIME)) % PRIME
    return (c1, c2)


def decrypt_elgamal(c1: int, c2: int, a: int) -> int:
    """Decrypt cyphertext encrypted with an Elgamal Scheme given:
    cyphertext1 <c1>, cyphertext2 <c2>, private key <a>"""
    return (pow(c1, -a, PRIME)*c2 % PRIME)
    
    
# |---------- Cracking the DLP ---------|

# The shanks can be done in a simpler way:
# Instead of having to calculate all of the sgiants then comparing, we can
# find the first one, and then check, raise it to the power of p, then check
# again. This should save some loops
# I'll update this if I have extra time, however this worked (in my attempt
# for Charlie, I was able to find it in ~3.5 Minutes)

# Shank's Collision algorithm for a direct attack on the DLP
def shanks_collision_dlp(p:int, g:int, h:int) -> int:
    n = 1 + math.floor(math.sqrt(p))
    sbaby = {}
    sgiant = {}
    for i in range(0, n):
        sbaby[pow(g, i, p)] = i
        sgiant[h*pow(g, -i*n, p)%p] = i
    for key in sbaby:
        if key in sgiant:
            return (sbaby[key] + sgiant[key]*n)%p


# Shank's Collision algorithm for use in the SPH algorithm
def shanks_collision_sph(p:int, g: int, h:int, gord: int) -> int: 
    n = 1 + math.floor(math.sqrt(gord))
    sbaby = {}
    sgiant = {}
    for i in range(0, n):
        sbaby[pow(g, i, p)] = i
        sgiant[h*pow(g, -i*n, p)%p] = i
    for key in sbaby:
        if key in sgiant:
            return (sbaby[key] + sgiant[key]*n)%p


# NOTE: Avoid using this. Shank's is much better for large numbers,
# however brute force might be fine for small numbers.
def dlp_brute_force(p, g, h, orderg):
    """Brute force way to solve DLP. NOTE: This is not efficient,
    only for use in solving smaller DLP's that arise from SPH"""
    for x in range(1, orderg):
        if pow(g, x, p) == h:
            return x
    return None

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
        a_ks.append(shanks_collision_sph(p, g_ks[i], h_ks[i], list_of_powers[i]))
        # a_ks.append(dlp_brute_force(p, g_ks[i], h_ks[i], list_of_powers[i]))
    result = sympy.ntheory.modular.crt(list_of_powers, a_ks)
    time_end = time.time()
    print(f"DLP Cracked using the SPH Algorithm with Shank's Collision Algorithm\
    for DLP subproblems in {time_end - time_start} seconds.")
    return result[0]
