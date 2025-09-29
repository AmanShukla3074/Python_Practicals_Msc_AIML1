# 18.	Print all countries and capitals using a loop.
# Answer:
# Print each pair on its own line.

pairs = input("Enter country:capital pairs comma separated: ")
countries = dict((p.split(':')[0].strip(), p.split(':')[1].strip()) for p in pairs.split(',') if p.strip())
for c, cap in countries.items():
    print(c, ":", cap)
