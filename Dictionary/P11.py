# 11.	Remove "grapes" from a fruit price dictionary.
# Answer:
# Safely remove grapes if present.

pairs = input("Enter fruit:price pairs comma separated: ")
d = dict((p.split(':')[0].strip(), float(p.split(':')[1])) for p in pairs.split(',') if p.strip())
d.pop("grapes", None)
print("After removing grapes (if present):", d)
