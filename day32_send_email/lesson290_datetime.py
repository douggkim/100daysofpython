import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
if year == 2022:
    print("Wear a face mask ㅠㅠ")

# class type: datetime.datetime
print(type(now))

date_of_birth = dt.datetime(year=2022 , month=8, day=4, hour=4)
print(date_of_birth)
