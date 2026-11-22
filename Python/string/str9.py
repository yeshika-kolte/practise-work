#check character on even and odd position
str = input("Enter a string: ")
even_chars = ""
odd_chars = ""
for i in range(len(str)):
    if i % 2 == 0:
        odd_chars += str[i]
    else:
        even_chars += str[i]
print("Characters at even positions: ", even_chars)
print("Characters at odd positions: ", odd_chars)
