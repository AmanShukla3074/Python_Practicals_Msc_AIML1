# 15.	Write a menu Python program for a given string:
# Answer:
# The menu will let user pick actions (16-35 correspond to various string ops).

s = input("Enter a string for the menu-driven operations: ")
print("Menu (pick a number):")
print("1 - length without len(); 2 - first & last char; 3 - reverse using slicing")
print("4 - count vowels; 5 - check palindrome; 6 - check if word exists")
print("7 - replace 'Python' with 'Java'; 8 - remove spaces; 9 - word count")
print("10 - char frequencies; 11 - extract middle three chars; 12 - to upper")
print("13 - title case; 14 - startswith 'Hello'; 15 - endswith 'World'")
print("16 - split into words; 17 - join words with spaces; 18 - remove punctuation")
print("19 - print ASCII values; 20 - most frequent character")
choice = input("Enter choice (1-20): ").strip()
# We'll implement a few choices simply and defer to built-ins for others:
if choice == "1":
    # length without len()
    cnt = 0
    for _ in s:
        cnt += 1
    print("Length (without len):", cnt)
elif choice == "2":
    if s:
        print("First char:", s[0], "Last char:", s[-1])
    else:
        print("Empty string.")
elif choice == "3":
    print("Reversed (slicing):", s[::-1])
elif choice == "4":
    vowels = set("aeiouAEIOU")
    c = sum(1 for ch in s if ch in vowels)
    print("Vowel count:", c)
elif choice == "5":
    clean = "".join(ch.lower() for ch in s if ch.isalnum())
    print("Is palindrome?:", clean == clean[::-1])
elif choice == "6":
    word = input("Enter word to search: ")
    print("Word found?" , word in s)
elif choice == "7":
    print("Replaced string:", s.replace("Python", "Java"))
elif choice == "8":
    print("Without spaces:", s.replace(" ", ""))
elif choice == "9":
    words = s.split()
    print("Word count:", len(words))
elif choice == "10":
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    print("Char frequencies:", freq)
elif choice == "11":
    n = len(s)
    if n >= 3 and n % 2 == 1:
        mid = n // 2
        print("Middle three chars:", s[mid-1:mid+2])
    else:
        print("String too short or even length for 'middle three' rule.")
elif choice == "12":
    print("Uppercase:", s.upper())
elif choice == "13":
    print("Title case:", s.title())
elif choice == "14":
    print("Starts with 'Hello'?:", s.startswith("Hello"))
elif choice == "15":
    print("Ends with 'World'?:", s.endswith("World"))
elif choice == "16":
    print("Split into words:", s.split())
elif choice == "17":
    parts = input("Enter words separated by commas to join: ").split(',')
    print("Joined:", " ".join(p.strip() for p in parts))
elif choice == "18":
    import string
    cleaned = "".join(ch for ch in s if ch not in string.punctuation)
    print("Without punctuation:", cleaned)
elif choice == "19":
    print("ASCII values:")
    for ch in s:
        print(ch, ord(ch))
elif choice == "20":
    if not s:
        print("Empty string.")
    else:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        most = max(freq.items(), key=lambda x: x[1])
        print("Most frequent character:", most)
else:
    print("Choice not implemented in this simple demo.")
