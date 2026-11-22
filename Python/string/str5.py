def balancedStringSplit(s: str) -> int:
    l_count = 0
    r_count = 0
    balanced_count = 0
    for char in s:
        if char == 'L':
            l_count += 1
        elif char == 'R':
            r_count += 1
        if l_count == r_count:
            balanced_count += 1
    return balanced_count
s = input("Enter a string of 'L' and 'R': ")
result = balancedStringSplit(s)
print("Number of balanced strings: ", result)
