# 20.	check if a string is a palindrome.
# Answer:
# We'll ignore non-alphanumeric and case for a fair check.

s = input("Enter a string to check palindrome: ")
clean = "".join(ch.lower() for ch in s if ch.isalnum())
print("Is palindrome?:", clean == clean[::-1])
