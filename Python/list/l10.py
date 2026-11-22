n= int(input("Enter the number of elements in the list: "))
lst= [input(f"Enter element {i}: ") for i in range(n)]
size =len(lst)
dict={}

for i in lst:
    if dict.get(i):
        dict[i]+=1
    else:
        dict[i]=1

print(dict)      