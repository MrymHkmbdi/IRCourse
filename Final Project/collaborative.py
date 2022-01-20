import pandas as pd
import numpy as np
import operator
from sklearn.metrics.pairwise import cosine_similarity

anime = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/irm-final-dataset/anime.csv")
rating = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/irm-final-dataset/rating.csv")
