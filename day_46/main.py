from pprint import pprint
import requests
from bs4 import BeautifulSoup
import spotipy
import os
from dotenv import load_dotenv


########## BILLBOARD ##########

# getting the html from billboard
date = input("Turn back time to (YYYY-MM-DD): ")
BILLBOARD = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(BILLBOARD)
billboard_html = response.text
# print(billboard_html)

# making soup and a list of top 100 songs
soup = BeautifulSoup(billboard_html, "html.parser")
# print(soup.prettify())
song_tags = soup.select("li ul li h3")
song_names = [tag.get_text().strip() for tag in song_tags]


########## SPOTIFY and SPOTIPY ##########
load_dotenv()
# Spotify credentials from .env
SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI  = "http://example.com"

spotify = spotipy.Spotify(
        auth_manager=spotipy.oauth2.SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="playlist-modify-private",
    ))


user_id = spotify.me()['id']

########## SPOTIPY SONG URIs##########

song_uris=[]
year = date.split('-')[0]
for song in song_names:
    song_object = spotify.search(f"track:{song} year:{year}", type="track")

    try:
        track_uri = song_object["tracks"]["items"][0]["uri"]
        song_uris.append(track_uri)
    except IndexError:
        print(f"{song} not found in Spotify. Skipped.")

########## CREATING PLAYLIST ##########
playlist_name = f"{date} Billboard 100"

playlist_id = spotify.user_playlist_create(user=user_id, name=playlist_name, public=False, collaborative=False, description='Created using Music Time Machine 💦')['id']

########## ADDING SONGS ##########

spotify. user_playlist_add_tracks(
    user = user_id, 
    playlist_id = playlist_id, 
    tracks = song_uris
    )
print("CHECK YOUR LIBRARY, BABE ❤️")