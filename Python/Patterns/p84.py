# a
# bc
# d f
# g  j
# klmno

ch = 97

for i in range(1, 6):
    for j in range(1, i + 1):
        if (i == 3 or i == 4) and j != 1 and j != i:
            print(" ", end="")
            ch += 1
        else:
            print(chr(ch), end="")
            ch += 1
    print()
