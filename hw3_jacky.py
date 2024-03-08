import dlp_and_elgemal as dlp

# Just a little script that has all the information I receied from Jacky
# and all of my solutions. There is nothing of real value here unless you
# want to look through and see how stuff might be used.

# |---------- ALICE ----------|
# SENT
alice_priv = 7777777
alice_pub = pow(dlp.GENERATOR, alice_priv, dlp.PRIME)
# RECEIVED
c1_received = 243
c2_received = 6648230620510680
# DECRYPTED
m_decrypted = dlp.decrypt_elgamal(c1_received, c2_received, alice_priv)

# |---------- BOB ---------|
# RECEIVED
a_priv_sph = 16 # Found from previous crack
a_pub = 43046721
# SENT
bob_priv = 4577
message_text = "MCLAREN"
message_numeric = 22122110271423
c1, c2 = dlp.encrypt_elgamal(message_numeric, a_pub, alice_priv)

# |--------- CHARLIE ---------|
# INTERCEPTED
pub_intercept = 243
c1_intercept = 6586167870143629
c2_intercept = 12525101016277682
# INFO CRACKED
priv_cracked = 5 # Found previously with SPH
m_cracked = dlp.decrypt_elgamal(c1_intercept, c2_intercept, priv_cracked)
m_cracked_text = "KIA"

print(f'---------- Begin Mission ---------\n')
print(f'Mission Report: Alice')
print(f'Public key {alice_pub} sent.')
print(f'Cyphertext {c1_received, c2_received} received. Message \
decrypted to {m_decrypted}.\nText equivalent: SUBARU\n')
print(f'Mission Report: Bob')
print(f'Bob: Public key {a_pub} received.') 
print(f'{message_numeric} encrypted into ({c1, c2}) using key {bob_priv}.\n')
print(f'Mission Report: Charlie')
print(f'Intercepted: public key {243}, cyphertext: {c1_intercept, c2_intercept}')
print(f'Public key cracked using SPH. Private key: {priv_cracked}')
print(f'Message decrypted and found to be {m_cracked}.\nText equivalent: KIA\n')
print(f'Mission Complete. Terminating Log\n')
print(f'---------- End Mission ----------')


