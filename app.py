import streamlit as st

import requests

st.title("YouTube Playlist Length Calculator")

# Get the URL of the YouTube playlist

playlist_url = st.text_input("Enter the URL of the YouTube playlist:")

# Extract the playlist ID from the URL

playlist_id = playlist_url.split("=")[1]

# Use the Invidious API to get information about the playlist

response = requests.get(f"https://vid.priv.au/api/v1/playlists/{playlist_id}")

# Extract the total length of the playlist from the API response

total_length = 0

for video in response.json()["videos"]:

    total_length += video["lengthSeconds"]

# Convert the total length from seconds to minutes

total_length_minutes = total_length / 60

# Display the total length of the playlist

st.write(f"Total length of playlist: {total_length_minutes:.2f} minutes")

