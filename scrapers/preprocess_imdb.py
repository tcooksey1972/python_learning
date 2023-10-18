import json
import math
from collections import defaultdict

# 1. Data Loading
with open('top_movies.json', 'r') as f:
    movies = json.load(f)

# 2. Data Cleaning
# Convert 'votes' from strings with commas to integers
for movie in movies:
    movie['votes'] = int(movie['votes'].replace(',', ''))

# Director and Actor Extraction and Cleaning
directors_count = defaultdict(int)
for movie in movies:
    # Ensure actors are stripped of any whitespace
    movie['actors'] = [actor.strip() for actor in movie.get('actors', [])]
    directors_count[movie.get('director', '').strip()] += 1  # Count movies for each director

# 3. Feature Engineering
# Categorize movies based on their rating
for movie in movies:
    if movie['rating'] >= 8.5:
        movie['rating_category'] = 'High'
    elif movie['rating'] >= 7.5:
        movie['rating_category'] = 'Medium'
    else:
        movie['rating_category'] = 'Low'

    # Extract year from title and remove it
    if '(' in movie['title'] and ')' in movie['title']:
        year = movie['title'].split('(')[-1].split(')')[0]
        title_clean = movie['title'].replace(f"({year})", '').strip()
        movie['year'] = int(year)
        movie['title'] = title_clean
    else:
        movie['year'] = None

    # Star actors
    star_actors = ["Brad Pitt", "Meryl Streep", "Leonardo DiCaprio", "Cate Blanchett"]  # Example set of star actors
    movie['has_star_actor'] = any(actor in star_actors for actor in movie['actors'])

    # Director popularity
    movie['director_popularity'] = directors_count.get(movie.get('director', '').strip(), 0)

    # Compute the popularity score
    movie['popularity_score'] = movie['rating'] * math.log(movie['votes'])

# Print preprocessed data to the screen
for movie in movies:
    print(f"Title: {movie['title']}")
    print(f"Year: {movie['year']}")
    print(f"Rating: {movie['rating']}")
    print(f"Votes: {movie['votes']}")
    print(f"Rating Category: {movie['rating_category']}")
    print(f"Popularity Score: {movie['popularity_score']}")
    print(f"Director: {movie.get('director', 'N/A')}")
    print(f"Actors: {', '.join(movie.get('actors', []))}")
    print(f"Has Star Actor: {movie['has_star_actor']}")
    print(f"Director Popularity (Movies in Top List): {movie['director_popularity']}\n")

# Save the preprocessed data back to a new JSON file
with open('preprocessed_movies.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(movies, jsonfile, ensure_ascii=False, indent=4)
