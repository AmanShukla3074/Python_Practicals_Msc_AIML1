# 42.	Convert a tuple of (product, price) pairs into a dictionary.
# Answer:
# Expect input like (p1,100),(p2,200) but we'll take simpler "p:price" pairs.

pairs = input("Enter product:price pairs comma separated: ")
d = dict((p.split(':')[0].strip(), float(p.split(':')[1])) for p in pairs.split(',') if p.strip())
print("Product price dict:", d)
