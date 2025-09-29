# 41.	Convert two lists (keys, values) into a dictionary of city populations.
# Answer:
# Read keys and values and zip into dict.

keys = input("Enter city names separated by spaces: ").split()
vals = input("Enter populations separated by spaces: ").split()
vals = [int(v) for v in vals]
city_pop = dict(zip(keys, vals))
print("City populations:", city_pop)
