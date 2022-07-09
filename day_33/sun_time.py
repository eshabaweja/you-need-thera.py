import requests
from datetime import datetime

MY_LAT = 26.912434
MY_LONG = 75.787270

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0,

}
# <endpoint>?<param>=<value>&<param>=<value>
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

# All times are in UTC 
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
time_now = datetime.now()

# getting the hour in 24 hour clock
print(sunrise)
print(sunset)