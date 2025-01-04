from config import API_KEY, MY_LAT, MY_LONG
import requests

API_URL = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}
def call_api(api_url, parameters=None):
    if parameters != None:
        response = requests.get(url=api_url, params=parameters)
    else:
        response = requests.get(url=api_url)
    response.raise_for_status()
    return response.json()

def rain_in_forecast()->bool:
    five_day_forecast = call_api(API_URL, parameters)
    will_rain = False
    for forecast in five_day_forecast["list"]:
        if forecast["weather"][0]["id"] < 700:
            will_rain = True
    return will_rain

if rain_in_forecast() == True:
    print("Bring an umbrella.")
else:
    print("Leave the umbrella at home.")
