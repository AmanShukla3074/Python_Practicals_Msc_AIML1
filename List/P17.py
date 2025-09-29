# 17.	Write a Python program to remove the elements at even indices from a list.
# Answer:
# I keep elements at odd indices (1,3,5,...). Indexing is 0-based so "even indices" mean 0,2,4,...

lst = input("Enter elements separated by spaces: ").split()
result = [item for i, item in enumerate(lst) if i % 2 == 1]
print("List after removing elements at even indices:", result)
