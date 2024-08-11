import streamlit as st
from PIL import Image
from models.model import find_similar_movies, search, visualize_movie_ratings
import pandas as pd


st.title(":red[Notflix]")

# Input form for user parameters
user_input = st.text_input("Search for any movie:")

# Store the selected movie and search results in session state
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None
if "search_results" not in st.session_state:
    st.session_state.search_results = []

if st.button("Search"):
    response = search(user_input)
    st.session_state.search_results = response

# Display search results
if len(st.session_state.search_results) > 0:
    st.text("Search Results:")
    for _, result in st.session_state.search_results.iterrows():
        if st.button(result["title"], key=result["movieId"]):
            st.session_state.selected_movie = result

# Display the selected movie
if st.session_state.selected_movie is not None and not st.session_state.selected_movie.empty:
    selected_movie = st.session_state.selected_movie.to_dict()
    st.write(f"Selected Movie: {selected_movie['title']}")
    
    # Display the rating histogram
    img_data = visualize_movie_ratings(selected_movie["movieId"])
    img = Image.open(img_data)
    st.image(img, caption="Rating Distribution", use_column_width=True)
    
    # Display recommendations for the selected movie
    results = find_similar_movies(selected_movie["movieId"])
    st.header("You should watch...")
    st.dataframe(results[["title", "genres"]], hide_index=True )