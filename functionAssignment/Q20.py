# 20. Write a function that takes a list of numbers and returns a list of squares of each.
def list_squares(lst):
    return [x * x for x in lst]

print(list_squares([1, 2, 3, 4]))
