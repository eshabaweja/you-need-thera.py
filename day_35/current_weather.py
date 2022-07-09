import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

lat = 23.2599
lon = 77.4126
part = "current,minutely,daily,alerts"
load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={os.environ['api_key']}")
response.raise_for_status()
weather_data = response.json()

def need_umbrella():
    for i in range(12):
        weather_id = weather_data["hourly"][i]["weather"][0]["id"]
        if (weather_id < 700):
            return True
    return False

if need_umbrella():
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="You'll need an umbrella ☂️. It's gonna rain babeyyy.",
                     from_=os.environ['TWILIO_NUM'],
                     to=os.environ['MY_NUM']
                 )
    print(message.sid)

else: 
    pass