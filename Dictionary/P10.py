# 10.	Add a new movie and director to a movie dictionary.
# Answer:
# Read existing movie:director pairs then add a new one.

pairs = input("Enter movie:director pairs comma separated: ")
movies = dict((p.split(':')[0].strip(), p.split(':')[1].strip()) for p in pairs.split(',') if p.strip())
movie = input("Enter new movie title: ")
director = input("Enter its director: ")
movies[movie] = director
print("Updated movies:", movies)
