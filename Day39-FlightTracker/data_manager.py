import requests
from pprint import pprint

API_KEY = "pFWdhxXKElM55GBOJSc6Awme4KAbFkfQ"
LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"

SHEET_ENDPOINT = "https://api.sheety.co/42b0edaf1e6e4a297a2cdd89224544d5/flightDeals/prices"
sheet_headers = {"Authorization": "Bearer ajhfb2932ufwflnkewwk"}

location_search_header = {"apikey" : API_KEY}


class DataManager:

    def get_destination_data(self):
        
        response = requests.get(url=SHEET_ENDPOINT,headers=sheet_headers)
        data = response.json()["prices"]
        return data
    
    def update_destination_code(self,code,row_num):
            
            iata_data = {"price":{'iataCode': code}}
            requests.put(url=f"{SHEET_ENDPOINT}/{row_num}",json=iata_data,headers=sheet_headers)

