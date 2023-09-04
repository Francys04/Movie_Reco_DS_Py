from src.pre_processing import movie_data, similarity
import difflib
import numpy as np
import pandas as pd

# getting the movie name from the user

movie_name = input(' Enter your favorite movie name: ')

'''ctreating a list with all the movie names given in the dataset '''

list_of_all_titles = movie_data['title'].tolist()

print(list_of_all_titles)

'''finding the close match for the movie name given by the user'''

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
print(find_close_match)

# close match movie for user input
close_match = find_close_match[0]
print(close_match)

# finding the index of the movie with title
index_of_the_movie = movie_data[movie_data.title == close_match]['index'].values[0]
print(index_of_the_movie)

# getting  a list of similar movies

similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)

print("similarity score length: ", len(similarity))

'''
sorting the movies based on their similarity score
'''
sorted_similar_movie = sorted(similarity_score, key=lambda x: x[1], reverse=True)
print(sorted_similar_movie)

# print the name of the similar movies based on the index
print('Movies suggested for you: \n')

i = 1

for movie in sorted_similar_movie:
    index = movie[0]
    titel_from_index = movie_data[movie_data.index == index]['title'].values[0]
    if i < 31:  # first 30 movies
        print(i, '.', titel_from_index) # formating the output
        i += 1

#%%
