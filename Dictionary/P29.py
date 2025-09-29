# 29.	Given a paragraph, store word frequencies in a dictionary.
# Answer:
# Split on whitespace and count lowercased words.

para = input("Enter a paragraph: ")
words = [w.strip(".,!?;:()[]\"'").lower() for w in para.split()]
freq = {}
for w in words:
    if w:
        freq[w] = freq.get(w, 0) + 1
print("Word frequencies:", freq)
