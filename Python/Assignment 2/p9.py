# Write a pyhton program using the conditional operator to compare two arithmetic expressions and display the greater result.

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number: "))

res1= num1 + num2;
res2 = num1 - num2;

if res1>res2:
    print("Exp 1 have greater result", (res1),">",(res2))
elif res1==res2:
    print("Exp 1 and Exp 2 result is same", (res1),"=",(res2))
else:
    print("Exp 2 have greater result", (res2),">",(res1))
