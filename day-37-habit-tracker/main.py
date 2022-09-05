from datetime import datetime
import os
from this import d
import requests

USERNAME = "agurski"
TOKEN = os.environ["PIXELA_TOKEN"]
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# Initial setup
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

date = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": date,
    "quantity": input("How many pages did you read today? ")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

print(response.text)

update_data = {
   "quantity": "5000" 
}

update_endpoint = pixel_creation_endpoint + f"/{date}"

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)

# requests.delete(url=update_endpoint, headers=headers)