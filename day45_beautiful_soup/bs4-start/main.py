from bs4 import BeautifulSoup

# import lxml
# DOCUMENTATION https://www.crummy.com/software/BeautifulSoup/bs4/doc/
with open("website.html", encoding="utf-8") as file:
    contents = file.read()

# TODO 1: parse html with bs4
# str: 대상 문서, parser: 뭘로 파싱할건지
# lxml: 다른 유형의 parser
soup = BeautifulSoup(contents, "html.parser")

# TODO 2: read the object soup
print(soup.title)
# tag의 이름
print(soup.title.name)
# tag의 내용물
print(soup.title.string)
# 전체 html
print(soup)
# html with indentation
print(soup.prettify())
# first anchor tag
print(soup.a)
# all the anchor tags
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
# print only text from the anchor tags
all_anchor_tags_string = [a.getText() for a in all_anchor_tags]
print(all_anchor_tags_string)
# print only href from the anchor tags
all_anchor_tags_url = [a.get("href") for a in all_anchor_tags]
print(all_anchor_tags_url)
# find a tag based on id
heading = soup.find(name="h1", id="name")
print(heading)
print(heading.get("id"))
# use class_ instead of class. (class is a reserved keyword)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))
# select one element among many -> a tag inside p tag
company_url = soup.select_one(selector="p a")
print(company_url)
# can select ids
name = soup.select_one(selector="#name")
print(name)
# select class
headings = soup.select(".heading")
print(headings)