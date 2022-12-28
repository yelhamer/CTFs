#!/usr/bin/python3



# Obtained from reversing the BPF program
a = [72, 12, 54, 69, 28, 98, 16, 36, 63, 34, 45, 70, 31, 68, 31, 111, -2, 114, -81, 206]

# Partition it into subsets of 5 elements
a = [a[i*5:(i+1)*5] for i in range(5)]

# Construct Flag
flag = []
for arr in a:
    temp = 0
    for elem in arr:
        flag.append(elem+temp)
        temp = elem

# Print Flag
flag = "".join(map(chr, flag))
print(f"Flag is {flag}")
