# 9.	Write a Python program to find the missing numbers in a list of continuous numbers.
# Answer:
# I build the full range from min to max and subtract the given set to list missing values.

lst = input("Enter numbers (continuous range with possibly multiple missing) separated by spaces: ").split()
nums = [int(x) for x in lst]

if not nums:
    print("No numbers provided.")
else:
    full = set(range(min(nums), max(nums) + 1))
    missing = sorted(list(full - set(nums)))
    if missing:
        print("Missing numbers:", missing)
    else:
        print("No missing numbers in the given range.")
