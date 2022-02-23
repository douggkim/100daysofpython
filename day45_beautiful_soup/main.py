from bs4 import BeautifulSoup
import requests

# TODO 1 : get html text
response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text

# TODO 2 : get soup to read the data
soup = BeautifulSoup(response, "html.parser")

# TODO 3 : extract titles for the data
title_list = soup.find_all(class_="article-title-description__text")
title_list_str = [element.select(".title")[0].getText() for element in title_list]
# you can also print the list in reverse order with title_list_str = title_list_str[::-1]
title_list_str.reverse()

# TODO 4 : save titles as a file
with open("movies_list.txt", "w", encoding="utf-8") as file:
    for line in title_list_str:
        file.write(line+"\n")
        print(line)

