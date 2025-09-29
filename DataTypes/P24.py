# 24.	count how many words are in a sentence.
# Answer:
# Split on whitespace and count resulting words.

s = input("Enter a sentence: ")
words = s.split()
print("Word count:", len(words))
