#check string is palindrome or not
str = input("Enter a string: ")
i=0
j=len(str)-1
flag = True
while i<j:
    if str[i] != str[j]:
        flag = False
        break
    i+=1
    j-=1
if flag:
    print("String is palindrome")
else:
    print("String is not palindrome")

