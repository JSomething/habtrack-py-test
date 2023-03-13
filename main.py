import requests
from datetime import datetime

USERNAME = "glopp"
TOKEN = "lasdfjklasdfjk"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH = "graph1"

user_params = {
    "token": "lasdfjklasdfjk",
    "username": "glopp",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "walking_graph",
    "unit": "miles",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3.5",
}

# response = requests.post(url=pixel_creation, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "5.5",
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)