from selenium import webdriver
import time
chrome_driver_path = "C:/Users/slaki/OneDrive/문서/dev/100daysofpython/chromedriver_win32/chromedriver.exe"

# TODO 1 : initialize a chrome driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.com")
time.sleep(2)
# only closes the tab
driver.close()
# Closes the entire program
driver.quit()
