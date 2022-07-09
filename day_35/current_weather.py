import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

# TWILIO_ACCOUNT_SID = "ACe60a15263abea9944641c1523ec52ef8"
# TWILIO_AUTH_TOKEN = "7c7d39e7dfc1bf54811c851091a7cef6"
# TWILIO_NUM = "+19894761086"
# MY_NUM = "+919098155349"

# api_key = "3740da1986c5ee4421528c54bfef2a7c"
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