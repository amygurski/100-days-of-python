import requests
import os
from twilio.rest import Client

OPEN_WEATHER_MAP_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ["OPEN_WEATHER_MAP_KEY"]
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

PARAMS= {
    "lat": "41.4993",
    "lon": "-81.6944",
    "appid": API_KEY,
    "exclude": "daily,current,minutely,alerts"
}

response = requests.get(OPEN_WEATHER_MAP_ENDPOINT, params=PARAMS, verify=False)
response.raise_for_status()
weather_data = response.json()

# Check for rain in the next 12 hours.
will_rain = False

weather_slice = weather_data["hourly"][:12]

for hour in weather_slice:
    # Weather condition codes: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
    weather_condition_code = hour["weather"][0]["id"]
    if int(weather_condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                    body="It's going to rain. Remember to bring an umbrella ☔️.",
                    from_='',
                    to=''
                )

    print(message.status)   
