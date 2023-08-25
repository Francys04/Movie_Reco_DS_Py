import numpy as np
import pandas as pd
from src.config import movie_data
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

'''Loading the data'''
print(movie_data.head(3000))

# number of rows and columns in the dataframe
print(movie_data.shape)

# selecting the relevant feature for recommendation

selected_feature = ['genres', 'keywords', 'tagline', 'cast', 'director']
print(selected_feature)

# replacing the null values with null string

for feature in selected_feature:
    movie_data[feature] = movie_data[feature].fillna('')

# combining all the 5 selected features

combined_features = movie_data['genres']+' '+movie_data['keywords']+' '+movie_data['tagline']+' '+movie_data['cast']+\
                    ' '+movie_data['director']
print(combined_features)

# converting the text data in feature vectors with machine learning model

vectorizer = TfidfVectorizer()

feature_vectors = vectorizer.fit_transform(combined_features)
print(feature_vectors)

'''Cosine similarity'''
# similarity score using cosine similarity

similarity = cosine_similarity(feature_vectors)
print(similarity)

print(similarity.shape)


