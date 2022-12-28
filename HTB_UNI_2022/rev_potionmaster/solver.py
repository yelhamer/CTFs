#!/usr/bin/python3

from sys import argv


# Clues
sub_vals = [-43, 61, 58, 5, -4, -11, 64, -40, -43, 61, 62, -51, 46, 15, -49, -44, 47, 4, 6, -7, 47, 7, -59, 52, -15, 11, 7, 61, 0]
xor_vals = [6, 106, 10, 0, 119, 52, 51, 101, 0, 0, 15, 48, 116, 22, 10, 58, 125, 100, 102, 33]
sum_vals = [304, 357, 303, 320, 304, 307, 349, 305, 257, 337, 340, 309, 428, 270, 66]

# Split the Flag into sets of lcm(2,3,4) = 12, and solve each equation system corresponding to the 12 unknowns
flag = []
for i in range(0, int(len(sum_vals)/3)):
    # Array of 12 unknowns
    dodeca = [0 for _ in range(12)]


    # Find first quadruple
    # Bruteforce 1st element
    for a in range(256):
        # Get a
        dodeca[0] = sub_vals[i*6] + a
        # Get b
        dodeca[1] = a 
        # Get c
        dodeca[2] = xor_vals[i*4] ^ dodeca[0] ^ dodeca[1]
        # Fet d
        dodeca[3] = dodeca[2] - sub_vals[i*6+1]
        # Check if quadruple is satisfying final condition
        if dodeca[0] + dodeca[1] + dodeca[2] + dodeca[3] == sum_vals[i*3]:
            # Register as possible quadruple
            break
            

    # Find last quadruple       
    # Bruteforce last element
    if i == 4:
        dodeca[8] = 33
        dodeca[9] = 33
        dodeca[10] = 0
        dodeca[11] = 0

    else:
        for l in range(256):
            # Get l
            dodeca[11] = l
            # Get k
            dodeca[10] = sub_vals[i*6+5] + l
            # Get j
            dodeca[9] = xor_vals[i*4+3] ^ dodeca[10] ^ dodeca[11]
            # Get i
            dodeca[8] = dodeca[9] + sub_vals[i*6+4]
            # Check if quadruple is satisfying final condition
            if dodeca[8] + dodeca[9] + dodeca[10] + dodeca[11] == sum_vals[i*3+2]:
                # Register as possible quadruple
                break


    # Find middle quadruple
    # Test out all possible vals
    # Bruteforce vals of e and f
    v1 = []
    for e in range(256):
        for f in range(256):
            if e-f == sub_vals[i*6+2] and e^f == xor_vals[i*4+1] ^ dodeca[3]:
                v1.append((e, f))
    
    # Bruteforce vals of g and h
    v2 = []
    for g in range(256):
        for h in range(256):
            if g-h == sub_vals[i*6+3] and g^h == xor_vals[i*4+2] ^ dodeca[8]:
                v2.append((g, h))

    # Print all possible values for the middle quadruple
    print(f"Other possible values for substring flag[{i*12+4}:{i*12+8}]: ")
    for e, f in v1:
        for g, h in v2:
            # If all vals are compatible add to flag
            if e+f+g+h == sum_vals[i*3+1]:
                dodeca[4] = e
                dodeca[5] = f
                dodeca[6] = g
                dodeca[7] = h
                if i == 4:
                    print(f"{''.join(map(chr, dodeca[4:8]))}")

    flag += dodeca

flag = map(chr, flag)
flag = "".join(flag)
print(f"\nFlag is: {flag[0:58-6]}")
print(f"flag_length: {len(flag)}")


