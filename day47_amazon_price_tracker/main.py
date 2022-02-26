from bs4 import BeautifulSoup
import requests
import pprint
import datetime
from SendMail import SendMail

AMAZON_URL = "https://www.amazon.com/Effects-Fat-Fuzz-Factory-Germanium/dp/B00D8FPKAE/ref=sr_1_2?crid=WX49XPBR1C5E&keywords=fuzz+factory&qid=1645851611&sprefix=fuzz+factor%2Caps%2C251&sr=8-2"
RECEIVERS_MAIL = "slakingex@yahoo.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
           "Connection": "close", "Upgrade-Insecure-Requests": "1"}

# TODO 0 : Ask the User if he/she wants to scrape the data again
user_answer = input("Do you want to scrape the data again? Type Y or N ").lower()

# TODO 0 : set a target price
user_price = float(input("What is your target price? Type only numbers: "))


# TODO 1 : Scrape the price from amazon (at a set time)
if user_answer == "y":
    response = requests.get(url=AMAZON_URL, headers=headers).content
    pprint.pprint(response)
    with open("amazon2.txt", "wb") as file:
        file.write(response)
with open("amazon2.txt", "rb") as file:
    html_file = file.readlines()

# TODO 2 : parse the html from amazon
soup = BeautifulSoup(str(html_file), parser="lxml", features="lxml")
price_span = soup.find(class_="a-price a-text-price a-size-medium apexPriceToPay")
price = float(soup.find(class_="a-price a-text-price a-size-medium apexPriceToPay").getText().split("$")[1])

# TODO 3 : Check if the price is below our target price
# TODO 4 : Send an Email
if price <= user_price:
    content = f"New Price Alert!! \n\n Current Price: ${price}\n\n You have to buy now! \n\n Product URL : {AMAZON_URL}\n\n"
    sendmail = SendMail()
    result = sendmail.sendmail(content=content,to_email=RECEIVERS_MAIL)
    with open("results.txt", "a") as file:
        date = str(datetime.datetime.now()).split(" ")[0]
        if result:
            print(f"{date} Price alert triggered. Mail sent to {RECEIVERS_MAIL}!")
            file.write(f"{date} Price alert triggered. Mail sent to {RECEIVERS_MAIL}!\n")
        else:
            print(f"{date} Price alert triggered. However there was an error sending the email to {RECEIVERS_MAIL}")
            file.write(f"{date} Price alert triggered. However there was an error sending the email to {RECEIVERS_MAIL}\n")


else:
    with open("results.txt", "a") as file:
        date = str(datetime.datetime.now()).split(" ")[0]
        print(f"{date}  No alert triggered. Current Price: ${price} \n")
        file.write(f"{date} No alert triggered. Current Price: ${price} \n")


