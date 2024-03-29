from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint



CLIENT_ID = "98a743c51619412b937fdda410abee13"
CLIENT_SECRET = "7813876da98d4a309941d83fc662f593"
REDIRECT_URI = "https://open.spotify.com/"

scope = "playlist-modify-private"

song_website = "https://www.billboard.com/charts/hot-100/"
date = input ("Which year do you want to travel > Type the date in this format YYYY-MM-DD:")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
song_website_html = response.text
# print(song_website_html)

soup = BeautifulSoup(song_website_html,"html.parser")
top_songs = soup.select("li ul li h3")
top_song_artist = soup.select("li ul li span")
# print(top_songs[0])

song_titles = [song.getText().strip() for song in top_songs]
song_artist = [artist.getText().strip() for artist in top_song_artist][::7]

song_artist_dict = {}

for i in range(len(song_artist)):
    song_artist_dict[song_titles[i]]=song_artist[i]

# print(song_artist_dict)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]

# print(user_id)

song_uri=[]
for (song , artist) in song_artist_dict.items():
    # print(song)
    # print(artist)
    try:
        result = sp.search(q=f"track:{song} artist:{artist}",limit=10,offset=0,type="track",market=None)
        song_uri.append(result["tracks"]["items"][0]["id"])
    except:
        pass

print(f"Number of songs found : {len(song_uri)}")

playlist = sp.user_playlist_create(user=user_id,name=f"{date} Billboard 100",public=False)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uri)
print(f"New playlist {date} Billoard 100 created on spotify")