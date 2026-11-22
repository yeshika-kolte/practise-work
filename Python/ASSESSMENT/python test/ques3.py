#find the  intersection of two list

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

n1= len(l1)
n2= len(l2)
result =[]
i = 0
j = 0
while i<n1 and j<n2:
    if l1[i] < l2[j]:
        i += 1
    elif l2[j] < l1[i]:
        j += 1
    else:
        result.append(l1[i])
        i += 1
        j += 1
print(f"Intersection : {result}")