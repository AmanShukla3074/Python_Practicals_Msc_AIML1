# 25.	find the frequency of each character in a string.
# Answer:
# Use a simple loop with a dict to count frequency.

s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print("Character frequencies:", freq)
