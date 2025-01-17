import requests
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
    print(response.text)

exercise_text = input("Tell me which exercises you did:")
get_exercise_data(exercise_text)