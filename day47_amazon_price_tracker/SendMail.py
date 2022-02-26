import datetime
import pandas as pd
import os
import random
import smtplib


class SendMail:
    def __init__(self):
        """Class to send mail"""
        self.content = ""
        self.my_email = "hyunduk.kim.doug@gmail.com"
        with open("CONFIG.txt") as file:
            self.pw = str(file.readline().strip())

    def sendmail(self, content: str, to_email: str) -> bool:
        """Takes in the content of the message and receiver's address as input. Returns True if succeeded"""
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.pw)
                connection.sendmail(from_addr=self.my_email, to_addrs=to_email, msg=f"Subject: Price Alert!! \n\n {content}")
            return True
        except:
            return False
#
