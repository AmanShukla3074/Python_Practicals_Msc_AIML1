# 35.	find the most frequent character in a string.
# Answer:
# Count characters then pick the max by frequency.

s = input("Enter a string: ")
if not s:
    print("Empty string.")
else:
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    most_char, most_count = max(freq.items(), key=lambda x: x[1])
    print(f"Most frequent character: '{most_char}' occurs {most_count} times.")
