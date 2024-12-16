import requests, datetime, smtplib
from geopy import distance
from config import MY_LAT, MY_LONG, TZID, my_email, my_password, my_recipient, my_smtp

ISS_IS_NOW = "http://api.open-notify.org/iss-now.json"
SUNRISE_SUNSET = "https://api.sunrise-sunset.org/json"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "tzid": TZID,
    "formatted": 0
}
def call_api(api_url, parameters=None):
    if parameters != None:
        response = requests.get(url=api_url, params=parameters)
    else:
        response = requests.get(url=api_url)
    response.raise_for_status()
    return response.json()

def send_email(message, recipient_email):
    with smtplib.SMTP(my_smtp) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=recipient_email, 
            msg=f"Subject:The ISS is overhead!\n\n{message}")


iss_position = call_api(ISS_IS_NOW)
longitude = iss_position["iss_position"]["longitude"]
latitude = iss_position["iss_position"]["latitude"]
iss_position = (latitude, longitude)
my_position = (MY_LAT, MY_LONG)
distance_from_me = distance.distance(iss_position, my_position).miles


sunrise_sunset_data = call_api(SUNRISE_SUNSET, parameters=parameters)
sunrise = sunrise_sunset_data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = sunrise_sunset_data["results"]["sunset"].split("T")[1].split(":")[0]
timenow = datetime.datetime.now()


if distance_from_me < 2500: 
    if timenow.hour >= int(sunset) or timenow.hour <= int(sunrise):
        message = "The ISS is flying over your location and it is dark enough so see!"
        send_email(message, my_recipient)
        
   

