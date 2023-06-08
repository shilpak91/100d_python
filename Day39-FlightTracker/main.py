#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import data_manager as dm
import flight_search as fs
from datetime import datetime,timedelta

data = dm.DataManager()
dest_data = data.get_destination_data()
flight_search = fs.FlightSearch()

ORIGIN_CITY_IATA = "LON"


city_code_check = {i["city"]:{"iataCode": i["iataCode"],"row_num" : i["id"]} for i in dest_data}
# print(city_code_check)

for city in city_code_check:
    if city_code_check[city]["iataCode"] == "":
        iata_code = flight_search.get_destination_code(city)
        record = city_code_check[city]["row_num"]
        data.update_destination_code(iata_code,record)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


for destination in dest_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )