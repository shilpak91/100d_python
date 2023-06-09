import requests
from flight_data import FlightData
API_KEY = "pFWdhxXKElM55GBOJSc6Awme4KAbFkfQ"
LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
search_endpoint = "https://api.tequila.kiwi.com/v2/search"

location_search_header = {"apikey" : API_KEY}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self,city):
            param = {"term" : {city}}
            response = requests.get(url=LOCATION_ENDPOINT,params=param ,headers=location_search_header)
            iata_code = response.json()["locations"][0]["code"]
            return iata_code
    
    def check_flights(self,origin_city_code, destination_city_code, from_time, to_time):
        flight_search_header = {"apikey" : API_KEY}

        query = {"fly_from": origin_city_code,
                "fly_to": destination_city_code,
                "date_from":from_time.strftime("%d/%m/%Y"),
                "date_to": to_time.strftime("%d/%m/%Y"),
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "GBP"
                }

        response = requests.get(url=search_endpoint,params=query,headers=flight_search_header)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        # print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
