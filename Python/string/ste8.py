#reverse a string
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
s = list(input("Enter a string: "))
reversed_s = reverseString(s)
print("Reversed string: ", ''.join(reversed_s))
