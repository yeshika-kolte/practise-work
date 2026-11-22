# Write a JavaScript program using nested ternary operators to find the maximum of three numbers.

n1 = int(input("Enter 1st number: "));
n2 = int(input("Enter 2nd number: "));
n3 = int(input("Enter 3rd number: "));
if n1>n2 and n1>n3:
    print("First number is maximum", (n1))
elif n2>n1 and n2>n3:
    print("Second number is maximum", (n2))
else:
    print("Third number is maximum", (n3))