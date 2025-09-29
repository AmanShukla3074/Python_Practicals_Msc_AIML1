# 15.	Write a Python program to split a list into chunks of a given size.
# Answer:
# I slice the list into pieces of the requested chunk size.

lst = input("Enter elements separated by spaces: ").split()
chunk = int(input("Enter chunk size (positive integer): "))

if chunk <= 0:
    print("Chunk size must be positive.")
else:
    result = [lst[i:i+chunk] for i in range(0, len(lst), chunk)]
    print("Chunks:", result)
