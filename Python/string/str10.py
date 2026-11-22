#isomorphic strings
def IsomorphicStrings(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    mapping_s_to_t = {}
    mapping_t_to_s = {}
    for char_s, char_t in zip(s, t):
        if char_s in mapping_s_to_t and mapping_s_to_t[char_s] != char_t:
            return False
        if char_t in mapping_t_to_s and mapping_t_to_s[char_t] != char_s:
            return False
        mapping_s_to_t[char_s] = char_t
        mapping_t_to_s[char_t] = char_s
    return True
s = input("Enter the first string: ")
t = input("Enter the second string: ")
result = IsomorphicStrings(s, t)
if result:
    print("The strings are isomorphic.")

else:
    print("The strings are not isomorphic.")
        