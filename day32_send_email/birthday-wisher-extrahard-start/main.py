import datetime
import pandas as pd
import os
import random
import smtplib

birthday_email = {}
my_email = "hyunduk.kim.doug@gmail.com"
pw = input("What is your password?")
# 1. Update the birthdays.csv
birthdays_df = pd.read_csv("./birthdays.csv")
print(birthdays_df)

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.datetime.now()
for (index, date) in birthdays_df.iterrows():
    if date["month"] == now.month and date["day"] == now.day:
        birthday_email[date["name"]] = date["email"]
        print(birthday_email)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
entries = os.listdir("letter_templates")
print(entries)
print(type(entries))
# 4. Send the letter generated in step 3 to that person's email address.
for person, email in birthday_email.items():
    # content
    mail_file = random.choice(entries)
    print(mail_file)
    with open(f"letter_templates/{mail_file}") as content :
        mail_content = content.read()
        mail_content = mail_content.replace("[NAME]", person)
        print(person, email)
    # smtp setup
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject: Happy Birthday!! \n\n {mail_content}")


#
