n = int(input("Enter number of elements: "))
lst = [input(f"Enter element {i}: ") for i in range(n)]
k=int(input("Enter the value of k: "))
print(f"before {lst}")
for i in range(len(lst)-1):
    for j in range (i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]

print(f"after {lst}")
print(f"{k}th largest element :{lst[len(lst)-k]}")
print(f"{k}th smallest element:{lst[k-1]}")


