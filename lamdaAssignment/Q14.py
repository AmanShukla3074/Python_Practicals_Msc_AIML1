# 14. Program to sort a list of strings by their length using lambda.
words = ["apple", "kiwi", "banana"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
