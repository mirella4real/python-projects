import requests
from datetime import datetime
from config import *
HOST_DOMAIN = "https://trackapi.nutritionix.com"
API_ENDPOINT = "/v2/natural/exercise"

headers = {
    "x-app-id" : APP_ID,
    "x-app-key": API_KEY
}

def get_exercise_data(exercise_txt:str):
    parameters = {
        "query": exercise_txt,
        "gender": GENDER,
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": AGE
    }
    response = requests.post(url=f"{HOST_DOMAIN}{API_ENDPOINT}", json=parameters, headers=headers)
    return response.text

def parse_exercise_parameters(response_data):
    exercise = response_data["exercises"][0]["name"]
    today_date = datetime.today().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%I:%M %p")
    duration = response_data["exercises"][0]["duration_min"]
    kcals = response_data["exercises"][0]["nf_calories"]
    parameters = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise,
            "duration": duration,
            "calories": "259.3"
        }
    }
    return parameters

def save_workout(parameters):
    response = requests.post(url=SHEETY_API_ENDPOINT, json=parameters, headers=SHEETY_HEADER)
    print(response.text)

# exercise_text = input("Tell me which exercises you did:")
# respose = get_exercise_data(exercise_text)

save_workout(parse_exercise_parameters(TEST_RESPONSE))