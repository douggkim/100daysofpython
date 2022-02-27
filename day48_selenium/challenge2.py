from selenium import webdriver

chrome_driver_path = "C:/Users/slaki/OneDrive/문서/dev/100daysofpython/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
number_of_articles = driver.find_element_by_xpath("//*[@id='articlecount']/a[1]")
number_of_articles_by_css = driver.find_element_by_css_selector("#articlecount a")

print(number_of_articles.text)
print(f"Found with xpath Selector : {number_of_articles.text}")
print(f"Found with CSS Selector : {number_of_articles_by_css.text}")


driver.close()