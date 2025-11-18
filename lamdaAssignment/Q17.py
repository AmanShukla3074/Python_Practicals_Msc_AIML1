# 17. Program to sort a list of words based on their last character using lambda.
words = ["cat", "apple", "bat"]
sorted_last_char = sorted(words, key=lambda x: x[-1])
print(sorted_last_char)
