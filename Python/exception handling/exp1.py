print("this the first line of the code")

try:
    a= int(input("enter the first number "))
    b= int(input("enter the second numebr"))
    c=a//b

except ArithmeticError  as e:
    print (f"arirthmetic error occur {e}")  

print("this the last line of the code")