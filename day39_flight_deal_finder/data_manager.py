import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    # DOCUMENTATION : https://dashboard.sheety.co/projects/620da1cc6b61d53cacb7021b/sheets/prices
    def __init__(self):
        self.SHEETY_GET_URL = "https://api.sheety.co/7c090537428edb8f5d934a5c07876b52/flightDeals/prices"
        self.SHEETY_POST_URL = "https://api.sheety.co/7c090537428edb8f5d934a5c07876b52/flightDeals/prices"
        self.SHEETY_PUT_URL = "https://api.sheety.co/7c090537428edb8f5d934a5c07876b52/flightDeals/prices/"
        self.response = requests.get(url=self.SHEETY_GET_URL).json()
        self.ticket_data = []
        for price in self.response["prices"]:
            ticket_dict = {"id": price["id"], "city": price["city"], "iataCode": price["iataCode"],
                           "lowestPrice": price["lowestPrice"] }
            self.ticket_data.append(ticket_dict)

    def get_data(self) -> dict:
        return self.ticket_data

    def update_data(self, ticket_dict: dict):
        for price in self.ticket_data:
            sheety_post_body = {"price": price}
            response = requests.put(url=self.SHEETY_PUT_URL + str(price["id"]), json=sheety_post_body).json()
            print(response)
