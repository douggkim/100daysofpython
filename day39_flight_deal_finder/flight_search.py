import requests
import datetime


class FlightSearch:
    # DOCUMENTATION : https://tequila.kiwi.com/portal/docs/
    def __init__(self, airport_code: str, lowest_price: int, date_from_now: int):
        with open("FLIGHT_CONFIG.txt") as file:
            self.TEQUILA_API_KEY = file.readline().strip()
        self.TEQUILA_API_URL = "https://tequila-api.kiwi.com/v2/search"
        self.search_header = {
            "apikey": self.TEQUILA_API_KEY
        }
        self.date_to = datetime.datetime.now() + datetime.timedelta(days=date_from_now)
        self.search_params = {
            "fly_from": "ICN",
            "fly_to": airport_code,
            "dateFrom": str(datetime.datetime.now().strftime("%d/%m/%Y")),
            "dateTo": str(self.date_to.strftime("%d/%m/%Y")),
            "curr": "KRW"
        }
        self.response = requests.get(url=self.TEQUILA_API_URL,
                                     headers=self.search_header,
                                     params=self.search_params).json()
        self.response = self.response["data"]
        self.lowest_price = lowest_price
        self.lowest_airplane = {}

    def get_flight(self):
        return self.response

    def update_lowest_price(self) -> bool:
        is_lower = False
        for record in self.response:
            if record["price"] < self.lowest_price:
                self.lowest_price = record["price"]
                self.lowest_airplane = record
                is_lower = True
        return is_lower
