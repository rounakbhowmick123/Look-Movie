import pickle
import streamlit as st
import pandas as pd
import requests


# css markdown
def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             height : 100%;
             background-image: url("https://wallpaperaccess.com/full/3901966.jpg");
             width:100%;
             height:100%; 
             background-attachment: fixed;
             background-size: cover
             background-color: rgba(0, 0, 0, 0)

             height:100%;

        }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()


#css markdown
st.markdown("<h2 <b  style='text-align: center;font-color: purple;  font-family: Times New Roman, Times, serif; '> YOUR MOVIE RECOMENDER </b></h2>", unsafe_allow_html=True)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)   # API
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id   # To fetch posters
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))   # Loading the dumped dictionary
movies = pd.DataFrame(movies_dict)  # Creating a dataframe

similarity = pickle.load(open('similarity.pkl','rb'))


#st.title('Your Movie Recomender')

# Creating the select box
selected_movie = st.selectbox('Select your movie',movies['title'].values)

# Creating the Recomend button
if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])