# 15. Program to find all palindromic words in a list using lambda and filter().
words = ["level", "hello", "radar", "world"]
palindromes = list(filter(lambda w: w == w[::-1], words))
print(palindromes)
