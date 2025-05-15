import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Sample user-movie ratings data
data = {
    'User': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Carol', 'Carol', 'Dave', 'Dave', 'Eve'],
    'Movie': ['Titanic', 'Avatar', 'Inception', 'Titanic', 'Inception', 'Avatar', 'Avengers', 'Avengers', 'Inception', 'Titanic'],
    'Rating': [5, 4, 5, 5, 4, 4, 5, 3, 5, 4]
}
df = pd.DataFrame(data)

# Create user-item matrix
user_movie_matrix = df.pivot_table(index='User', columns='Movie', values='Rating').fillna(0)

# Normalize ratings (optional but improves cosine similarity)
scaler = StandardScaler()
normalized_matrix = scaler.fit_transform(user_movie_matrix)

# Compute similarity matrix
similarity = cosine_similarity(normalized_matrix)
similarity_df = pd.DataFrame(similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

ef get_recommendations(target_user, top_n=2):
    if target_user not in similarity_df.index:
        return []

    # Get similarity scores for the target user
    sim_scores = similarity_df[target_user].drop(index=target_user)
    top_users = sim_scores.sort_values(ascending=False).head(top_n).index

    # Get movies rated by similar users but not yet watched by target user
    target_movies = set(user_movie_matrix.loc[target_user][user_movie_matrix.loc[target_user] > 0].index)
    similar_user_movies = user_movie_matrix.loc[top_users]
    # Weighted movie scores
    movie_scores = {}
    for user in top_users:
        for movie, rating in user_movie_matrix.loc[user].items():
            if movie not in target_movies and rating > 0:
                movie_scores[movie] = movie_scores.get(movie, 0) + rating * sim_scores[user]

    # Sort recommendations
    sorted_recs = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)
    return [movie for movie, _ in sorted_recs]

# Example usage
user_input = 'Alice'
recommendations = get_recommendations(user_input)
print(f"Recommended movies for {user_input}: {recommendations}")



