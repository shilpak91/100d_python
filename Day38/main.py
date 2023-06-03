import requests
import datetime as dt
from time import sleep

APP_ID = "9f3a3145"
APP_KEY = "70d5a072e5b7ec65f6c5a62eb3d1b07b"

ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/42b0edaf1e6e4a297a2cdd89224544d5/myWorkouts/workouts"

exercise_headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : APP_KEY,
    "Content-Type" : "application/json",
    }

sheet_headers = {"Authorization": "Bearer 1764fyuafjavkhfrhvbsdhjbm67wr"}

date = dt.datetime.now().strftime("%d/%m/%Y")
# print(date)
time = dt.datetime.now().strftime("%X")
# print(time)


def get_data_from_sheet ():
    response_sheet = requests.get(url=sheet_endpoint,headers=sheet_headers)
    print(response_sheet.json())


def input_data():
    user_input = input("What exercise did you do today ?")

    exercise_details = {
        "query":user_input,
        "gender":"male",
        "weight_kg":85.5,
        "height_cm":183.00,
        "age":31}
    
    exercise_response = requests.post(url=ENDPOINT,json=exercise_details,headers=exercise_headers)
    exercise_data = exercise_response.json()["exercises"]

    for i in exercise_data:
        data = {"workout" : {"date": date, "time": time, "exercise": i["name"],"duration": i["duration_min"],"calories":i["nf_calories"]}}
        response = requests.post(url=sheet_endpoint,json=data,headers=sheet_headers)

    # print(exercise_data)

def delete_rows_sheet(*argv):
    for arg in argv:
        requests.delete(url=f"{sheet_endpoint}/{arg}",headers=sheet_headers)
        print(f"Row {arg} deleted !!")
        sleep(2)


# input_data()
delete_rows_sheet(3)

