import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# DOCUMENTATION : https://openweathermap.org/api/one-call-api

API_URL = "https://api.openweathermap.org/data/2.5/weather"
with open("CONFIG.txt") as file:
    API_KEY = str(file.readline()).strip()
    account_sid = str(file.readline()).strip()
    auth_token = str(file.readline()).strip()

CITY_ID = 1835847
MY_LAT = 37.50717  # Your latitude
MY_LONG = 127.07869  # Your longitude
MY_LAT = 45.174
MY_LONG = 14.693

parameters = {
    "id": CITY_ID,
    "appid": API_KEY
}

response = requests.get(url=API_URL, params=parameters)
# print(response.json())


hourly_api_url = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "appid": API_KEY,
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url=hourly_api_url, params=parameters)
weather_for_today = response.json()["hourly"][0:12]
for hourly_weather in weather_for_today:
    if hourly_weather["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    # proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It's going to rain. Remember to bring an umbrella.", to="+821071294021",
                                     from_="+18608916564")
    print(message.status)
