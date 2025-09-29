# 16.	print its length without using len() function.
# Answer:
# We'll count characters manually.

s = input("Enter a string to count its length without len(): ")
count = 0
for _ in s:
    count += 1
print("Length (manual count):", count)
