n = int(input("Enter number of elements: "))
list= [int(input(f"Enter element {i}: ")) for i in range(n)]

element = int(input("Enter element to insert: "))
position = int(input("Enter position : "))

list.append(0)
for i in range(n, position-1, -1):
    list[i] = list[i-1]
    list[position-1] = element

print("Updated list:", list)
