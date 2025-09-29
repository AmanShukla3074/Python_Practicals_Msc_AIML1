# 14.	Write a Python program to check whether an identifier is valid.
# Answer:
# This is the same as checking isidentifier(); I'll ask user for input.

identifier = input("Enter the identifier to validate: ")
print(f"Is '{identifier}' a valid identifier? ->", identifier.isidentifier())
