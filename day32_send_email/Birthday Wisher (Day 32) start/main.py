import smtplib
import random
import datetime as dt


# load data
with open("quotes.txt", "r") as quotes_file:
    quotes_list = quotes_file.readlines()

# set email
my_email = "hyunduk.kim.doug@gmail.com"
pw = input("Input your password : ")
# check weekday
now = dt.datetime.now()
if now.weekday() == 6:
    random_quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(from_addr=my_email, to_addrs="slakingex@yahoo.com",
                        msg=f"Subject: Quote of the day \n\n{random_quote}")
else:
    print("Today is not Sunday")
