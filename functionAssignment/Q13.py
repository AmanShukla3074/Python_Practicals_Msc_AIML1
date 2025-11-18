# 13. Write a function to count how many even and odd numbers are present in a list.
def count_even_odd(lst):
    even = sum(1 for x in lst if x % 2 == 0)
    odd = len(lst) - even
    return even, odd

print(count_even_odd([1, 2, 3, 4, 5, 6]))
