import pandas as pd

ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

merged_df = pd.merge(ratings_df, movies_df, on='movieId')
merged_df['genres'] = merged_df['genres'].str.split('|')

merged_df = merged_df[merged_df['genres'].apply(lambda x: x != ['(no genres listed)'] and x != [])]

all_genres = set(genre for genres in merged_df['genres'] for genre in genres)
print("Available genres:")
print(", ".join(sorted(all_genres)))

def popularity_based_recommender(genre, min_ratings_threshold, num_recommendations):
    genre_filtered = merged_df[merged_df['genres'].apply(lambda x: genre in x)]
    print(f"Total movies in genre '{genre}': {len(genre_filtered)}")
    
    movie_ratings_count = genre_filtered.groupby('movieId').size()

    filtered_movies = genre_filtered[genre_filtered['movieId'].isin(
        movie_ratings_count[movie_ratings_count >= min_ratings_threshold].index)]
    
    top_movies = filtered_movies.groupby(['movieId', 'title']).agg({'rating': 'mean'}).reset_index()
    top_movies = top_movies.sort_values(by='rating', ascending=False)
    
    top_movies = top_movies.reset_index(drop=True)
    top_movies.index += 1  # Start the index from 1 instead of 0
    
    return top_movies.head(num_recommendations)

print("\nPlease choose a genre from the list above.")

genre = input("Enter the genre: ")
min_ratings_threshold = int(input("Enter the minimum ratings threshold: "))
num_recommendations = int(input("Enter the number of recommendations: "))

popularity_recommendations = popularity_based_recommender(genre, min_ratings_threshold, num_recommendations)
print("\nTop {} movies in the genre '{}':".format(num_recommendations, genre))
print(popularity_recommendations)
