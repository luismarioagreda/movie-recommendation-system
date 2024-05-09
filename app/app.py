from io import BytesIO

import requests
import streamlit as st
from PIL import Image

st.title(":red[Notflix]")

# Input form for user parameters
user_input = st.text_input("Search for any movie:")

# Store the selected movie and search results in session state
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None
if "search_results" not in st.session_state:
    st.session_state.search_results = []

# Send request to Flask API when button clicked
if st.button("Search"):
    response = requests.post("http://127.0.0.1:5000/search", json={"title": user_input})
    st.session_state.search_results = response.json()

# Display search results
if st.session_state.search_results:
    st.text("Search Results:")
    for result in st.session_state.search_results:
        if st.button(result["title"], key=result["movieId"]):
            st.session_state.selected_movie = result

# Display the selected movie
if st.session_state.selected_movie:
    selected_movie = st.session_state.selected_movie
    st.write(f"Selected Movie: {selected_movie['title']}")

    # Display the rating histogram
    response = requests.post(
        "http://127.0.0.1:5000/visualize",
        json={"movieId": selected_movie["movieId"]},
    )
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    st.image(img, caption="Rating Distribution", use_column_width=True)

    # Display recommendations for the selected movie
    response = requests.post(
        "http://127.0.0.1:5000/recommendations",
        json={"movieId": selected_movie["movieId"]},
    )
    results = response.json()

    st.header("You should watch...")
    for result in results:
        st.markdown(f'- {result["title"]}')
