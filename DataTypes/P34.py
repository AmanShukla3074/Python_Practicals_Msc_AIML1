# 34.	print the ASCII value of each character in a string.
# Answer:
# Use ord() for each character.

s = input("Enter a string: ")
for ch in s:
    print(f"'{ch}' ->", ord(ch))
