from selenium import webdriver
import keyboard
import threading
import time

# TODO 0 : Set up selenium
target_url = "https://orteil.dashnet.org/cookieclicker/"
chrome_driver_path = "C:/Users/slaki/OneDrive/문서/dev/100daysofpython/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# TODO 1 : Click the cookie
driver.get(target_url)
time.sleep(8)
cookie = driver.find_element_by_xpath("//*[@id='bigCookie']")


# //*[@id="product1"]/div[3]
# //*[@id="product0"]/div[3]
# //*[@id="product2"]/div[3] .product unlocked enabled content

# TODO 2 : Schedule a purchaser
def purchase_items():
    threading.Timer(5.0, purchase_items).start()
    print("purchase triggered")

    price_element_list = driver.find_elements_by_css_selector("product unlocked enabled price")
    price_list = [price_element.text for price_element in price_element_list]
    print(price_list)
    largest_index = price_list.index(max(price_list))
    print(largest_index)
    # driver.find_element_by_xpath(f"//*[@id='product{largest_index}']/div[3]").click()


purchase_items()

# TODO 3 : Click the cookie!

while True:
    cookie.click()
    if keyboard.is_pressed('q'):
        break
