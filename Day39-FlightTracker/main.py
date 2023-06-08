#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import data_manager as dm
import flight_search as fs

data = dm.DataManager()
dest_data = data.get_destination_data()

flight_data = fs.FlightSearch()


city_code_check = {i["city"]:{"iataCode": i["iataCode"],"row_num" : i["id"]} for i in dest_data}
# print(city_code_check)

for city in city_code_check:
    if city_code_check[city]["iataCode"] == "":
        iata_code = flight_data.get_destination_code(city)
        record = city_code_check[city]["row_num"]
        data.update_destination_code(iata_code,record)
