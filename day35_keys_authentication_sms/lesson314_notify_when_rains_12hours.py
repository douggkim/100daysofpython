import requests

with open("CONFIG.txt") as file:
    API_KEY = str(file.readline()).strip()
CITY_ID = 1835847
MY_LAT = 37.50717  # Your latitude
MY_LONG = 127.07869  # Your longitude

hourly_api_url = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "appid": API_KEY,
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url=hourly_api_url, params=parameters)
print(response.json()["hourly"])
