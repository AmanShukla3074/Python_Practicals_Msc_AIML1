# 8.	Write a Python program to find the missing number in a list of consecutive numbers.
# Answer:
# I compute expected sum from min to max and subtract actual sum.

lst = input("Enter consecutive numbers with one missing, separated by spaces: ").split()
nums = [int(x) for x in lst]

if not nums:
    print("No numbers provided.")
else:
    low, high = min(nums), max(nums)
    expected_sum = (high + low) * (high - low + 1) // 2
    missing = expected_sum - sum(nums)
    if missing == 0:
        print("No missing number detected between", low, "and", high)
    else:
        print("Missing number is:", missing)
