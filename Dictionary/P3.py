# 3.	Create a dictionary of 3 countries and their capitals. Print the capital of "Japan".
# Answer:
# Read three country:capital pairs and print Japan's capital.

pairs = input("Enter three country:capital pairs comma separated (e.g. Japan:Tokyo,India:New Delhi,...): ")
d = dict(tuple(p.split(':')) for p in pairs.split(',') if p.strip())
print("Capital of Japan:", d.get("Japan", "Japan not in dictionary"))
