# Question 5 — File Handling with Exception Handling

# Create a program that:

# Asks the user for a filename.
# Reads the content of the file.
# Displays the total number of:
# characters
# words
# lines

# Use proper exception handling for:

# FileNotFoundError
# PermissionError
# Sample Output
# Total Characters: 120
# Total Words: 25
# Total Lines: 5

filename = input("Enter filename: ")

try:
    with open(filename, "r") as f:

        content = f.read()
        total_character = len(content)
        total_words = len(content.split())
        total_lines = len(content.splitlines())

        print("Total Characters:", total_character)
        print("Total Words:", total_words)
        print("Total Lines:", total_lines)

except FileNotFoundError as e:
    print("Error:- File not found")

except PermissionError as e:
    print("Error:- Permission problem.")
