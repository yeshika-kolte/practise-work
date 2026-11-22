#length of last word of a string
s=input("Enter a string: ")
i=len(s)-1
length=0
while i>=0 and s[i]==' ':
    i-=1
    
while i>=0 and s[i]!=' ':
    length+=1
    i-=1
print("Length of last word is: ",length)