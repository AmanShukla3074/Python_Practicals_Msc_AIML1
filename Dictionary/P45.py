# 45.	Convert a dictionary of items into a list of tuples.
# Answer:
# Use items() to get list of tuples.

pairs = input("Enter key:value pairs comma separated: ")
d = dict((p.split(':')[0].strip(), p.split(':')[1].strip()) for p in pairs.split(',') if p.strip())
print("List of tuples:", list(d.items()))
