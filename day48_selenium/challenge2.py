from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/slaki/OneDrive/문서/dev/100daysofpython/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
number_of_articles = driver.find_element_by_xpath("//*[@id='articlecount']/a[1]")
number_of_articles_by_css = driver.find_element_by_css_selector("#articlecount a")

print(number_of_articles.text)
print(f"Found with xpath Selector : {number_of_articles.text}")
print(f"Found with CSS Selector : {number_of_articles_by_css.text}")

# click the element
# number_of_articles.click()

# find an element with "link_text"
all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# find the searchbar
search_bar = driver.find_element_by_name("search")
# input the keyword
search_bar.send_keys("python")
# you have to import a separate package to input a special key
search_bar.send_keys(Keys.ENTER)

driver.close()