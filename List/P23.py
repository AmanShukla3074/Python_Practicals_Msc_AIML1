# 23.	Write a Python program to find the index of the first occurrence of an element in a list without using the built-in index function.
# Answer:
# I use enumerate to scan the list and break on first match.

lst = input("Enter elements separated by spaces: ").split()
target = input("Enter the element to find: ")

found = -1
for i, val in enumerate(lst):
    if val == target:
        found = i
        break

if found == -1:
    print(f"Element '{target}' not found.")
else:
    print(f"First occurrence of '{target}' is at index {found}.")
