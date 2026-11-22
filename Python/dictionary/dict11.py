words = ["hi", "hello", "hey", "python"]

result = {}
for char in words:
    length = len(char)                 
    if length not in result:        
        result[length] = []         
    result[length].append(char)       

print(result)