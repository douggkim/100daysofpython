from selenium import webdriver
import keyboard
import threading
import time

# TODO 0 : Set up selenium
target_url = "https://orteil.dashnet.org/cookieclicker/"
chrome_driver_path = "C:/Users/slaki/OneDrive/문서/dev/100daysofpython/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
game_on = True


# TODO 1 : Click the cookie
driver.get(target_url)
time.sleep(8)
cookie = driver.find_element_by_xpath("//*[@id='bigCookie']")


# //*[@id="product1"]/div[3]
# //*[@id="product0"]/div[3]
# //*[@id="product2"]/div[3] .product unlocked enabled content

# TODO 2 : Schedule a purchaser
def purchase_items():
    # Purchase the most expensive item every 5 seconds
    global game_on
    # Stop the scheduler after five minutes
    if not game_on:
        print("Five Minutes have passed : Scheduler Finished")
    else:
        threading.Timer(5.0, purchase_items).start()
        print("purchase triggered")
        # collect the price information
        price_element_list = driver.find_elements_by_css_selector(".product.unlocked.enabled .content .price")
        price_list = [price_element.text.replace(",", "") for price_element in price_element_list]
        for index in range(len(price_list)):
            if price_list[index] != "":
                price_list[index] = float(price_list[index])
        print(price_list)
        # If there are things available for purchase, purchase the item
        if price_list:
            # see how many cookies are collected
            number_of_cookies = driver.find_element_by_xpath("// *[ @ id = 'cookies']").text
            number_of_cookies = number_of_cookies.split(" ")[0].replace(",", "")
            if number_of_cookies:
                print(int(number_of_cookies))
                # get the index of the most expensive item that can be purchased at the moment
                largest_index = 0
                for index in range(len(price_list)):
                    if price_list[index] <= int(number_of_cookies):
                        largest_index = index

            print(largest_index)
            driver.find_element_by_xpath(f"//*[@id='product{largest_index}']").click()

# trigger the batch job
purchase_items()


# TODO 3 : Make the project run for 5 minutes
def check_five_minutes():
    global game_on
    print("Five Minutes have passed: Clicking Finished")
    game_on = False


threading.Timer(5*60, check_five_minutes).start()
# TODO 4 : Click the cookie!
while game_on:
    cookie.click()
    if keyboard.is_pressed('q'):
        break
