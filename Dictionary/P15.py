# 15.	Safely remove "mango" from a fruit dictionary only if it exists.
# Answer:
# Check membership before deleting.

pairs = input("Enter fruit:price pairs comma separated: ")
fruits = dict((p.split(':')[0].strip(), float(p.split(':')[1])) for p in pairs.split(',') if p.strip())
if "mango" in fruits:
    del fruits["mango"]
    print("Mango removed.")
else:
    print("Mango not in dictionary.")
print("Fruits:", fruits)
