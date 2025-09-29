# 21.	Check if "apple" exists in a fruit price dictionary.
# Answer:
# Check membership of the key 'apple'.

pairs = input("Enter fruit:price pairs comma separated: ")
d = dict((p.split(':')[0].strip(), float(p.split(':')[1])) for p in pairs.split(',') if p.strip())
print("Apple exists?" , "apple" in d)
