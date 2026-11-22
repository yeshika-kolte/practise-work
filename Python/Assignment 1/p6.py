# 6. Write a program to print absolute vlaue of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1

a = int(input("Enter a no. : "))

if a < 0:
    val = -a
else:
    val = a
print(val)

