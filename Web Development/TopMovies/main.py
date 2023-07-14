from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-coming-of-age-movies/")
website_html = response.text

soup = BeautifulSoup(website_html,"html.parser")

all_movies = soup.find_all(name="h2")
print(all_movies)

movie_titles = [movie.getText() for movie in all_movies] 
# [::-1] reverses a list
movies = movie_titles[::-1]

with open ("movies.txt",mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")