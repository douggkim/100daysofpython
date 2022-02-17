#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

# TODO 1: get data from sheety
data_manager = DataManager()
notification_manager = NotificationManager()
old_flight_data = data_manager.get_data()

# TODO 2: search for ticket data
for data in old_flight_data:
    fl_inst = FlightSearch(data["iataCode"], data["lowestPrice"], 30)
    if_lower = fl_inst.update_lowest_price()
    # TODO 3 : replace the price with the lowest price
    if if_lower:
        data["lowestPrice"] = fl_inst.lowest_price
        messenger_string = f"Low price alert! Only {data['lowestPrice']} to fly from {fl_inst.lowest_airplane['cityFrom']} - \
{fl_inst.lowest_airplane['cityCodeFrom']} to {fl_inst.lowest_airplane['cityTo']} - {fl_inst.lowest_airplane['cityCodeTo']} from \
{fl_inst.lowest_airplane['utc_departure']} to {fl_inst.lowest_airplane['utc_arrival']}"
        notification_manager.send_message(messenger_string)


# TODO 4 : Update the data on sheety
data_manager.update_data(old_flight_data)