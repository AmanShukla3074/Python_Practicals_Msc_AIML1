# 5. Write a function to check whether a string is a palindrome or not.
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("level"))
