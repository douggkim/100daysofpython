from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        with open("twilio_CONFIG.txt") as file:
            twilio_account_sid = file.readline()
            twilio_auth_token = file.readline()
        self.client = Client(twilio_account_sid, twilio_auth_token)
        self.message = ""

    def send_message(self, message_to_send: str):
        self.message = self.client.messages.create(body=message_to_send, to="+821071294021",
                                                   from_="+18608916564")
        print(self.message.status)

