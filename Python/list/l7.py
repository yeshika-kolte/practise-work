n = int(input("Enter number of elements: "))
list = [int(input(f"Enter element {i}: ")) for i in range(n)]


for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if list[j] < list[min_index]:
            list[i], list[min_index] = list[min_index], list[i]

print("Sorted list:", list)

search = int(input("Enter element to search: "))

low, high = 0, n-1
found = False

while low <= high:
    mid = (low + high) // 2
    if list[mid] == search:
        print(f"Element {search} found at position {mid+1}")
        found = True
        break
    elif list[mid] < search:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print(f"Element {search} not found in the list")
