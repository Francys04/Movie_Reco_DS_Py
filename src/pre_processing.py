"""This imports the NumPy library and assigns it the alias 'np.' NumPy is a fundamental library for numerical and
mathematical operations in Python. It provides support for arrays and matrices, essential for scientific computing."""
import numpy as np

"""This imports the Pandas library and assigns it the alias 'pd.' Pandas is a powerful library for data manipulation
 and analysis. It provides data structures like DataFrames and Series, making it easier to work with structured data."""
import pandas as pd

"""This appears to import a specific variable or data from a 'movie_data' module located in the 'src.config' package. 
It's common to store configuration data or constants in separate modules for easy access and maintenance."""
from src.config import movie_data

"""This imports the 'difflib' module, which provides tools for comparing sequences, including strings. 
It can be useful for finding similarities or differences between strings."""
import difflib
"""This imports the 'TfidfVectorizer' class from the 'sklearn.feature_extraction.text' module. 
TfidfVectorizer is a technique used for text feature extraction in natural language processing (NLP) and 
information retrieval. It converts text data into numerical vectors based on the Term Frequency-Inverse 
Document Frequency (TF-IDF) values."""
from sklearn.feature_extraction.text import TfidfVectorizer
"""This imports the 'cosine_similarity' function from the 'sklearn.metrics.pairwise' module. 
Cosine similarity is a metric used to measure the similarity between two non-zero vectors in an inner product space. 
It is commonly used in information retrieval and recommendation systems to assess the similarity between documents or 
items based on their features."""
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

combined_features = movie_data['genres'] + ' ' + movie_data['keywords'] + ' ' + movie_data['tagline'] + ' ' + \
                    movie_data['cast'] + \
                    ' ' + movie_data['director']
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
