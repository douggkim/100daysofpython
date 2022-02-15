import requests
import datetime

STOCK = "GOOGL"
COMPANY_NAME = "google"
ALPHA_URL = "https://www.alphavantage.co/query"

# date before yesterday
target_date = str(datetime.datetime.now() - datetime.timedelta(days=1)).split(" ")[0]
#  if it's tuesday/ monday/ sunday
if int(datetime.datetime.now().weekday()) == 6 or int(datetime.datetime.now().weekday()) <= 1:
    day_before_target_date = str(datetime.datetime.now() - datetime.timedelta(days=2)).split(" ")[0]



with open("CONFIG.txt") as file:
    ALPHA_API_KEY = file.readline().strip()

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "datatype": "json",
    "apikey": ALPHA_API_KEY,
}

alpha_response = requests.get(url=ALPHA_URL, params=alpha_parameters)
yesterday_price = alpha_response.json()["Time Series (Daily)"][day_before_target_date]["4. close"]
today_price = alpha_response.json()["Time Series (Daily)"][target_date]["4. close"]

print(f"Yesterday's Closing Price of {STOCK}: {today_price}\nToday's closing price of {STOCK}: {today_price}")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
