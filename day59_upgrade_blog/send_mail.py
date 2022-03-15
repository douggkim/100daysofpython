import smtplib

class send_mail:
    def __init__(self):
        self.my_email = "hyunduk.kim.doug@gmail.com"
        with open("CONFIG.txt") as file:
            self.pw = file.readline().strip()
        # self.pw = "evlngood2!"
        self.connection = smtplib.SMTP("smtp.gmail.com")
        # secure connection
        self.connection.starttls()
        self.connection.login(user=self.my_email, password=self.pw)
        # subject 없으면 스팸으로 분류됨
        #  \n\n후에 본문 넣으면
    def send(self, msg:str, to_addr:str):
        self.connection.sendmail(from_addr=self.my_email, to_addrs=to_addr, msg=msg)
        # 꼭 닫아줘야 함
        self.connection.close()

        return "MESSAGE SENT"


        #  gmail 에서 security - less secure app access 꺼야함
