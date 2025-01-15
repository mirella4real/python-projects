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

def post_a_pixel():
    today = datetime.today()
    yyyyMMdd_date = today.strftime("%Y%m%d")
    post_pixel = {
        "date": yyyyMMdd_date,
        "quantity": "90"
    }
    response = requests.post(url=f"{PIXELA_GRAPH_ENDPOINT}/graph1", json=post_pixel, headers=headers)
    print(response.text)

post_a_pixel()



