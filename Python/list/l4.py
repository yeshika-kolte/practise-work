n = int(input("Enter number of elements: "))
list = [int(input(f"Enter element {i}: ")) for i in range(n)]

find = int(input("Enter element to find: "))

if find in list:
    print(f"Element {find} found at position {list.index(find)}")
else:
    print(f"Element {find} not found in the list")
