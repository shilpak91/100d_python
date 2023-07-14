from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# import PrettyPrinter


CLIENT_ID = "98a743c51619412b937fdda410abee13"
CLIENT_SECRET = "7813876da98d4a309941d83fc662f593"
REDIRECT_URI = "https://open.spotify.com/"

scope = "playlist-modify-private"

song_website = "https://www.billboard.com/charts/hot-100/"
# date = input ("Which year do you want to travel > Type the date in this format YYYY-MM-DD:")

response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12",verify=False)
song_website_html = response.text
# print(song_website_html)

soup = BeautifulSoup(song_website_html,"html.parser")
top_songs = soup.select("li ul li h3")
top_song_artist = soup.select("li ul li span")
# print(top_songs[0])

song_titles = [song.getText().strip() for song in top_songs]
song_artist = [artist.getText().strip() for artist in top_song_artist][::7]
# print(song_titles)
# print(song_artist)

song_artist_dict = {}

for i in range(len(song_artist)):
    song_artist_dict[song_titles[i]]=song_artist[i]

print(song_artist_dict)

# with open ("text.txt",mode="w") as file:
#     file.write(f"{top_song_artist}")
# print("********************************************************************************")
# print(top_song_artist[0].h3.getText())
# print(top_song_artist[0].span.getText())

# top_songs_list = [tag.li.h3.getText() for tag in top_song_artist]
# print(top_songs_list)

# for i in top_song_artist:
#     print(i)

# # top_songs_list = {item.h3.getText():item.span.getText() for item in top_song_artist}
# print(top_songs_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="31DEWJBRIV4vpucdlfby23ZGSSDA", 
    )
)
# user_id = sp.current_user()["id"]
