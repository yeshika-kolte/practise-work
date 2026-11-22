#count occurence of each element in a list 
data = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
result = {}
for i in data:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(result)      