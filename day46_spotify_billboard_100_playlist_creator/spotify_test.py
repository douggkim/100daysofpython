import spotipy
import urllib.parse
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import pprint

with open("CONFIG.txt") as file:
    SPOTIFY_CLIENT_ID = file.readline().strip()
    SPOTIFY_CLIENT_TOKEN = file.readline().strip()
    SPOTIFY_REDIRECT_URI = "http://example.com"

# auth_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_TOKEN)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-public", client_id=SPOTIFY_CLIENT_ID, \
                                               client_secret=SPOTIFY_CLIENT_TOKEN, redirect_uri=SPOTIFY_REDIRECT_URI))

searched_result = sp.search(type="track", q="artist:mogwai")
pprint.pprint(searched_result["tracks"]["items"][0]["album"]["name"])
pprint.pprint(searched_result["tracks"]["items"][0]["album"]["artists"][0]["name"])
pprint.pprint(searched_result["tracks"]["items"][0]["album"]["id"])

sp.user_playlist_create(user="31ncn5mfydxigz3ze4pkjknxmvtu", name="test", public=True, collaborative=False, description='')
# pprint.pprint(searched_result["tracks"]["items"][0]["album"]["artists"][0]["name"])
# playlists = sp.user_playlists('spotify')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None
