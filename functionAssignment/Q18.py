# 18. Write a function to return the second largest element in a list.
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]

print(second_largest([10, 20, 30, 40]))
