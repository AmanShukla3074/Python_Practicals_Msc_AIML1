# 32.	From a list of names, create a dictionary mapping names to their lengths.
# Answer:
# Read names and map to len().

names = input("Enter names separated by spaces: ").split()
lengths = {n: len(n) for n in names}
print("Name lengths:", lengths)
