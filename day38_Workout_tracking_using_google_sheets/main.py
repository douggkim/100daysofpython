import requests
import datetime

with open("CONFIG.txt") as file:
    APP_ID = str(file.readline().strip())
    API_KEY = str(file.readline().strip())
    SHEETY_API_KEY = str(file.readline().strip())

# TODO 1 : NLP EXERCISE INPUT
# DOCUMENTATION : https://gist.github.com/mattsilv/d99cd145cc2d44d71fa5d15dd4829e03
NLP_EXERCISE_API_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
nlp_exercise_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

nlp_exercise_body = {
    "query": input("What kind of exercise have you done today?"),
    "gender": "male",
    "weight_kg": 77.1,
    "height_cm": 179.5,
    "age": 29,
}

response = requests.post(url=NLP_EXERCISE_API_URL, headers=nlp_exercise_header, json=nlp_exercise_body).json()
print(response)
# TODO 2 : RECORD DATA WITH SHEETY
# DOCUMENTATION : https://dashboard.sheety.co/projects/620d01d76b61d53cacb6fd6c/sheets/workouts
# response["exercises"]["duration_min"]
# response["exercises"]["nf_calories"]
# response["exercises"]["name"]
recorded_time = datetime.datetime.now().strftime("%H:%M:%S")
recorded_date = datetime.datetime.now().strftime("%d/%m/%Y")

SHEETY_POST_URL = "https://api.sheety.co/7c090537428edb8f5d934a5c07876b52/myWorkouts/workouts"
sheety_header = {
    "Content-Type": "application/json",
    "Authorization": SHEETY_API_KEY
}

sheety_post_body = {
    "workout": {
        "date": recorded_date,
        "time": recorded_time,
        "exercise": response["exercises"][0]["name"].title(),
        "duration": response["exercises"][0]["duration_min"],
        "calories": response["exercises"][0]["nf_calories"]
    }
}

response = requests.post(url=SHEETY_POST_URL, headers=sheety_header, json=sheety_post_body)
print(response.json())