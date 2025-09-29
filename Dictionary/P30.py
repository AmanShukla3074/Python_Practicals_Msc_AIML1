# 30.	Track the number of orders per product in a shop using a dictionary.
# Answer:
# Input product names per order; tally.

orders = input("Enter product names for orders separated by spaces: ").split()
orders_count = {}
for p in orders:
    orders_count[p] = orders_count.get(p, 0) + 1
print("Orders per product:", orders_count)
