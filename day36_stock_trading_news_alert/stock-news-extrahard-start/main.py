import requests
import datetime

STOCK = "GOOGL"
COMPANY_NAME = "google"
ALPHA_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"
with open("CONFIG.txt") as file:
    ALPHA_API_KEY = file.readline().strip()
    NEWS_API_KEY = file.readline().strip()

# date before yesterday

#  if it's  monday/ sunday don't do anything
if int(datetime.datetime.now().weekday()) == 6 or int(datetime.datetime.now().weekday()) == 0:
    pass
elif int(datetime.datetime.now().weekday()) == 1:
    target_date = str(datetime.datetime.now() - datetime.timedelta(days=1)).split(" ")[0]
    day_before_target_date = str(datetime.datetime.now() - datetime.timedelta(days=4)).split(" ")[0]
else:
    target_date = str(datetime.datetime.now() - datetime.timedelta(days=1)).split(" ")[0]
    day_before_target_date = str(datetime.datetime.now() - datetime.timedelta(days=2)).split(" ")[0]

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "datatype": "json",
    "apikey": ALPHA_API_KEY,
}

news_parameters = {
    "q": COMPANY_NAME,
    "from": day_before_target_date,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY,
    "pageSize": 5,
    "page": 1

}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_response = requests.get(url=ALPHA_URL, params=alpha_parameters)
yesterday_price = float(alpha_response.json()["Time Series (Daily)"][day_before_target_date]["4. close"])
today_price = float(alpha_response.json()["Time Series (Daily)"][target_date]["4. close"])
price_diff = yesterday_price - today_price
change_percentage = abs(price_diff / yesterday_price) * 100
print(f"Yesterday's Closing Price of {STOCK}: {yesterday_price}\nToday's closing price of {STOCK}: {today_price}")

print(yesterday_price)
print(abs(price_diff))
print(change_percentage)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if abs(price_diff) >= yesterday_price * 0.0000001:
    news_response = requests.get(url=NEWS_URL, params=news_parameters).json()
    articles = news_response["articles"]


    for article in news_response.json()["articles"]:
        print(article["title"])
        print(article["description"])
        print(article["url"])

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
