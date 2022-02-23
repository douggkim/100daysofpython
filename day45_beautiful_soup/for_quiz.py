from bs4 import BeautifulSoup

with open("quiz.html") as file:
    html_text = file.read()

soup = BeautifulSoup(html_text, "html.parser")
print(soup.find("input").get("maxlength"))
