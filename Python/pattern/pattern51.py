rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == rows:
            if not (i == rows and (j == 2 or j == 3)):
                print(j, end="")
            else:
                print(" ", end="")
        else:
            print(" ", end="")
    print()
for i in range(rows - 1, 0, -1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == rows:
            print(j, end="")
        else:
            print(" ", end="")
    print()
