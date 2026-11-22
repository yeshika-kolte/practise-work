for i in range(65, 91):
    for j in range(65, 91):
        if j == 65 or i == j or i == 90:
            print(chr(j), end="")
        else:
            print(" ", end="")
    print()