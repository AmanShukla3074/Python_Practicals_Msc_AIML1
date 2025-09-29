# 13.	Write a Python program to find the longest increasing subsequence from a given list of numbers.
# Answer:
# I implement a simple O(n^2) dynamic programming approach which is clear and human-like.

lst = input("Enter numbers separated by spaces: ").split()
nums = [int(x) for x in lst]

if not nums:
    print("No subsequence (empty list).")
else:
    n = len(nums)
    dp = [1]*n
    prev = [-1]*n
    best_i = 0
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > dp[best_i]:
            best_i = i
    # reconstruct
    lis = []
    cur = best_i
    while cur != -1:
        lis.append(nums[cur])
        cur = prev[cur]
    lis.reverse()
    print("Longest increasing subsequence:", lis)
