# 21.	Write a Python program to check if a list is a palindrome.
# Answer:
# I compare the list to its reversed version.

lst = input("Enter elements separated by spaces: ").split()
if lst == lst[::-1]:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
