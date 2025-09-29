# 26.	extract the middle three characters from a string.
# Answer:
# This only makes sense for strings with odd length >=3.

s = input("Enter a string (odd length and at least 3): ")
n = len(s)
if n >= 3 and n % 2 == 1:
    mid = n // 2
    print("Middle three characters:", s[mid-1:mid+2])
else:
    print("String must be odd-length and at least 3 characters long.")
