# 1.	Remove empty strings from the list of strings without using any loops
# Answer:
# I used Python's filter to remove empty strings. This avoids explicit for/while loops.

s = input("Enter strings separated by commas (e.g. a,,b, ,c): ").split(',')
# strip whitespace from each entry then filter out exact empty strings
cleaned = list(filter(lambda x: x != '', [item.strip() for item in s]))
print("Removed empty strings. Result:", cleaned)
