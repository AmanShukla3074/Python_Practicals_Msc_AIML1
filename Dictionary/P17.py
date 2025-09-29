# 17.	Loop through a dictionary of product prices and display "Product → Price".
# Answer:
# Straightforward iteration.

pairs = input("Enter product:price pairs comma separated: ")
products = dict((p.split(':')[0].strip(), float(p.split(':')[1])) for p in pairs.split(',') if p.strip())
for prod, price in products.items():
    print(f"{prod} → {price}")
