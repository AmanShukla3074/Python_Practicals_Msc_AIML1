# 17.	print the first and last characters of a string.
# Answer:
# Just index 0 and -1; handle empty string.

s = input("Enter a string: ")
if s:
    print("First character:", s[0])
    print("Last character:", s[-1])
else:
    print("Empty string, no characters to show.")
