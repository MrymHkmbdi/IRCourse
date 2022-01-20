import pandas as pd
import numpy as np
import operator
from sklearn.metrics.pairwise import cosine_similarity

anime = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/irm-final-dataset/anime.csv")
rating = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/irm-final-dataset/rating.csv")

anime_ratings_frame = pd.DataFrame(rating.groupby('anime_id')['rating'].count())
anime_ratings_frame = anime_ratings_frame[anime_ratings_frame.rating >= 1000]

user_rating_counts_frame = pd.DataFrame(rating.groupby('user_id')['rating'].count())
user_rating_counts_frame = user_rating_counts_frame[user_rating_counts_frame.rating >= 200]

reduced_frame = rating[rating.anime_id.isin(anime_ratings_frame.index.tolist())]
reduced_frame = rating[rating.anime_id.isin(user_rating_counts_frame.index.tolist())]

reduced_frame = reduced_frame.replace(-1, np.nan)


