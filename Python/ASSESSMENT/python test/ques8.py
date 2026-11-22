#Group Words by Length
#Group a list of words into a dictionary where key = word length.
#Example:
#words = ["hi", "hello", "hey", "python","bye"]
#👉 Output:
#{2: ['hi'], 3: ['hey',"bye"], 5: ['hello'], 6: ['python']}

words = ["hi", "hello", "hey", "python","bye"]
result = {}
for word in words:
    length = len(word)
    if length in result:
        result[length].append(word)
    else:
        result[length] = [word]
print(result)