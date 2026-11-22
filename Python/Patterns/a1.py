for i in range(97, 123):
    for j in range(97, 123):
        if j == 97 or i == j or i == 122:
            print(chr(j), end="")
        else:
            print(" ", end="")
    print()
