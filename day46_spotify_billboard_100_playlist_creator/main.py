from bs4 import BeautifulSoup
import requests
import spotipy

# TODO 0 : get all the credentials
with open("CONFIG.txt") as file:
    SPOTIFY_CLIENT_ID = file.readline()
    SPOTIFY_CLIENT_TOKEN = file.readline()

# TODO 1 : ask user about the date they want to query
# date_to_query = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD")
billboard_base_url = "https://www.billboard.com/charts/hot-100/"

# TODO 2 : get the html from billboard
response = requests.get(url=billboard_base_url + "1992-08-04" + "/").text

# TODO 3 : parse the data to get title_list
soup = BeautifulSoup(response, "html.parser")
raw_title_list = soup.find_all(class_="lrv-u-width-100p")
title_list = [element.select("#title-of-a-story")[0].getText() for element in raw_title_list if
              element.select("#title-of-a-story")][1:101]
title_list = [element.replace("\n", "") for element in title_list]

# TODO 4 : parse the data to get artist_list
raw_artist_list = soup.find_all(True,
                                {"class": [
                                    "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max "
                                    "u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block "
                                    "a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only "
                                    "u-font-size-20@tablet",
                                    "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max "
                                    "u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block "
                                    "a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"]})
artist_list = [element.getText().replace("\n", "") for element in raw_artist_list]

# TODO 5 :


# print(artist_list)
# print(f"No. of artists : {len(artist_list)}")
#
# print(title_list)
# print(f"No. of titles : {len(title_list)}")
# title_list_str = [element.getText() for element in title_list]
# print(len(title_list_str))
