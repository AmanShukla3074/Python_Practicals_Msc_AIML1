# 10. Write a function that takes a list and returns a new list with unique elements (no duplicates).
def unique_list(lst):
    return list(set(lst))

print(unique_list([1, 2, 2, 3, 4, 4, 5]))
