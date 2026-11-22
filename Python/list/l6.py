n = int(input("Enter number of elements: "))
list = [int(input(f"Enter element {i}: ")) for i in range(n)]


for i in range(n):
    min_index = i
    for j in range(i, n):
        if list[j] < list[min_index]:
            min_index = j
    list[i], list[min_index] = list[min_index], list[i]

print("Sorted list:", list)
