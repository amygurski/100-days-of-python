from datetime import datetime
import os
import requests

APP_ID = os.environ["NUTRITIONIX_APP_ID"]
APP_KEY = os.environ["NUTRITIONIX_APP_KEY"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/ad6bb8b3f54926e9e65898b4e27e53f1/myWorkouts/workouts"

exercise_query = input("What workout did you do? ")

# Get exercise info (calories burned, etc)
params = {
    "query": exercise_query,
    "gender": "female",
    "weight_kg": "56.7",
    "height_cm": "160",
    "age": "42"
}
response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()

# Add to spreadsheet with Sheety
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

print(sheet_response.text)