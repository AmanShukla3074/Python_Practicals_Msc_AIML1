# 38.	Create a shopping cart dictionary where each item stores price and quantity.
# Answer:
# Build dict with nested price/qty.

items = input("Enter item:price:qty triples separated by commas (e.g. apple:30:2): ")
cart = {}
for trip in items.split(','):
    if trip.strip():
        name, price, qty = trip.split(':')
        cart[name.strip()] = {"price": float(price), "qty": int(qty)}
print("Shopping cart:", cart)
