# 32.	join a list of words into a single string with spaces.
# Answer:
# Use ' '.join() after getting words from user.

words_input = input("Enter words separated by commas (e.g. hello,world): ")
words = [w.strip() for w in words_input.split(',') if w.strip()]
joined = " ".join(words)
print("Joined string:", joined)
