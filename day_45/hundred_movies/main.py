import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# making soup
response = requests.get(URL).text
soup = BeautifulSoup(response, "html.parser")
movie_tags = soup.find_all(name="h3", class_="title")

# listing movie names
movies = []
for movie in movie_tags:
        movies.append(movie.get_text())

# adding to file in reverse order using string slice
with open("movies.txt", 'a') as movie_file:
    for movie in movies[::-1]:
        movie_file.write(f"{movie}\n")