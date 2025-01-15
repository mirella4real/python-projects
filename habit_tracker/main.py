import requests
from datetime import datetime
from config import *

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

def create_a_graph():
    graph_config = {
        "id": "graph1",
        "name": "Studying Graph",
        "unit": "minutes",
        "type": "float",
        "color": "sora"
    }
    response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=graph_config, headers=headers)
    print(response.text)

def post_a_pixel(minutes):
    today = datetime.today()
    yyyyMMdd_date = today.strftime("%Y%m%d")
    post_pixel = {
        "date": yyyyMMdd_date,
        "quantity": minutes
    }
    response = requests.post(url=f"{PIXELA_GRAPH_ENDPOINT}/graph1", json=post_pixel, headers=headers)
    print(response.text)

def update_a_pixel(pixel_date, quantity):
    yyyyMMdd_date = pixel_date.strftime("%Y%m%d")
    post_pixel = {
        "quantity": quantity
    }
    response = requests.put(url=f"{PIXELA_GRAPH_ENDPOINT}/graph1/{yyyyMMdd_date}", json=post_pixel, headers=headers)
    print(response.text)

def delete_a_pixel(pixel_date):
    yyyyMMdd_date = pixel_date.strftime("%Y%m%d")
    response = requests.delete(url=f"{PIXELA_GRAPH_ENDPOINT}/graph1/{yyyyMMdd_date}", headers=headers)
    print(response.text)

# update_date = datetime(year=2025, month=1, day=14)
# update_a_pixel(update_date, "130")

# delete_date = datetime(year=2025, month=1, day=14)
# delete_a_pixel(delete_date)

minutes_studying = input("How many minutes did you study today?")
post_a_pixel(minutes_studying)