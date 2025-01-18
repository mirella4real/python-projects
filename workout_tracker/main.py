import requests
import os
from datetime import datetime
from config import *
HOST_DOMAIN = "https://trackapi.nutritionix.com"
API_ENDPOINT = "/v2/natural/exercise"

def save_environment_vars():
    os.environ["APP_ID"] = APP_ID
    os.environ["API_KEY"] = API_KEY

def get_app_id():
    return os.environ.get("APP_ID")

def get_api_key():
    return os.environ.get("API_KEY")

headers = {
    "x-app-id" : get_app_id(),
    "x-app-key": get_api_key()
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
    # print(response.text)
    return response.json()

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
            "calories": kcals
        }
    }
    return parameters

def save_workout(parameters):
    response = requests.post(url=SHEETY_API_ENDPOINT, json=parameters, headers=SHEETY_HEADER)

save_environment_vars()
exercise_text = input("Tell me which exercises you did:")
response = get_exercise_data(exercise_text)
save_workout(parse_exercise_parameters(response))
