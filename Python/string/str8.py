#shuffle a string
def shuffleString(s, indices):
    shuffled = [''] * len(s)
    for i, index in enumerate(indices):
        shuffled[index] = s[i]
    return ''.join(shuffled)
s = input("Enter the string to shuffle: ")
indices = list(map(int, input("Enter the indices (space-separated): ").split()))
shuffled_string = shuffleString(s, indices)
print("Shuffled string: ", shuffled_string)
