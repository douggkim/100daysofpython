from twilio.rest import Client

with open("TWILIO_CONFIG.txt") as file:
    TWILIO_SID = file.readline().strip()
    TWILIO_AUTH_TOKEN = file.readline().strip()
    TWILIO_VERIFIED_NUMBER = file.readline().strip()
    TWILIO_VIRTUAL_NUMBER = file.readline().strip()


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
