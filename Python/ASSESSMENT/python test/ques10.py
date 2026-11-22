#find the second maximum and second minimum in the list

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
max1 = float('-inf')
max2 = float('-inf')
min1 = float('inf')
min2 = float('inf')
for num in l1:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2 and num != max1:
        max2 = num
        
    if num < min1:
        min2 = min1
        min1 = num
    elif num < min2 and num != min1:
        min2 = num
print(f"Second Maximum: {max2}")
print(f"Second Minimum: {min2}")