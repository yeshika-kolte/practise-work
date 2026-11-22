#Find the occurance of all the number in list
l1= [1, 2, 3, 4, 5, 1, 2, 3, 4, 5,6,66,6,7,7,8]
result = {}
for num in l1:
    if num in result:
        result[num] += 1
    else:
        result[num] = 1 
print(result)