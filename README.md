## Movie Recommendation System 
### Introduction
- This code project implements a movie recommendation system using Python and various libraries for data manipulation, natural language processing (NLP), and machine learning. The system suggests similar movies to a user based on their favorite movie input.

### Prerequisites
1. Before running this code, ensure you have the following dependencies installed:

- Python (version 3)
- NumPy
- Pandas
- scikit-learn (sklearn)
- difflib
#### You can install these dependencies using pip:

`pip install numpy pandas scikit-learn difflib`
### Usage
- Clone the repository to your local machine:

`git clone https://github.com/Francys04/Movie_Reco_DS_Py`
### Navigate to the project directory:

Follow the on-screen instructions to input your favorite movie.

The system will suggest a list of similar movies based on your input.

### Data
- The code uses a dataset containing information about movies, including titles, genres, keywords, cast, and directors. This data is used to calculate movie similarity.

### Code Structure
`user-input.py`: The main script for running the recommendation system.
`src/config.py`: Configuration data for the project.
`src/pre_processing.py`: Pre-processing steps for data and similarity calculations.
#### How It Works
- The code loads movie data from the dataset.
- It selects relevant features for recommendation (genres, keywords, tagline, cast, director).
- Null values in these features are replaced with empty strings.
- Features are combined into feature vectors using TF-IDF (Term Frequency-Inverse Document Frequency) transformation.
- Cosine similarity is calculated between movies based on their feature vectors.
#### Users input their favorite movie.
- The code finds the closest match to the user's input.
- It suggests similar movies based on cosine similarity scores.
#### Limitations
- The quality of recommendations depends on the dataset's coverage and the features used.
- The code assumes user input matches a movie title in the dataset.
- Improving the recommendation algorithm or using user feedback could enhance the system.

#### Fig.1 Input: Iron Man and the result of the program
<img src="img/Iron man result movie.JPG">

