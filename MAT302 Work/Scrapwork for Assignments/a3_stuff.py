import math
# IGNORE: misc stuff used for calculations

# brute
# for i in range(1, 41):
#     print(f"g^{i} equiv {pow(6, i, 41)} mod 41")
#shanks
# y = 15
# g = 6
# n = 1 + math.floor(math.sqrt(41))
# for i in range(0, n+1):
#     baby = pow(g, i, 41)
#     giant = y*pow(g, (-i*n), 41)%41
#     print(f"i = {i}, baby = {baby}, giant = {giant}")

# Shanks baby giant:
# for baby and giant: dictionary as {num: index}

for i in range(1, 20):
    print((5**i - 1)/4)