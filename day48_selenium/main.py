from selenium import webdriver
import time
chrome_driver_path = "C:/Users/slaki/OneDrive/문서/dev/100daysofpython/chromedriver_win32/chromedriver.exe"

# TODO 1 : initialize a chrome driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# TODO 2: Scrape the amazon_website
driver.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463")
#  by_id 도 가능
size = driver.find_elements_by_class_name("selection")
for _ in size:
    print(_.text)
# only closes the tab
driver.close()
# TODO 3: scrape python.org
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org")
search_bar = driver.find_element_by_name("q")
print(search_bar.get_attribute("placeholder"))
# find the python logo and get its size
logo = driver.find_element_by_class_name("python-logo")
print(logo.size)
# get the anchortag inside other elements
documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
print(documentation_link.text)
# use xpath
# Copy xpath : right click an element -> copy -> copy xpath
bug_link = driver.find_element_by_xpath("//*[@id='site-map']/div[2]/div/ul/li[3]/a")
print(bug_link.text)
# Closes the entire program
driver.quit()
