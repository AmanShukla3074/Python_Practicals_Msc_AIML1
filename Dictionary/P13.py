# 13.	Pop the capital of "Germany" from a country-capital dictionary.
# Answer:
# Use pop to get and remove Germany's capital.

pairs = input("Enter country:capital pairs comma separated: ")
d = dict((p.split(':')[0].strip(), p.split(':')[1].strip()) for p in pairs.split(',') if p.strip())
capital = d.pop("Germany", None)
print("Popped capital of Germany:", capital)
print("Remaining dict:", d)
