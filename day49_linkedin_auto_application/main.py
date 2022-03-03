from selenium import webdriver
import datetime
import pyautogui
import pprint
import time
import pandas as pd
import os

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


# TODO 3 : A Function to Collect info from each page
def collect_info_each_page():
    # get the job titles
    job_titles = driver.find_elements_by_css_selector(
        ".disabled.ember-view.job-card-container__link.job-card-list__title")
    # for index in range(len(job_titles)):
    #     job_titles[index] = job_titles[index].text
    job_titles = [title.text for title in job_titles]
    # get the company names
    company_names = driver.find_elements_by_css_selector(
        ".job-card-container__link.job-card-container__company-name.ember-view")
    # for index in range(len(company_names)):
    #     company_names[index] = company_names[index].text
    company_names = [name.text for name in company_names]

    # get the location
    location_list = driver.find_elements_by_css_selector(".job-card-container__metadata-item")
    location_list = [location.text for location in location_list]

    # process exceptional cases (on-site, remote, hybrid jobs)
    new_location_list = [None] * len(location_list)
    for index in range(len(location_list)):
        if location_list[index] == "On-site" or location_list[index] == "Remote" or location_list[index] == "Hybrid":
            location = f"{location_list[index - 1]} ({location_list[index]})"
            new_location_list[index - 1] = location
        elif "benefit" in location_list[index]:
            pass
        else:
            new_location_list[index] = location_list[index]
    new_location_list = [location for location in new_location_list if location is not None]

    # combine the scraped data into a pandas DF
    job_dict = {}
    for index in range(len(new_location_list)):
        job_dict[index] = {
            "Company": company_names[index],
            "Position": job_titles[index],
            "Location": new_location_list[index],
        }
    pprint.pprint(job_dict)
    job_df = pd.DataFrame(job_dict).T

    file_name = datetime.datetime.now().strftime("%y%m%d")+"_job_listing.csv"
    job_df.to_csv(file_name, mode='a', header= not os.path.exists(file_name))

# TODO 4 : Scrape from each page
# move the mouse to the job listing part of the page
pyautogui.moveTo(500, 540)

# get the list of pagination buttons
button_list = driver.find_elements_by_css_selector(
    ".artdeco-pagination__indicator.artdeco-pagination__indicator--number.ember-view button")

# iterate and scrape each page
for num in range(len(button_list)):
    # have to scroll to the end of the page because the page is loaded as it scrolls to the bottom
    pyautogui.scroll(-4000)
    # wait until all the elements are loaded
    time.sleep(3)
    collect_info_each_page()
    # each element has different class names for each page, so the paginatino buttons should be newly loaded
    button_list = driver.find_elements_by_css_selector(
        ".artdeco-pagination__indicator.artdeco-pagination__indicator--number.ember-view button")
    if num != len(button_list) - 1:
        button_list[num + 1].click()
