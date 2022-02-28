from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# TODO 0 : Set up the driver
chrome_driver_path = "C:/Users/slaki/OneDrive/문서/dev/100daysofpython/chromedriver_win32/chromedriver.exe"
target_uri = "http://secure-retreat-92358.herokuapp.com/"

# TODO 1 : initialize a chrome driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(target_uri)

# TODO 2 : enter inputs
for num in range(1, 5):
    if num == 4:
        xpath = "/html/body/form/button"
        signup_button = driver.find_element_by_xpath(xpath)
        signup_button.click()
        break

    xpath = f"/html/body/form/input[{num}]"
    input_prompt = driver.find_element_by_xpath(xpath)
    input_prompt.send_keys("sdlkfsjlnw")
    if num == 3:
        input_prompt.send_keys("slakingexxx@naver.com")


driver.close()
