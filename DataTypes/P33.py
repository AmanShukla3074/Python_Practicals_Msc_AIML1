# 33.	remove all punctuation marks from a string.
# Answer:
# Use str.isalnum() to keep letters/numbers and spaces.

import string
s = input("Enter a string: ")
clean = "".join(ch for ch in s if ch.isalnum() or ch.isspace())
print("Without punctuation:", clean)
