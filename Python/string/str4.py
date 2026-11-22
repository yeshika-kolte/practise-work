# find frequent vowel and consonant in a string
s = input("Enter a string: ")
vowels = 'aeiouAEIOU'
vowel_count = {}
consonant_count = {}
for char in s:
    if char.isalpha():
        if char in vowels:
            vowel_count[char] = vowel_count.get(char, 0) + 1
        else:
            consonant_count[char] = consonant_count.get(char, 0) + 1
if vowel_count:
    most_frequent_vowel = max(vowel_count, key=vowel_count.get)
    print(f"Most frequent vowel: {most_frequent_vowel} (Count: {vowel_count[most_frequent_vowel]})")
else:
    print("No vowels found.")
if consonant_count:
    most_frequent_consonant = max(consonant_count, key=consonant_count.get)
    print(f"Most frequent consonant: {most_frequent_consonant} (Count: {consonant_count[most_frequent_consonant]})")
else:
    print("No consonants found.")

        