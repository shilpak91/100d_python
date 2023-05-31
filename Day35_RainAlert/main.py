import requests
import datetime as dt

api_key = "39SR6WKXA454E6Q67A6AQDZFL"

parameters = {
    "key" : api_key
}

today = dt.datetime.now()
today_date = today.date()
current_hour = int(today.hour)


# print(current_hour)


response = requests.get(url="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/21,124",params=parameters)
next_hourly_data = response.json()["days"][0]["hours"][current_hour-1:]

# print(next_hourly_data)
is_rain = False

for data in next_hourly_data:
    if "Rain" in data["conditions"]:
        is_rain = True

if is_rain:
    print("Bring and unbrella")
    # We can also send a email here from smtb lib




# https://api.openweathermap.org/data/2.5/weather?lat=52.0248&lon=5.0918&appid=8cc17e3bca0b1304370a5ccd50a96adc
# https://api.openweathermap.org/data/3.0/onecall?lat=lat=52.0248&lon=5.0918&appid=8cc17e3bca0b1304370a5ccd50a96adc
# https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Utretcht,Netherlands?key=39SR6WKXA454E6Q67A6AQDZFL