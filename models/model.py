import io
import re

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("../data/movie.csv")
ratings = pd.read_csv("../data/rating.csv")


def clean_title(title):
    """
    Cleans the given title by removing any non-alphanumeric characters.

    Parameters:
    title (str): The title to be cleaned.

    Returns:
    str: The cleaned title.
    """
    return re.sub("[^a-zA-Z0-9 ]", "", title)


movies["clean_title"] = movies["title"].apply(clean_title)

vectorizer = TfidfVectorizer(ngram_range=(1, 2))
tfidf = vectorizer.fit_transform(movies["clean_title"])


def search(title: str) -> pd.DataFrame:
    """
    Search for movies based on the given title.

    Args:
        title (str): The title of the movie to search for.

    Returns:
        pd.DataFrame: A DataFrame containing the search results, sorted by similarity.
    """
    title = clean_title(title)
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = movies.iloc[indices].iloc[::-1]

    return results


def find_similar_movies(movie_id: int) -> pd.DataFrame:
    """
    Finds similar movies based on the given movie ID.

    Args:
        movie_id (int): The ID of the movie to find similar movies for.

    Returns:
        pd.DataFrame: A DataFrame containing the top 10 similar movies, along with their scores, titles, and genres.
    """

    similar_users = ratings[(ratings["movieId"] == movie_id) & (ratings["rating"] > 4)][
        "userId"
    ].unique()
    similar_user_recs = ratings[
        (ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)
    ]["movieId"]
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)

    similar_user_recs = similar_user_recs[similar_user_recs > 0.10]
    all_users = ratings[
        (ratings["movieId"].isin(similar_user_recs.index)) & (ratings["rating"] > 4)
    ]
    all_user_recs = all_users["movieId"].value_counts() / len(
        all_users["userId"].unique()
    )
    rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]

    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
    rec_percentages = rec_percentages.sort_values("score", ascending=False)
    return rec_percentages.head(10).merge(movies, left_index=True, right_on="movieId")[
        ["score", "title", "genres"]
    ]


def visualize_movie_ratings(movie_id):
    """
    Visualizes the distribution of ratings for a specified movie.

    Parameters:
    movie_id (int): The ID of the movie to visualize the ratings for.

    Returns:
    io.BytesIO: A buffer containing the image of the plot.
    """
    movie_ratings = ratings[ratings["movieId"] == movie_id][
        "rating"
    ]  # Filter the ratings for the specified movie

    # Visualize the distribution of ratings
    plt.figure(figsize=(8, 6))
    sns.histplot(data=movie_ratings, bins=10, kde=True)
    plt.title(
        f"Distribution of Ratings for {movies[movies['movieId'] == movie_id]['title'].values[0]}"
    )
    plt.xlabel("Rating")
    plt.ylabel("Count")

    # Save the plot as an image file
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)
    plt.close()

    return img_buffer
