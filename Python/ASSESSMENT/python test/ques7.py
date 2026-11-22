#Invert a Dictionary (Handle Duplicates)
#Swap keys and values. If values repeat, store keys in a list.
#Example:
#data = {"a": 1, "b": 2, "c": 1}
#👉 Output:
#{1: ['a', 'c'], 2: ['b']}

data = {"a": 1, "b": 2, "c": 1}
result= {}
for key, value in data.items():
    if value in result:
        result[value].append(key)
    else:
       result[value]=[key]
print(result)