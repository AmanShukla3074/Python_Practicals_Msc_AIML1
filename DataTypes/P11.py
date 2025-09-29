# 11.	Write a Python program to check if a keyword exists in Python.
# Answer:
# Use keyword.iskeyword() to check membership.

kw = input("Enter a word to check if it's a Python keyword: ")
import keyword
print(f"Is '{kw}' a keyword? ->", keyword.iskeyword(kw))
