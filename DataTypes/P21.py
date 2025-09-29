# 21.	check if a given word exists in a string.
# Answer:
# Use 'in' to check substring presence; ask user for the word.

s = input("Enter the main string: ")
word = input("Enter the word to search for: ")
print(f"Does the word '{word}' exist in the string? ->", word in s)
