#WAP to program to calculate the sum of all element of array.
n = int(input("Enter number of elements: "))
l1 = [int(input(f"Enter element {i}: ")) for i in range(n)]

total = 0
for x in l1:
    total =total + x

print("Sum of all elements:", total)
