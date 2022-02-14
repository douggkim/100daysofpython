import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# HTTP status 별 exception 처리해줌 
response.raise_for_status()

data = response.json()
# data["iss_position"]["longitude"] 로 특정 데이터에 접근
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
print(data)