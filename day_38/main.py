from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
BEARER_TOKEN = os.environ["BEARER_SHEETY"]

headers={
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}
query = input("Enter your exercise: ")
params = {
 "query":query,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=exercise_endpoint, json=params, headers=headers).json()

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")
exercise = response['exercises'][0]['name'].title()
duration = response['exercises'][0]['duration_min']
calories = response['exercises'][0]['nf_calories']
id = response['exercises'][0]['tag_id']

# sheety
sheety_get = requests.get(url="https://api.sheety.co/7dda2a9d7766374f2fbf2d69ceac1a55/workoutTracking/workouts")

workout ={ 
    "workout": {
    'date': date,
    'time': time,
    'exercise': exercise,
    'duration': duration,
    'calories': calories,
    }
}

bearer_headers = {
    "Authorization" : f"Bearer {BEARER_TOKEN}"
}
sheety_post = requests.post(
    url="https://api.sheety.co/7dda2a9d7766374f2fbf2d69ceac1a55/workoutTracking/workouts",
    json=workout,
    headers=bearer_headers
)

print(sheety_post)