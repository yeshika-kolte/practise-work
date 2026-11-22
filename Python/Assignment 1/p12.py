# 12.A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one. E.g.-
# INPUT : 1234        OUTPUT : 4321
# INPUT : 5982        OUTPUT : 2895 

num = int(input("Enter a 4 digit number: "))
d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10
rev = d4 * 1000 + d3 * 100 + d2 * 10 + d1
print(rev)