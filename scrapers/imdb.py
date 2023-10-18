import requests
from bs4 import BeautifulSoup
import json

# Get top 50 movies of 2023 from IMDb
URL = 'https://www.imdb.com/search/title/?year=2023&sort=num_votes,desc&page=1'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')
movies = soup.find_all('div', class_='lister-item-content')

top_movies = []
for movie in movies:
    title = movie.find('a').get_text()
    rating = float(movie.find('div', class_='inline-block ratings-imdb-rating').get('data-value'))
    votes = movie.find('span', attrs={"name": "nv"}).get_text()

    # Extracting the director and actors
    credits = movie.find('p', class_='').get_text(strip=True)
    try:
        director, actors = credits.split('|')
        director = director.split(':')[1].strip()
        actors = actors.split(':')[1].strip().split(',')
    except ValueError:
        # Handle case where either director or actors may not be present
        director = credits if 'Director' in credits else ''
        actors = credits if 'Stars' in credits else ''

    top_movies.append({'title': title, 'rating': rating, 'votes': votes, 'director': director, 'actors': actors})

    # Print to the screen
    print(f"Title: {title}, Rating: {rating}, Votes: {votes}, Director: {director}, Actors: {actors}")

# Save the list to a JSON file
with open('top_movies.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(top_movies, jsonfile, ensure_ascii=False, indent=4)
