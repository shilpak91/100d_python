import requests

api_key = "39SR6WKXA454E6Q67A6AQDZFL"

parameters = {
    "key" : api_key
}

response = requests.get(url="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Utrecht,Netherlands",params=parameters)
print(response.json())


# https://api.openweathermap.org/data/2.5/weather?lat=52.0248&lon=5.0918&appid=8cc17e3bca0b1304370a5ccd50a96adc
# https://api.openweathermap.org/data/3.0/onecall?lat=lat=52.0248&lon=5.0918&appid=8cc17e3bca0b1304370a5ccd50a96adc
# https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Utretcht,Netherlands?key=39SR6WKXA454E6Q67A6AQDZFL