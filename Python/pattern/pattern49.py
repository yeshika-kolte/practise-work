rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, 2 * i):
        if j % 2 == 0:
            print("_", end="")
        else:
            print("*", end="")
    print()
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(1, 2 * i):
        if j % 2 == 0:
            print("_", end="")
        else:
            print("*", end="")
    print()
