import smtplib

my_email = "hyunduk.kim.doug@gmail.com"
pw = input("Input the password: ")
connection = smtplib.SMTP("smtp.gmail.com")
# secure connection
connection.starttls()
connection.login(user=my_email, password=pw)
# subject 없으면 스팸으로 분류됨
#  \n\n후에 본문 넣으면
connection.sendmail(from_addr=my_email, to_addrs="slakingex@yahoo.com", msg="Subject: What is the reason?\n\n This is me.")
# 꼭 닫아줘야 함
connection.close()


#  gmail 에서 security - less secure app access 꺼야함
