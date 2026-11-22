# 9. Write a program to check whether a entered character is lowercase ( a to z ) or uppercase ( A to Z ).

char = input("Enter any char: ")

if len(char) !=1:
    print("Enter a single char")
elif "a"<= char <="z":
    print({char},"is lowercase")
elif "A"<= char <="Z":
    print({char},"is uppercase")
else:
    print("Invalid input")