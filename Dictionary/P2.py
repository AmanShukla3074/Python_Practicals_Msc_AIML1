# 2.	Store the prices of fruits in a dictionary. Retrieve the price of "apple".
# Answer:
# User supplies fruit-price pairs; I look up 'apple'.

items = input("Enter fruit:price pairs separated by commas (e.g. apple:30,banana:10): ")
d = {}
for pair in items.split(','):
    if pair.strip():
        k, v = pair.split(':')
        d[k.strip()] = float(v.strip())
print("Dictionary:", d)
print("Price of apple:", d.get("apple", "apple not found"))
