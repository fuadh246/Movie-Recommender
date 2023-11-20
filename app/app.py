import streamlit as st
import pickle
import pandas as pd
import requests


def recommend(movie):
    recommended_movies = []
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


movies_dict = pickle.load(open('app/movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('app/similarity.pkl', 'rb'))
st.title('Hey')
selected_movie_name = st.selectbox(
    'Please enter a movie you like',
    movies['title']
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
