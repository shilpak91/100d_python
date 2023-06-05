import requests

API_KEY = "pFWdhxXKElM55GBOJSc6Awme4KAbFkfQ"
LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"

SHEET_ENDPOINT = "https://api.sheety.co/42b0edaf1e6e4a297a2cdd89224544d5/flightDeals/prices"
sheet_headers = {"Authorization": "Bearer ajhfb2932ufwflnkewwk"}

location_search_header = {"apikey" : API_KEY}


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) :
        pass

    def get_data(self):
        response = requests.get(url=SHEET_ENDPOINT,headers=sheet_headers)
        return response.json()["prices"]



sheet_data = DataManager()
records = sheet_data.get_data()
cities = [record["city"] for record in records]

# print(cities)

# https://api.tequila.kiwi.com/locations/query?term=Berlin&locale=en-US&location_types=airport&limit=10&active_only=true


for city in cities:
    param = {"term" : {city}}
    response = requests.get(url=LOCATION_ENDPOINT,params=param ,headers=location_search_header)
    # response = requests.get(url="https://api.tequila.kiwi.com/locations/query?term=Berlin&locale=en-US&location_types=airport&limit=10&active_only=true",headers=location_search_header)
    # print(response.json()["locations"][0]["code"])
    print(response.json())




