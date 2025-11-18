# 16. Write a function that accepts a string and counts the number of uppercase and lowercase letters.
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

print(count_case("Hello World"))
