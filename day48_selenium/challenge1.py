from selenium import webdriver

# TODO 1 : Set up selenium driver
chrome_driver_path = "C:/Users/slaki/OneDrive/문서/dev/100daysofpython/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://python.org")
# TODO 2: Scrape the calendar data
""" 
event_times = driver.find_elements_by_css_selector(".event-widget time")"
for time in event_times:
    print(time.text)"""
calendar_date = []
for i in range(1, 6):
    xpath = f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i}]/time"
    date = driver.find_element_by_xpath(xpath)
    calendar_date.append(date.text)
# TODO 3 : Scrape the calendar event name
""" 
events= driver.find_elements_by_css_selector(".event-widget li a")"
for event in events:
    print(event.text)"""
calendar_event = []
for i in range(1, 6):
    xpath = f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i}]/a"
    event_name = driver.find_element_by_xpath(xpath)
    calendar_event.append(event_name.text)

# TODO 4 : Create a dict with the events
calendar_dict = {}

for n in range(len(calendar_date)):
    calendar_dict[n] = {
        "date": calendar_date[n],
        "event": calendar_event[n]
    }


print(calendar_dict)

# TODO : Close the driver
driver.close()
