for i in range(5, 0, -1):
    for j in range(1, i + 1):
        if i == 5:
            print(chr(64 + j), end="")
        elif j == 1 or j == i:
            print(chr(64 + j), end="")
        elif i == 2:
            print(chr(64 + j), end="")
        else:
            print(" ", end="")
    print()
