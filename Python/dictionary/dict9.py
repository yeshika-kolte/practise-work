#data = {"a": 1, "b": 2, "c": 1, "d": 3} Output: keys with duplicate values → ['a', 'c']
data = {"a": 1, "b": 2, "c": 1, "d": 3}

result = {}
for key, value in data.items():
    if value not in result:       
        result[value] = []
    result[value].append(key)       

duplicates = [key for value, keys in result.items() if len(keys) ]

print(duplicates)
