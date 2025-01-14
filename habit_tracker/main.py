import requests
from config import *

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Studying Graph",
    "unit": "minutes",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(response.text)