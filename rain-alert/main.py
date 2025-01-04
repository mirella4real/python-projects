from config import *
from twilio.rest import Client
import requests


def call_api(api_url, parameters=None):
    if parameters != None:
        response = requests.get(url=api_url, params=parameters)
    else:
        response = requests.get(url=api_url)
    response.raise_for_status()
    return response.json()

def rain_in_forecast()->bool:
    parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": OPENWEATHER_API_KEY,
    "cnt": 4
}
    five_day_forecast = call_api(OPENWEATHERMAP_ENDPOINT, parameters)
    will_rain = False
    for forecast in five_day_forecast["list"]:
        if forecast["weather"][0]["id"] < 700:
            will_rain = True
    return will_rain

def send_sms(sms_message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_TOKEN)
    message = client.messages.create(
        body=sms_message,
        from_=whatsapp_sender_number,
        to=whatsapp_recipient_number,
    )
    print(message.status)

if rain_in_forecast() == True:
    send_sms(f"It's going to rain today in {LOCATION}. Remember to bring an ☔️")
else:
    print("Leave the umbrella at home.")
