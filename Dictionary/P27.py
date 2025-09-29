# 27.	Keep track of the number of times each fruit is sold using a dictionary.
# Answer:
# Input sold fruit names; tally counts.

sold = input("Enter sold fruits separated by spaces: ").split()
tally = {}
for f in sold:
    tally[f] = tally.get(f, 0) + 1
print("Sales tally:", tally)
