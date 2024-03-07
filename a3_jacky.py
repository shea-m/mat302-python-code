import math
import sympy
import time

# %-%-%-%-%-%-%-%-% IMPORTANT %-%-%-%-%-%-%-%-%-%
# THIS SCRIPT IS PURELY FOR EDUCATIONAL PURPOSES. DO NOT USE FOR ANYTHING THAT
# REQUIRES ACTUAL SECURITY, THE PRIME NUMBER USED HERE IS TOO SMALL AND CAN BE
# EASILY CRACKED WITH THE GIVEN ALGORITHMS ON A LAPTOP.

# For the Jacky part of HW3. Elgamal Encryption stuff.
# TODO: Make the algorithms separate from the HW stuff.
# Make separate HW file then import the algorithms.

# CONSTANTS GIVEN BY JACKY
PRIME = 16977708269389697
GENERATOR = 3

# Creating Elgamal Encryption Scheme
# NOTE: Assignment has a help tool to convert our message to a number,
# so im assuming that we encrypt the whole number as one thing and as
# such im treating this as enrypting one number as the message

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

# This works for just using shanks. Next will adapt it for SPH
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


# This is taking longer????? EDIT: Seems like i just had a lucky guess so it was
# slower. With problem from Jacky its faster.
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


def dlp_brute_force(p, g, h, orderg):
    """Brute force way to solve DLP. NOTE: This is not efficient,
    only for use in solving smaller DLP's that arise from SPH"""
    for x in range(1, orderg):
        if pow(g, x, p) == h:
            return x
    return None

# Implemented using Shank's Collision algorithm. To use brute force, comment out
# line 98 and uncomment line 9.
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


# |--------- Parts for Jacky ---------|

# My Keys and Info
alice_priv = 7777777
alice_pub = pow(GENERATOR, alice_priv, PRIME)
bob_priv = 4577
message_text = "MCLAREN"
message_numeric = 22122110271423
# Found from previous crack
a_priv_sph = 7954955227814072

# Keys and Info received from Jacky
a_pub = 16
# a_priv = sph_method(PRIME, GENERATOR, a_pub)
a_pub_check = pow(GENERATOR, a_priv_sph, PRIME)
print(f"Alice's private key found to be {a_priv_sph} using SPH Cracking. Check \
Equivalancy: Given pub {a_pub} == g^(Found priv:{a_priv_sph}) mod p? \
{a_pub == a_pub_check}\n")

cypher1, cypher2 = encrypt_elgamal(message_numeric, a_pub, bob_priv)
plaintext_decrypted = decrypt_elgamal(cypher1, cypher2, a_priv_sph)
print(f'''Message {message_numeric} encrypted into ({cypher1}, {cypher2}). \
Cyphertext decrypted into {plaintext_decrypted}.''')

# |---------- Testing ---------- |

# print(shanks_collision_dlp(41, 6, 15))

# print(alice_priv, alice_pub)

# print(sph_method(16977708269389697, 3, pow(3, 295656438765387, P)))

# print(pow(3, 7777777, 16977708269389697))

# message = 123456789
# cypher1, cypher2 = encrypt_elgamal(message, alice_pub, bob_priv)
# plain = decrypt_elgamal(cypher1, cypher2, alice_priv)
# print(f"Message: {message} has been encrypted into Cyphertext ({cypher1},\
# {cypher2}). \n This has been decrypted into plaintext {plain}.")