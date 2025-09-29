# 19.	Create a dictionary of 5 words and their meanings. Print them in "word: meaning" format.
# Answer:
# Read five pairs and print prettily.

pairs = input("Enter word:meaning pairs comma separated (5 pairs): ")
d = dict((p.split(':')[0].strip(), p.split(':')[1].strip()) for p in pairs.split(',') if p.strip())
for w, m in d.items():
    print(f"{w}: {m}")
