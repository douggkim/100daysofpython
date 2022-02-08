import csv
import pandas as pd

with open('weather_data.txt', mode='rt') as weather_data:
    csv_reader = csv.reader(weather_data, delimiter=',')
    header = next(csv_reader)
    temperatures = []
    for line in csv_reader:
        temperatures.append(line[1])
    print(header)
    print(temperatures)

# 동일한 작업을 pandas로 진행data = pd.read_csv("weather_data.txt")

# pandas dataframe 이라는 형식이 있다print(type(data))

# pandas series 라는 형식임 (data.temp 로도 표현 가능)print(type(data["temp"]))
print(data)

# dict로 전환 (각 series를 하나의 dictionary로 변환)print(data.to_dict())

#  list형태로 반환print(data["temp"].to_list())

# average 반환# average = sum(data["temp"].to_list())/len(data["temp"].to_list())print(data["temp"].mean())

# maximum value 반환print(data["temp"].max())

# 월요일만 뽑자# 소문자만 뽑기 data.day.str.lower()print(data[data.day.str.lower() == "monday"])

# 최대인 row 반환print(data[data.temp == data["temp"].max()])

# farenheit를 celsius로 변환temp = data["temp"]
print((temp * 9 / 5) + 32)

# create a dataframe from scratch & create a csv
filedata_dict = {
    "students": ["Amy", "James", "Angela"],    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.txt")