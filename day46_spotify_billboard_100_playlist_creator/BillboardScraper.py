from bs4 import BeautifulSoup
import requests


class BillboardScraper:
    def __init__(self):
        self.billboard_base_url = "https://www.billboard.com/charts/hot-100/"

    def scrape_titles(self, target_date: str) -> list[str]:
        """scrape the list of song titles in the billboard top 100 list of the target date"""
        response = requests.get(url=self.billboard_base_url + target_date + "/").text
        soup = BeautifulSoup(response, "html.parser")
        raw_title_list = soup.find_all(class_="lrv-u-width-100p")
        title_list = [element.select("#title-of-a-story")[0].getText() for element in raw_title_list if
                      element.select("#title-of-a-story")][1:101]
        title_list = [element.replace("\n", "") for element in title_list]

        return title_list

    def scrape_artists(self, target_date: str) -> list[str]:
        """scrape the list of artists in the billboard top 100 list of the target date"""
        response = requests.get(url=self.billboard_base_url + target_date + "/").text
        soup = BeautifulSoup(response, "html.parser")
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

        return artist_list


