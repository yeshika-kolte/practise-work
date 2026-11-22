#Given a dictionary, find keys that have the same values.
d = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}
same_values = {}
for key, value in d.items():
    if value in same_values:
        same_values[value].append(key)
    else:
        same_values[value] = [key]
for value, keys in same_values.items():
    if len(keys) > 1:
        print(f"Keys with value {value}: {keys}")