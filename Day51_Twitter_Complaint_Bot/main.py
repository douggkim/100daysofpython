import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

# TODO 1 : Set up needed configurations
PROMISED_UP = 500
PROMISED_DOWN = 500
CHROME_DRIVER_PATH = "C:/Users/slaki/OneDrive/문서/dev/100daysofpython/chromedriver_win32/chromedriver.exe"
TARGET_URL = ["https://twitter.com/i/flow/login", "https://www.speedtest.net/"]

with open("twitter_CONFIG.txt") as file:
    TWITTER_ID = file.readline().strip()
    TWITTER_PW = file.readline().strip()
    TWITTER_NAME = "Doug90180618"

# TODO 2 : call the InternetSpeedTwitterBot
ist = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

# TODO 3 : Get the internet speed
speed_tuple = ist.get_internet_speed()

# TODO 5 : Tweet if the internet speed is lower than the promised speed
msg = f"My download speed is {speed_tuple[0]}MB/s / My Upload speed is {speed_tuple[1]}MB/s!"
ist.tweet_at_provider(twitter_id=TWITTER_ID, twitter_pw=TWITTER_PW, twitter_name=TWITTER_NAME, msg=msg)
if ist.tweet_result:
    print("The job is done.")
