rows = 4


for i in range(1, rows + 1):
    print(" " * (rows - 1), end="")
    print(i)


for i in range(1, rows + 1):
    print(i, end="")
for i in range(rows - 1, 0, -1):
    print(i, end="")
print()


for i in range(rows, 0, -1):
    print(" " * (rows - 1), end="")
    print(i)
