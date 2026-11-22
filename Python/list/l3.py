n = int(input("Enter number of elements: "))
l1 = [int(input(f"Enter element {i}: ")) for i in range(n)]

even_sum = 0
odd_sum = 0

for x in l1:
    if x % 2 == 0:
        even_sum += x
    else:
        odd_sum += x

print("Sum of even elements:", even_sum)
print("Sum of odd elements:", odd_sum)
