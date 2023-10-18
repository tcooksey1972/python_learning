import sys
import json
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

print(sys.executable)

# 1. Data Loading
with open('preprocessed_movies.json', 'r') as f:
    movies = json.load(f)

# 4. Feature Extraction
numeric_features = ['rating', 'votes', 'year', 'director_popularity', 'popularity_score']
text_features = ['title', 'director', 'actors']

# 5. Feature Engineering
current_year = 2023
for movie in movies:
    if movie['year']:
        movie['movie_age'] = current_year - movie['year']
    else:
        movie['movie_age'] = None

star_directors = ["Christopher Nolan", "Martin Scorsese", "Quentin Tarantino"]
for movie in movies:
    movie['is_star_director'] = movie['director'] in star_directors

print("\n--- Movies after Feature Engineering ---\n")
for movie in movies:
    print(f"Title: {movie['title']}")
    print(f"Movie Age: {movie['movie_age']}")
    print(f"Is Star Director: {movie['is_star_director']}\n")

# 6. Normalization & Standardization
data = [[movie[feature] for feature in numeric_features] for movie in movies if movie['year']]
if not data:
    print("No movies with release years found!")
else:
    data = StandardScaler().fit_transform(data)

    for i, movie in enumerate([movie for movie in movies if movie['year']]):
        for j, feature in enumerate(numeric_features):
            movie[f"{feature}_standardized"] = data[i][j]

    print("\n--- Movies after Normalization & Standardization ---\n")
    for movie in movies:
        print(f"Title: {movie['title']}")
        for feature in numeric_features:
            print(f"{feature} (Standardized): {movie.get(f'{feature}_standardized', 'N/A')}")
        print("\n")

# 7. Text Preprocessing
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform([movie['title'] for movie in movies])
tfidf_feature_names = tfidf.get_feature_names_out()

print("\n--- Top TF-IDF Features for Movie Titles ---\n")
print(tfidf_feature_names[:50])

# Save the processed data
with open('processed_movies.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(movies, jsonfile, ensure_ascii=False, indent=4)
