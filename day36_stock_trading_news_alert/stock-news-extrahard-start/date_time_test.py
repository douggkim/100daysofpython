import datetime

print(str(datetime.datetime.now()).split(" ")[0])
print(str(datetime.datetime.now() - datetime.timedelta(days=1)).split(" ")[0])

print(datetime.datetime.now().weekday())