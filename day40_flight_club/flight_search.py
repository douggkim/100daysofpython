import requests
from flight_data import FlightData
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
with open("FLIGHT_CONFIG.txt") as file:
    TEQUILA_API_KEY = file.readline().strip()


def get_destination_code(city_name):
    location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
    headers = {"apikey": TEQUILA_API_KEY}
    query = {"term": city_name, "location_types": "city"}
    response = requests.get(url=location_endpoint, headers=headers, params=query)
    results = response.json()["locations"]
    code = results[0]["code"]
    return code


class FlightSearch:
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, stop_overs=0, via_city=""):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "KRW",
            "max_stopovers": stop_overs,
            "via_city": via_city,
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 5
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            try:
                data = response.json()["data"][0]
            except IndexError:
                pass
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    via_city=data["route"][0]["cityTo"]
                )
                print(f"Flight has {len(data['routes'])-1} stop over, via {data['route'][0]['cityTo']}.")
                print(f"{data['route'][0]['cityTo']}: ₩{flight_data.price}")
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: ₩{flight_data.price}")
            return flight_data
