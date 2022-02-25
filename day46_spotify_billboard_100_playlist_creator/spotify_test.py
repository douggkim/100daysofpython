import spotipy
import urllib.parse
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import pprint
#
# with open("CONFIG.txt") as file:
#     SPOTIFY_CLIENT_ID = file.readline().strip()
#     SPOTIFY_CLIENT_TOKEN = file.readline().strip()
#     SPOTIFY_REDIRECT_URI = "http://example.com"
#

class spotifyManager:
    def __init__(self, directory: str):
        with open(directory) as file:
            self.SPOTIFY_CLIENT_ID = file.readline().strip()
            self.SPOTIFY_CLIENT_TOKEN = file.readline().strip()
            self.SPOTIFY_REDIRECT_URI = "http://example.com"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-public",
                                                            client_id=self.SPOTIFY_CLIENT_ID, \
                                                            client_secret=self.SPOTIFY_CLIENT_TOKEN,
                                                            redirect_uri=self.SPOTIFY_REDIRECT_URI))

    def search(self, track: str, artist: str) -> str:
        """search a track based with artist name and track name. return track ID"""
        try:
            search_result = self.sp.search(type="track", q=f"artist:{artist} track:{track}")
        except:
            pass
        else:
            track_name = search_result["tracks"]["items"][0]["name"]
            artist_name = search_result["tracks"]["items"][0]["album"]["artists"][0]["name"]
            track_id = search_result["tracks"]["items"][0]["id"]
            pprint.pprint(search_result)

            return track_id

    def create_playlist(self, user_id: str, playlist_name: str) -> str:
        """create a playlist and returns its playlist ID"""
        playlist_create_result = self.sp.user_playlist_create(user=user_id,
                                                         name=playlist_name,
                                                         public=True,
                                                         collaborative=False,
                                                         description='')
        created_playlist_id = playlist_create_result["id"]
        return created_playlist_id

    def add_items_to_playlist(self, playlist_id: str, track_id: list[str]) -> str:
        playlist_result = self.sp.playlist_add_items(playlist_id, track_id, position=None)
        return playlist_result

    # auth_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_TOKEN)


spotifymanager = spotifyManager("CONFIG.txt")
print(spotifymanager.search(track="mogwai fear satan", artist="mogwai"))
USER_ID = "31ncn5mfydxigz3ze4pkjknxmvtu"


# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-public", client_id=SPOTIFY_CLIENT_ID, \
#                                                client_secret=SPOTIFY_CLIENT_TOKEN, redirect_uri=SPOTIFY_REDIRECT_URI))
#
# search_result = sp.search(type="track", q="artist:mogwai")
# pprint.pprint(search_result)
# pprint.pprint(search_result["tracks"]["items"][0]["name"])
# pprint.pprint(search_result["tracks"]["items"][0]["album"]["artists"][0]["name"])
# track_id = search_result["tracks"]["items"][0]["id"]
# pprint.pprint(track_id)
# #
# # # create playlist
# playlist_create_result = sp.user_playlist_create(user="31ncn5mfydxigz3ze4pkjknxmvtu",
#                                                  name="test2",
#                                                  public=True,
#                                                  collaborative=False,
#                                                  description='')
# # # the id of the created playlist
# created_playlist_id = playlist_create_result["id"]
# print(created_playlist_id)
# # # query playlist Id
# # # playlists = sp.user_playlists("31ncn5mfydxigz3ze4pkjknxmvtu")
# # # print(playlists)
# # add items to playlist
# sp.playlist_add_items("1eyT3E65QzykRuKIhJOq5j", [track_id], position=None)
# pprint.pprint(searched_result["tracks"]["items"][0]["album"]["artists"][0]["name"])
# playlists = sp.user_playlists('spotify')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None
