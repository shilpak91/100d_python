import requests
API_KEY = "pFWdhxXKElM55GBOJSc6Awme4KAbFkfQ"
LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"

location_search_header = {"apikey" : API_KEY}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self,city):
            param = {"term" : {city}}
            response = requests.get(url=LOCATION_ENDPOINT,params=param ,headers=location_search_header)
            iata_code = response.json()["locations"][0]["code"]
            return iata_code
