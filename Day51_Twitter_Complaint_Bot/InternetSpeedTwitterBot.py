from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.down = None
        self.up = None
        self.tweet_result = False

    def get_internet_speed(self):
        '''Get the internet speed and return them as integers'''
        self.driver.get("https://www.speedtest.net/")
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')))

        speed_measure_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        speed_measure_button.click()

        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH,
                                                                         '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/a')))
        download_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        upload_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')

        self.down = float(download_speed.text)
        self.up = float(upload_speed.text)

        return self.down, self.up

    def tweet_at_provider(self, twitter_id: str, twitter_pw: str, twitter_name: str, msg: str) -> bool:
        """Login to tweeter and enter the inputted message"""
        # TODO 3 : Login to twitter
        # Enter Twitter login page and wait for it to load
        self.driver.get("https://twitter.com/i/flow/login")
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                        "//*[@id='layers']/div/div/div/div/div/div/div["
                                                                        "2]/div[2]/div/div/div[2]/div[2]/div["
                                                                        "1]/div/div/div[5]/label/div/div[2]/div/input")))

        # Input the Email and confirm
        email_input = self.driver.find_element_by_xpath(
            "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div["
            "2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input")
        email_input.send_keys(twitter_id)

        email_confirm_button = self.driver.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div["
                                                                 "2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span")
        email_confirm_button.click()

        # Moved to the PW Page
        # input the Password and login
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "//*[@id='layers']/div/div/div/div/div/div/div["
                                                                            "2]/div[2]/div/div/div[2]/div[2]/div["
                                                                            "1]/div/div/div[3]/div/label/div/div[2]/div["
                                                                            "1]/input")))
            pw_input = self.driver.find_element_by_xpath(
                "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div["
                "2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")

            pw_input.send_keys(twitter_pw)
            pw_confirm_button = self.driver.find_element_by_xpath(
                "//*[@id='layers']/div/div/div/div/div/div/div[2]/div["
                "2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/span/span")
            pw_confirm_button.click()
        except:
            id_input = self.driver.find_element_by_xpath(
                "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div["
                "2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input")
            id_input.send_keys(twitter_name)
            id_confirm_button = self.driver.find_element_by_xpath(
                "//*[@id='layers']/div/div/div/div/div/div/div[2]/div["
                "2]/div/div/div[2]/div[2]/div[2]/div/div/span/span")
            id_confirm_button.click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
                By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div['
                          '1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
            pw_input = self.driver.find_element_by_xpath(
                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                '3]/div/label/div/div[2]/div[1]/input')

            pw_input.send_keys(twitter_pw)
            pw_confirm_button = self.driver.find_element_by_xpath(
                "//*[@id='layers']/div/div/div/div/div/div/div[2]/div["
                "2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/span/span")
            pw_confirm_button.click()

        # Click the tweeter input
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                        "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")))
        tweet_input_toggle = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
        tweet_input_toggle.click()
        tweet_input_toggle.send_keys(msg)

        tweet_write_button = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div["
            "1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div["
            "3]/div/div/div[2]/div[3]/div/span")
        tweet_write_button.click()
        self.tweet_result = True

        return self.tweet_result
