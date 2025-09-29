# 39.	Store details of movies with title, year, and ratings in a nested dictionary.
# Answer:
# Build nested mapping movie->details.

n = int(input("How many movies? "))
movies = {}
for _ in range(n):
    title = input("Title: ")
    year = int(input("Year: "))
    rating = float(input("Rating: "))
    movies[title] = {"year": year, "rating": rating}
print("Movies dict:", movies)
