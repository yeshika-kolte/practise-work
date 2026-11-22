n = int(input("Enter number of elements: "))
l1 = [int(input(f"Enter element {i}: ")) for i in range(n)]

for i in range(n):
    if l1[i] % 5 == 0:
        l1[i] = 0

print("new array:", l1)
