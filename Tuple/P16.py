# 16.	You have a tuple of student marks (85, 92, 78, 90). Find the maximum and minimum marks.
# Answer:
# I use built-in max() and min() functions.

t = tuple(map(int, input("Enter marks separated by spaces: ").split()))
print("Maximum marks:", max(t))
print("Minimum marks:", min(t))
