# 19. Write a function to check if two strings are anagrams of each other.
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))
