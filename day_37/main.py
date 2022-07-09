import random
import requests
from datetime import datetime

USERNAME = "boinky"
TOKEN = "boinkyssecret"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME, 
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
    }

# created my user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": "reading",
    "name": "Reading Graph",
    "unit": "chapters",
    "type": "int",
    "color": "ichou",
}
# header for auth
headers = {
    "X-USER-TOKEN": TOKEN
}
requests.post(url=graph_endpoint, json=graph_config,headers=headers)

# post a pixel 
today = datetime.now()

pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_config['id']}"
pixel_config ={
    "date": today.strftime("%Y%m%d"),
    "quantity": str(random.randint(1,9)),
    # generating random quantity lmfao
}
requests.post(url=pixel_endpoint, json=pixel_config,headers=headers)