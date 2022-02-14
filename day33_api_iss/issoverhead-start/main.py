import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 37.50717  # Your latitude
MY_LONG = 127.07869  # Your longitude
MY_EMAIL = "hyunduk.doug.kim@gmail.com"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = str(datetime.now())
hour_now = time_now.split(" ")[1].split(":")[0]

while True:
    time.sleep(60)
    if is_iss_overhead():
        if hour_now >= sunset or hour_now <=sunrise:
            pw = input("What is your password?")
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password = pw)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs="slakingex@yahoo.com", msg=f"Subject:Look up!! \n\n Look "
                                                                                            f"up! ISS is over your head!")



# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
