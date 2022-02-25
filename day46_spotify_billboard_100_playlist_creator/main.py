from bs4 import BeautifulSoup
from BillboardScraper import BillboardScraper
from SpotifyManager import spotifyManager
import requests

# TODO 0 : get all the credentials
with open("CONFIG.txt") as file:
    SPOTIFY_CLIENT_ID = file.readline().strip()
    SPOTIFY_CLIENT_TOKEN = file.readline().strip()
    USER_ID = file.readline().strip()
    SPOTIFY_REDIRECT_URI = "http://example.com"


# TODO 1 : ask user about the date they want to query
date_to_query = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD ")

# TODO 2 : scrape top 100 titles,artists from billboard
scraper = BillboardScraper()
title_list = scraper.scrape_titles(date_to_query)
print(f"titles_scraped : {len(title_list)}")
artist_list = scraper.scrape_artists(date_to_query)
print(f"artists_scraped : {len(artist_list)}")
# print(artist_list)
# print(range(len(artist_list)))
# song_dict = {}
# for i in range(len(artist_list)):
#     song_dict[artist_list[i]] = title_list[i]
#     print(f"{artist_list[i]}: {title_list[i]}")
# # song_dict = {artist_list[i]: title_list[i] for i in range(len(artist_list))}
# print(f"Number of songs scraped: {len(song_dict)}")

# TODO 3 : load spotify manager
spotifymanager = spotifyManager(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_TOKEN, SPOTIFY_REDIRECT_URI)

# TODO 4 : create a playlist=
playlist_id = spotifymanager.create_playlist(user_id=USER_ID, playlist_name=f"Billboard Top 100_{date_to_query}")

# TODO 5 : search songs on spotify
song_id_list = []
for song in range(len(artist_list)):
    track_id = spotifymanager.search(track=title_list[song], artist=artist_list[song])
    if track_id is None:
        continue
    else:
        song_id_list.append(track_id)
        print(f"{len(song_id_list)} / 100 songs added to playlist.")
print(f"Number of Songs found on Spotify: {len(song_id_list)}")

# TODO 6 : add_songs_to_the_playlist
print(spotifymanager.add_items_to_playlist(track_id=song_id_list, playlist_id=playlist_id))




