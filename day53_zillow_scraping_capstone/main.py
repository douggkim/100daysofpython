from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import lxml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TODO 0 : Set the environment
CHROME_DRIVER_PATH = "C:/Users/slaki/OneDrive/문서/dev/100daysofpython/chromedriver_win32/chromedriver.exe"
ZILLOW_URL = "https://www.zillow.com/los-angeles-ca/rentals/2-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
             "%22usersSearchTerm%22%3A%22Los%20Angeles%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-118" \
             ".88101747548623%2C%22east%22%3A-118.26097658193154%2C%22south%22%3A33.716591305934905%2C%22north%22" \
             "%3A34.38581368707091%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6" \
             "%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22" \
             "%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C" \
             "%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B" \
             "%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse" \
             "%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B" \
             "%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D "

GOOGLE_SURVEY_URL = "https://forms.gle/A6m34eNWQFdUCNms8"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/98.0.4758.102 Safari/537.36",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
           "Connection": "close", "Upgrade-Insecure-Requests": "1"
           }

# TODO 1 : Scrape the Zillow site : get the price, address, url for each location
zillow_response = requests.get(ZILLOW_URL, headers=headers).text
print(zillow_response)
soup = BeautifulSoup(zillow_response, parser="lxml", features="lxml")
price_list = soup.find_all(class_="list-card-price")

price_list = [price.text for price in price_list]
print(price_list)

address_list = soup.find_all(class_="list-card-addr")
address_list = [address.text for address in address_list]
print(address_list)

url_list = soup.find_all(class_="list-card-link list-card-link-top-margin")
url_list = [url['href'] for url in url_list]
print(url_list)

print(f"Are the number of lists all same? {len(price_list) == len(address_list) and len(address_list) == len(url_list)}")

# TODO 2 : setup selenium

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(GOOGLE_SURVEY_URL)
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                           '//*[@id="mG61Hd"]/div[2]/div/div[2]/div['
                                                           '1]/div/div/div[2]/div/div[1]/div/div['
                                                           '1]/input')))


for index in range(len(address_list)):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div['
                                                               '1]/div/div/div[2]/div/div[1]/div/div['
                                                               '1]/input')))
    address_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    url_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    send_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address_input.click()
    address_input.send_keys(address_list[index])
    price_input.click()
    price_input.send_keys(price_list[index])
    url_input.click()
    url_input.send_keys(url_list[index])
    send_button.click()

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                               '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
    resend_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    resend_button.click()
