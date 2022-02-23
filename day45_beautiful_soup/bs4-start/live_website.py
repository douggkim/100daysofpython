from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text
# TODO 1 : get bs4 to read the page
soup = BeautifulSoup(yc_web_page, "html.parser")

# TODO 2 : get the text of all the titles
soup_titlelink = soup.find_all(class_="titlelink")
print(soup_titlelink[0].getText())
soup_titlelink_str = [ _.string for _ in soup_titlelink]
print(soup_titlelink_str[0])

# TODO 3 : get the list of upvotes and links
# get urls
soup_titlelink_url = [link.get("href") for link in soup_titlelink]
#  get upvotes
soup_score_html = soup.find_all(class_="score")
soup_upvote = [a.get_text() for a in soup_score_html]
soup_upvote = [int(point.split(" ")[0]) for point in soup_upvote]
largest_upvote_idx = soup_upvote.index(max(soup_upvote))
# article with largest votes
print(f"Title: {soup_titlelink_str[largest_upvote_idx]}")
print(f"URL : {soup_titlelink_url[largest_upvote_idx]}")
print(f"Upvotes : {soup_upvote[largest_upvote_idx]}")


