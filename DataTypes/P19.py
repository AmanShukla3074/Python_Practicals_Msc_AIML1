# 19.	count how many vowels are present in a given string.
# Answer:
# Iterate and check membership in vowel set.

s = input("Enter a string: ")
vowels = set("aeiouAEIOU")
count = sum(1 for ch in s if ch in vowels)
print("Number of vowels:", count)
