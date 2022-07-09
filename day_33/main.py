import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response," is out response code.")
response.raise_for_status()

# getting json from response
data = response.json()
print(data)

longitude = response.json()['iss_position']['longitude']
print(longitude)

latitude = response.json()['iss_position']['latitude']
print(latitude)

# making it a tuple
iss_position = (longitude, latitude)