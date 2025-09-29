# 24.	Verify if "Titanic" exists in a movie dictionary.
# Answer:
# Check for key 'Titanic'.

pairs = input("Enter movie:director pairs comma separated: ")
movies = dict((p.split(':')[0].strip(), p.split(':')[1].strip()) for p in pairs.split(',') if p.strip())
print("Titanic present?", "Titanic" in movies)
