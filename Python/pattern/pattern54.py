rows = 5
for i in range(1, rows):
    print(" " * (rows - i), end="")
    if i == 1:
        print("1")
    else:
        print("1" + "*" * (2 * i - 3) + "1")


for j in range(1, 2 * rows):
    print("1", end="")
print()
