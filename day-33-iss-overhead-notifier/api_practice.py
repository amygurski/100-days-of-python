import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
position = response.json()["iss_position"]["longitude"]
print(position)

# The requests module is the most popular way for python developers to 
# work with apis.