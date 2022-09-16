import streamlit as st
import pickle
import requests
import pandas as pd
import numpy as np

def fetch_poster(movie_id):
    #use your own API key generated from TMDB website
    url = "https://api.themoviedb.org/3/movie/{}?api_key=419142bffc27085692644b1877255b45".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path



def recommend (movie):
  idx=df[df['title']==movie].index[0]
  distances=sim_matrix[idx].argsort()[::-1][1:6]
  recommended_movie_names=list()
  recommended_movie_posters=list()
  for ind in distances:
    movie_id=df.iloc[ind]['id']
    recommended_movie_posters.append(fetch_poster(movie_id))
    recommended_movie_names.append(df.iloc[ind]['title'])
  return recommended_movie_names,recommended_movie_posters


st.header('Mimicing Netflix Now...')
movies_dict = pickle.load(open('models/movie_dict.pkl','rb'))
df=pd.DataFrame(movies_dict)
sim_matrix = pickle.load(open('models/m-m_sim.pkl','rb'))

movie_list = np.sort(np.array(df['title'].values))
d=np.array(['#Horror'])
movie_list=np.setdiff1d(movie_list,d)
selected_movie = st.selectbox(
    "Select a movie",
    movie_list
)

if st.button('Which movies should I watch next?'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5,gap='medium')
    with col1:
        st.write(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.write(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.write(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.write(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.write(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
