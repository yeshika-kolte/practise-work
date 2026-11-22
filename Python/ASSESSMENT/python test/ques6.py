#program to insert an element at specific index

l1=[1,2,3,4,5]
element = 10
index = 4
l1.append(0)  
for i in range(len(l1)-1, index, -1):
    l1[i] = l1[i-1]  
    l1[index] = element  
print(l1)
