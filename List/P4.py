# 4.	Write a Python program to find the second smallest element in a list.
# Answer:
# I convert to a set to remove duplicates, sort, and take the second item if available.

lst = input("Enter numbers separated by spaces: ").split()
nums = [float(x) for x in lst]

unique_sorted = sorted(set(nums))
if len(unique_sorted) < 2:
    print("No second smallest element (not enough unique values).")
else:
    print("Second smallest element is:", unique_sorted[1])
