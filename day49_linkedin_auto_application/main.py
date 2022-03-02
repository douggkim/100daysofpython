from selenium import webdriver
from infinite_scroll import Infinite_Scroll
import pyautogui
import time

# TODO 0 : load the confidentials
with open("CONFIG.txt") as file:
    login_id = file.readline().strip()
    login_pw = file.readline().strip()

# TODO 1 : Set up selenium
target_url = "https://www.linkedin.com/jobs/search/?f_E=1&geoId=102095887&keywords=business%20analyst&location" \
             "=California%2C%20United%20States&sortBy=R "
chrome_driver_path = "C:/Users/slaki/OneDrive/문서/dev/100daysofpython/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# TODO 2 : login to linkedin
driver.get(target_url)
# click the login button
login_button = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]")
login_button.click()

# input the login info
email_input = driver.find_element_by_xpath("//*[@id='username']")
email_input.send_keys(login_id)

pw_input = driver.find_element_by_xpath("//*[@id='password']")
pw_input.send_keys(login_pw)

# press the login button
login_confirm_button = driver.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button")
login_confirm_button.click()


# TODO 3 : enter the job search page
def collect_info_each_page():
    job_titles = driver.find_elements_by_css_selector(
        ".disabled.ember-view.job-card-container__link.job-card-list__title")
    for index in range(len(job_titles)):
        job_titles[index] = job_titles[index].text
        print(job_titles[index])
    company_names = driver.find_elements_by_css_selector(
        ".job-card-container__link.job-card-container__company-name.ember-view")
    for index in range(len(company_names)):
        company_names[index] = company_names[index].text
        print(company_names[index])
    location_list = driver.find_elements_by_css_selector(".job-card-container__metadata-item")
    location_list = [location.text for location in location_list]
    new_location_list = [None] * len(location_list)
    for index in range(len(location_list)):
        if location_list[index] == "On-site" or location_list[index] == "Remote":
            location = f"{location_list[index - 1]} ({location_list[index]})"
            print(location)
            new_location_list[index - 1] = location
        else:
            new_location_list[index] = location_list[index]
    new_location_list = [location for location in new_location_list if location is not None]
    print(new_location_list)
    job_dict = {}
    for index in range(len(company_names)):
        job_dict[index] = {
            "Company": company_names[index],
            "Position": job_titles[index],
            "Location": new_location_list[index],
        }
    print(job_dict)



pyautogui.moveTo(500, 540)
print
while not driver.find_elements_by_css_selector(".artdeco-pagination__indicator.artdeco-pagination__indicator--number.ember-view button"):
    collect_info_each_page()
    pyautogui.scroll(-1500)
    print(driver.find_elements_by_css_selector(".artdeco-pagination__indicator.artdeco-pagination__indicator--number.ember-view"))

driver.find_elements_by_css_selector(".artdeco-pagination__indicator.artdeco-pagination__indicator--number.ember-view")[0].click()

# infinite_scroll = Infinite_Scroll(driver=driver)

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     # Wait to load page
#     collect_info_each_page()
#     time.sleep(SCROLL_PAUSE_TIME)
#
#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
#     # infinite_scroll.exec()

# while driver.find_element_by_css_selector('.jobs-search__left-rail'):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     collect_info_each_page()
#     Divs = driver.find_element_by_css_selector('.jobs-search__left-rail').text
#     if 'End of Results' in Divs:
#         print('end')
#         break
#     else:
#         continue



