#WAP to Enter n element in array and print array
n = int(input("Enter number of elements: "))
list = [input(f"Enter element {i}: ") for i in range(n)]
print("The list is:", list)
